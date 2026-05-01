def retrieve_docs(domain):
    with open(f"data/{domain}_docs.txt", "r") as f:
        return f.read()
