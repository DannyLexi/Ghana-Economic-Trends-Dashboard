# Ghana Macroeconomic Trends Dashboard (2009–2025)

A data analytics and business intelligence project that uses World Bank macroeconomic data, a Python ETL pipeline, MySQL, and Power BI to explore Ghana's economic trends from 2009 to 2025.

## 📊 Project Overview

This project examines four key macroeconomic indicators for Ghana:

- GDP growth
- Inflation rate
- USD/GHS exchange rate
- Cedi year-over-year depreciation/appreciation

The project demonstrates an end-to-end data workflow:

**World Bank API → Python ETL → MySQL → Power BI Dashboard**

The accompanying project explanation presents the data as a 17-year view of Ghana's economic trends and discusses major periods including the 2014 cedi depreciation, the COVID-19 period, the 2021–2023 economic crisis, and the 2024–2025 recovery period.

## 🎯 Objectives

The dashboard was designed to help users understand:

1. How Ghana's economy grew between 2009 and 2025.
2. How the Ghanaian cedi changed against the US dollar.
3. How inflation changed over the period.
4. The relationship between exchange-rate movements and inflation.
5. Major economic periods and changes visible in the historical data.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data extraction and transformation |
| World Bank API / `wbgapi` | Macroeconomic data source |
| Pandas | Data manipulation |
| SQLAlchemy | Database connection |
| PyMySQL | MySQL driver |
| MySQL | Data storage |
| Power BI | Dashboard and visualization |
| Git / GitHub | Version control and project sharing |

## 🔄 Data Pipeline

```text
                    World Bank API
                          │
                          ▼
                  Python ETL Script
                          │
                  ┌───────┴───────┐
                  │               │
             Extract          Transform
                  │               │
                  └───────┬───────┘
                          ▼
                       MySQL
                 macro_indicators
                          │
                          ▼
                     Power BI
                          │
                          ▼
                Interactive Dashboard
```

## 📈 Data Processing

The ETL script retrieves Ghana data for 2009–2025 using the following World Bank indicators:

| World Bank Indicator | Project Field |
|---|---|
| `FP.CPI.TOTL.ZG` | `inflation_rate` |
| `NY.GDP.MKTP.KD.ZG` | `gdp_growth` |
| `PA.NUS.FCRF` | `usd_ghs_rate` |
| `SL.UEM.TOTL.ZS` | `unemployment_rate` |

The pipeline also calculates:

**Cedi depreciation/appreciation (%)**

```text
(current USD/GHS rate - previous USD/GHS rate)
------------------------------------------------ × 100
previous USD/GHS rate
```

The resulting data is written to a MySQL table named:

```text
macro_indicators
```

## 📊 Power BI Dashboard

The Power BI dashboard presents the historical data through KPI cards, trend visualizations, and analytical charts.



- Inflation trends
- GDP growth
- USD/GHS exchange-rate movements
- Cedi depreciation/appreciation
- Historical economic periods
- Relationships between macroeconomic indicators

## 🔎 Key Insights

According to the accompanying project explanation, the dashboard highlights several notable periods:

- **2009–2013:** relatively stable economic growth.
- **2014:** major cedi depreciation.
- **2015–2019:** recovery and relative exchange-rate stabilization.
- **2020:** COVID-19 disruption.
- **2021–2023:** a period marked by significant currency depreciation and high inflation.
- **2024:** inflation began declining and the project identifies the beginning of a recovery period.
- **2025:** the project data shows a lower USD/GHS rate and lower inflation compared with 2024.

The project documentation also explores the relationship between a weaker cedi and higher prices through the concept of exchange-rate pass-through.

## 🗄️ Database

Create the MySQL database before running the ETL:

```sql
CREATE DATABASE ghana_economy;
```

The Python pipeline creates/replaces the following table:

```text
macro_indicators
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ghana-economic-trends-dashboard.git
cd ghana-economic-trends-dashboard
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the MySQL database

```sql
CREATE DATABASE ghana_economy;
```

### 5. Configure environment variables

Copy `.env.example` to `.env`:

```bash
copy .env.example .env
```

Then update `.env` with your local MySQL credentials.

**Never commit `.env` to GitHub.**

### 6. Run the ETL pipeline

```bash
python etl/etl.py
```

The script retrieves the World Bank data, transforms it, calculates cedi depreciation/appreciation, and loads the result into MySQL.

## 📁 Repository Structure

```text
ghana-economic-trends-dashboard/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── etl/
│   └── etl.py
│
├── powerbi/
│   └── Ghana_Economy_Dashboard.pbix
│
├── documentation/
│   └── Ghana Economy Dashboard Explained.docx
│
├── images/
│   ├── dashboard-overview.png
│   ├── economic-trends.png
│   └── correlation-analysis.png
│
└── data/
    └── README.md
```

## 📚 Data Source

The project uses macroeconomic indicators retrieved from the World Bank through the `wbgapi` Python package.

The ETL pipeline currently retrieves Ghana data for **2009–2025**.

## ⚠️ Notes

- The ETL pipeline expects a local MySQL server.
- Database credentials are supplied through environment variables.
- The Power BI `.pbix` file may require updating the local data-source connection when opened on another computer.
- The ETL process uses `if_exists="replace"`, meaning the `macro_indicators` table is rebuilt when the pipeline runs.

## 👤 Author

**Daniel Asare**

Aspiring Data Scientist | Data Analytics | Python | SQL | Power BI

Portfolio: `https://sites.google.com/view/danielasare`

LinkedIn: `https://linkedin.com/in/daniel-asare-b29a352a1`

## ⭐ Project Purpose

This project was built as part of a practical data portfolio to demonstrate an end-to-end workflow involving API data collection, data transformation, database storage, and business intelligence visualization.
