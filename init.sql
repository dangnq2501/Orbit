-- We don't need to create the database as it's created by Docker using POSTGRES_DB
-- We don't need to create the user as it's created by Docker using POSTGRES_USER

-- Create the table
CREATE TABLE IF NOT EXISTS walletall (
    "from" VARCHAR(42),
    "to" VARCHAR(42),
    value_eth NUMERIC,
    timestamp TIMESTAMP
);

-- Grant permissions
GRANT ALL PRIVILEGES ON TABLE walletall TO myuser;

-- Grant sequence permissions if needed
ALTER TABLE walletall OWNER TO myuser;