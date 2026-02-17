AI automation demo using Python and OpenAI

This small PoC exposes a REST API to answer frequently asked questions potentially associated with internal company documentation using a catalog-based approach.

## Objective
- Receive a text-based question
- Use internal documentation as a knowledge catalog
- Generate an automated response
- Expose a single API endpoint

## Requirements
- Python 3.10+
- An OpenAI API key, which must be configured in the `.env` file

## Project Structure

ai-automation-demo/
app/main.py
data/docs.txt
.env
README.txt

## Configuration
- Activate the appropriate virtual environment
- Configure the OpenAI API key in the `.env` file
- Run the service ("uvicorn app.main:app --reload")

## Uso endpoint

{
  "question": "How do I configure the VPN?",
  "answer": "..."
}

