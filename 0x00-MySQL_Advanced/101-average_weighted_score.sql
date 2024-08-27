-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Declare variables
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE weighted_average FLOAT;

    -- Declare a cursor to iterate over all users
    DECLARE user_cursor CURSOR FOR 
        SELECT id FROM users;

    -- Declare a handler for when the cursor is exhausted
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open the cursor
    OPEN user_cursor;

    -- Loop through all users
    read_loop: LOOP
        FETCH user_cursor INTO user_id;
        
        -- Exit the loop when no more rows are found
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        -- Calculate the total weighted score and total weight for the current user
        SELECT IFNULL(SUM(score * weight), 0), IFNULL(SUM(weight), 0)
        INTO total_score, total_weight
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;
        
        -- Compute the average weighted score
        IF total_weight > 0 THEN
            SET weighted_average = total_score / total_weight;
        ELSE
            SET weighted_average = 0;
        END IF;
        
        -- Update the average_score for the user
        UPDATE users
        SET average_score = weighted_average
        WHERE id = user_id;
    END LOOP;

    -- Close the cursor
    CLOSE user_cursor;
END //

DELIMITER ;
