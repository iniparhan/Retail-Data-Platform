# Retail Data Foundation

Retail Data Foundation is an end-to-end data project that simulates a real-world retail system,
from transactional database design to analytics, data engineering, and AI-ready use cases.

This repository is structured to reflect the **full lifecycle of data**:
Database → Analytics → Data Engineering → Machine Learning.


## Project Goals

- Design a normalized **OLTP retail database**
- Generate realistic dummy data using Python
- Prepare a clean foundation for:
  - SQL analytics & BI
  - ETL & data warehouse design
  - Machine learning experiments

## Data Flow Overview

```text
PostgreSQL (OLTP)
      ↓
Analytics SQL
      ↓
ETL / Data Engineering
      ↓
Data Warehouse
      ↓
Machine Learning / AI
```

## Repository Structure

Retail-Data-Foundation/
│
├── 01-database/            # Database schema & seeder
├── 02-analytics/           # SQL analysis & dashboards
├── 03-data-engineering/    # ETL & data warehouse
├── 04-ml/                  # Machine learning experiments
├── diagrams/               # ERD & pipeline diagrams
└── README.md

## Project Stages

### 1. Database Layer
- PostgreSQL schema design
- Referential integrity & enums
- Python-based database seeder

### 2. Analytics Layer
- Business-driven SQL queries
- Revenue, customer, and product analysis
- BI/dashboard-ready datasets

### 3. Data Engineering Layer
- ETL pipelines (extract, transform, load)
- Star schema (fact & dimension tables)
- Data quality & transformation logic

### 4️. Machine Learning Layer
- Customer segmentation
- Sales forecasting
- Feature engineering from transactional data

## Tech Stack
- PostgreSQL
- Python
- Faker
- SQL
- Pandas
- dbdiagram.io
- (Optional) Airflow, Docker, Streamlit




## Markdown Each Sub-Files

````

---

# 📁 README KECIL PER FOLDER

## 01-database/README.md

```md
# 01 - Database

This module contains the transactional database design and data seeding logic.

### Contents
- Database schema (PostgreSQL)
- Python-based database seeder
- Entity relationships and constraints

### Output
- Fully populated OLTP retail database
- Ready for analytics and ETL pipelines

### Status
✅ Implemented
````

---

## 02-analytics/README.md

```md
# 02 - Analytics

This module focuses on answering business questions using SQL.

### Scope
- Sales performance analysis
- Customer behavior analysis
- Product & category insights

### Example Questions
- What is the total revenue per month?
- Which products are best-selling?
- How many repeat customers do we have?

### Output
- SQL query files
- Dashboard-ready datasets

### Status
In progress
```

---

## 03-data-engineering/README.md

```md
# 03 - Data Engineering

This module transforms transactional data into analytics-ready structures.

### Scope
- ETL pipelines
- Data warehouse modeling
- Fact and dimension tables

### Planned Output
- fact_sales
- dim_customer
- dim_product
- dim_date

### Status
Planned
```

---

## 04-ml/README.md

```md
# 04 - Machine Learning

This module applies machine learning techniques to retail data.

### Scope
- Customer segmentation
- Sales forecasting
- Feature engineering

### Planned Models
- KMeans (customer clustering)
- Time series forecasting
- Recommendation baseline

### Status
Planned
```

---

## diagrams/README.md

```md
# Diagrams

This folder contains visual documentation for the project.

### Contents
- ERD (Entity Relationship Diagram)
- Data pipeline architecture
- Data warehouse schema
```

---

# MILESTONE PER STAGE

## [Done] Stage 1 — Database (DONE / STRONG)

**Milestone:**

* [x] OLTP schema
* [x] Foreign keys & enums
* [x] Python seeder with Faker
* [x] ERD

**Portfolio value**: Database design & SQL fundamentals

---

## Stage 2 — Analytics (MINIMAL → STRONG)

**Milestone minimum (wajib):**

* [ ] 5–7 business SQL queries
* [ ] Revenue & customer analysis

**Upgrade (opsional):**

* [ ] BI dashboard screenshots

**Portfolio value**: Data analytics & business thinking

---

## Stage 3 — Data Engineering

**Milestone minimum:**

* [ ] ETL script (Postgres → analytical tables)
* [ ] Star schema SQL

**Upgrade:**

* [ ] Incremental load
* [ ] Data validation
* [ ] Airflow DAG

**Portfolio value**: Data engineer readiness

---

## Stage 4 — Machine Learning

**Milestone minimum:**

* [ ] 1 ML notebook (segmentation / forecasting)

**Upgrade:**

* [ ] Feature store logic
* [ ] Model evaluation report

**Portfolio value**: End-to-end AI pipeline

