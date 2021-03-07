/*DATABASE ASSIGMENT 2

Teamates :
--> Lohitha Yalavarthi (002289255)  (lyalavarthi@ubishops.ca)
--> Nitish Kumar Pilla (002286814)  (npilla@ubishops.ca)
--> Bhargav Movva      (002292699)  (BMOVVA21@ubishops.ca)*/

/* II. Programming with SQL
        Problem 2           */


-- query 1 - Solution to Find the titles of courses in the Comp. Sci. department that have 3 credits.
SELECT  title FROM course WHERE dept_name = 'Comp. Sci.' AND credits=3;


-- query 2 - solution to Find the IDs of all students who were taught by an instructor named Einstein
make sure there are no duplicates in the result.*/
SELECT DISTINCT student.id
FROM ( student JOIN takes ON student.id=takes.id )
      JOIN ( instructor JOIN teaches ON instructor.id=teaches.id)
      USING (course_id, sec_id, semester, year)
  WHERE instructor.name = 'Einstein';


-- query 3 - solution to Find the highest salary of any instructor.
SELECT MAX(salary) FROM instructor;


/* query 4 - solution to Find all instructors earning the highest salary
 (there may be more than one with the same salary). */
SELECT name FROM instructor WHERE salary = (SELECT max(salary) FROM instructor);


-- query 5 - solution to Find the enrollment of each section that was offered in Autumn 2009.
SELECT course_id,sec_id,count(id) FROM section JOIN takes
USING (course_id,sec_id, semester, year)
WHERE semester='Fall' and year=2009
GROUP BY course_id,sec_id;


-- query 6 -  Solution to Find the maximum enrollment, across all sections, in Autumn 2009.
with max_enroll_t as (SELECT course_id,sec_id,count(id) as enroll
   FROM section JOIN takes
   USING (course_id,sec_id, semester, year)
   WHERE semester = 'Fall' and  year = 2009
   GROUP BY course_id,sec_id)
SELECT enroll FROM max_enroll_t WHERE enroll=(SELECT max(enroll) FROM max_enroll_t);


-- query 7 -  Solution to Find the sections that had the maximum enrollment in Autumn 2009.
with enroll_t as (SELECT course_id,sec_id,count(id) as enroll
  FROM section JOIN takes
  USING (course_id,sec_id, semester, year)
  WHERE semester = 'Fall' and  year = 2009
  GROUP BY course_id,sec_id)
 SELECT course_id,sec_id,enroll
 FROM enroll_t
 WHERE enroll=(SELECT max(enroll) FROM enroll_t);


/* query 8 - Solution to Find the total grade-points earned by the student with ID 12345,
 across all courses taken by the student. */
SELECT sum(credits*points) FROM (takes JOIN course USING(course_id)) NATURAL JOIN grade_points
WHERE ID = '24746';


/* query 9 - Solution to Find the grade-point average (GPA) for the above student, that is,
the total grade-points divided by the total credits for the associated courses.*/
SELECT SUM(credits*points)/SUM(credits) AS GPA FROM (takes JOIN course USING(course_id)) NATURAL JOIN grade_points
WHERE ID='24746';


-- query 10 - Solution to Find the ID and the grade-point average of every student.
SELECT ID, sum(credits * points)/sum(credits) as GPA
FROM (takes JOIN course USING (course_id)) natural join grade_points
GROUP BY  ID;


-- query 11 - Solution to Increase the salary of each instructor in the Comp. Sci. department by 10%.
UPDATE instructor SET salary = salary * 1.10 WHERE dept_name = 'Comp. Sci.';


-- query 12 - Solution to Delete all courses that have never been offered (that is, do not occur in the section relation).
DELETE FROM course WHERE course_id not in (SELECT course_id FROM section);


-- query 13 - Solution to Insert every student whose tot_cred attribute is greater than 100 as an instructor
-- in the same department, with a salary of $10,000.*/
INSERT into instructor SELECT id, name, dept_name, 10000 FROM student
WHERE tot_cred > 100;
