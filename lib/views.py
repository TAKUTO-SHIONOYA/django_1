from django.shortcuts import render
from .models import Book, Category, Author
from django.http import HttpResponse
from .forms import CreateForm,createForm,FindForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
import pandas as pd

# Create your views here.

def pagination(request, queryset, count):

    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj

def main(request, page):

    data = Book.objects.all()
    paginator = Paginator(data, 10)

    page = request.GET.get('page')
    contacts = paginator.get_page(page)



        
    return render(request,'lib/main.html',{'data':data} ,{'contacts': contacts})

def content(request,num):
    book = Book.objects.get(id=num)
    num = book.id
    content = book.book_context
    return render(request, 'lib/book_content.html',{'book':book},{'num':num})

def create(request):

    if (request.method == 'POST'):
        obj = Book()
        book = createForm(request.POST, instance=obj)
        book.save()
        return redirect(to='/main/1/')
    params ={
            'form': createForm()

    }

    return render(request, 'lib/create.html', params)

def index(request,num):
    data = Book.objects.all()
    page_obj = paginate_queryset(request, data, 10)

    params = {
        'data': page_obj.object_list,
        'page_obj': page_obj,



        }
    return render(request, 'lib/index.html', params)

def find(request):
    if (request.method == 'POST'):
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from Lib_Authors'
        if (msg != ''):
            sql += ' where ' + msg
        data = Book.objects.raw(sql)
        msg = sql
    else:
        msg = 'search words...'
        form = FindForm()
        data = Book.objects.all()

    params = {
        'title': 'Hello',
        'message': msg,
        'form':form,
        'data':data,

    }
    return render(request, 'lib/find.html', params)
