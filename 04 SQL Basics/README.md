
# SQL Training Course - Unit 2: SQL Basics

This unit focuses on learning the fundamentals of databases using SQL. Below is an overview of the topics covered:

## 1. SQL Syntax
SQL (Structured Query Language) is the standard language for relational databases. It consists of commands to perform operations on the data:
- **SELECT**: To retrieve data from the database.
- **FROM**: Specifies the tables to select or delete from.
- **WHERE**: Filters records based on specified conditions.
- **INSERT INTO**: Adds new records to the database.
- **UPDATE**: Modifies existing data.
- **DELETE**: Removes data from the database.

Example:
```sql
SELECT name, age FROM students WHERE age > 18;
```

## 2. Data Types
Different databases support various data types, and you must define data types for each column. Key data types include:
- **INTEGER**: For whole numbers.
- **VARCHAR**: For text.
- **DATE**: For dates.
- **BOOLEAN**: For true/false values.
- **FLOAT/DOUBLE**: For decimal numbers.

Example:
```sql
CREATE TABLE employees (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  salary FLOAT,
  hire_date DATE
);
```

## 3. CRUD Operations
CRUD stands for Create, Read, Update, and Delete, the four basic operations on data:
- **Create**: Add new data.
- **Read**: Retrieve existing data.
- **Update**: Modify existing data.
- **Delete**: Remove data.

Examples:
- **Create**:
```sql
INSERT INTO employees (id, name, salary, hire_date)
VALUES (1, 'John Doe', 50000, '2024-01-01');
```
- **Read**:
```sql
SELECT * FROM employees;
```
- **Update**:
```sql
UPDATE employees SET salary = 55000 WHERE id = 1;
```
- **Delete**:
```sql
DELETE FROM employees WHERE id = 1;
```

## 4. Joins
Joins are used to retrieve data from multiple tables based on a relationship between them:
- **INNER JOIN**: Retrieves records that have matching values in both tables.
- **LEFT JOIN**: Retrieves all records from the left table and the matched records from the right table.
- **RIGHT JOIN**: Retrieves all records from the right table and the matched records from the left table.
- **FULL JOIN**: Retrieves all records when there is a match in either table.

Example:
```sql
SELECT students.name, courses.course_name
FROM students
INNER JOIN courses ON students.course_id = courses.id;
```

## 5. Aggregation Functions
Aggregation functions perform a calculation on a set of values and return a single value:
- **COUNT()**: Counts the number of records.
- **SUM()**: Adds values together.
- **AVG()**: Returns the average value.
- **MAX()**: Finds the maximum value.
- **MIN()**: Finds the minimum value.

Example:
```sql
SELECT COUNT(*) FROM employees;
SELECT AVG(salary) FROM employees;
```

## 6. Subqueries
A subquery is a SQL query nested inside another query. It is used to retrieve complex results or intermediate values.
Example:
```sql
SELECT name FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);
```

## 7. Indexes
Indexes improve the speed of data retrieval by creating a quick lookup table for records.
Example:
```sql
CREATE INDEX idx_salary ON employees (salary);
```

## 8. Transactions
A transaction is a group of SQL statements executed as a single unit. Transactions ensure data integrity by following the ACID properties:
- **Atomicity**: All operations are completed, or none are.
- **Consistency**: The database remains in a valid state.
- **Isolation**: Transactions do not interfere with each other.
- **Durability**: Changes are permanent once the transaction is committed.

Example:
```sql
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;
COMMIT;
```

## 9. Stored Procedures
A stored procedure is a collection of SQL statements stored in the database, which can be executed as needed. It offers improved performance and security by executing on the server side.
Example:
```sql
CREATE PROCEDURE RaiseSalary(IN emp_id INT, IN raise_amount FLOAT)
BEGIN
  UPDATE employees SET salary = salary + raise_amount WHERE id = emp_id;
END;
```

## 10. ORM (Object Relational Mapping)
ORM allows you to interact with a database using object-oriented programming concepts, without needing to write raw SQL queries. Popular ORM libraries include:
- **SQLAlchemy** (Python).
- **Hibernate** (Java).

ORM simplifies the development process by mapping database tables to objects in the code.

---

These topics aim to provide a comprehensive understanding of how to manage and work with relational databases using SQL.
