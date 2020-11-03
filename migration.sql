alter table t_shops
add column processed INTEGER NOT NULL default 0;

INSERT INTO t_budgets
    (a_shop_id, a_month, a_budget_amount, a_amount_spent)
VALUES
    (1, '2020-11-01', 700.00, 725.67),
    (2, '2020-11-01', 800.00, 886.63),
    (3, '2020-11-01', 650.00, 685.91),
    (4, '2020-11-01', 740.00, 746.92),
    (5, '2020-11-01', 630.00, 507.64),
    (6, '2020-11-01', 640.00, 946.32),
    (7, '2020-11-01', 980.00, 640.16),
    (8, '2020-11-01', 790.00, 965.64);

