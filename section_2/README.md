# Thoughts
It is not idea to perform analytical queries on operational database, especially when it involves large amount of data like that below.
ODS should be setup and data should be ingested to proper DataWarehouse architecture (perhaps Kimball) which is optimised for these queries. 

#  List of our customers and their spending
```sql
WITH transaction_tab AS (
    SELECT
        customer_id
        ,   SUM(purchase_price) AS total_purchase_price
        ,   AVG(purchase_price) AS avg_purchase_price
        ,   MAX(purchase_price) AS max_purchase_price
        ,   MIN(purchase_price) AS min_purchase_price
        ,   COUNT(1)            AS purchase_count
    FROM
        transactions
    GROUP BY
        customer_id
)

SELECT
    c.customer_id
    ,   c.name
    ,   t.total_purchase_price
    ,   t.avg_purchase_price
    ,   t.max_purchase_price
    ,   t.min_purchase_price
    ,   t.purchase_count
FROM
    transaction_tab AS t
JOIN
    customers AS c
on  t.customer_id = c.customer_id
```

# Top 3 car manufacturers that customers bought by sales (quantity) and the sales number for it in the current month
Assumption: Top 3 car manufacturers here represent it has the highest total purchase **and** the highest purchase count. 
```sql
WITH transaction_tab AS (
    SELECT
        car_id,
        ,   purchase_price
    FROM
        transactions
    WHERE
        DATE_TRUNC('month', transaction_date) = DATE_TRUNC('month', current_date())
)

aggregates_tab AS (
    SELECT
        c.manufacturer
        ,   SUM(t.purchase_price) AS total_purchase_price
        ,   COUNT(1)              AS total_purchase_count
    FROM 
        transaction_tab AS t
    JOIN
        cars as c
    ON
        t.car_id = c.car_id
    GROUP BY
        c.manufacturer
)

ranking_tab AS (
    SELECT
        manufacturer
        ,   DENSE_RANK() OVER (ORDER BY total_purchase_price DESC) AS price_ranking
        ,   DENSE_RANK() OVER (ORDER BY total_purchase_count DESC) AS count_ranking
    FROM 
        aggregates_tab
)

SELECT
    manufacturer
FROM
    ranking_tab
WHERE
    price_ranking < 4 
    AND count_ranking < 4

```