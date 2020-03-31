-- Prepares a MySQL server for the project.
-- DataBase
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
-- Sets password
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
-- User Privileges ALL
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- User Privileges SELECT
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
