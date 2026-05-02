# Smart-Support-Agent

# 🧠 Multi-Domain Support Triage Agent

## 🚀 Overview

This project is a **terminal-based AI support agent** built for the HackerRank Orchestrate Hackathon.

The system processes customer support tickets across multiple domains and intelligently:

* Classifies the issue
* Identifies the correct platform (HackerRank / Claude / Visa)
* Retrieves relevant documentation
* Decides whether to respond or escalate
* Generates safe, grounded responses

---

## 🧩 Problem Statement

Support systems must handle diverse user queries while ensuring:

* Accurate classification
* Safe handling of sensitive issues
* No hallucinated responses
* Proper escalation when needed

This project solves that by building a **rule-based + retrieval-driven AI pipeline**.

---

## ⚙️ Features

* ✅ Multi-domain ticket handling (HackerRank, Claude, Visa)
* ✅ Issue classification (billing, access, general, etc.)
* ✅ Context retrieval from provided support corpus
* ✅ Escalation for sensitive cases (fraud, billing, account access)
* ✅ Safe response generation (no hallucinations)
* ✅ Logging for chat transcript submission
* ✅ CSV output generation for evaluation

---

## 🏗️ Project Structure

```
smart-support-agent/
│── data/
│   ├── hackerrank_docs.txt
│   ├── claude_docs.txt
│   ├── visa_docs.txt
│
│── tickets/
│   └── support_issues.csv
│
│── classifier.py
│── retriever.py
│── decision.py
│── generator.py
│── utils.py
│── main.py
│── output.csv
│── log.txt
│── README.md
```

---

## 🔄 System Pipeline

```
Ticket Input
   ↓
Text Cleaning (utils.py)
   ↓
Classification (classifier.py)
   ↓
Document Retrieval (retriever.py)
   ↓
Decision Engine (decision.py)
   ↓
Response Generation (generator.py)
   ↓
Logging + CSV Output
```

---

## 🧠 Approach

### 1. Classification

* Keyword-based classification is used to identify:

  * Domain (HackerRank / Claude / Visa)
  * Issue type (billing, access, general)

### 2. Retrieval

* The system strictly uses **provided documentation only**
* Prevents hallucination by grounding responses

### 3. Decision Engine

* Sensitive issues are detected:

  * Fraud
  * Billing
  * Account access
* Such cases are **automatically escalated**

### 4. Response Generation

* If safe → respond using retrieved docs
* If sensitive → escalate to human support

---

## 🛡️ Safety Measures

* ❌ No external knowledge used
* ❌ No fabricated answers
* ✅ Strict reliance on provided corpus
* ✅ Sensitive issue detection
* ✅ Escalation handling

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install pandas
```

### 2. Run the agent

```bash
python main.py
```

### 3. Output files generated

* `output.csv` → Final predictions
* `log.txt` → Chat transcript

---

## 📊 Output Format

The generated CSV contains:

| ticket | domain | issue | escalate | response |
| ------ | ------ | ----- | -------- | -------- |

---

## 🧪 Example

**Input Ticket:**

```
I was charged twice for my payment
```

**Output:**

```
Domain: Visa
Issue: Billing
Escalate: True
Response: Escalated to human support
```

---

## 🚧 Future Improvements

* 🔹 Use ML/NLP models for better classification
* 🔹 Implement vector search (FAISS) for smarter retrieval
* 🔹 Add LLM-based reasoning
* 🔹 Improve domain detection accuracy
* 🔹 Build web interface (optional)

---

## 👨‍💻 Author

Built as part of a hackathon submission.

---

## 🏁 Conclusion

This project demonstrates a **safe, structured, and scalable approach** to building AI-powered support systems that:

* Avoid hallucination
* Handle sensitive cases responsibly
* Provide reliable assistance across domains

---
