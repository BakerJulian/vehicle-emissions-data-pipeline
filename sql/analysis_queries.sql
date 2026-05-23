-- Average CO2 emissions by vehicle class
SELECT
    vehicle_class,
    AVG(co2_emissions) AS average_co2_emissions
FROM vehicle_emissions
GROUP BY vehicle_class
ORDER BY average_co2_emissions DESC;

-- Average CO2 emissions by fuel type
SELECT
    fuel_type,
    AVG(co2_emissions) AS average_co2_emissions
FROM vehicle_emissions
GROUP BY fuel_type
ORDER BY average_co2_emissions DESC;

-- Highest emitting manufacturers
SELECT
    make,
    AVG(co2_emissions) AS average_co2_emissions
FROM vehicle_emissions
GROUP BY make
ORDER BY average_co2_emissions DESC;