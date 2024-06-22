from django.db import models

from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator,MinValueValidator




class AlbumModel(models.Model):

    album_title=models.CharField(max_length=100)

    year=models.CharField(max_length=100)

    director=models.CharField(max_length=100)

    language=models.CharField(max_length=100)



    options=(
        ("pending","pending"),

        ("in-progress","in-progress"),

        ("completed","completed")
    )

    status=models.CharField(max_length=200,choices=options,default="completed")

    creaded_date=models.DateField(auto_now_add=True)

    updated_date=models.DateField(auto_now=True)

    is_active=models.BooleanField(default=True)
    
    
    @property
    def track_count(self):

        return TrackModel.objects.filter(album=self).count()
    
    @property
    def tracks(self):

        return TrackModel.objects.filter(album=self)
    
    @property
    def review_count(self):

        return ReviewModel.objects.filter(album=self).count()
    
    @property
    def reviews(self):

        return ReviewModel.objects.filter(album=self)
    

    def __str__(self) -> str:

        return self.album_title




class TrackModel(models.Model):
     
     track_title=models.CharField(max_length=200)

     singers=models.CharField(max_length=200)

     genre=models.CharField(max_length=200)

     duration=models.CharField(max_length=200)

     album=models.ForeignKey(AlbumModel,on_delete=models.CASCADE)

     creaded_date=models.DateField(auto_now_add=True)

     updated_date=models.DateField(auto_now=True)

     is_active=models.BooleanField(default=True)

     def __str__(self) -> str:

        return self.track_title
     


class  ReviewModel(models.Model):

    comments=models.CharField(max_length=200)

    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    album=models.ForeignKey(AlbumModel,on_delete=models.CASCADE)

    created_date=models.DateField(auto_now_add=True)

    updated_date=models.DateField(auto_now=True)

    is_active=models.BooleanField(default=True)

    def __str__(self) -> str:

        return self.comments


