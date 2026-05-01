def generate_response(ticket, docs, escalate):
    if escalate:
        return "This issue is sensitive and has been escalated to human support."

    return f"Based on documentation: {docs[:200]}"
