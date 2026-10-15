# 🌱 EcoPrint – Smart Printing & Paper Waste Analyzer

**EcoPrint** is a smart sustainability-focused web application designed to analyze printing activities and estimate their environmental impact. The application helps users understand paper consumption, water usage, CO₂ emissions, printing costs, and potential savings through sustainable printing practices such as double-sided printing. 

🔗 **Live Demo:** https://ecoprint-nmit.streamlit.app/

---

## 📌 Project Overview

Printing is a common activity in educational institutions and organizations, but excessive printing contributes to paper waste, resource consumption, and environmental impact.

EcoPrint provides an interactive platform to:

* Calculate the environmental impact of printing
* Compare single-sided and double-sided printing
* Analyze printing datasets
* Estimate potential paper, water, CO₂, and cost savings
* Visualize printing patterns through interactive charts
* Provide sustainability insights and recommendations

The project demonstrates the application of **Green Computing, Data Analytics, and Sustainable Technology** principles in a practical scenario.

---

## 🎯 Objectives

* Reduce unnecessary paper consumption.
* Encourage double-sided printing.
* Estimate the environmental impact of printing activities.
* Analyze historical printing data.
* Provide data-driven sustainability insights.
* Promote environmentally responsible printing practices.

---

## 🚀 Key Features

### 🖨️ 1. Print Calculator

Users can enter printing details such as:

* Number of pages
* Number of copies
* Single-sided or double-sided printing
* Paper size
* Colour or Black & White printing
* Cost per sheet

EcoPrint calculates:

* Total paper sheets required
* Estimated water consumption
* Estimated CO₂ emissions
* Printing cost
* Potential paper savings
* Potential water savings
* Potential CO₂ reduction
* Potential monetary savings
* Sustainability score

---

### 📊 2. Dataset Analyzer

Users can upload a CSV file containing printing records.

The application performs:

* Data cleaning
* Printing activity analysis
* Paper consumption calculation
* Water consumption estimation
* CO₂ estimation
* Cost analysis
* Double-sided printing analysis

It also provides interactive visualizations such as:

* Daily paper consumption
* Printing method distribution
* Colour vs. Black & White printing

---

### 🌍 3. Sustainability Dashboard

The dashboard summarizes the overall sustainability impact of the analyzed printing data.

It displays:

* 📄 Total pages printed
* 📃 Total sheets used
* 💧 Estimated water consumption
* 🌫️ Estimated CO₂ emissions
* 💰 Printing cost
* ♻️ Potential paper savings
* 💧 Potential water savings
* 🌫️ Potential CO₂ reduction
* 💵 Potential cost savings
* 🌱 Sustainability score

The dashboard also provides sustainability recommendations based on the analyzed data.

---

## 🛠️ Technologies Used

| Technology       | Purpose                             |
| ---------------- | ----------------------------------- |
| **Python**       | Application development             |
| **Streamlit**    | Web application framework           |
| **Pandas**       | Data processing and analysis        |
| **Plotly**       | Interactive data visualization      |
| **Git & GitHub** | Version control and project hosting |

---

## 📁 Project Structure

```text
EcoPrint/
│
├── app.py
├── requirements.txt
├── README.md
└── sample_data.csv
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/vampire-debug/EcoPrint.git
```

### 2. Navigate to the project directory

```bash
cd EcoPrint
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## 📄 Dataset Format

EcoPrint accepts CSV files containing the following columns:

```text
Date
Pages
Copies
Print_Type
Colour
Paper_Cost
```

Example:

| Date       | Pages | Copies | Print_Type   | Colour        | Paper_Cost |
| ---------- | ----: | -----: | ------------ | ------------- | ---------: |
| 2026-10-01 |    50 |      1 | Single-sided | Colour        |          1 |
| 2026-10-02 |   100 |      2 | Double-sided | Black & White |          1 |
| 2026-10-03 |   200 |      1 | Single-sided | Black & White |          1 |

---

## 🌱 Environmental Impact Methodology

EcoPrint uses approximate educational estimates to demonstrate the environmental impact of printing.

### Water Consumption

```text
Water Consumption = Sheets Used × 7 Litres
```

The value of **7 litres per A4 sheet** is used as an approximate midpoint of published estimates.

### CO₂ Emissions

```text
CO₂ Emissions = Sheets Used × 0.00464 kg
```

This corresponds to an approximate estimate of **4.64 g CO₂e per A4 sheet**.

These values are intended for **educational estimation and comparative analysis**, not as exact measurements for a particular printer, paper manufacturer, or electricity source.

---

## ♻️ Sustainability Approach

EcoPrint focuses on reducing unnecessary paper usage through **double-sided printing**.

For single-sided printing, the application estimates how much paper could potentially be saved if the same pages were printed double-sided.

The resulting potential savings are then used to estimate:

* Paper saved
* Water saved
* CO₂ reduction
* Printing cost reduction

---

## 📊 Application Workflow

```text
User Input / CSV Dataset
          ↓
     Data Processing
          ↓
   Printing Analysis
          ↓
 Environmental Impact
          ↓
     Savings Analysis
          ↓
 Interactive Dashboard
          ↓
 Sustainability Insights
```

---

## 🎓 Academic Context

**Project Title:** EcoPrint – Smart Printing & Paper Waste Analyzer

**Course:** Green Computing

**Institution:** Nitte Meenakshi Institute of Technology (NMIT)

**Department:** Computer Science and Engineering

This project demonstrates how software and data analytics can be used to encourage sustainable resource utilization and support Green Computing practices.

---

## 🔮 Future Enhancements

Possible future improvements include:

* Monthly and yearly sustainability reports
* Printing history database
* User authentication
* Institution-level dashboards
* Printer-wise analytics
* Advanced sustainability scoring
* Automated PDF reports
* Cloud database integration
* Machine learning-based printing prediction
* Real-time printer integration
* Carbon footprint benchmarking

---

## 👨‍💻 Team

**EcoPrint Project Team**

* **Dhruv Sharma** — Project Development & Implementation
* **Bhargavi** — Synopsis & Documentation
* **Bhavy** — Presentation & PPT

---

## 🌐 Links

**Live Application:**
https://ecoprint-nmit.streamlit.app/

**GitHub Repository:**
https://github.com/vampire-debug/EcoPrint

---

## ⭐ Acknowledgement

This project was developed as part of an academic Green Computing project with the objective of applying software development and data analytics techniques to promote sustainable printing practices.

---

### 🌱 EcoPrint

**Print smarter. Waste less. Compute greener.**
