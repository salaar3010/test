print(
    '''
Create Table:
CREATE TABLE emp (
    empno NUMBER(4) PRIMARY KEY,                
    ename VARCHAR2(10) NOT NULL,                
    job   VARCHAR2(9),
    mgr   NUMBER(4),
    hiredate DATE DEFAULT SYSDATE,              
    sal   NUMBER(7,2) CHECK (sal > 0),          
    comm  NUMBER(7,2),
    deptno NUMBER(2),
    CONSTRAINT fk_dept FOREIGN KEY (deptno) REFERENCES dept(deptno)  
);

CREATE TABLE dept (
    deptno NUMBER(2) PRIMARY KEY,       
    dname VARCHAR2(14) UNIQUE,          
    loc   VARCHAR2(13) DEFAULT 'CHENNAI'  
);
Inserting

TO_DATE('date_string', 'format_model')
INSERT INTO emp (empno, ename, hiredate, deptno)
VALUES (1007, 'MILLER', SYSDATE, 10);









ALTER Table

1. The main command used to change the structure of an existing table.
ALTER TABLE table_name <subcommand>;

2. ADD — Add New Columns or Constraints
ALTER TABLE emp
ADD (email VARCHAR2(50));
ALTER TABLE emp
ADD CONSTRAINT chk_salary CHECK (sal > 0);

3. MODIFY — Change an Existing Column’s Definition
Used to change the datatype, size, or constraints of an existing column.
Example 1 — Increase column size
ALTER TABLE emp
MODIFY ename VARCHAR2(30);

Example 2 — Add NOT NULL constraint
ALTER TABLE emp
MODIFY job VARCHAR2(20) NOT NULL;

4. DROP COLUMN — Remove a Column
Used to delete a column from the table permanently.
 Example:
ALTER TABLE emp
DROP COLUMN comm;

5. DROP CONSTRAINT — Remove a Constraint
Used to delete a constraint like a primary key, foreign key, check, etc.
ALTER TABLE emp
DROP CONSTRAINT fk_dept;

6. RENAME COLUMN — Rename an Existing Column
ALTER TABLE emp
RENAME COLUMN ename TO employee_name;

7. RENAME (Table-Level) — Rename a Table
RENAME emp TO employee_master;

JOINS
Self-join
SELECT e.emp_name AS employee,
       m.emp_name AS manager
FROM emp28 e, emp28 m
WHERE e.mgr = m.emp_no;
 


| Join Type            | Description                       | Matching Type       | Missing Rows?            |
| -------------------- | --------------------------------- | ------------------- | ------------------------ |
| **Equi Join**        | Matches equal columns             | `=`                 | Excluded                 |
| **Non-Equi Join**    | Matches range                     | `BETWEEN`, `<`, `>` | Excluded                 |
| **Self Join**        | Table with itself                 | `=`                 | —                        |
| **Cross Join**       | Every row with every row          | none                | —                        |
| **Inner Join**       | Only matches                      | `=`                 | Excluded                 |
| **Left Outer Join**  | All from left, matched from right | `=`                 | Right side may show NULL |
| **Right Outer Join** | All from right, matched from left | `=`                 | Left side may show NULL  |
| **Full Outer Join**  | All from both                     | `=`                 | None excluded            |

Advance sub query concepts

SELECT columns
FROM table1 t1
WHERE EXISTS (
    SELECT 1
    FROM table2 t2
    WHERE t1.some_column = t2.some_column
);

Keyword	Meaning	Typical Use	Works With
IN	True if value matches any value in subquery	Equality comparisons	=, IN
EXISTS	True if subquery returns any row	Correlated subqueries	Logical check
ANY / SOME	True if condition is true for at least one value	Comparisons	=, <, >, <=, >=
ALL	True if condition is true for every value	Comparisons	=, <, >, <=, >=
NOT IN, NOT EXISTS, != ALL	Opposites of above	Exclusion filters	Same as above

Views

 Definition:
A VIEW is a virtual table based on the result of a SQL query.
It doesn’t store data itself — it just shows data from one or more base tables.
 Think of it like:
“A saved SQL query that behaves like a table.”

1.  Syntax

CREATE OR REPLACE VIEW view_name AS
SELECT columns
FROM table_name
WHERE condition;

 2. Example: Simple View
Task:
Create a view to display employee name, department name, and salary.

CREATE VIEW emp_dept_view AS
SELECT e.emp_name, d.dept_name, e.salary
FROM emp28 e
JOIN dept28 d USING (dept_no);

Now you can query it like a table:
SELECT * FROM emp_dept_view;


3. Create a view Employee_Department_View that includes employee name, department name, and manager name by joining the Employees and Departments tables.

SELECT e.emp_name AS employee_name,
       d.dept_name AS department_name,
       m.emp_name AS manager_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
LEFT JOIN employees m ON e.mgr_id = m.emp_id;






PL SQL
1.
SET SERVEROUTPUT ON;
BEGIN
   DBMS_OUTPUT.PUT_LINE('Hello salaar, welcome to PL/SQL!');
END;
/

2. DECLARING VARIABLES

DECLARE
   name VARCHAR2(20);
   salary NUMBER(8,2);
BEGIN
   name := 'salaar';
   salary := 85000;
   DBMS_OUTPUT.PUT_LINE('Name: ' || name);
   DBMS_OUTPUT.PUT_LINE('Salary: ' || salary);
END;
/

3. CONTROL STRUCTURES (IF-ELSE)

DECLARE
   salary NUMBER := 70000;
BEGIN
   IF salary > 80000 THEN
      DBMS_OUTPUT.PUT_LINE('High salary');
   ELSIF salary BETWEEN 50000 AND 80000 THEN
      DBMS_OUTPUT.PUT_LINE('Average salary');
   ELSE
      DBMS_OUTPUT.PUT_LINE('Low salary');
   END IF;
END;
/

4. LOOPS IN PL/SQL

BEGIN
   FOR i IN 1..5 LOOP
      DBMS_OUTPUT.PUT_LINE('Iteration ' || i);
   END LOOP;
END;
/
PROCEDURE IN PL/SQL
Basic Syntax
CREATE OR REPLACE PROCEDURE procedure_name (parameters)
IS
   -- Declaration section
BEGIN
   -- Executable section
EXCEPTION
   -- Error handling (optional)
END procedure_name;
/


2. Procedure for Inserting a Record
CREATE OR REPLACE PROCEDURE insert_emp
(
   p_empno   IN emp28.emp_no%TYPE,
   p_ename   IN emp28.emp_name%TYPE,
   p_salary  IN emp28.salary%TYPE,
   p_deptno  IN emp28.dept_no%TYPE
)
IS
BEGIN
   INSERT INTO emp28 (emp_no, emp_name, salary, dept_no)
   VALUES (p_empno, p_ename, p_salary, p_deptno);

   DBMS_OUTPUT.PUT_LINE('Record inserted successfully!');
END;
/

TO EXECUTE IT:
EXEC insert_emp(108, 'Gokul', 55000, 20);

3.PROCEDURE FOR FETCHING EMPLOYEE DETAILS
CREATE OR REPLACE PROCEDURE get_emp_details (p_empno IN emp28.emp_no%TYPE)
IS
   v_name   emp28.emp_name%TYPE;
   v_salary emp28.salary%TYPE;
BEGIN
   SELECT emp_name, salary
   INTO v_name, v_salary
   FROM emp28
   WHERE emp_no = p_empno;

   DBMS_OUTPUT.PUT_LINE('Employee: ' || v_name);
   DBMS_OUTPUT.PUT_LINE('Salary: ' || v_salary);
EXCEPTION
   WHEN NO_DATA_FOUND THEN
      DBMS_OUTPUT.PUT_LINE('No record found for employee no ' || p_empno);
END;
/

4. Procedure for Deleting a Record
CREATE OR REPLACE PROCEDURE delete_emp (p_empno IN emp28.emp_no%TYPE)
IS
BEGIN
   DELETE FROM emp28
   WHERE emp_no = p_empno;

   IF SQL%ROWCOUNT = 0 THEN
      DBMS_OUTPUT.PUT_LINE('No such employee found!');
   ELSE
      DBMS_OUTPUT.PUT_LINE('Employee record deleted successfully!');
   END IF;
END;
/

5. Procedure Showing All Employees
CREATE OR REPLACE PROCEDURE show_all_emps
IS
BEGIN
   FOR rec IN (SELECT emp_no, emp_name, salary, dept_no FROM emp28)
   LOOP
      DBMS_OUTPUT.PUT_LINE('EMP_NO: ' || rec.emp_no || 
                           ', NAME: ' || rec.emp_name || 
                           ', SALARY: ' || rec.salary ||
                           ', DEPT_NO: ' || rec.dept_no);
   END LOOP;
END;
/

TRIGGERS

1.Syntax of a Trigger
CREATE OR REPLACE TRIGGER trigger_name
BEFORE | AFTER
INSERT | UPDATE | DELETE
ON table_name
[FOR EACH ROW]
BEGIN
   -- Trigger logic here
END;
/

2. Simple Example — BEFORE INSERT Trigger
Let’s say we want to log a message whenever a record is inserted into EMP28.
CREATE OR REPLACE TRIGGER trg_before_insert
BEFORE INSERT
ON emp28
BEGIN
   DBMS_OUTPUT.PUT_LINE('A new record is being inserted into EMP28 table.');
END;
/

3. Row-Level Trigger (FOR EACH ROW)
Now let’s log details of the inserted record.
CREATE OR REPLACE TRIGGER trg_row_insert
AFTER INSERT
ON emp28
FOR EACH ROW
BEGIN
   DBMS_OUTPUT.PUT_LINE('Employee Inserted: ' || :NEW.emp_name || 
                        ' | Salary: ' || :NEW.salary);
END;
/
4.CREATE A TABLE STUDENT. CREATE A "TRIGGER" WHICH CALCULATES THE PERCENTAGE AUTOMATICALLY:

CREATE OR REPLACE TRIGGER stud
BEFORE INSERT OR UPDATE ON student
FOR EACH ROW
BEGIN
   :NEW.total := :NEW.m1 + :NEW.m2;
   :NEW.per := (:NEW.total / 2);
END;
/
5. Write a trigger which allows only positive values while inserting record.
create or replace trigger positive
 before insert on emp
for each row 
begin 
if :new.no < 0 then 
	raise_application_error(-20005,’Insert only positive values’);
end if;
end ;
/

6.WRITE A BLOCK THAT BACKUP OF ALL THE ROWS AUTOMATICALLY WHEN THEY ARE DELETED:
create or replace trigger backup 
before delete on emp1 
for each row 
begin 
insert into emp1_backup values (:old.no,:old.name,sysdate); 
end; 
/

7. CREATE A TRIGGER, WHICH VERIFY THAT UPDATED SALARY OF EMPLOYEE MUST BE
GREATER THAN HIS/HER PREVIOUS SALARY:

create or replace trigger verify_sal_inc
before update on emp28 
for each row 
begin 
if :old.salary > :new.salary then
	raise_application_error(-20001,'salary should be greater then prev');
end if;
end;
/

8. PREVENT EXCESS EMP’S:

CREATE OR REPLACE TRIGGER dept_emp_limit
BEFORE INSERT ON emp28
FOR EACH ROW
DECLARE
   u_count NUMBER;
BEGIN
   SELECT COUNT(*)
   INTO u_count
   FROM emp28
   WHERE dept_no = :NEW.dept_no;

   IF u_count >= 5 THEN
      RAISE_APPLICATION_ERROR(-20001, 'Number of employees in a department cannot exceed 5');
   END IF;
END;
/

9. PREVENT DELETING AN EMPLOYEE FROM HR DEPARTMENT:

CREATE OR REPLACE TRIGGER trg_no_delete_hr
BEFORE DELETE
ON emp28
FOR EACH ROW
BEGIN
   IF :OLD.dept_no = 10 THEN
      RAISE_APPLICATION_ERROR(-20001, 'You cannot delete employees from the HR department!');
   END IF;
END;
/

10. STOP UPDATING DEPARTMENT NUMBER:

CREATE OR REPLACE TRIGGER trg_no_dept_change
BEFORE UPDATE OF dept_no
ON emp28
FOR EACH ROW
BEGIN
   RAISE_APPLICATION_ERROR(-20005, 'Department number cannot be changed!');
END;
/


PL FUNCTIONS

Basic Syntax

CREATE OR REPLACE FUNCTION function_name (parameter_list)
RETURN datatype
IS
   -- Variable declarations
BEGIN
   -- Executable statements
   RETURN value;
EXCEPTION
   -- Error handling (optional)
END function_name;
/

Example 1 — Simple Function (Add Two Numbers)
CREATE OR REPLACE FUNCTION add_numbers(a NUMBER, b NUMBER)
RETURN NUMBER
IS
   sum_result NUMBER;
BEGIN
   sum_result := a + b;
   RETURN sum_result;
END;
/

'''

)


