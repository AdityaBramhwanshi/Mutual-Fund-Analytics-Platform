Mutual Fund Analytics Platform

End-to-End Financial Analytics using Python, SQL & Power BI

Bluestock Fintech Data Analyst Internship Capstone Project

Project Overview

The Mutual Fund Analytics Platform is an end-to-end financial analytics solution developed during the Bluestock Fintech Data Analyst Internship.

The project integrates multiple mutual fund datasets, performs data cleaning and transformation through an ETL pipeline, calculates advanced financial risk metrics, and delivers interactive Power BI dashboards to support investment analysis and business decision-making.

The platform demonstrates the complete analytics lifecycle—from raw financial data to business-ready insights.

---

Project Objectives

* Develop an automated ETL pipeline using Python.
* Clean and validate multiple financial datasets.
* Build interactive Power BI dashboards.
* Analyze mutual fund performance using financial KPIs.
* Study investor behavior and SIP trends.
* Perform advanced financial risk analytics.
* Build a rule-based mutual fund recommendation system.

---

Technologies Used

* Python
* Pandas
* NumPy
* SQL
* Microsoft Power BI
* DAX
* Power Query
* Jupyter Notebook
* Git & GitHub
* Microsoft Excel

---

Dataset Summary

| Dataset                   | Records |
| ------------------------- | ------: |
| Fund Master               |      40 |
| NAV History               |  46,000 |
| Investor Transactions     |  32,778 |
| Portfolio Holdings        |     322 |
| Total Integrated Datasets |      12 |

---

Project Architecture

```text
Raw Financial Data
        │
        ▼
Python ETL Pipeline
        │
        ▼
Data Cleaning & Validation
        │
        ▼
Feature Engineering
        │
        ▼
Power BI Dashboard
        │
        ▼
Advanced Financial Analytics
        │
        ▼
Business Insights
```

---

Dashboard Modules

1. Industry Overview Dashboard

* Total AUM
* SIP Inflow
* Industry Folios
* Market Share Analysis
* Top Asset Management Companies

2. Fund Performance Dashboard

* CAGR Analysis
* Sharpe Ratio
* Alpha
* Benchmark Comparison
* Risk vs Return Analysis

3. Investor Analytics Dashboard

* State-wise Transactions
* Age Group Analysis
* Gender Distribution
* City Tier Analysis
* Monthly Transactions

4. SIP & Market Trends Dashboard

* Monthly SIP Growth
* Category-wise Net Inflow
* Active SIP Accounts
* Benchmark Performance

---

Advanced Analytics

Implemented advanced financial analytics including:

* Historical Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Herfindahl-Hirschman Index (HHI)
* Rule-Based Mutual Fund Recommendation System

---

Key Business Insights

* Mutual fund industry AUM continues to grow steadily.
* Small-cap funds deliver the highest returns but also exhibit the highest risk.
* Investors aged 26–45 contribute the largest investment volumes.
* SIP remains the preferred investment method among retail investors.
* Most portfolios are moderately diversified according to HHI analysis.
* Risk-based fund recommendations improve investment decision-making.

---

Folder Structure

```text
Mutual_Fund_Analytics_Platform/

├── dashboard/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── reports/
├── exports/
├── recommender.py
├── README.md
└── requirements.txt
```

---

How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the ETL pipeline

```bash
python run_pipeline.py
```

4. Open the Power BI dashboard

Open the `.pbix` file located in the **dashboard** folder using Microsoft Power BI Desktop.

---

Future Scope

* Live AMFI API Integration
* Machine Learning Recommendation Engine
* Azure Cloud Deployment
* Automated ETL Pipeline
* Power BI Service Integration
* Portfolio Optimization
* Predictive Financial Analytics

---

Author

**Aditya Bramhwanshi**

Data Analyst Intern

Bluestock Fintech

---

License

This project was developed for educational and internship purposes as part of the Bluestock Fintech Data Analyst Internship.
