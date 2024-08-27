-- Create an index on the first letter of the name column and the score column
CREATE INDEX idx_name_first_score ON names (name(1), score);

-- Verify the index creation
SHOW INDEX FROM names;

-- Test the index by performing a query
SELECT COUNT(name) FROM names WHERE name LIKE 'a%' AND score < 80;
