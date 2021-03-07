--This assignment has been done by
--1.Lohitha Yalavarthi(002289255)
--2.Nitish Kumar(002286814)
--3.Bhargav Movva(002292699)


--Select Query


-- Query1: Find the name(s) of all TEACHERs(s) who are from ECE department.
select t_name from TEACHER where t_dept='ECE';

-- Query2: Find the name(s) of all STUDENT(s) enrolled in CS250.
select S.s_name from STUDENT AS S ,ENROLMENT AS E where S.s_id=E.s_id AND E.c_id='CS250';

--Query3: Find the STUDENT id(s) and names(s) of all STUDENTs enrolled in CS348 and either in ECE264 or in CS503.
SELECT subrecord.s_id,subrecord.s_name
FROM (SELECT STUDENT.s_id,STUDENT.s_name FROM STUDENT,ENROLMENT WHERE ENROLMENT.c_id='CS348' AND STUDENT.s_id=ENROLMENT.s_id) subrecord, ENROLMENT
WHERE (ENROLMENT.c_id='ECE264' OR ENROLMENT.c_id='CS503') AND subrecord.s_id=ENROLMENT.s_id;

--Query4: Find the name of the TEACHER teaching MA525.
select Te.t_name from TEACHER AS Te, COURSE_SCHEDULE AS CS where Te.t_id=CS.t_id AND CS.c_id='MA525';

 --Query 5: Find the name(s) of all STUDENTs enrolled in one or three COURSEs.
SELECT S.s_name FROM STUDENT AS S INNER JOIN ENROLMENT AS E ON E.s_id = S.s_id GROUP BY S.s_id, S.s_name HAVING COUNT(*) = 3 or count(*)=1;

 --Query6: Find the name(s) of all STUDENTs who are being taught by Prof. Christopher Clifton.
select S.s_name from STUDENT AS S , ENROLMENT AS E, COURSE_SCHEDULE AS CS, TEACHER AS  Te  where S.s_id=E.s_id AND E.c_id=CS.c_id AND CS.t_id=Te.t_id AND Te.t_name='Christopher Clifton';

--Query7: Name any undergraduate COURSE(s) being taken by graduate STUDENT(s).
select Ce.c_name from COURSE AS Ce,STUDENT AS S,ENROLMENT AS E where Ce.c_id=E.c_id AND E.s_id=S.s_id AND S.s_status='GR';


--Query8: Name any undergraduate STUDENT(s) who is taking a COURSE with Prof. Sheron Noel.
select S.s_name from STUDENT as S where S.s_status!='GR' and S.s_name in (select S.s_name from STUDENT as s, COURSE as Co,TEACHER as T,ENROLMENT as E,COURSE_SCHEDULE as CS where S.s_id =E.s_id AND E.c_id=Co.c_id and Co.c_id=CS.c_id and CS.t_id=T.t_id AND T.t_name='Sheron Noel');
