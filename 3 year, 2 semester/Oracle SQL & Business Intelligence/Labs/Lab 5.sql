REM   Script: Lab 5
REM   lab 5

-- Task 1
-- Используя функцию RANK выполнить ранжирование значений средних зарплат по годам.
SELECT year, avg_salary, RANK() OVER(ORDER BY avg_salary) salary_rank   
FROM   
(SELECT year, ROUND(AVG(salvalue),2) avg_salary   
FROM SALARY  
GROUP BY year);

-- Task 2
-- Используя функцию DENSE_RANK выполнить ранжирование значений суммарных зарплат по годам и месяцам.
SELECT year, month, sum_salary, DENSE_RANK() OVER(ORDER BY sum_salary) salary_rank   
FROM   
(SELECT year, month, SUM(salvalue) sum_salary   
FROM SALARY  
GROUP BY year, month);

-- Task 3.1
-- Используя функции RANK и DENSE_RANK выполнить ранжирование значений зарплат по годам и месяцам для каждого имени сотрудника (PARTITION BY).
SELECT empname, year, month, salvalue, RANK() OVER(PARTITION BY empname ORDER BY salvalue) salary_rank    
FROM SALARY JOIN EMP USING(empno);

-- Task 3.2
SELECT empname, year, month, salvalue, DENSE_RANK() OVER(PARTITION BY empname ORDER BY salvalue) salary_rank    
FROM SALARY JOIN EMP USING(empno);

-- Task 4
-- Используя функцию RANK выполнить ранжирование значений средних зарплат по годам и месяцам, по годам, по месяцам (CUBE, GROUPING_ID).
SELECT year, month, avg_salary, RANK() OVER(PARTITION BY category ORDER BY avg_salary DESC) salary_rank    
FROM    
(SELECT year, month, ROUND(AVG(salvalue),2) avg_salary,    
GROUPING(year) || GROUPING(month) AS category    
FROM SALARY   
GROUP BY CUBE(year, month));

-- Task 5
-- Используя функцию CUME_DIST определить позицию зарплаты сотрудника относительно должностей.
SELECT jobname, empname, salvalue, ROUND(CUME_DIST() OVER (PARTITION BY jobname ORDER BY salvalue),3) cume_dist   
FROM SALARY JOIN EMP USING(empno) JOIN CAREER USING(empno) JOIN JOB USING(jobno);

-- Task 6
-- Используя функцию PERCENT_RANK определить позицию зарплаты сотрудника относительно должностей.
SELECT jobname, empname, salvalue, ROUND(PERCENT_RANK() OVER (PARTITION BY jobname ORDER BY salvalue),3) percent_rank  
FROM SALARY JOIN EMP USING(empno) JOIN CAREER USING(empno) JOIN JOB USING(jobno);

