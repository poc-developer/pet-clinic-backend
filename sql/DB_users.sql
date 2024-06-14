-- Create admin user with superuser privileges
CREATE USER admin WITH PASSWORD 'admin_password' SUPERUSER;

-- Create regular users with standard privileges
CREATE USER desmond_wong WITH PASSWORD 'desmond_password';
CREATE USER jemma WITH PASSWORD 'jemma_password';
CREATE USER sairam_kaleru WITH PASSWORD 'sairam_password';

-- Grant privileges on all tables to admin
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO admin;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO admin;

-- Grant crud operation privileges to regular users 
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO desmond_wong;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO jemma;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO sairam_kaleru;