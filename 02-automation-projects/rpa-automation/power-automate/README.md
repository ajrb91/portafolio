# 🤖 RPA Challenge – Power Automate Desktop

## 📌 Overview
This project is a desktop automation built using Power Automate Desktop that solves the RPA Challenge.

The bot reads data from an Excel file and fills a dynamic web form where field positions change after each submission, simulating a real-world automation scenario.

---

## 🎯 Objective
- Automate data entry from Excel into a dynamic web form  
- Handle changing UI elements without relying on fixed positions  
- Achieve high accuracy and full completion of all records  

---

## ⚙️ Solution Architecture

### 🧩 Flow Design
The automation is designed in a simple and clean structure, with all logic contained in a single `Main` flow.

- No subflows  
- Centralized execution logic  
- Easy to understand and maintain  

---

### 🔑 Input Variables

The flow is controlled by only two input parameters:

| Variable | Description |
|----------|------------|
| `str_UrlExcelFile` | URL to download the Excel input file |
| `str_UrlRpaChallenge` | URL of the RPA Challenge website |

This makes the solution flexible and reusable without modifying the core logic.

---

## 🔄 Process Flow

1. Launch browser and navigate to the challenge website  
2. Retrieve current Windows user (for dynamic file paths)  
3. Download Excel file from provided URL  
4. Read Excel data into a data table  
5. Click **Start** on the website  
6. Loop through each row in Excel  
7. Dynamically identify fields using labels  
8. Fill the form with corresponding values  
9. Submit the form  
10. Repeat until all records are processed  

---

## 🧠 Key Features

- Minimalist design (single flow – `Main`)  
- Parameter-driven execution  
- Dynamic field identification (label-based)  
- Excel data-driven automation  
- Environment-independent file handling  

---

## 🛠️ Technologies Used

- Power Automate Desktop  
- Microsoft Excel  
- Web UI Automation  

---

## 📊 Execution Logic

The automation follows this sequence:

### Initialization
- Launch Chrome  
- Navigate to target URL  

### Data Preparation
- Download Excel file  
- Read data into `ExcelData`  

### Execution
- Start challenge  
- Iterate over each row (`CurrentItem`)  
- Fill all required fields dynamically  

### Completion
- Submit all entries  
- End process when dataset is completed  

---

## 📁 Project Structure

/RPA-Challenge-PAD
│
├── Flow
│ └── rpa_challenge (Main flow)
│
├── Input
│ └── Excel file (downloaded dynamically)
│
├── Assets
│ └── UI selectors
│
└── README.md


---

## ▶️ How to Run

1. Open Power Automate Desktop  
2. Import the solution / flow  
3. Configure input variables:
   - `str_UrlExcelFile`
   - `str_UrlRpaChallenge`  
4. Run the `Main` flow  
5. Monitor execution in the browser  

---

## 📈 Expected Results

- All rows are processed successfully  
- Form is completed with 100% accuracy  
- Automation adapts to dynamic UI changes  
- No manual intervention required  

---

## 🚀 Value of This Project

This project demonstrates:

- Strong understanding of RPA fundamentals  
- Ability to handle dynamic web interfaces  
- Clean and maintainable automation design  
- Use of parameterized and reusable flows  

---

## 👤 Author

**Amilcar Rodriguez**  
RPA & Data Automation Engineer  