-- Prepares a MySQL server for the project.
-- DataBase
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
-- Sets password
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';
-- User Privileges ALL
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- User Privileges SELECT
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
