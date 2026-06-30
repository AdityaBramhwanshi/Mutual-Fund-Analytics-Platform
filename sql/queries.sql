-- Query 1 : Top 5 Fund Houses by AUM

SELECT
    fund_house,
    MAX(aum_crore) AS total_aum_crore
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum_crore DESC
LIMIT 5;

-- Query 2 : Average NAV Per Month

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav),2) AS average_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- Query 3 : SIP YoY Growth

SELECT
    month,
    yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;

-- Query 4 : Transactions By State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- Query 5 : Funds With Expense Ratio Less Than 1%

SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- Query 6 : Top 10 Funds By 5-Year Return

SELECT
    scheme_name,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- Query 7 : Average Transaction Amount By Transaction Type

SELECT
    transaction_type,
    ROUND(AVG(amount_inr),2) AS average_amount
FROM investor_transactions
GROUP BY transaction_type;

-- Query 8 : Portfolio Holdings By Sector

SELECT
    sector,
    COUNT(*) AS number_of_holdings
FROM portfolio_holdings
GROUP BY sector
ORDER BY number_of_holdings DESC;

-- Query 9 : Average Benchmark Index Value

SELECT
    index_name,
    ROUND(AVG(close_value),2) AS average_close_value
FROM benchmark_indices
GROUP BY index_name
ORDER BY average_close_value DESC;

-- Query 10 : Number Of Funds By Category

SELECT
    category,
    COUNT(*) AS total_funds
FROM fund_master
GROUP BY category
ORDER BY total_funds DESC;

