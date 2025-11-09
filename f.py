print(
    '''
CHARACTER FUNCTIONS
| Function                           | Description                                        | Example Query                                            | Example Output  |
| ---------------------------------- | -------------------------------------------------- | -------------------------------------------------------- | --------------- |
| `LOWER(string)`                    | Converts string to lowercase                       | `SELECT LOWER('SIVA') FROM dual;`                        | `siva`          |
| `UPPER(string)`                    | Converts string to uppercase                       | `SELECT UPPER('siva') FROM dual;`                        | `SIVA`          |
| `INITCAP(string)`                  | Capitalizes first letter of each word              | `SELECT INITCAP('d m siva') FROM dual;`                  | `D M Siva`      |
| `LENGTH(string)`                   | Returns number of characters                       | `SELECT LENGTH('Siva') FROM dual;`                       | `4`             |
| `SUBSTR(string, m, n)`             | Returns substring from position `m` for length `n` | `SELECT SUBSTR('Siva',2,2) FROM dual;`                   | `iv`            |
| `INSTR(string, substring)`         | Returns position of substring                      | `SELECT INSTR('DataScience','Sci') FROM dual;`           | `5`             |
| `LPAD(string, len, pad_char)`      | Pads left side with given character                | `SELECT LPAD('Siva',8,'*') FROM dual;`                   | `****Siva`      |
| `RPAD(string, len, pad_char)`      | Pads right side                                    | `SELECT RPAD('Siva',8,'*') FROM dual;`                   | `Siva****`      |
| `LTRIM(string, chars)`             | Removes characters from left                       | `SELECT LTRIM('***Siva','*') FROM dual;`                 | `Siva`          |
| `RTRIM(string, chars)`             | Removes characters from right                      | `SELECT RTRIM('Siva***','*') FROM dual;`                 | `Siva`          |
| `TRIM(chars FROM string)`          | Removes characters from both ends                  | `SELECT TRIM('*' FROM '*Siva*') FROM dual;`              | `Siva`          |
| `REPLACE(string, search, replace)` | Replaces occurrences of a substring                | `SELECT REPLACE('SQL LAB','LAB','PRACTICAL') FROM dual;` | `SQL PRACTICAL` |
| `CONCAT(str1, str2)`               | Concatenates two strings                           | `SELECT CONCAT('Hello','World') FROM dual;`              | `HelloWorld`    |


 NUMERIC FUNCTIONS

 | Function                  | Description                       | Example Query                       | Example Output |
| ------------------------- | --------------------------------- | ----------------------------------- | -------------- |
| `ROUND(number, decimals)` | Rounds a number to given decimals | `SELECT ROUND(45.678,2) FROM dual;` | `45.68`        |
| `TRUNC(number, decimals)` | Truncates digits after decimals   | `SELECT TRUNC(45.678,2) FROM dual;` | `45.67`        |
| `MOD(m, n)`               | Returns remainder of division     | `SELECT MOD(10,3) FROM dual;`       | `1`            |
| `CEIL(number)`            | Smallest integer ≥ number         | `SELECT CEIL(4.2) FROM dual;`       | `5`            |
| `FLOOR(number)`           | Largest integer ≤ number          | `SELECT FLOOR(4.8) FROM dual;`      | `4`            |
| `POWER(m, n)`             | Returns m raised to power n       | `SELECT POWER(2,3) FROM dual;`      | `8`            |
| `ABS(number)`             | Returns absolute value            | `SELECT ABS(-10) FROM dual;`        | `10`           |
| `SIGN(number)`            | Returns -1, 0, or 1 based on sign | `SELECT SIGN(-20) FROM dual;`       | `-1`           |
| `SQRT(number)`            | Returns square root               | `SELECT SQRT(81) FROM dual;`        | `9`            |


 DATE FUNCTIONS

 | Function                    | Description                             | Example Query                                                                     | Example Output |
| --------------------------- | --------------------------------------- | --------------------------------------------------------------------------------- | -------------- |
| `SYSDATE`                   | Returns current system date and time    | `SELECT SYSDATE FROM dual;`                                                       | `08-NOV-25`    |
| `CURRENT_DATE`              | Returns current date (session timezone) | `SELECT CURRENT_DATE FROM dual;`                                                  | `08-NOV-25`    |
| `MONTHS_BETWEEN(d1, d2)`    | Returns months difference               | `SELECT MONTHS_BETWEEN(SYSDATE, TO_DATE('01-JAN-2020','DD-MON-YYYY')) FROM dual;` | `70.25`        |
| `ADD_MONTHS(date, n)`       | Adds months to date                     | `SELECT ADD_MONTHS(SYSDATE, 6) FROM dual;`                                        | `08-MAY-26`    |
| `NEXT_DAY(date, 'DAY')`     | Returns next given weekday              | `SELECT NEXT_DAY(SYSDATE,'FRIDAY') FROM dual;`                                    | `14-NOV-25`    |
| `LAST_DAY(date)`            | Returns last day of month               | `SELECT LAST_DAY(SYSDATE) FROM dual;`                                             | `30-NOV-25`    |
| `ROUND(date, format)`       | Rounds date to nearest month/year       | `SELECT ROUND(SYSDATE,'MONTH') FROM dual;`                                        | `01-DEC-25`    |
| `TRUNC(date, format)`       | Truncates date to given unit            | `SELECT TRUNC(SYSDATE,'MONTH') FROM dual;`                                        | `01-NOV-25`    |
| `TO_CHAR(date, 'format')`   | Converts date to string                 | `SELECT TO_CHAR(SYSDATE, 'DD-MON-YYYY') FROM dual;`                               | `08-NOV-2025`  |
| `TO_DATE(string, 'format')` | Converts string to date                 | `SELECT TO_DATE('30-10-2004','DD-MM-YYYY') FROM dual;`                            | `30-OCT-2004`  |

________________________________________
 NULL FUNCTIONS

 | Function                            | Description                          | Example Query                                    | Example Output        |
| ----------------------------------- | ------------------------------------ | ------------------------------------------------ | --------------------- |
| `NVL(expr1, expr2)`                 | Replaces NULL with given value       | `SELECT NVL(comm,0) FROM emp28;`                 | If `comm=NULL` → `0`  |
| `NVL2(expr1, expr2, expr3)`         | If expr1 not NULL → expr2 else expr3 | `SELECT NVL2(comm,'Yes','No') FROM emp28;`       | If `comm=NULL` → `No` |
| `NULLIF(expr1, expr2)`              | Returns NULL if expr1 = expr2        | `SELECT NULLIF(10,10) FROM dual;`                | `NULL`                |
| `COALESCE(expr1, expr2, expr3,...)` | Returns first non-NULL value         | `SELECT COALESCE(NULL, NULL, 'Siva') FROM dual;` | `Siva`                |

'''
)