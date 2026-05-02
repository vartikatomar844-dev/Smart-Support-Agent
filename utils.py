import re
import pandas as pd
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  
    text = text.strip()
    return text


def read_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return ""


def log_interaction(ticket, response):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}]\n")
        f.write(f"Ticket: {ticket}\n")
        f.write(f"Response: {response}\n")
        f.write("-" * 50 + "\n")


def save_to_csv(results, filename="output.csv"):
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    print(f"Saved results to {filename}")


def is_sensitive(text):
    sensitive_keywords = [
        "fraud", "scam", "unauthorized", "stolen",
        "chargeback", "refund", "password", "login issue"
    ]

    text = text.lower()
    return any(word in text for word in sensitive_keywords)


def normalize_domain(domain):
    domain = clean_text(domain)
    if "visa" in domain:
        return "visa"
    elif "claude" in domain:
        return "claude"
    else:
        return "hackerrank"


def project_path(*parts):
    return BASE_DIR.joinpath(*parts)
