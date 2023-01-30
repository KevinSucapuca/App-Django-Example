
from rest_framework.views import APIView, Response,status

from series.models import Serie



class SerieApiView(APIView):
    
    def get (self, request):
        series = [serie.title for serie in Serie.objects.all()]
        return Response(data= series, status=status.HTTP_200_OK)
    
    def post (self, request):
        Serie.objects.create(title=request.POST['title'], descripcion=request.POST['descripcion'])
        

        return self.get(request)

        

    