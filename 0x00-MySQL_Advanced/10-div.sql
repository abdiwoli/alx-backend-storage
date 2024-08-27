-- Drop the function if it already exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Create the SafeDiv function
DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    -- Return 0 if b is 0, otherwise return the division result
    RETURN IF(b = 0, 0, a / b);
END$$

DELIMITER ;

-- Test the function
-- The following queries will test the SafeDiv function on the existing numbers table

SELECT a, b, SafeDiv(a, b) AS result
FROM numbers;
