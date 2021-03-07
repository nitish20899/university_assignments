--This assignment has been done by
--1.Lohitha Yalavarthi(002289255)
--2.Nitish Kumar(002286814)
--3.Bhargav Movva(002292699)

/* II. Programming with SQL
        Problem I           */

-- Insertion Query

INSERT INTO COURSE(
	c_name, c_level, c_id)
	VALUES ('Intro to Computers', 'F', 'CS110');

INSERT INTO COURSE(
	c_name, c_level, c_id)
	VALUES ('Computer Architecture','SP','CS250');

INSERT INTO COURSE(
	c_name, c_level, c_id)
	VALUES ('Information Systems','S','CS348');

INSERT INTO COURSE(
	c_name, c_level, c_id)
	VALUES ('Intro to Data Bases','S','CS448');

INSERT INTO COURSE(
	c_name, c_level, c_id)
	VALUES (' Operating System ','GR','CS503');

INSERT INTO COURSE(
	c_name, c_level, c_id)
	VALUES ('Intro to Electric Analysis & Design','S','ECE255');

INSERT INTO COURSE(
	c_name, c_level, c_id)
	VALUES ('Advanced C Programming ','S','ECE264');

INSERT INTO COURSE(c_name, c_level, c_id)
	VALUES ('Linear Algebra ','GR','MA511');

INSERT INTO COURSE(
	c_name, c_level, c_id)
	VALUES ('Intro to Complex Analysis ','GR','MA525');







INSERT INTO TEACHER(
	t_id, t_name, t_status, t_dept)
	VALUES (00111, 'John A. Brown', 'P', 'CS');
INSERT INTO TEACHER(
	t_id, t_name, t_status, t_dept)
	VALUES (00112, 'James kareter', 'P', 'ECE');
INSERT INTO TEACHER(
	t_id, t_name, t_status, t_dept)
	VALUES (00113, 'Christopher Lee', 'AP', 'ECE');
INSERT INTO TEACHER(
	t_id, t_name, t_status, t_dept)
	VALUES (00114, 'Susanne Hambrusch', 'L', 'CS');
INSERT INTO TEACHER(
	t_id, t_name, t_status, t_dept)
	VALUES (00115, 'Sheron Noel', 'P', 'MA');
INSERT INTO TEACHER(
	t_id, t_name, t_status, t_dept)
	VALUES (00116, 'Kim Basinger', 'AP', 'ECE');
INSERT INTO TEACHER(
	t_id, t_name, t_status, t_dept)
	VALUES (00117 , 'Christopher Clifton', 'P', 'CS');
INSERT INTO TEACHER(
	t_id, t_name, t_status, t_dept)
	VALUES (00118, 'Elisa Bertino', 'P', 'CS');
INSERT INTO TEACHER(
	t_id, t_name, t_status, t_dept)
	VALUES (00119, 'Susanne Hambrusch', 'AP', 'CS');


INSERT INTO COURSE_SCHEDULE(
	c_id, t_id)
	VALUES ('CS110', 00114);
INSERT INTO COURSE_SCHEDULE(
	c_id, t_id)
	VALUES ('CS348', 00117);
INSERT INTO COURSE_SCHEDULE(
	c_id, t_id)
	VALUES ('CS250', 00118);
INSERT INTO COURSE_SCHEDULE(
	c_id, t_id)
	VALUES ('CS448', 00114);
INSERT INTO COURSE_SCHEDULE(
	c_id, t_id)
	VALUES ('MA511', 00115);
INSERT INTO COURSE_SCHEDULE(
	c_id, t_id)
	VALUES ('CS503', 00119);
INSERT INTO COURSE_SCHEDULE(
	c_id, t_id)
	VALUES ('MA525', 00115);
INSERT INTO COURSE_SCHEDULE(
	c_id, t_id)
	VALUES ('ECE264', 00113);
INSERT INTO COURSE_SCHEDULE(
	c_id, t_id)
	VALUES ('ECE255', 00116);




INSERT INTO STUDENT(
	s_id, s_name, s_status)
	VALUES (234, 'Anglo Anebal', 'F');
INSERT INTO STUDENT(
	s_id, s_name, s_status)
	VALUES (235, 'Abram Ace', 'S');
INSERT INTO STUDENT(
	s_id, s_name, s_status)
	VALUES (236, 'Adelbert Antti', 'SP');
INSERT INTO STUDENT(
	s_id, s_name, s_status)
	VALUES (237, 'William Walker', 'GR');
INSERT INTO STUDENT(
	s_id, s_name, s_status)
	VALUES (238, 'Emila Wdyth', 'GR');
INSERT INTO STUDENT(
	s_id, s_name, s_status)
	VALUES (239, 'Judith Elba', 'S');
INSERT INTO STUDENT(
	s_id, s_name, s_status)
	VALUES (240, 'Benjamin Bratt', 'SP');
INSERT INTO STUDENT(
	s_id, s_name, s_status)
	VALUES (241, 'Tawny Kitaen', 'F');



INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('CS110',240 );
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('CS110',241 );
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('CS348',235 );
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('CS348',239 );
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('CS348', 237);
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('CS250', 236);
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('CS250',241 );
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('ECE264',236 );
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('ECE264',237 );
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('ECE264',238 );
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('MA525',236 );
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('CS503',238 );
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('CS503',239 );
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('CS448',240 );
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('CS250',240 );
INSERT INTO ENROLMENT(
	c_id, s_id)
	VALUES ('MA511',240 );
