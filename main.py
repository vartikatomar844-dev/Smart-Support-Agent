import pandas as pd
from zipfile import ZipFile

from classifier import classify_row
from retriever import retrieve_docs
from decision import should_escalate_ticket
from generator import generate_response
from utils import clean_text, project_path, save_to_csv


ZIP_PATH = project_path("tickets", "support_tickets.zip")
CSV_IN_ZIP = "support_tickets/support_tickets.csv"
OUTPUT_PATH = project_path("output.csv")


def load_tickets():
    if not ZIP_PATH.exists():
        raise FileNotFoundError(f"Input file not found: {ZIP_PATH}")

    with ZipFile(ZIP_PATH) as archive:
        with archive.open(CSV_IN_ZIP) as file:
            df = pd.read_csv(file)

    required_columns = {"Issue", "Subject", "Company"}
    missing_columns = required_columns.difference(df.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"CSV is missing required column(s): {missing}")

    return df


def process_tickets(df):
    results = []

    for _, row in df.iterrows():
        ticket = clean_text(row["Issue"])
        subject = row["Subject"]

        domain, issue = classify_row(row)
        docs = retrieve_docs(domain)
        escalate = should_escalate_ticket(ticket, issue)
        response = generate_response(ticket, docs, escalate)

        results.append(
            {
                "subject": subject,
                "ticket": ticket,
                "domain": domain,
                "issue": issue,
                "escalate": escalate,
                "response": response,
            }
        )

    return results


def main():
    df = load_tickets()
    results = process_tickets(df)
    save_to_csv(results, OUTPUT_PATH)
    print(f"Done. Processed {len(results)} tickets.")


if __name__ == "__main__":
    main()
