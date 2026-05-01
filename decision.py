def should_escalate(issue):
    sensitive = ["fraud", "billing", "account access"]

    if issue in sensitive:
        return True
    return False
    
