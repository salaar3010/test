print('''
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


hi bhags i see you !!

      ''')


