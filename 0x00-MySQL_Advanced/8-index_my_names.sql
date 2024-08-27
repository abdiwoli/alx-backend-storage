-- Create an index on the first letter of the name column
CREATE INDEX idx_name_first ON names (name(1));

-- Verify the index creation
SHOW INDEX FROM names;

-- Test the index by performing a query
SELECT COUNT(name) FROM names WHERE name LIKE 'a%';
