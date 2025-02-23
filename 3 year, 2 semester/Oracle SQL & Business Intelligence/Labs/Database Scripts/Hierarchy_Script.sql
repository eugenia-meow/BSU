REM   Script: Hierarchy_Script
REM   Hierarchy_Script

DROP TABLE CAREER;

DROP TABLE SALARY;

DROP TABLE EMP;

DROP TABLE DEPT;

DROP TABLE JOB;

CREATE TABLE DEPT 
       (DEPTNO NUMBER(2) 
             PRIMARY KEY, 
	DEPTNAME VARCHAR2(50) 
             NOT NULL,   
	DEPTADDR VARCHAR2(50));

COMMIT


INSERT INTO DEPT VALUES 
	(10, 'ACCOUNTING',   'NEW YORK');

INSERT INTO DEPT VALUES  
        (20, 'RESEARCH',     'DALLAS');

INSERT INTO DEPT VALUES 
	(30, 'SALES',        'CHICAGO');

INSERT INTO DEPT VALUES 
	(40, 'OPERATIONS',   'BOSTON');

COMMIT


CREATE TABLE EMP 
       (EMPNO NUMBER(4) 
             PRIMARY KEY, 
	EMPNAME VARCHAR2(30) 
             NOT NULL,  
        BIRTHDATE DATE,  
        MANAGER_ID NUMBER(4)  
	     REFERENCES EMP(EMPNO));

INSERT INTO EMP VALUES 
    (7790, 'JOHN KLINTON',    to_date('9-07-1980', 'dd-mm-yyyy'), NULL);

INSERT INTO EMP VALUES 
    (7499, 'ALLEN',           to_date('20-2-1961','dd-mm-yyyy'), 7790);

INSERT INTO EMP VALUES 
    (7521, 'WARD',            to_date('22-2-1958','dd-mm-yyyy'), 7790);

INSERT INTO EMP VALUES 
    (7566,'JONES',            to_date('2-4-1973','dd-mm-yyyy'), 7790);

INSERT INTO EMP VALUES 
    (7789, 'ALEX BOUSH',      to_date('21-09-1982', 'dd-mm-yyyy'), 7790);

INSERT INTO EMP VALUES 
    (7369, 'SMITH',           to_date('17-12-1948','dd-mm-yyyy'), 7789);

INSERT INTO EMP VALUES 
    (7654,'JOHN MARTIN',      to_date('28-9-1945','dd-mm-yyyy'), 7789);

INSERT INTO EMP VALUES 
    (7698,'RICHARD MARTIN',   to_date('1-5-1981','dd-mm-yyyy'), 7789);

INSERT INTO EMP VALUES 
    (7782,'CLARK',            NULL, 7499);

INSERT INTO EMP VALUES 
    (7788,'SCOTT',            to_date('13-08-1987', 'dd-mm-yyyy'), 7499);

COMMIT


CREATE TABLE JOB 
       (JOBNO NUMBER(4) 
             PRIMARY KEY, 
	JOBNAME VARCHAR2(30) 
             NOT NULL,  
        MINSALARY NUMBER(6)) ;

COMMIT


INSERT INTO JOB VALUES 
    (1000, 'MANAGER',               2500);

INSERT INTO JOB VALUES 
    (1001, 'FINANCIAL DIRECTOR',    7500);

INSERT INTO JOB VALUES 
    (1002, 'EXECUTIVE DIRECTOR',    8000);

INSERT INTO JOB VALUES 
    (1003, 'SALESMAN',              1500);

INSERT INTO JOB VALUES 
    (1004, 'CLERK',                  500);

INSERT INTO JOB VALUES 
    (1005, 'DRIVER',                1800);

INSERT INTO JOB VALUES 
    (1006, 'PRESIDENT',            15000);

COMMIT


CREATE TABLE CAREER 
       (JOBNO NUMBER(4) 
             REFERENCES JOB(JOBNO) NOT NULL, 
        EMPNO NUMBER(4) 
             REFERENCES EMP(EMPNO) NOT NULL, 
        DEPTNO NUMBER(4) 
             REFERENCES DEPT(DEPTNO), 
	STARTDATE DATE 
             NOT NULL,  
	ENDDATE DATE) ;

COMMIT


INSERT INTO CAREER VALUES 
    (1004, 7698, 10, to_date('21-5-1999','dd-mm-yyyy'), to_date('1-6-1999','dd-mm-yyyy'));

INSERT INTO CAREER VALUES 
    (1003, 7698, 10, to_date('1-6-2010','dd-mm-yyyy'), NULL);

INSERT INTO CAREER VALUES 
    (1003, 7369, 20, to_date('21-5-2005','dd-mm-yyyy'), NULL);

INSERT INTO CAREER VALUES 
    (1001, 7499, 30, to_date('2-1-2003','dd-mm-yyyy'), to_date('31-12-2005','dd-mm-yyyy'));

INSERT INTO CAREER VALUES 
    (1004, 7654, 20, to_date('21-7-1999','dd-mm-yyyy'), to_date('1-6-2004','dd-mm-yyyy'));

INSERT INTO CAREER VALUES 
    (1002, 7499, 30, to_date('1-6-2006','dd-mm-yyyy'), to_date('25-10-2008','dd-mm-yyyy'));

INSERT INTO CAREER VALUES 
    (1001, 7499, NULL, to_date('12-10-2006','dd-mm-yyyy'), NULL);

INSERT INTO CAREER VALUES 
    (1004, 7369, 30, to_date('1-7-2000','dd-mm-yyyy'), NULL);

INSERT INTO CAREER VALUES 
    (1001, 7499, 10, to_date('1-1-2008','dd-mm-yyyy'), NULL);

INSERT INTO CAREER VALUES 
    (1005, 7789, 40, to_date('1-1-2001','dd-mm-yyyy'), NULL);

INSERT INTO CAREER VALUES 
    (1006, 7790, 40, to_date('1-10-2001','dd-mm-yyyy'), NULL);

COMMIT


CREATE TABLE SALARY 
       (EMPNO NUMBER(4) 
             REFERENCES EMP(EMPNO), 
        MONTH NUMBER(2) 
             CHECK(MONTH>0 AND MONTH<13), 
        YEAR NUMBER(4) 
             CHECK(YEAR>1987 AND YEAR<2017), 
	SALVALUE NUMBER(6));

COMMIT


INSERT INTO SALARY VALUES 
    (7369, 05, 2007, 2580);

INSERT INTO SALARY VALUES 
    (7369, 06, 2007, 2650);

INSERT INTO SALARY VALUES 
    (7369, 07, 2007, 2510);

INSERT INTO SALARY VALUES 
    (7369, 08, 2007, 2495);

INSERT INTO SALARY VALUES 
    (7369, 09, 2007, 1750);

INSERT INTO SALARY VALUES 
    (7369, 10, 2007, 3540);

INSERT INTO SALARY VALUES 
    (7369, 11, 2007, 2580);

INSERT INTO SALARY VALUES 
    (7369, 12, 2007, 2050);

INSERT INTO SALARY VALUES 
    (7789, 01, 2008, 1850);

INSERT INTO SALARY VALUES 
    (7789, 02, 2008, 1900);

INSERT INTO SALARY VALUES 
    (7789, 03, 2008, 1950);

INSERT INTO SALARY VALUES 
    (7789, 04, 2008, 1950);

INSERT INTO SALARY VALUES 
    (7790, 05, 2009, 600);

INSERT INTO SALARY VALUES 
    (7790, 06, 2009, 650);

INSERT INTO SALARY VALUES 
    (7790, 07, 2009, 700);

INSERT INTO SALARY VALUES 
    (7499, 08, 2010, 8050);

INSERT INTO SALARY VALUES 
    (7499, 09, 2010, 8050);

INSERT INTO SALARY VALUES 
    (7499, 10, 2010, 8150);

INSERT INTO SALARY VALUES  
    (7369, 01, 2015, 3000);

INSERT INTO SALARY VALUES  
    (7369, 02, 2015, 3000);

INSERT INTO SALARY VALUES  
    (7369, 03, 2015, 3000);

INSERT INTO SALARY VALUES  
    (7369, 04, 2015, 3000);

INSERT INTO SALARY VALUES  
    (7369, 05, 2015, 3000);

INSERT INTO SALARY VALUES  
    (7499, 01, 2015, 3200);

INSERT INTO SALARY VALUES  
    (7499, 02, 2015, 3200);

INSERT INTO SALARY VALUES  
    (7499, 03, 2015, 3200);

INSERT INTO SALARY VALUES  
    (7499, 04, 2015, 3200);

INSERT INTO SALARY VALUES  
    (7499, 05, 2015, 3200);

INSERT INTO SALARY VALUES  
    (7499, 01, 2016, 3500);

INSERT INTO SALARY VALUES  
    (7499, 02, 2016, 3500);

INSERT INTO SALARY VALUES  
    (7499, 03, 2016, 3500);

INSERT INTO SALARY VALUES  
    (7499, 04, 2016, 3500);

INSERT INTO SALARY VALUES  
    (7369, 01, 2016, 3100);

INSERT INTO SALARY VALUES  
    (7369, 02, 2016, 3100);

INSERT INTO SALARY VALUES  
    (7369, 03, 2016, 3100);

COMMIT


select empno, empname, deptname,  jobname, salvalue, month, year  
from salary join (job join (dept join (emp join career using(empno)) using(deptno)) using(jobno)) using(empno);

