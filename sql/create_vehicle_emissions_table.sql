CREATE TABLE vehicle_emissions (
    model_year INTEGER,
    make VARCHAR(100),
    model VARCHAR(150),
    vehicle_class VARCHAR(100),
    engine_size DECIMAL(4, 2),
    cylinders INTEGER,
    transmission VARCHAR(50),
    fuel_type VARCHAR(50),
    fuel_consumption_city DECIMAL(5, 2),
    fuel_consumption_hwy DECIMAL(5, 2),
    fuel_consumption_comb DECIMAL(5, 2),
    co2_emissions INTEGER,
    co2_rating INTEGER,
    smog_rating INTEGER
);