from PackService.models.PackModel import PackModel


class PackAPI:

    def get_all_packs(self):
        resposne = {
            "data": []
        }
        for pack in PackModel.objects.all():
            pack_struct = {
                'pack_id': pack.pk,
                'pack_name': pack.pack_name
            }
            resposne["data"].append(pack_struct)
        return resposne


"""
    except Packs.DoesNotExist:
        resposne["message"] = "not found"
        return 'not found'
"""
