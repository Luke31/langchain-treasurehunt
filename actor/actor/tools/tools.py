def get_profile_url(name: str):
    """Searches for Linkedin or twitter Profile Page."""
    search = CustomSerpAPIWrapper()
    res = search.run(f"{name}")
    return res