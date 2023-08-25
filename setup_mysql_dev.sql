-- script that prepares mysql server for the project.
CREATE DATABASE
    IF NOT EXISTS cyclife_dev_db;
CREATE USER
    IF NOT EXISTS 'cyclife_dev'@'localhost' IDENTIFIED BY '<password>';

GRANT ALL PRIVILEGES ON `cyclife_dev_db`.* TO 'cyclife_dev'@'localhost';
