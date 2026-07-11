from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TotalFloors(models.Model):
    floor_name=models.CharField(max_length=100)
    description=models.TextField()
    floor_img=models.ImageField(upload_to='floorimg/',null=True,blank=True)
   
   
    def __str__(self):
        return self.floor_name


class supervisor(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    floor=models.ForeignKey(TotalFloors,on_delete=models.CASCADE)


class products(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.IntegerField()
    color=models.CharField(max_length=100)
    fabric=models.CharField(max_length=100)
    product_img=models.ImageField(upload_to='productimg',blank=True,null=True)
    floor=models.ForeignKey(TotalFloors,related_name='totalfloors',on_delete=models.CASCADE)

    # def _str_(self):
    #     return self.product_name

   
