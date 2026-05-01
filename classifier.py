def classify_ticket(text):
    text = text.lower()

    if "visa" in text:
        domain = "visa"
    elif "claude" in text:
        domain = "claude"
    else:
        domain = "hackerrank"

    if "payment" in text or "charged" in text:
        issue = "billing"
    elif "login" in text:
        issue = "access"
    else:
        issue = "general"

    return domain, issue
