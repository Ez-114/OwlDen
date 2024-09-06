-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS owlden_test_db;
CREATE USER IF NOT EXISTS 'owlden_test'@'localhost' IDENTIFIED BY 'OwlDen98_test1_pwd';
GRANT ALL PRIVILEGES ON `owlden_test_db`.* TO 'owlden_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'owlden_test'@'localhost';
FLUSH PRIVILEGES;
