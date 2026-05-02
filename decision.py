from utils import clean_text, is_sensitive


def should_escalate(issue):
    sensitive = {"fraud", "billing", "access"}
    return clean_text(issue) in sensitive


def should_escalate_ticket(ticket, issue):
    return should_escalate(issue) or is_sensitive(ticket)
