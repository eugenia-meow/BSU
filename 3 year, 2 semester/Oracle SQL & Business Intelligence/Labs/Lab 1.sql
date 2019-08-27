REM   Script: Lab 1
REM   Lab 1

-- Task 1
-- Выдать информацию о местоположении отдела продаж (SALES) компании.
SELECT * FROM DEPT 
WHERE DEPTNAME='SALES';

-- Task 2
-- Выдать информацию об отделах, расположенных в Chicago и New York.
SELECT * FROM DEPT 
WHERE DEPTADDR IN ('CHICAGO', 'NEW YORK');

-- Task 3
-- Найти минимальную заработную плату, начисленную в 2009 году.
SELECT MIN(SALVALUE) FROM SALARY 
WHERE YEAR=2009;

-- Task 4
-- Подсчитать число работников, сведения о которых имеются в базе данных.
SELECT COUNT(EMPNO) FROM EMP 
WHERE EMPNO IS NOT NULL AND EMPNAME IS NOT NULL AND BIRTHDATE IS NOT NULL;

-- Task 5
-- Выдать информацию о должностях, изменив названия должности “CLERK” и
“DRIVER” на “WORKER”.
SELECT JOBNO,  
CASE 
WHEN JOBNAME IN ('DRIVER', 'CLERK') THEN 'WORKER' 
ELSE JOBNAME 
END AS JOBNAME, MINSALARY 
FROM JOB;

-- Task 6
-- Определите максимальную зарплату за каждый год.
SELECT MAX(SALVALUE), YEAR FROM SALARY 
GROUP BY YEAR 
ORDER BY YEAR ASC;

-- Task 7
-- Определите среднюю зарплату за годы, в которые были начисления не менее чем
за три месяца.
SELECT AVG(SALVALUE), YEAR FROM SALARY 
GROUP BY YEAR HAVING COUNT(MONTH) >= 3 
ORDER BY YEAR ASC;

-- Task 8
-- Выполните декартово произведение таблиц EMP, CAREER, SALES.
SELECT * FROM EMP CROSS JOIN CAREER CROSS JOIN SALARY;

-- Task 9
-- Выведете ведомость получения зарплаты с указанием имен служащих. Выполните
сортировку по имени сотрудника (ORDER BY).
SELECT EMPNAME, MONTH, YEAR, SALVALUE FROM EMP JOIN SALARY ON EMP.EMPNO=SALARY.EMPNO 
ORDER BY EMPNAME, YEAR, MONTH;

-- Task 10
-- Выдайте сведения о карьере сотрудников с указанием их имён, наименования
должности, и названия отдела.
SELECT EMPNAME, JOBNAME, DEPTNAME FROM EMP 
JOIN CAREER ON EMP.EMPNO=CAREER.EMPNO JOIN JOB ON CAREER.JOBNO=JOB.JOBNO JOIN DEPT ON CAREER.DEPTNO=DEPT.DEPTNO 
ORDER BY EMPNAME;

-- Task 11
-- Найти имена сотрудников, получивших за годы начисления зарплаты
минимальную зарплату.
SELECT DISTINCT T1.EMPNAME, T1.SALVALUE, T1.YEAR FROM (SELECT EMPNAME, YEAR, SALVALUE FROM EMP JOIN SALARY ON EMP.EMPNO=SALARY.EMPNO) T1 
JOIN (SELECT MIN(SALVALUE) MIN_SALVALUE, YEAR FROM SALARY GROUP BY YEAR) T2  
ON T1.YEAR = T2.YEAR AND T1.SALVALUE = T2.MIN_SALVALUE 
ORDER BY T1.YEAR;

-- Task 12
-- Разделите сотрудников на возрастные группы: A) возраст 20-30 лет; B) 31-40 лет;
C) 41-50; D) 51-60 или возраст не определён.
SELECT EMPNAME, FLOOR(MONTHS_BETWEEN(CURRENT_DATE, BIRTHDATE)/12) AS AGE, 
CASE 
WHEN FLOOR(MONTHS_BETWEEN(CURRENT_DATE, BIRTHDATE)/12) BETWEEN 20 AND 30 THEN 'BETWEEN 20 AND 30' 
WHEN FLOOR(MONTHS_BETWEEN(CURRENT_DATE, BIRTHDATE)/12) BETWEEN 31 AND 40 THEN 'BETWEEN 31 AND 40' 
WHEN FLOOR(MONTHS_BETWEEN(CURRENT_DATE, BIRTHDATE)/12) BETWEEN 41 AND 50 THEN 'BETWEEN 41 AND 50' 
WHEN FLOOR(MONTHS_BETWEEN(CURRENT_DATE, BIRTHDATE)/12) > 50 OR FLOOR(MONTHS_BETWEEN(CURRENT_DATE, BIRTHDATE)/12) IS NULL THEN 'OLDER THAN 50 OR NO DATA' 
ELSE NULL 
END AS AGE_GROUP 
FROM EMP, DUAL;

