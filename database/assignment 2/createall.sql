--This assignment has been done by
--1.Lohitha Yalavarthi(002289255)
--2.Nitish Kumar(002286814)
--3.Bhargav Movva(002292699)

/* II. Programming with SQL
        Problem 1           */

--query for creating tables

create table TEACHER
	(t_id		integer,
	 t_name		varchar(30),
	 t_status	varchar(30),
	 t_dept     varchar(30),
	 primary key (t_id)
	);
create table COURSE
    (c_id  varchar(30),
	 c_name varchar(60),
	 c_level varchar(30),
	 primary key (c_id)
	);
create table STUDENT
    (s_id integer,
	 s_name varchar(30),
	 s_status varchar(30),
	 primary key (s_id)
	);
create table ENROLMENT
    (c_id varchar(30),
	 s_id integer,
	 foreign key (c_id) references COURSE,
	 foreign key (s_id) references STUDENT
	 );
create table COURSE_SCHEDULE
    (c_id varchar(30),
	 t_id integer,
	 foreign key (c_id) references COURSE,
	 foreign key (t_id) references TEACHER
	);
