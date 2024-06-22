from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet

from rest_framework import authentication,permissions

from rest_framework.decorators import action

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from api.models import AlbumModel,TrackModel,ReviewModel

from api.serializers import AlbumSerializer,TrackSerializer,Registration,ReviewSerializer


class Userregister(APIView):

    def post(self,request,*args,**kwargs):

        serializer=Registration(data=request.data)

        if serializer.is_valid():

            serializer.save()
            
        return Response(serializer.data)
    

class AlbumViewSetView(ModelViewSet):

    queryset=AlbumModel.objects.all()

    serializer_class=AlbumSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    
    #custom method

    @action(methods=["post"],detail=True)
    def add_track(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_instance=AlbumModel.objects.get(id=id)

        serializer=TrackSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(album=album_instance)  #except an customer object

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)
        

        
    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        album_instance=AlbumModel.objects.get(id=id)

        serializer=ReviewSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(album=album_instance)  #except an customer object

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)
        


class TrackMixinView(RetrieveUpdateDestroyAPIView):


    serializer_class=TrackSerializer

    queryset=TrackModel.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]




class ReviewMixinview(RetrieveUpdateDestroyAPIView):

    queryset=ReviewModel.objects.all()

    serializer_class=ReviewSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]
    




    
    
    

    


        

        









    