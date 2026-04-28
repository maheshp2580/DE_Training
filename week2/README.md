# Week 2 – SQL Fundamentals for Data Engineering (Elite Training Version)

**Goal:** Build strong SQL fundamentals to query, filter, join, and analyze data confidently.

---

## 1. SELECT Statement

### Theory
`SELECT` is used to retrieve data from a table.

### Example
```sql
SELECT name, age FROM customers;
```

### Step-by-step Explanation
`SELECT` chooses the columns. `FROM` tells which table to get the data from.

### Exercises
1. Get all columns
2. Get only 'city'

### Common Mistakes
- Using wrong column names

### Trainer Notes
- Check if student understands column selection.

---

## 2. WHERE Clause

### Theory
Filters rows based on a condition.

### Example
```sql
SELECT * FROM customers WHERE age > 25;
```

### Step-by-step Explanation
Only rows with `age > 25` are returned.

### Exercises
1. Find customers from Chennai
2. Find age < 30

### Common Mistakes
- Using wrong operator

### Trainer Notes
- Ask student to explain condition in words.

---

## 3. ORDER BY

### Theory
Sorts data.

### Example
```sql
SELECT * FROM customers ORDER BY age DESC;
```

### Step-by-step Explanation
`DESC` = highest first, `ASC` = lowest first.

### Exercises
1. Sort by age ASC
2. Sort by name

### Common Mistakes
- Confusing ASC/DESC

### Trainer Notes
- Check understanding of sorting logic.

---

## 4. JOIN

### Theory
Combines data from multiple tables.

### Example
```sql
SELECT c.name, o.amount FROM customers c INNER JOIN orders o ON c.id = o.customer_id;
```

### Step-by-step Explanation
Matches rows using keys.

### Exercises
1. Join customers and orders
2. Get name + amount

### Common Mistakes
- Missing ON condition

### Trainer Notes
- Ensure student understands relationship.

---

## 5. GROUP BY

### Theory
Groups rows to apply aggregation.

### Example
```sql
SELECT city, COUNT(*) FROM customers GROUP BY city;
```

### Step-by-step Explanation
Groups rows by city.

### Exercises
1. Count per city
2. Sum amounts

### Common Mistakes
- Forgetting GROUP BY

### Trainer Notes
- Check aggregation logic.

---

## 6. HAVING

### Theory
Filters grouped results.

### Example
```sql
SELECT city, COUNT(*) FROM customers GROUP BY city HAVING COUNT(*) > 1;
```

### Step-by-step Explanation
`HAVING` works after grouping.

### Exercises
1. Cities with >1 customers

### Common Mistakes
- Using WHERE instead

### Trainer Notes
- Explain difference between WHERE vs HAVING.

---

## 7. NULL Handling

### Theory
`NULL` represents missing values.

### Example
```sql
SELECT * FROM customers WHERE age IS NULL;
```

### Step-by-step Explanation
Use `IS NULL`, not `= NULL`.

### Exercises
1. Find missing values

### Common Mistakes
- Using `= NULL`

### Trainer Notes
- Check understanding of missing data.

---

## 8. CASE Statement

### Theory
Conditional logic in SQL.

### Example
```sql
SELECT name, CASE WHEN age > 18 THEN 'Adult' ELSE 'Minor' END FROM customers;
```

### Step-by-step Explanation
Works like if-else.

### Exercises
1. Classify rows

### Common Mistakes
- Forgetting END

### Trainer Notes
- Ask student to explain logic.

---

## Trainer Notes (Elite)

**Focus on:**
- Concept clarity
- Real-world explanation
- Logical thinking

**Avoid:**
- Memorization
- Syntax-only learning

**Check:**
- Can student explain query in simple English?
- Can they relate SQL to business problem?
