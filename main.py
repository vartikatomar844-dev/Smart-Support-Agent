import pandas as pd

from classifier import classify_ticket
from retriever import retrieve_docs
from decision import should_escalate
from generator import generate_response


df = pd.read_csv("tickets/support_issues.csv")

print("Columns:", df.columns)

results = []

for index, row in df.iterrows():
    
    ticket = row['ticket']   

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

output_df = pd.DataFrame(results)
output_df.to_csv("output.csv", index=False)

print("Done! Output saved as output.csv")
