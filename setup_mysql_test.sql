
-- script that prepares mysql server for the project.
CREATE DATABASE IF NOT EXISTS cyclife_test_db;
CREATE USER IF NOT EXISTS 'cyclife_test'@'%' IDENTIFIED BY 'cyclifepass';
GRANT ALL PRIVILEGES ON `cyclife_test_db`.* TO 'cyclife_test'@'%';
