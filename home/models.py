from django.db import models

# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Textarea


class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # image= models.ImageField(blank=True, upload_to='images/')
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=20)
    smtemail = models.CharField(blank=True, max_length=20)
    smtppassword = models.CharField(blank=True, max_length=10)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactFormMessage(models.Model):
    STATUS=(
        ('New', 'New'),
        ('Read', 'Read'),
    )
    name =models.CharField(blank=True, max_length=20)
    email=models.CharField(blank=True, max_length=50)
    subject= models.CharField(blank=True, max_length=50)
    message=models.CharField(blank=True, max_length=255)
    status=models.CharField(max_length=10, choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note= models.CharField(blank=True, max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields=['name','email','subject','message']
        widgets ={
            'name'   :TextInput(attrs={'class': 'input', 'placeholder': 'Ad Soyad'}),
            'subject':TextInput(attrs={'class': 'input', 'placeholder':'Konu'}),
            'email'  :TextInput(attrs={'class': 'input', 'placeholder':'Email'}),
            'message':Textarea(attrs={'class': 'input', 'placeholder':'Mesajiniz', 'row':'5'}),
        }
