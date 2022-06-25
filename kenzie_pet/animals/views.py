from rest_framework.views import APIView, Response
from django.shortcuts import get_object_or_404
from .models import Animal
from .serializers import AnimalSerializer



class AnimalView(APIView):
    def get(self, request):

        animals = Animal.objects.all()

        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = AnimalSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)


class AnimalIdView(APIView):
    def get(self, request, animal_id):
        animal = get_object_or_404(Animal, pk=animal_id)
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)
    
    
    def patch(self, request, animal_id):
        animal = get_object_or_404(Animal, pk=animal_id)

        serializer = AnimalSerializer(animal, request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        invalid_keys = ("group", "sex")

        for key in serializer.validated_data.keys():
            if key in invalid_keys:
                return Response({"message" : f"You can not update {key} property."}, status=422)

        serializer.save()

        return Response(serializer.data)

    def delete(self, request, animal_id):
        animal = get_object_or_404(Animal, pk=animal_id)
        animal.delete()
        return Response(status=204)
    
class HomeView(APIView):
    def get(self, _):
        return Response({"Method " : "Route        :      Description",
                         "- GET    - /animals    ":"    List all animals",
                         "- POST   - /animals    ":"    Register new animal",
                         "- GET    - /animals/id/":"    Get Aniaml by id",
                         "- PATCH  - /animals/id ":"    Update animal",
                         "- DELETE - /animals/id ":"    Delete animal"
                         
                         }, status=200)
        
