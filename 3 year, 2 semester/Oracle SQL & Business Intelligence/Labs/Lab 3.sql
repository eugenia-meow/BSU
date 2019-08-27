REM   Script: Lab 3
REM   lab 3

-- Task 1 - Вычисление простых подсумм
-- Получить результирующее множество, содержащее количество сотрудников в
каждом отделе, а также общее количество сотрудников.
SELECT   
CASE GROUPING(DEPTNAME)   
WHEN 0 THEN DEPTNAME   
ELSE 'TOTAL'   
END AS DEPTNAME, COUNT(EMPNO) AS EMP_COUNT FROM DEPT JOIN CAREER USING(DEPTNO)  
GROUP BY ROLLUP(DEPTNAME);

-- Task 2 - Вычисление подсумм для всех возможных сочетаний
-- Требуется найти количество сотрудников по отделам, по должностям и для
каждого сочетания DEPTNAME/JOBNAME.
SELECT DEPTNAME, JOBNAME,   
CASE GROUPING(DEPTNAME) || GROUPING(JOBNAME)  
WHEN '00' THEN 'TOTAL BY DEPTNAME AND JOBNAME'  
WHEN '01' THEN 'TOTAL BY DEPTNAME'  
WHEN '10' THEN 'TOTAL BY JOBNAME'  
WHEN '11' THEN 'GRAND TOTAL'  
END AS CATEGORY,  
COUNT(EMPNO) EMP_COUNT FROM DEPT JOIN CAREER USING(DEPTNO) JOIN JOB USING(JOBNO)  
GROUP BY CUBE(DEPTNAME, JOBNAME)  
ORDER BY GROUPING(DEPTNAME), GROUPING(JOBNAME), DEPTNAME, JOBNAME;

-- Task 3 - Вычисление подсумм для всех возможных сочетаний
-- Требуется найти среднее значение суммы всех заработных плат по отделам, по
должностям и для каждого сочетания DEPTNAME/JOBNAME.
SELECT DEPTNAME, JOBNAME,   
CASE GROUPING(DEPTNAME) || GROUPING(JOBNAME)  
WHEN '00' THEN 'TOTAL BY DEPTNAME AND JOBNAME'  
WHEN '01' THEN 'TOTAL BY DEPTNAME'  
WHEN '10' THEN 'TOTAL BY JOBNAME'  
WHEN '11' THEN 'GRAND TOTAL'  
END AS CATEGORY,  
ROUND(AVG(MINSALARY)) AVG_SALARY FROM DEPT JOIN CAREER USING(DEPTNO) JOIN JOB USING(JOBNO)  
GROUP BY CUBE(DEPTNAME, JOBNAME)  
ORDER BY GROUPING(DEPTNAME), GROUPING(JOBNAME), DEPTNAME, JOBNAME;

-- Task 4 - Выявление строк, в которых представлены не подсуммы
-- Создайте запрос на распознавание строк, сформированных оператором GROUP
BY, и строк, являющихся результатом выполнения CUBE.
SELECT DEPTNAME, JOBNAME,   
CASE GROUPING(DEPTNAME) || GROUPING(JOBNAME)  
WHEN '00' THEN 'TOTAL BY DEPTNAME AND JOBNAME'  
WHEN '01' THEN 'TOTAL BY DEPTNAME'  
WHEN '10' THEN 'TOTAL BY JOBNAME'  
WHEN '11' THEN 'GRAND TOTAL'  
END AS CATEGORY,  
ROUND(AVG(MINSALARY)) AVG_SALARY,   
GROUPING(DEPTNAME) DEPT_SUBTOTAL,  
GROUPING(JOBNAME) JOB_SUBTOTAL  
FROM DEPT JOIN CAREER USING(DEPTNO) JOIN JOB USING(JOBNO)  
GROUP BY CUBE(DEPTNAME, JOBNAME)  
ORDER BY GROUPING(DEPTNAME), GROUPING(JOBNAME), DEPTNAME, JOBNAME;

-- Task 5-4 - Агрегация разных групп одновременно
-- Создайте запросы по заданиям пунктов 4-6.
Требуется выполнить агрегацию «в разных измерениях» одновременно. Например,
необходимо получить результирующее множество, в котором для каждого
сотрудника указаны имя, отдел, количество сотрудников в отделе (включая его
самого), количество сотрудников, занимающих ту же должность, что и этот
сотрудник (включая его самого), и общее число сотрудников в таблице.
SELECT EMPNAME, DEPTNAME,   
COUNT(*) OVER(PARTITION BY DEPTNAME) AS DEPTNAME_EMP_COUNT,   
JOBNAME,   
COUNT(*) OVER(PARTITION BY JOBNAME) AS JOBNAME_EMP_COUNT,   
COUNT(*) OVER() AS TOTAL  
FROM DEPT JOIN CAREER USING(DEPTNO) JOIN JOB USING(JOBNO) JOIN EMP USING(EMPNO);

-- Task 5-5 - Агрегация скользящего множества значений
-- Создайте запросы по заданиям пунктов 4-6.
Требуется выполнить скользящую агрегацию, например, найти скользящую сумму
заработных плат. Вычислять сумму для каждого интервала в 90 день, начиная с даты
приема на работу (поле STARTDATE таблицы CAREER) первого сотрудника, чтобы
увидеть динамику изменения расходов для каждого 90-дневного периода между
датами приема на работу первого и последнего сотрудника.
SELECT STARTDATE, SALVALUE,  
SUM(SALVALUE) OVER (ORDER BY STARTDATE RANGE BETWEEN 90 PRECEDING AND CURRENT ROW) SPENDING_PATTERN  
FROM CAREER JOIN SALARY USING(EMPNO)  
ORDER BY STARTDATE, YEAR, MONTH;

-- Task 5-6 - Определение доли от целого в процентном выражении
-- Создайте запросы по заданиям пунктов 4-6.
Требуется вывести множество числовых значений, представив каждое из них как
долю от целого в процентном выражении. Например, требуется получить
результирующее множество, отражающее распределение заработных плат по
должностям, чтобы можно было увидеть, какая из позиций JOB обходится компании
дороже всего.
SELECT DISTINCT JOBNAME,  
COUNT(*) OVER(PARTITION BY JOBNAME) AS NUM_EMPS,  
CONCAT(TO_CHAR(ROUND((RATIO_TO_REPORT(MINSALARY) OVER ())*100*(COUNT(*) OVER(PARTITION BY JOBNAME)), 2)),'%')   
AS PCT_OF_ALL_SALARIES  
FROM JOB JOIN CAREER USING(JOBNO)  
ORDER BY JOBNAME;

