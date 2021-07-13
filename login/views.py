from django.db.models import Avg, Count, Max, Min
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from login import models
import datetime

from django.shortcuts import HttpResponse

# Create your views here.


def index(request):
    students = models.Student.objects.all()
    m = models.Student(name='wc22', age=31, sex=1, mobile=13022214434, createTime=datetime.datetime.now())
    m.save()
    list = []
    for k in students:
        list.append({
            "name": k.name,
            "age": k.age,
        })
    return render(request, 'index.html', {"data": list})

def add_book(request):
    pub_obj = models.Publish.objects.filter(pk=1).first()
    pk = pub_obj.pk
    book = models.Book.objects.create(title='django教程2xxxx',price=25,pub_date='2012-12-13', publish_id=pk)
    print(book, type(book))
    return  HttpResponse(book)

def add_book2(request):
    chong = models.Author.objects.filter(name='令狐冲').first()
    ying = models.Author.objects.filter(name='任盈盈')
    book = models.Book.objects.filter(title='django教程2').first()
    book.anthors.add(chong.pk)
    return  HttpResponse(ying.values())

def add_book3(request):
    chong = models.Author.objects.filter(name='令狐冲').first()
    book = models.Book.objects.filter(title='django教程3').first()

    chong.book_set.add(book)
    return  HttpResponse('success')

def add_book4(request):
    pub = models.Publish.objects.filter(name='明教出版社').first()
    wo = models.Author.objects.get(name='任我行')
    # wo.book_set.create(title='吸星大法',price=300,pub_date='2012-11-23',publish=pub)
    book_obj = models.Book.objects.create(title='吸星大法2',price=300,pub_date='2012-11-23',publish=pub)
    book_obj.anthors.add(wo)
    return HttpResponse('success')

def add_book5(request):
    author_obj = models.Author.objects.get(id=3)
    book_obj = models.Book.objects.get(id=1)
    book_obj.anthors.remove(author_obj)
    return HttpResponse('success')

def remove_authors(request):
    book_obj = models.Book.objects.filter(title='吸星大法2').first()
    book_obj.anthors.clear()
    return  HttpResponse('success')

def query1(request):
    book = models.Book.objects.filter(pk=1).first()

    res = book.publish.email
    return HttpResponse(res)

def query2(request):
    pub = models.Publish.objects.filter(name='明教出版社').first()

    books = pub.book_set.all()
    return  HttpResponse('ok')

def query3(request):
    # author = models.Author.objects.filter(name='令狐冲').first()
    # res = author.au_detail.tel
    addr = models.AuthorDetail.objects.filter(addr='黑木崖').first()
    res = addr.author.name
    return  HttpResponse(res)

def query4(request):
    book = models.Book.objects.filter(title='吸星大法').first()
    res = book.anthors.all()
    for k in res:
        print(k.au_detail.tel)
    return JsonResponse(dict(a=1,b=2))

def query5(request):
    book = models.Book.objects.filter(publish__name='华山出版社').values_list('title', 'price')
    res1 = models.Author.objects.filter(name='任我行').values_list('au_detail__tel')
    res2 = models.AuthorDetail.objects.filter(author__name='任我行').values_list('tel')

    res3 = models.Author.objects.filter(name='任我行').values_list('book__title')

    res4 = models.Book.objects.filter(anthors__name='任我行').values_list('title')
    return HttpResponse(res3)

def agg(request):
    res = models.Book.objects.aggregate(avg = Avg('price'))
    print(models.Book.objects.aggregate(c=Count('id'), max=Max('price'), min=Min('price')))
    return JsonResponse(res)

def agg2(request):
    # res = models.Publish.objects.values('name').annotate(in_price=Avg('book__price'))
    # res2 = models.Book.objects.annotate(all=Count('anthors__name')).filter(all__gt=0).values('title', 'all')
    res2 = models.Book.objects.annotate(city=Count('publish__city')).values('title', 'city')
    return HttpResponse(res2)

class Book(View):
    def get(self,request):
        id = request.GET.get('id', 1)
        print(id)
        book_obj = models.Book.objects.get(pk=id)
        return HttpResponse(book_obj)

    def post(self, request):
        title = request.POST.get('title')
        price = request.POST.get('price')

        pub_date = request.POST.get('pub_date')
        publish_id = request.POST.get('publish_id')
        author_id = request.POST.get('author_id')
        book = models.Book.objects.create(title=title,price=price,pub_date=pub_date,publish_id=publish_id)
        book.anthors.add(author_id)
        return HttpResponse('success')





