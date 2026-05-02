from utils import project_path, read_file


DOC_FILES = {
    "visa": "visa_docs.txt",
    "claude": "claude_docs.txt",
    "hackerrank": "hackerRank_docs.txt",
}


def retrieve_docs(domain):
    filename = DOC_FILES.get(domain, DOC_FILES["hackerrank"])
    docs = read_file(project_path("data", filename)).strip()

    if docs:
        return docs

    return "No detailed documentation is available for this domain yet."
