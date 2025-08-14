from src.env import load_env
from src.immich import get_asset_people_name, get_memes, put_archive


def archive():
    env = load_env()
    memes = get_memes(env)
    for meme in memes:
        people = get_asset_people_name(env, meme)
        if len(people) == 0:
            put_archive(env, meme)
