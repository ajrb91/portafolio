# 🧠 AI-Powered Message Triage Automation

Automated message analysis, prioritization, alerting, and logging using **n8n**, **OpenAI**, and **Slack**.

## 👤 Author

Amilcar Rodriguez

---

## 📌 Overview

This project demonstrates a real-world **AI-driven automation workflow** designed to analyze incoming messages, determine their urgency, notify internal teams when escalation is required, and return a structured response.

It simulates common business scenarios such as:
- customer complaints
- operational incidents
- service requests
- inbound leads

The solution is implemented using **n8n** as the orchestration layer and **OpenAI** for natural language understanding.

---

## 🎯 Key Features

- 🔔 Event-driven workflow using Webhooks  
- 🧠 AI-powered text analysis (sentiment, tags, recommended action)  
- 🚨 Automatic urgency detection  
- 💬 Slack notifications for urgent cases  
- 📄 Structured JSON response  
- 🧩 Modular and extensible design  

---

## 🏗️ Architecture

Step 1: Incoming Message (Webhook)
Step 2: Text Extraction
Step 3: OpenAI Analysis
Step 4: Normalized AI Output
Step 5: Urgency & Priority Logic
Step 6: Slack Notification (if urgent)
Step 7: Final Structured Response

---

## 🛠️ Technologies Used

- **n8n** – Workflow orchestration  
- **OpenAI API (Responses API)** – AI text analysis  
- **Slack API** – Internal notifications  
- **JavaScript Expressions** – Decision logic & data transformation  

---

## 📥 Input Example

```json
{
  "text": "This is unacceptable. My card is blocked, I cannot make any payments and I need an urgent solution today."
}
```
---

## 📤 AI Analysis Output Example

```
{
  "summary": "A customer is upset because their card is blocked and they need an immediate solution.",
  "sentiment": "negative",
  "tags": ["urgent", "customer support", "complaint"],
  "recommended_action": "Escalate the case and contact the customer immediately."
}
```
---

## 🚨 Slack Notification (Urgent Case)

🚨 AI TRIAGE (HIGH)
Sentiment: negative
Summary: A customer is upset because their card is blocked...
Tags: urgent, customer support, complaint
Action: Escalate the case and contact the customer immediately.

---

## 📦 Final Webhook Response

```
{
  "priority": "HIGH ",
  "analysis": {
    "summary": "...",
    "sentiment": "negative",
    "tags": ["urgent", "customer support"],
    "recommended_action": "..."
  },
  "slack_notified": true,
  "request_id": "resp_xxxxx"
}
```

##  🚀 Possible Extensions

- WhatsApp / Telegram / Email as message input
- Historical logging (Google Sheets or database)
- Automatic customer replies
- Dashboard and analytics
- CRM or ticketing system integration