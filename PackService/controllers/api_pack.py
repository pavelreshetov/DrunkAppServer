from PackService.models.packs import Packs


class PackApi:

    def all_packs():
        data = {}
        try:
            for pack in Packs.objects.all():
                data[pack.pack_id] = {
                    'pack_name': pack.pack_name
                }
            return data
        except Exception:
            return 'not found'






