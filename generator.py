def generate_response(ticket, docs, escalate):
    if escalate:
        return (
            "This request has been escalated to human support because it may "
            "involve account access, billing, fraud, or another sensitive issue."
        )

    summary = docs.strip()[:300]
    return (
        "Thanks for contacting support. Based on the available documentation, "
        f"here is the most relevant guidance: {summary}"
    )
