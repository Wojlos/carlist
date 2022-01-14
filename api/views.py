from django.db.models import Count

from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Car
from api.serializers import CarSerializer, RatingSerializer, PopularCarSerializer



class CarGenericApiView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    queryset = Car.objects
    serializer_class = CarSerializer

    def get(self, request, pk = None):
        if pk:
            return Response(self.retrieve(request).data, status = status.HTTP_200_OK)
        else:
            return Response(self.list(request).data, status = status.HTTP_200_OK)

    def post(self, request):
        return Response(self.create(request).data, status = status.HTTP_201_CREATED)
    
    def delete(self, request, pk = None):
        if not pk:
            return Response(
                    {"error":"Car with this id does not exists in database!"},
                    status = status.HTTP_404_NOT_FOUND
                )
        self.destroy(request)
        return Response( {"message":f'Car with id {pk} was deleted!'}, status = status.HTTP_204_NO_CONTENT)

        
@api_view(['POST'])
def rate_car(request):
    serializer = RatingSerializer(data = request.data)
    serializer.is_valid(raise_exception= True)
    serializer.save()
    
    return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET'])
def get_popular_cars(request):
    queryset = Car.objects.all().annotate(rates_number = Count('ratings')).order_by("-rates_number")
    serializer = PopularCarSerializer(queryset, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)
