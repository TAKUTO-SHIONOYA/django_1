from django.shortcuts import render
from .models import Book, Category, Author
from django.http import HttpResponse
from .forms import CreateForm,createForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

# Create your views here.
def paginate_queryset(request, queryset, count):
    """Pageオブジェクトを返す。

    ページングしたい場合に利用してください。

    countは、1ページに表示する件数です。
    返却するPgaeオブジェクトは、以下のような感じで使えます。

        {% if page_obj.has_previous %}
          <a href="?page={{ page_obj.previous_page_number }}">Prev</a>
        {% endif %}

    また、page_obj.object_list で、count件数分の絞り込まれたquerysetが取得できます。

    """
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


def main(request,num):
    data = Book.objects.all()
    page_obj = paginate_queryset(request, data, 10)

    params = {
        'data': page_obj.object_list,
        'page_obj': page_obj,



        }
    return render(request,'lib/main.html', params)

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
