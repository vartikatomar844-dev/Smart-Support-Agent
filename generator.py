def generate_response(ticket, docs, escalate):
    if escalate:
        return "This issue requires human support. Escalating..."

    return f"Based on our docs: {docs[:200]}"
