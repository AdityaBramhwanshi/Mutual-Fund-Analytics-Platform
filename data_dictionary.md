# Mutual Fund Analytics Platform - Data Dictionary

## Project
Mutual Fund Analytics Platform

## Description
This document describes all datasets used in the project, including column names, data types, business definitions, and source files.

---

# Dataset 1 : fund_master

**Source File:** data/raw/01_fund_master.csv

| Column | Data Type | Business Definition |
|---------|-----------|--------------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Name of Asset Management Company (AMC) |
| scheme_name | Text | Mutual fund scheme name |
| category | Text | Fund category |
| sub_category | Text | Fund sub-category |
| plan | Text | Regular/Direct plan |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Annual expense ratio (%) |
| exit_load_pct | Float | Exit load percentage |
| min_sip_amount | Integer | Minimum SIP investment |
| min_lumpsum_amount | Integer | Minimum lump sum investment |
| fund_manager | Text | Fund manager name |
| risk_category | Text | Risk level |
| sebi_category_code | Text | SEBI category code |

---

# Dataset 2 : nav_history

**Source File:** data/raw/02_nav_history.csv

| Column | Data Type | Business Definition |
|---------|-----------|--------------------|
| amfi_code | Integer | AMFI scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

# Dataset 3 : aum_by_fund_house

**Source File:** data/raw/03_aum_by_fund_house.csv

| Column | Data Type | Business Definition |
|---------|-----------|--------------------|
| date | Date | Reporting date |
| fund_house | Text | Asset Management Company |
| aum_lakh_crore | Float | Assets Under Management (Lakh Crore) |
| aum_crore | Float | Assets Under Management (Crore) |
| num_schemes | Integer | Number of schemes |

---

# Dataset 4 : monthly_sip_inflows

**Source File:** data/raw/04_monthly_sip_inflows.csv

| Column | Data Type | Business Definition |
|---------|-----------|--------------------|
| month | Date | Reporting month |
| sip_inflow_crore | Float | SIP inflow amount |
| active_sip_accounts_crore | Float | Active SIP accounts |
| new_sip_accounts_lakh | Float | New SIP accounts |
| sip_aum_lakh_crore | Float | SIP Assets Under Management |
| yoy_growth_pct | Float | Year-over-Year SIP growth |

---

# Dataset 5 : category_inflows

**Source File:** data/raw/05_category_inflows.csv

| Column | Data Type | Business Definition |
|---------|-----------|--------------------|
| month | Date | Reporting month |
| category | Text | Mutual fund category |
| net_inflow_crore | Float | Net inflow amount |

---

# Dataset 6 : industry_folio_count

**Source File:** data/raw/06_industry_folio_count.csv

| Column | Data Type | Business Definition |
|---------|-----------|--------------------|
| month | Date | Reporting month |
| total_folios_crore | Float | Total folios |
| equity_folios_crore | Float | Equity folios |
| debt_folios_crore | Float | Debt folios |
| hybrid_folios_crore | Float | Hybrid folios |
| others_folios_crore | Float | Other folios |

---

# Dataset 7 : scheme_performance

**Source File:** data/raw/07_scheme_performance.csv

| Column | Data Type | Business Definition |
|---------|-----------|--------------------|
| amfi_code | Integer | AMFI scheme code |
| scheme_name | Text | Mutual fund scheme |
| fund_house | Text | AMC |
| category | Text | Category |
| plan | Text | Plan type |
| return_1yr_pct | Float | 1-year return |
| return_3yr_pct | Float | 3-year return |
| return_5yr_pct | Float | 5-year return |
| benchmark_3yr_pct | Float | Benchmark return |
| alpha | Float | Alpha |
| beta | Float | Beta |
| sharpe_ratio | Float | Sharpe Ratio |
| sortino_ratio | Float | Sortino Ratio |
| std_dev_ann_pct | Float | Annualized Standard Deviation |
| max_drawdown_pct | Float | Maximum Drawdown |
| aum_crore | Float | Assets Under Management |
| expense_ratio_pct | Float | Expense Ratio |
| morningstar_rating | Integer | Morningstar Rating |
| risk_grade | Text | Risk Grade |

---

# Dataset 8 : investor_transactions

**Source File:** data/raw/08_investor_transactions.csv

| Column | Data Type | Business Definition |
|---------|-----------|--------------------|
| investor_id | Text | Unique investor ID |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Scheme code |
| transaction_type | Text | SIP / Lumpsum / Redemption |
| amount_inr | Float | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | Tier classification |
| age_group | Text | Investor age group |
| gender | Text | Gender |
| annual_income_lakh | Float | Annual income |
| payment_mode | Text | Payment method |
| kyc_status | Text | KYC verification status |

---

# Dataset 9 : portfolio_holdings

**Source File:** data/raw/09_portfolio_holdings.csv

| Column | Data Type | Business Definition |
|---------|-----------|--------------------|
| amfi_code | Integer | Scheme code |
| stock_symbol | Text | Stock ticker |
| stock_name | Text | Company name |
| sector | Text | Industry sector |
| weight_pct | Float | Portfolio weight |
| market_value_cr | Float | Market value |
| current_price_inr | Float | Current stock price |
| portfolio_date | Date | Portfolio reporting date |

---

# Dataset 10 : benchmark_indices

**Source File:** data/raw/10_benchmark_indices.csv

| Column | Data Type | Business Definition |
|---------|-----------|--------------------|
| date | Date | Trading date |
| index_name | Text | Benchmark index |
| close_value | Float | Closing index value |