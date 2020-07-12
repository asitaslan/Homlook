from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage
from product.models import Product, Category, Images, danisman, DanismanImage, DugunSalonu, Sabit3Image, SabitImage, Sabit2Image


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:7]
    lastproducts = Product.objects.all().order_by('-id')[:3]
    lastdanismans = danisman.objects.all().order_by('-id')[:3]
    lastsalon = DugunSalonu.objects.all().order_by('-id')[:3]
    count = 6;

    context = { 'setting': setting,
                'page': 'home',
                'sliderdata': sliderdata,
                'lastproducts': lastproducts,
                'lastdanismans': lastdanismans,
                 'lastsalon' : lastsalon,
               }
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    sabithakkimizda1 = SabitImage.objects.all()[:1]
    sabithakkimizda2 = Sabit2Image.objects.all()[:1]
    context = {'setting': setting, 'sabithakkimizda1':sabithakkimizda1, 'sabithakkimizda2': sabithakkimizda2, 'page': 'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def iletisim(request):
    sabitiletisim = Sabit3Image.objects.all()[:1]
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message =form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız Başarılı bir şekilde gönderilmiştir")
            return HttpResponseRedirect('/iletisim')


    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting' :setting ,'sabitiletisim':sabitiletisim, 'form':form}
    return render(request, 'iletisim.html', context)

def product_detail(request, id, slug):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
   # comments = Comment.objects.filter(product_id=id, status='True')
    context = {'product': product,
               'category': category,
               'images': images,
              # 'comments': comments,
               'setting': setting,

               }
    return render(request, 'product_detail.html', context)
def products(request):
    products = Product.objects.all()
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    context = {'products': products,
                'page'   : products,
               'setting' : setting,
               'sliderdata': sliderdata,
               }
    return render(request, 'products.html', context)

def danisman_detail(request, id ,slug):
    setting = Setting.objects.get(pk=1)
    danismans = danisman.objects.get(pk=id)
    images = DanismanImage.objects.filter(danismans_id=id)
   # comments = Comment.objects.filter(product_id=id, status='True')
    context = {'danismans': danismans,
               'images': images,
               'setting': setting,
               }
    return render(request, 'danisman_detail.html', context)

def danismans(request):
    setting = Setting.objects.get(pk=1)
    danismans = danisman.objects.all()

    context = {
               'page': danismans,
               'setting': setting,
               'danismans': danismans,

               }
    return render(request, 'danismans.html', context)

def salon(request):
    setting = Setting.objects.get(pk=1)
    slidersalondata =DugunSalonu.objects.all()[:100]
    salon = DugunSalonu.objects.all()

    context = {
        'page': salon,
        'setting': setting,
        'salon': salon,
        'slidersalondata': slidersalondata

    }
    return render(request, 'salon.html', context)
