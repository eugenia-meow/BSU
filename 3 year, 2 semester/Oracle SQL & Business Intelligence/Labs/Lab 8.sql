REM   Script: Lab 8
REM   lab 8

SELECT table_name  
FROM all_tables 
WHERE table_name LIKE 'JO%';

SELECT SUBSTR(first_name, 1, 1) || ' ' || last_name "Employee Names" 
FROM employees;

SELECT first_name || ' ' || last_name "Employee Name", email  
FROM employees  
WHERE email LIKE '%IN%';

SELECT MIN(last_name) "First Last Name", MAX(last_name) "Last Last Name" 
FROM employees;

SELECT '$' || week_salary "Weekly Salary" 
FROM 
(SELECT ROUND(salary/30*7,2) week_salary 
FROM employees) 
WHERE week_salary BETWEEN 700 AND 3000;

SELECT SUBSTR(first_name, 1, 1) || ' ' || last_name "Employee Name", job_title job 
FROM employees JOIN jobs USING(job_id) 
ORDER BY job_title;

SELECT SUBSTR(first_name, 1, 1) || ' ' || last_name "Employee Name",  
job_title job,  
min_salary || '-' || max_salary "Salary Range",  
salary "Employee's Salary" 
FROM employees JOIN jobs USING(job_id) 
ORDER BY job_title;

SELECT SUBSTR(first_name, 1, 1) || ' ' || last_name "Employee Name", department_name "Department Name" 
FROM employees NATURAL JOIN departments 
ORDER BY department_name;

SELECT SUBSTR(first_name, 1, 1) || ' ' || last_name "Employee Name", department_name "Department Name" 
FROM employees JOIN departments USING(department_id) 
ORDER BY department_name;

SELECT DECODE(manager_id, NULL, 'Nobody', 'Somebody') "Works For", last_name "Last Name" 
FROM employees;

SELECT last_name "Last Name", salary "Salary", DECODE(commission_pct, NULL, 'No', 'Yes') "Commissions" 
FROM employees;

SELECT last_name, department_name, city, state_province 
FROM employees RIGHT OUTER JOIN departments USING(department_id) JOIN locations USING(location_id) 
ORDER BY last_name;

SELECT first_name "First Name", last_name "Last Name",  
CASE  
    WHEN commission_pct IS NOT NULL THEN commission_pct 
    WHEN manager_id IS NOT NULL THEN manager_id 
    ELSE -1 
END "Which function???" 
FROM employees;

SELECT e.last_name, e.salary, g.grade_level 
FROM employees e JOIN job_grades g ON e.salary BETWEEN g.lowest_sal AND g.highest_sal 
WHERE department_id > 50;

SELECT last_name, department_name 
FROM employees FULL JOIN departments USING(department_id);

SELECT level position, last_name, PRIOR last_name manager_name  
FROM employees  
START WITH manager_id is NULL   
CONNECT BY PRIOR employee_id = manager_id;

SELECT TO_CHAR(MIN(hire_date), 'dd-Mon-yyyy') "Lowest", TO_CHAR(MAX(hire_date), 'dd-Mon-yyyy') "Highest", COUNT(employee_id) "No of Employees"  
FROM employees;

SELECT *  
FROM 
    (SELECT department_name, SUM(salary) salaries 
    FROM employees JOIN departments USING(department_id) 
    GROUP BY department_name) 
WHERE salaries BETWEEN 15000 AND 31000 
ORDER BY salaries;

WITH 
t1 as ( 
    SELECT ROUND(AVG(salary)) avg_dept_salary, department_id  
    FROM employees  
    GROUP BY department_id 
), 
t2 as ( 
    SELECT d.department_id dept_id, d.department_name dept_name, d.manager_id mng_id, e.last_name manager_name 
    FROM departments d JOIN employees e ON d.manager_id=e.employee_id 
) 
SELECT t2.dept_name, t2.mng_id, t2.manager_name, t1.avg_dept_salary  
FROM t1 JOIN t2 ON t1.department_id = t2.dept_id 
ORDER BY t1.avg_dept_salary


SELECT MAX(ROUND(AVG(salary))) highest_avg_dept_salary 
FROM employees  
GROUP BY department_id;

SELECT department_name, SUM(salary) salaries 
FROM employees JOIN departments USING(department_id) 
GROUP BY department_name 
ORDER BY department_name;

SELECT  department_name, job_title, monthly_cost FROM 
    (SELECT GROUPING(department_name)||GROUPING(job_title) gr, department_name, job_title, SUM(salary) monthly_cost  
    FROM departments JOIN employees USING(department_id) JOIN jobs USING(job_id)  
    GROUP BY CUBE(department_name, job_title) 
    ORDER BY department_name, job_title) 
WHERE gr<>'10';

SELECT department_name, job_title, SUM(salary) monthly_cost  
FROM departments JOIN employees USING(department_id) JOIN jobs USING(job_id)  
GROUP BY CUBE(department_name, job_title)   
ORDER BY department_name, job_title;

SELECT department_name, job_title, SUM(salary) monthly_cost, 
CASE GROUPING(department_name) 
    WHEN 0 THEN 'Yes' 
    ELSE 'No' 
END dept_id_used, 
CASE GROUPING(job_title) 
    WHEN 0 THEN 'Yes' 
    ELSE 'No' 
END dept_id_used 
FROM departments JOIN employees USING(department_id) JOIN jobs USING(job_id)  
GROUP BY CUBE(department_name, job_title)   
ORDER BY department_name, job_title;

SELECT department_name, job_title, city, SUM(salary) monthly_cost 
FROM departments JOIN employees USING(department_id) JOIN jobs USING(job_id) JOIN locations USING(location_id) 
GROUP BY GROUPING SETS ((department_name, job_title), (city)) 
ORDER BY department_name, job_title, city;

SELECT SUBSTR(first_name, 1, 1) || ' ' || last_name "Employee Name", department_id, NULL AS department_name, NULL AS city 
FROM employees 
UNION 
SELECT NULL AS "Employee Name", department_id, department_name, NULL AS city 
FROM departments 
UNION 
SELECT NULL AS "Employee Name", NULL AS department_id, NULL AS department_name, city 
FROM locations;

SELECT SUBSTR(first_name, 1, 1) || ' ' || last_name "Employee Name", salary, department_name 
FROM  
    (SELECT department_id, ROUND(AVG(salary)) avg_salary 
    FROM employees 
    GROUP BY department_id) 
JOIN employees USING(department_id) JOIN departments USING(department_id)  
WHERE salary > avg_salary;

