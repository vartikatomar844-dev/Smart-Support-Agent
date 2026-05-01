results = []

for _, row in df.iterrows():
    ticket = row['text']

    domain, issue = classify_ticket(ticket)
    docs = retrieve_docs(domain)
    escalate = should_escalate(issue)
    response = generate_response(ticket, docs, escalate)

    results.append({
        "ticket": ticket,
        "domain": domain,
        "issue": issue,
        "escalate": escalate,
        "response": response
    })

import pandas as pd
pd.DataFrame(results).to_csv("output.csv", index=False)
