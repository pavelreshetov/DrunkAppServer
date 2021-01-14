from PackService.models.packs import Packs


def get_all_packs():
    packs = {}
    for pack in Packs:
        packs[pack.pack_id] = {pack.pack_name}
    return packs


print(get_all_packs())