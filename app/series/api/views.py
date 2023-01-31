
from rest_framework.views import  Response,status
from rest_framework.viewsets import ModelViewSet
from series.models import Serie

from .serializers import SerieSerializer




#class SerieApiView(APIView):
#class SerieApiView(ViewSet):  


    #def get (self, request):
        #series = SerieSerializer(Serie.objects.all(), many = True)

        #return Response(data= series.data, status=status.HTTP_200_OK)
    #Def ViewSet
    #def list (self, request):
        #series = SerieSerializer(Serie.objects.all(), many = True)

        #return Response(data= series.data, status=status.HTTP_200_OK)
    
    #def retrieve (self, request, pk: int):
        #series = SerieSerializer(Serie.objects.get(pk=pk))

        #return Response(data= series.data, status=status.HTTP_200_OK)
    
    
    
    #def post (self, request):
        #serie = SerieSerializer(data=request.POST)
        #serie.is_valid(raise_exception=True)
        #Serie.objects.create(title=serie.validated_data['title'], descripcion=serie.validated_data['descripcion'])
        #return self.get(request)
    ##def ViewSet
    #def create (self, request):
        #serie = SerieSerializer(data=request.POST)
        #serie.is_valid(raise_exception=True)
        #Serie.objects.create(title=serie.validated_data['title'], descripcion=serie.validated_data['descripcion'])
        #return self.list(request)
class SerieApiView(ModelViewSet): 
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    