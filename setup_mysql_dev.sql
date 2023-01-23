-- Prepares a MySQL server for the project
-- Creates database, user and grants privileges to the user

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
GRANT ALL ON hbnb_dev_db.* to 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
SET FOREIGN_KEY_CHECKS=1;
