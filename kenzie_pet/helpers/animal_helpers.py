
from groups.models import Group
from characteristics.models import Characteristic


"""
Essa função vai validar  se existe ou não o grupo
e a característica. Se o grupo existir, retornará
o grupo existente, caso contrário vai criar.
Na característica, msm coisa
"""

class Helper:
    def get_or_create_group(search_group):
        group = []
        try:
            group = Group.objects.get(name=search_group["name"])
        except Group.DoesNotExist:
            group = Group.objects.create(**search_group)
        return group

    def get_or_create_characteristics(characteristics):
        characterist_list = []
        for characteristic in characteristics:
            try:
                characteristic_value = Characteristic.objects.get(name=characteristic["name"])
                characterist_list.append(characteristic_value)
            except Characteristic.DoesNotExist:
                characteristic_value = Characteristic.objects.create(**characteristic)
                characterist_list.append(characteristic_value)
        return characterist_list

