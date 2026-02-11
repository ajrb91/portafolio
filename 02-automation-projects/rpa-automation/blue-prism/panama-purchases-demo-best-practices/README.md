# Panama Purchases Automation

Link: https://drive.google.com/drive/folders/1dXHDjVxDgNihEgKy8oRNcfGv0epqzBpF?usp=drive_link

## Overview
This project automates the Panama Compras public procurement monitoring process using Robotic Process Automation (RPA).

The solution automatically:
- Monitors the Panama Compras website
- Extracts procurement opportunities
- Enriches each item with detailed information
- Generates an Excel report
- Sends the final report via email

The process runs automatically when triggered by an incoming email.

---

## Objectives
- Eliminate manual review of procurement listings
- Reduce processing time
- Ensure consistent and standardized reporting
- Deliver timely information to stakeholders
- Highlight high-value and urgent opportunities

---

## High-Level Architecture

### Processes
PTY_processes_panama_purchase
- Main Page
- Start Up
- Populate Queue
- Process Core
- Prepare the report and send it
- Mark Item as Completed / Exception
- Reset data
- Close

### Business Objects
Excel Report
- Initialize
- Clean up
- Create report
- Fill report stages
- Merge data
- Apply filters

Mail
- Initialize
- Send report
- Inbox monitor (trigger)

Web Panama Purchase
- Launch website
- Search items
- Scrape results
- Extract extra information
- Close browser

### Work Queues
Purchases

---

## Inputs & Outputs

### Inputs
- Items obtained from the Panama Compras website

### Outputs
- Processed and organized items in a final Excel report
- Automatic delivery via email

---

## Trigger Mechanism
The automation starts automatically when a user sends an email to the bot mailbox.

---

## Business Rules & Workflow

### Step 1 — Search & Initial Extraction
Filters applied:
- Description = system
- Status = active
- From date = 1 year before today

Extracted columns:
- Number
- Description
- Publication Date
- Link (URL)

All pages are navigated and consolidated into one Excel file.

---

### Step 2 — Detail Enrichment
For each item:
- Open link
- Extract Reference Price → Amount
- Extract Proposal submission date → Proposal Date
- Append data to Excel

---

### Step 3 — Post Processing
Sorting:
- Proposal Date (descending)
- Amount (descending)

Formatting:
- Amount > 50,000 → Bold + Yellow
- Proposal date within 3 months → Green

---

## Final Step — Delivery
The consolidated Excel report is automatically sent to the requesting email.

---

## Output File
Panama_Compras.xlsx

Contains:
- Procurement details
- Amounts
- Deadlines
- Priority highlights

---

## Suggested Technologies
- RPA (Blue Prism)
- Web scraping
- Excel automation
- Email automation

---

## Benefits
- Fully automated monitoring
- Faster detection of opportunities
- Reduced manual effort
- Standardized reporting
- Priority identification

---

## Author
Amilcar Rodriguez
February 2025
