import uuid


def generate_short_url(url: str) -> str:
    return f"http://localhost:8000/{uuid.uuid4().hex[:6]}/"