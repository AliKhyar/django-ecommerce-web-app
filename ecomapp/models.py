from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=200,unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='catgory'
        verbose_name_plural='catgories'
        def __str__(self):
            return self.name
class Product(models.Model):
    catalog=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name=models.CharField(max_length=40,db_index=True)
    slug=models.SlugField(max_length=100,db_index=True)
    image=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)
    def __str__(self):
        return self.name
