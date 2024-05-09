-- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
-- abdiwoli

SELECT band_name, COALESCE(split, 2022) - FORMED AS lifespan
FROM  metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
