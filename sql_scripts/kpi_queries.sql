SELECT 
    region,
    SUM(revenue) AS total_revenue,
    SUM(units_sold) AS total_units
FROM sales_data
GROUP BY region;

SELECT 
    product,
    AVG(price) AS avg_price
FROM sales_data
GROUP BY product;
