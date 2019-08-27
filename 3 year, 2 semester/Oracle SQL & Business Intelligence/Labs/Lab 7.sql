REM   Script: Lab 7
REM   lab 7

-- Task 1 - Рефлексивное соединение. Представление отношений родитель-потомок
-- Требуется представить имя каждого сотрудника таблицы EMP, а также имя его руководителя.
SELECT CONCAT(e1.empname, CONCAT(' works for ', e2.empname)) emp_manager 
FROM emp e1 JOIN EMP e2 ON e1.manager_id=e2.empno;

-- Task 2 - Иерархический запрос
-- Требуется представить имя каждого сотрудника таблицы EMP (даже сотрудника, которому не назначен руководитель) и имя его руководителя.
SELECT empno, empname, manager_id 
FROM emp 
START WITH manager_id is NULL 
CONNECT BY PRIOR empno = manager_id;

-- Task 2.1
SELECT CONCAT(empname, CONCAT(' reports to ', PRIOR empname)) walk_top_down 
FROM emp 
START WITH manager_id is NULL 
CONNECT BY PRIOR empno = manager_id;

-- Task 3 - Представление отношений потомок-родитель-прародитель
-- Требуется показать иерархию от CLARK до JOHN KLINTON.
SELECT ltrim(sys_connect_by_path(empname,'-->'),'-->') 
leaf___branch___root 
FROM emp 
WHERE LEVEL=3 
START WITH empname='CLARK' 
CONNECT BY PRIOR manager_id = empno;

-- Task 4 - Иерархическое представление таблицы
-- Требуется получить результирующее множество, описывающее иерархию всей таблицы.
SELECT ltrim(sys_connect_by_path(empname,'-->'),'-->') 
leaf___branch___root 
FROM emp 
START WITH manager_id is NULL 
CONNECT BY PRIOR empno = manager_id;

-- Task 5 - Представление уровня иерархии
-- Требуется показать уровень иерархии каждого сотрудника.
SELECT LPAD(empname, LENGTH(empname)+2*(level-1), '_') org_chart 
FROM emp 
START WITH manager_id is NULL 
CONNECT BY PRIOR empno = manager_id;

-- Task 6 - Выбор всех дочерних строк для заданной строки
-- Требуется найти всех служащих, которые явно или неявно подчиняются ALLEN.
SELECT empname 
FROM emp 
START WITH empname='ALLEN' 
CONNECT BY PRIOR empno = manager_id;

