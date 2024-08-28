--CREATE DATABASE studio
  -- WITH
  -- OWNER = postgres
  -- ENCODING = 'UTF8'
  -- LOCALE_PROVIDER = 'libc'
  -- CONNECTION LIMIT = -1
  -- IS_TEMPLATE = False;
   
DROP TABLE IF EXISTS pupils;

CREATE TABLE IF NOT EXISTS pupils (
	student_id SERIAL,
	surname VARCHAR(50) NOT NULL,
	name VARCHAR(50) NOT NULL,
	surname_2 VARCHAR(50),
	age INTEGER CHECK (age>0 AND age<100),
	grup_name VARCHAR(50) NOT NULL,
	avg_ball NUMERIC CHECK (avg_ball>0),
	note TEXT
);

INSERT INTO pupils(surname, name, surname_2, age, grup_name, avg_ball, note)
VALUES
('Петрова', 'Мария', 'Александровна', 12, 'Гр. № 1', 4.7, ''),
('Иванова', 'Нина', 'Николаевна', 8, 'Гр. № 2', 4.5, ''),
('Сидоров', 'Денис', 'Валерьевич', 9, 'Гр. № 2', 4.3, ''),
('Семенов', 'Данил', 'Сергеевич', 11, 'Гр. № 1', 4.8, '');
