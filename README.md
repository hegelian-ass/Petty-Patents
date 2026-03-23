# Petty Patents Analysis

This project focuses on collecting, cleaning, and analyzing petty patent data to understand patterns in innovation, filing trends, and domain distribution.

---

## Project Overview

The objective of this project is to build an end-to-end data pipeline that:

* Collects petty patent data through web scraping
* Cleans and structures the raw dataset
* Performs exploratory data analysis
* Extracts meaningful insights about innovation trends

The analysis aims to provide a clearer picture of how petty patents evolve over time and across different domains.

---

## Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* BeautifulSoup / Selenium
* Jupyter Notebook

---

## Project Structure

```
Petty-Patents/
│── data/                 # Raw and processed datasets
│── notebooks/            # Analysis notebooks
│── scripts/              # Scraping and preprocessing scripts
│── outputs/              # Visualizations and results
│── README.md
```

---

## Data Collection

Data was collected using web scraping techniques. The dataset includes:

* Patent title
* Filing date
* Applicant name
* Category or domain

---

## Data Cleaning

The raw dataset required preprocessing before analysis. The following steps were performed:

* Removal of missing and inconsistent values
* Standardization of formats such as dates and text
* Deduplication of records
* Structuring data for analysis

---

## Exploratory Data Analysis

The analysis focused on identifying trends and patterns, including:

* Year-wise distribution of patent filings
* Applicant-wise contribution
* Domain/category distribution
* Frequency and growth trends

---

## Key Insights

* Patent filings show a gradual increase over time
* Certain domains dominate the dataset, indicating concentrated innovation areas
* A small number of applicants contribute a significant portion of filings
* The data suggests a growing interest in practical and utility-based innovations

---

## Conclusions

Petty patents provide useful insight into grassroots innovation. The analysis indicates increasing participation in innovation activities, though contributions remain uneven across applicants and domains.

These findings can be useful for understanding innovation trends and may support decision-making in research, policy, and investment contexts.

---

## Future Work

* Apply machine learning models for trend prediction
* Build an interactive dashboard for visualization
* Automate data collection pipelines
* Perform text analysis on patent descriptions

---

## Learning Outcomes

* Built a complete data pipeline from data collection to analysis
* Gained experience working with unstructured real-world data
* Improved skills in data cleaning and preprocessing
* Developed the ability to extract insights from large datasets

---

## Contributing

Contributions are welcome. Feel free to fork the repository and suggest improvements.

---

## Acknowledgment

If you find this project useful, consider supporting it by sharing feedback or contributing to its improvement.
