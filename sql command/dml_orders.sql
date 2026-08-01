INSERT INTO orders
(order_id, customer_id, product_id, price, order_date, order_status, state, quantity)
SELECT
    gs AS order_id,
    (RANDOM() * 49 + 1)::INT AS customer_id,
    (RANDOM() * 99 + 1)::INT AS product_id,
    ROUND((RANDOM() * 900 + 100)::NUMERIC, 2)::REAL AS price,
    DATE '2025-01-01' + ((RANDOM() * 364)::INT) AS order_date,
    (ARRAY['Pending','Processing','Shipped','Delivered','Cancelled'])[FLOOR(RANDOM()*5 + 1)],
    (ARRAY[
        'California',
        'Texas',
        'Florida',
        'New York',
        'Illinois',
        'Arizona',
        'Washington',
        'Ohio',
        'Georgia',
        'Colorado'
    ])[FLOOR(RANDOM()*10 + 1)],
    (RANDOM() * 9 + 1)::INT AS quantity
FROM generate_series(1, 200) AS gs;