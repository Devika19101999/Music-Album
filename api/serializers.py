from rest_framework import serializers

from api.models import AlbumModel,TrackModel,User,ReviewModel




class Registration(serializers.ModelSerializer):

    class Meta:
         model=User
         fields=['username','email','password','first_name','last_name']
         

      #method override  
    def create(self,validated_data):
          
          return User.objects.create_user(**validated_data)
         


class TrackSerializer(serializers.ModelSerializer):
      

    album=serializers.StringRelatedField(read_only=True)

    
    class Meta:

        model=TrackModel

        fields="__all__"

        read_only_field=["id","album","created_date","updated_date","is_active"]


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:

        model=ReviewModel

        fields="__all__"

        read_only_fields=["id","album","created_date","updated_date","is_active"]



class AlbumSerializer(serializers.ModelSerializer):
    

    track_count=serializers.CharField(read_only=True)

    tracks=TrackSerializer(many=True,read_only=True)



    
    
    class Meta:

        model=AlbumModel

        fields="__all__"

        read_only_fields=["id","status","created_date","updated_date","is_active"]



