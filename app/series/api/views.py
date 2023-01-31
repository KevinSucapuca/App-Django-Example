
from rest_framework.views import APIView, Response,status

from series.models import Serie

from .serializers import SerieSerializer




class SerieApiView(APIView):
    
    def get (self, request):
        series = SerieSerializer(Serie.objects.all(), many = True)

        return Response(data= series.data, status=status.HTTP_200_OK)
    
    
    
    def post (self, request):
        serie = SerieSerializer(data=request.POST)
        serie.is_valid(raise_exception=True)
        Serie.objects.create(title=serie.validated_data['title'], descripcion=serie.validated_data['descripcion'])
        return self.get(request)
