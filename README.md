# Immich Meme Detector

Detects and archive memes in your Immich Library

## Running
Set the following env vars:
```
IMMICH_BASE_URL
IMMICH_API_KEY
SEARCH_KEYWORD -> Default "memes"
SEARCH_MAX_PAGES -> Default 1
```

Then run with uv
```
uv run python main.py
```

A Docker image is also provided with this project.

## How

- Do a search for `SEARCH_KEYWORD` (default "memes") in your library, excluding:
    - Photos in Albums
    - Archived Photos
    - Photos with Country / City / State
    - Photos with Camera Model / Camera Maker

- For each photo, check if there's a person with name assigned to it

- If there's no person with name assigned, archive the photo
