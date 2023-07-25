def get_docs() -> str:
    with open('../README.md', 'r') as file:
        docs = file.read()
    return docs