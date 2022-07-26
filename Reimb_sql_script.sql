--DROP TABLE user_type;
--DROP TABLE reimbursement;
--DROP TABLE users;

--USERS--

CREATE TABLE users (
user_id SERIAL PRIMARY KEY,
username VARCHAR(50) UNIQUE NOT NULL,
password VARCHAR(20) NOT NULL,
first_name VARCHAR(20) NOT NULL,
last_name VARCHAR(20) NOT NULL,
email VARCHAR(50) UNIQUE NOT NULL,
role VARCHAR(20) NOT NULL
);

INSERT INTO users (username, password, first_name, last_name, email, role) VALUES 

('johndoe', 'password', 'John', 'Doe', 'jimdoe@gmail.com', 'employee'),
('jimsmith', 'password', 'Jim', 'Smith', 'jimsmith@gmail.com', 'employee'),
('janedoe', 'password', 'Jane', 'Doe', 'janedoe@gmail.com', 'finance_manager');

--REIMBURSEMENT--

CREATE TABLE reimbursement (
reimb_id SERIAL PRIMARY KEY,
reimb_amount NUMERIC,
submission_date TIMESTAMP,
resolved_date TIMESTAMP,
status VARCHAR(20) DEFAULT 'pending',
type VARCHAR(20),
description VARCHAR(50),
receipt BYTEA,
reimb_author INTEGER REFERENCES users(user_id),
reimb_resolver INTEGER REFERENCES users(user_id)
);

INSERT INTO reimbursement (reimb_amount, type, description, reimb_author, submission_date) VALUES 
('300', 'travel', 'car rental', '1', CURRENT_TIMESTAMP),
('500', 'travel', 'hotel', '1', CURRENT_TIMESTAMP),
('1000', 'office', 'computer', '2', CURRENT_TIMESTAMP),
('200', 'travel', 'hotel', '2', CURRENT_TIMESTAMP),
('5000000', 'travel', 'yacht', '2', CURRENT_TIMESTAMP)
;


--USER TYPE--
--CREATE TABLE user_type (
--id SERIAL PRIMARY KEY,
--title VARCHAR(20) NOT NULL
--);
--
--INSERT INTO user_type (title)
--VALUES ('Employee'), ('Financial_Manager');
