REM   Script: Lab 6
REM   lab 6

-- Task 1 - Добавление, вычитание дней, месяцев, лет
-- Требуется используя значения столбца START_DATE получить дату за десять дней до и после приема на работу, пол года до и после приема на работу, год до и после приема на работу сотрудника JOHN KLINTON.
SELECT empno, empname,   
startdate, startdate+10 later, startdate-10 before,   
ADD_MONTHS(startdate,6) half_later, ADD_MONTHS(startdate,-6) half_before,  
ADD_MONTHS(startdate,12) year_later, ADD_MONTHS(startdate,-12) year_before  
FROM CAREER JOIN EMP USING(empno)   
WHERE empname='JOHN KLINTON';

-- Task 2 - Определение количества дней между двумя датами
-- Требуется найти  разность  между  двумя  датами  и  представить  результат  в  днях. Вычислите  разницу  в  днях  между  датами  приема  на  работу  сотрудников JOHN MARTIN и ALEX BOUSH.
WITH   
T1 as (  
    SELECT startdate  
    FROM CAREER JOIN EMP USING(empno)   
    WHERE empname='JOHN MARTIN'  
),   
T2 as (  
    SELECT startdate  
    FROM CAREER JOIN EMP USING(empno)   
    WHERE empname='ALEX BOUSH'  
)  
SELECT T1.startdate d1, T2.startdate d2, T2.startdate-T1.startdate difference FROM T1, T2


-- Task 3 - Определение количества месяцев или лет между датами
-- Требуется найти разность между двумя датамив месяцах и в годах.
SELECT startdate, enddate, ROUND(MONTHS_BETWEEN(enddate,startdate)) months_between, FLOOR(MONTHS_BETWEEN(enddate,startdate)/12) years_between  
FROM CAREER JOIN EMP USING(empno)   
WHERE empname='JOHN MARTIN';

-- Task 4 - Определение интервала времени между текущей и следующей записями
-- Требуется определить интервал времени в днях между двумя датами. Для каждого сотрудника 20-го отделе найти сколько дней прошло между датой его приема на работу и датой приема на работу следующего сотрудника.
SELECT empname, deptno, startdate, next_startdate, next_startdate-startdate difference  
FROM (  
    SELECT empname, deptno, startdate,  
    LEAD(startdate) OVER(ORDER BY startdate) next_startdate  
    FROM CAREER JOIN EMP USING(empno)  
    WHERE deptno='20'  
);

-- Task 5 - Определение количества дней в году
-- Требуется подсчитать количество дней в году по столбцу START_DATE.
SELECT startdate, cur_year, ADD_MONTHS(cur_year,12) next_year, EXTRACT(year FROM cur_year) year, ADD_MONTHS(cur_year,12)-cur_year days,  
CASE ADD_MONTHS(cur_year,12)-cur_year  
    WHEN 366 THEN 'leap'  
END as is_leap  
FROM (  
    SELECT startdate, cur_year, year,   
    ROW_NUMBER() OVER (PARTITION BY year ORDER BY startdate) AS rn  
    FROM (  
        SELECT startdate, TRUNC(startdate, 'YEAR') cur_year, EXTRACT(year FROM TRUNC(startdate, 'YEAR')) year  
        FROM CAREER  
    )  
)  
WHERE rn = 1  
ORDER BY year;

-- Task 6 - Извлечение единиц времени из даты
-- Требуется разложить  текущую  дату  на  день,  месяц,  год,  секунды,  минуты,  часы. Результаты вернуть в численном виде.
SELECT TO_CHAR(CURRENT_DATE, 'DD-MON-YYYY HH:MI:SS') cur_date, 
TO_CHAR(CURRENT_DATE, 'hh24') hours, 
TO_CHAR(CURRENT_DATE, 'mi') minutes, 
TO_CHAR(CURRENT_DATE, 'ss') seconds, 
TO_CHAR(CURRENT_DATE, 'dd') days, 
TO_CHAR(CURRENT_DATE, 'mm') months, 
TO_CHAR(CURRENT_DATE, 'yyyy') years 
FROM DUAL;

-- Task 7 - Определение первого и последнего дней месяца
-- Требуется получить первый и последний дни текущего месяца.
SELECT CURRENT_DATE cur_date,  
TRUNC(CURRENT_DATE, 'month') first_day,  
LAST_DAY(CURRENT_DATE) last_day  
FROM DUAL;

-- Task 8
-- Требуется возвратить даты начала и конца каждого из четырех кварталов данного года.
SELECT num_quarter, 
ADD_MONTHS(start_year, (num_quarter-1)*3 ) first_day, 
LAST_DAY(ADD_MONTHS(start_year, (num_quarter-1)*3+2)) last_day 
FROM ( 
    SELECT TO_DATE('01-jan-2019', 'dd-mon-yyyy') start_year, 
    ROWNUM num_quarter 
    FROM EMP 
    WHERE ROWNUM <= 4 
);

-- Task 9 - Выбор всех дат года, выпадающих на определенный день недели
-- Требуется найти  все  даты  года,  соответствующие  заданному  дню недели. Сформируйте список понедельников текущего года.
SELECT num, mondays 
FROM ( 
    SELECT cur_year, ROWNUM num, NEXT_DAY(cur_year, 'MON') + ((LEVEL - 1 ) * 7 ) mondays 
    FROM ( 
        SELECT TRUNC(CURRENT_DATE, 'year') cur_year FROM DUAL 
    ) 
    CONNECT BY LEVEL <= 53 
) 
WHERE TO_DATE(mondays, 'DD-MON-YY') < ADD_MONTHS(cur_year,12);

-- Task 10 - Создание календаря
-- Требуется создать  календарь  на  текущий  месяц.  Календарь  должен  иметь  семь столбцов в ширину и пять строк вниз.
WITH  
T1 as ( 
    SELECT week_number, day_number, week_day 
    FROM ( 
        SELECT cur_month, day, 
        TO_CHAR(day, 'iw') week_number, 
        TO_CHAR(day, 'dd') day_number, 
        TO_NUMBER(TO_CHAR(day, 'd')) week_day 
        FROM ( 
            SELECT TRUNC(CURRENT_DATE, 'month') cur_month, 
            TRUNC(CURRENT_DATE, 'month') + LEVEL -1 day 
            FROM DUAL 
            CONNECT BY LEVEL <=31 
        ) 
    ) 
    WHERE day < ADD_MONTHS(cur_month,1) 
) 
SELECT  
MAX (CASE week_day WHEN 2 THEN day_number END) "Пн", 
MAX (CASE week_day WHEN 3 THEN day_number END) "Вт", 
MAX (CASE week_day WHEN 4 THEN day_number END) "Ср", 
MAX (CASE week_day WHEN 5 THEN day_number END) "Чт", 
MAX (CASE week_day WHEN 6 THEN day_number END) "Пт", 
MAX (CASE week_day WHEN 7 THEN day_number END) "Сб", 
MAX (CASE week_day WHEN 1 THEN day_number END) "Вс" 
FROM T1 
GROUP BY week_number 
ORDER BY week_number


