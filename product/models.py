from django.db import models

# Create your models here.
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    STATUS =(
        ('True', 'Evet'),
        ('False', 'Hayir'),
    )
    title= models.CharField(max_length=30)
    keywords= models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    image= models.ImageField(blank=True, upload_to='images/')
    status= models.CharField(max_length=10, choices= STATUS)
    slug= models.SlugField()
    parent= TreeForeignKey('self', blank=True, null=True, related_name='children',on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now= True)

    class MPTTMeta:

        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '-->'.join(full_path[::-1])

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Product(models.Model):
    STATUS =(
        ('True', 'Evet'),
        ('False', 'Hayir'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    keywords= models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    image= models.ImageField(blank=True, upload_to='images/')
    status= models.CharField(max_length=10, choices= STATUS)
    detail = RichTextUploadingField()
    price = models.FloatField()
    slug = models.SlugField()
    amount = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now= True)
    alan = models.CharField(max_length= 20)
    oda =models.IntegerField()
    banyo = models.IntegerField()
    tip = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class danisman(models.Model):
    isim= models.CharField(max_length=30)
    soyisim = models.CharField(max_length=20)
    telefon = models.CharField(max_length=15)
    email = models.CharField(max_length= 200)
    image = models.ImageField(blank= True , upload_to= 'images/')
    detail = RichTextUploadingField()
    skype = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)

    def __str__(self):
         return self.isim

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class DanismanImage(models.Model):
    danismans = models.ForeignKey(danisman, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'




class DugunSalonu(models.Model):
    image = models.ImageField(blank= True , upload_to= 'images/')
    detail = RichTextUploadingField()


    def __str__(self):
        return self.detail

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'







class SalonImage(models.Model):
    salon = models.ForeignKey(DugunSalonu, on_delete=models.CASCADE)
    title = models.CharField(blank= True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class SabitImage(models.Model):
    title = models.CharField(blank= True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Sabit2Image(models.Model):
    title = models.CharField(blank= True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Sabit3Image(models.Model):
    title = models.CharField(blank= True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'