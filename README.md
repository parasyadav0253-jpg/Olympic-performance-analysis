# Olympic Performance Analysis

An interactive data visualization project analyzing historical Olympic data using Flask and Tableau.

## Author
* *Paras Yadav*

## Tableau Dashboard
* *Live Viz:* [Tableau Public Profile](https://public.tableau.com/app/profile/paras.yadav1102/viz/Olympic_Analysis_17931782712870/Dashboard1)

## Overview

The Olympic Games are a global stage where nations compete to show sporting excellence, but the volume of historical data makes it hard to see what really contributes to success. This project analyzes Olympic data to answer key questions such as:

* Which sports and countries win the most medals?
* How efficient is each country at turning investment into medals?
* How does performance differ by region?
* How do medal totals change over time across different categories?

---

## Features

* *5 Core Visualizations:* Bar, horizontal bar, pie, scatter plot, and trend charts
* *2 Interactive Dashboards:* Designed with clean tiled layouts (Executive Overview and Detailed Analytics)
* *Calculated Fields:* Performance efficiency metrics like Cost per Medal (SUM(Investment) / SUM(Medals))
* *Flask Web App:* Embeds the live Tableau Public dashboards for seamless browser presentation

---

## Tech Stack

| Tool | Purpose |
| :--- | :--- |
| *Tableau Public* | Data connection, calculated metrics, interactive dashboards |
| *Python 3 + Flask* | Web app backend that embeds Tableau views |
| *HTML / CSS* | Page templates and styling |
| *Git + GitHub* | Version control and source code hosting |

---

## Project Structure

```text
Olympic-performance-analysis/
│
├── app.py              # Flask application backend
├── requirements.txt    # Python dependencies
├── templates/          # HTML pages for dashboard views
├── static/             # Styling assets
├── data/               # Raw Olympic datasets
├── tableau/            # Tableau packaged workbook (.twbx)
└── README.md           # Project documentation

Visualizations & Worksheets
Top Medal Leaders: Horizontal Bar Chart

Medal History: Line / Trend Chart

Category Breakdown: Bar Chart

Regional Performance: Pie Chart

Funding Analysis: Scatter Plot Chart

Dashboards
Dashboard 1 (Executive Overview): Integrates Top Medal Leaders, Medal History, and Regional Performance.

Dashboard 2 (Detailed Analytics): Integrates Category Breakdown and Funding Analysis.

Screenshorts





How to Run Locally
1. Clone the repository
git clone [https://github.com/parasyadav0253-jpg/Olympic-performance-analysis.git](https://github.com/parasyadav0253-jpg/Olympic-performance-analysis.git)
cd Olympic-performance-analysis
2. (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Run the application
python app.py
5. Open in browser
Navigate to http://127.0.0.1:5000
