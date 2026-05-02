from utils import clean_text, normalize_domain


def classify_ticket(text):
    text = clean_text(text)

    if "visa" in text:
        domain = "visa"
    elif "claude" in text:
        domain = "claude"
    else:
        domain = "hackerrank"

    if "payment" in text or "charged" in text:
        issue = "billing"
    elif "login" in text or "access" in text or "password" in text:
        issue = "access"
    elif "refund" in text or "dispute" in text or "score" in text:
        issue = "dispute"
    elif "fraud" in text or "scam" in text or "unauthorized" in text:
        issue = "fraud"
    else:
        issue = "general"

    return domain, issue


def classify_row(row):
    ticket = row.get("Issue", "")
    company = row.get("Company", "")

    domain = normalize_domain(company)
    _, issue = classify_ticket(ticket)

    return domain, issue
