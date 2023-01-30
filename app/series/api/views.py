
from rest_framework.views import APIView, Response,status

from series.models import Serie

from .serializers import SerieSerializer



class SerieApiView(APIView):
    
    def get (self, request):
        series = SerieSerializer(Serie.objects.all(), many = True)

        return Response(data= series.data, status=status.HTTP_200_OK)
    
    def post (self, request):
        Serie.objects.create(title=request.POST['title'], descripcion=request.POST['descripcion'])
        

        return self.get(request)

        

    