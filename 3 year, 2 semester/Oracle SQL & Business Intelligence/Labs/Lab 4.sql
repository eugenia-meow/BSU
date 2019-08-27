REM   Script: Lab 4
REM   lab 4

-- Task 1 - Создание блоков данных фиксированного размера
SELECT CEIL(ROW_NUMBER() OVER(ORDER BY jobno)/4) grp,   
jobno, jobname, minsalary   
FROM JOB;

-- Task 2 - Создание заданного количества блоков
SELECT NTILE(3) OVER  
(PARTITION BY year   
ORDER BY month) grp, year, month, salvalue  
FROM SALARY  
ORDER BY year, month;

-- Task 3 - Создание горизонтальных гистограмм
-- Отобразить количество служащих в виде горизонтальной гистограммы.
SELECT jobno, LPAD('+', COUNT(*), '+') cnt  
FROM CAREER  
GROUP BY jobno  
ORDER BY cnt;

-- Task 4 - Создание вертикальных гистограмм
-- Отобразить количество служащих в виде вертикальной гистограммы.
SELECT rn, MAX(jobno_1000) j1000,  
MAX(jobno_1001) j1001,  
MAX(jobno_1002) j1002,  
MAX(jobno_1003) j1003,  
MAX(jobno_1004) j1004,  
MAX(jobno_1005) j1005,  
MAX(jobno_1006) j1006  
FROM (SELECT ROW_NUMBER() OVER(PARTITION BY jobno ORDER BY empno) rn,  
CASE WHEN jobno=1000 THEN '+' ELSE NULL END jobno_1000,  
CASE WHEN jobno=1001 THEN '+' ELSE NULL END jobno_1001,  
CASE WHEN jobno=1002 THEN '+' ELSE NULL END jobno_1002,  
CASE WHEN jobno=1003 THEN '+' ELSE NULL END jobno_1003,  
CASE WHEN jobno=1004 THEN '+' ELSE NULL END jobno_1004,  
CASE WHEN jobno=1005 THEN '+' ELSE NULL END jobno_1005,  
CASE WHEN jobno=1006 THEN '+' ELSE NULL END jobno_1006  
FROM CAREER)  
GROUP BY rn  
ORDER BY 1 DESC;

