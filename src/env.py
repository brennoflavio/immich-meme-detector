import os
from dataclasses import dataclass


@dataclass
class Env:
    IMMICH_BASE_URL: str
    IMMICH_API_KEY: str
    SEARCH_KEYWORD: str
    SEARCH_MAX_PAGES: int


def load_env() -> Env:
    IMMICH_BASE_URL = os.getenv("IMMICH_BASE_URL")
    IMMICH_API_KEY = os.getenv("IMMICH_API_KEY")
    SEARCH_KEYWORD = os.getenv("SEARCH_KEYWORD", "memes")
    SEARCH_MAX_PAGES = int(os.getenv("SEARCH_MAX_PAGES", "1"))

    assert IMMICH_BASE_URL, "IMMICH_BASE_URL is required"
    assert IMMICH_API_KEY, "IMMICH_API_KEY is required"

    return Env(
        IMMICH_BASE_URL=IMMICH_BASE_URL,
        IMMICH_API_KEY=IMMICH_API_KEY,
        SEARCH_KEYWORD=SEARCH_KEYWORD,
        SEARCH_MAX_PAGES=SEARCH_MAX_PAGES,
    )
