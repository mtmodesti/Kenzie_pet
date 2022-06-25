from rest_framework import serializers
from groups.serializers import GroupSerializer
from characteristics.serializers import CharacteristicSerializer
from .models import Animal
from helpers.animal_helpers import Helper

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField(max_length=15)

    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)

    def create(self, validated_data):
        
        group_info = validated_data.pop("group")
        characteristic_info = validated_data.pop("characteristics")
        
        #criar uma função de validação para o grupo e characteristica
        
        group = Helper.get_or_create_group(group_info)
        characterisct_list = Helper.get_or_create_characteristics(characteristic_info)
        
        animal = Animal.objects.create(**validated_data, group=group)
        animal.characteristics.set(characterisct_list)

        return animal

    def update(self, instance, validated_data):
        try:
            characteristic_info = validated_data.pop("characteristics")
            characterisct_list = Helper.get_or_create_characteristics(characteristic_info)
            for characteristic in characterisct_list:
                instance.characteristics.add(characteristic)
        finally:
            for key, value in validated_data.items():
                setattr(instance, key, value)
            instance.save()
            return instance
