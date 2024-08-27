-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    -- Declare variables
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
    DECLARE weighted_average FLOAT DEFAULT 0;
    
    -- Calculate the total weighted score and total weight
    SELECT SUM(score * weight), SUM(weight)
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
    
    -- Update the user's average_score
    UPDATE users
    SET average_score = weighted_average
    WHERE id = user_id;
END //

DELIMITER ;
