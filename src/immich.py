import requests
from src.env import Env
from urllib.parse import urljoin
from dataclasses import dataclass


@dataclass
class Asset:
    id: str


def get_memes(env: Env) -> list[Asset]:
    body = {
        "page": 1,
        "withExif": True,
        "isVisible": True,
        "language": "en-US",
        "query": env.SEARCH_KEYWORD,
        "country": "",
        "state": "",
        "make": "",
        "model": "",
        "isNotInAlbum": True,
    }

    index = 0
    assets: list[Asset] = []
    while True:
        index += 1
        if index > env.SEARCH_MAX_PAGES:
            break
        body["page"] = index
        response = requests.post(
            urljoin(env.IMMICH_BASE_URL, "/api/search/smart"),
            json=body,
            headers={"x-api-key": env.IMMICH_API_KEY},
        )
        response.raise_for_status()
        data = response.json()
        items = data.get("assets", {})["items"]
        if not items:
            break
        for item in items:
            assets.append(Asset(id=item["id"]))

    return assets


@dataclass
class People:
    name: str


def get_asset_people_name(env: Env, asset: Asset) -> list[People]:
    response = requests.get(
        urljoin(env.IMMICH_BASE_URL, f"/api/assets/{asset.id}"),
        headers={"x-api-key": env.IMMICH_API_KEY},
    )
    response.raise_for_status()
    data = response.json()
    people = [
        People(name=x.get("name")) for x in data.get("people", []) if x.get("name")
    ]
    return people


def put_archive(env: Env, asset: Asset) -> None:
    response = requests.put(
        urljoin(env.IMMICH_BASE_URL, f"/api/assets/{asset.id}"),
        json={"visibility": "archive"},
        headers={"x-api-key": env.IMMICH_API_KEY},
    )
    response.raise_for_status()
