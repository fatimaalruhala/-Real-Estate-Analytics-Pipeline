# Real Estate Investment & Property ROI Optimization Pipeline

## 🏢 Business Case & Project Overview
Modern real estate firms and PropTech companies heavily rely on structured data pipelines to drive high-yield property acquisitions. This project solves a common real-world problem: processing messy market listings, restructuring them for analytics, and creating an executive dashboard to detect undervalued housing inventory and maximize annual rental return trajectories.

## 🛠️ Tech Stack & Architecture
- **Environment:** Google Colab (Cloud Python Framework)
- **Data Engineering:** Python 3 (Pandas, NumPy)
- **Data Modeling:** Relational Star Schema (Fact and Dimension Table layout)
- **Business Intelligence & Visualization:** Tableau Desktop / Tableau Public

## 4 Phases
[Phase 1: Raw Data Injection] ──> [Phase 2: Python Data Cleaning] ──> [Phase 3: Relational Star Schema] ──> [Phase 4: Tableau Interactive BI Dashboard]

## 🧹 Key Engineering Accomplishments (Python)
- **Data Remediation:** Authored automated string cleaning rules in Pandas to strip localized currency patterns (`₹`) and remove numerical column commas.
- **Granular Feature Extraction:** Used regular expressions (`regex`) to parse categorical structural text variables (extracting numeric counts from string patterns like `"3 BHK"`).
- **Relational Data Modeling:** Broken down flat listing files into a optimized relational Star Schema database layout by separating transactional metrics (`fact_listings.csv`) from geographic lookup attributes (`dim_locality.csv`) to maximize future query performance.

## 📊 Analytical Insights & Dashboard Features (Tableau)
- **Locality Performance Macro-View:** A horizontal bar visualization tracking average property valuation trends across premium Bangalore markets, layered with a custom color gradient mapping active cash-flow return distributions.
- **Market Valuation Matrix Scatter Plot:** Houses 10,000 un-aggregated property listing marks to track space distribution against capital cost metrics, enabling stakeholders to instantly flag high-ROI anomalies.
- **Dynamic Cross-Filtering Actions:** Incorporates interactive dashboard filters and "Use as Filter" funnel actions, enabling users to click any neighborhood micro-metric and instantly zoom the property scatter plot below.

## 📂 Repository Structure
- `clean_data.py`: Production-ready Python script executing data cleaning and relational star schema modeling.
- `fact_listings.csv`: Modeled transactional metrics data file (Listing IDs, Sizes, Cleaned Prices, Yields).
- `dim_locality.csv`: Modeled locality dimensional configuration file (Locality ID, Locality Name, City).
  
  ## 📊 Final Dashboard Layout Preview
![Bangalore Real Estate Market Analytics Dashboard](dashboard_preview.png)

  

