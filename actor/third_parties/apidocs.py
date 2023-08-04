def get_docs() -> str:
    with open('api.md', 'r') as file:
        docs = file.read()
    return docs