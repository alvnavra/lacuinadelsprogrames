from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, Author, Blog, Language
from .forms import CommentForm, PostForm
from marketing.models import Signup
from django.utils.translation import get_language

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def get_blog():
    language = Language.objects.filter(llenguatge=get_language().upper())
    if language.exists():
        blog = Blog.objects.filter(language=language[0].id)
        if blog.exists():
            return blog[0]
    return None

def get_category_count(blog):
    queryset = Post.objects \
        .filter(blog=blog) \
        .filter(featured=True)\
        .values('categories__title')\
        .annotate(Count('categories'))

    return queryset

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    blog = get_blog()
    category_count = get_category_count(blog)
    most_recent = Post.objects.filter(blog=blog).filter(featured=True).order_by('-timestamp')[:3]

    if query:
        queryset = queryset.filter(blog=blog).filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)|
            Q(content__icontains=query)
        ).distinct()

        paginator = Paginator(queryset,4)
        page_request_var = 'page'
        page = request.GET.get(page_request_var)

        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages())


    context = {
        "active_classes": get_language_classes(),
        "queryset":paginated_queryset,
        "most_recent": most_recent,
        "page_request_var":page_request_var,
        "category_count":category_count,
    }


    return render(request, 'search_result.html',context)

def get_language_classes():

    active_classes = ['','','']
    active_str = 'class=active'
    active_language = Language.objects.filter(llenguatge=get_language().upper())
    if len(active_language) > 0:
        if active_language[0].llenguatge == 'CA':
            active_classes[2] = active_str
        elif active_language[0].llenguatge == 'ES':
            active_classes[1] = active_str
        elif active_language[0].llenguatge == 'EN':
            active_classes[0] = active_str

    context = {
    'active_en':active_classes[0],
    'active_es':active_classes[1],
    'active_ca':active_classes[2],
    }
    return context

def index(request):

    active_blog = get_blog()
    featured = Post.objects.filter(blog=active_blog).filter(featured = True)
    latest = Post.objects.filter(blog=active_blog).filter(featured = True).order_by('-timestamp')[0:3]

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
       'active_classes':get_language_classes(),
       'active_blog': active_blog,
       'object_list' :featured,
       'latest':latest
    }
    return render(request, 'index.html',context)

def blog(request):
    blog = get_blog()
    category_count = get_category_count(blog)
    most_recent = Post.objects.filter(blog=blog).filter(featured=True).order_by('-timestamp')[:3]
    post_list = Post.objects.filter(blog=blog).filter(featured=True)
    paginator = Paginator(post_list, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages())
    context = {
        "active_classes": get_language_classes(),
        "queryset":paginated_queryset,
        "most_recent": most_recent,
        "page_request_var":page_request_var,
        "category_count":category_count,
    }
    return render(request, 'blog.html',context)

def post(request, id):
    blog = get_blog()
    post = get_object_or_404(Post, id=id)
    most_recent = most_recent = Post.objects.filter(blog=blog).filter(featured=True).order_by('-timestamp')[:3]
    category_count = get_category_count(blog)
    comment_form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.instance.post = post
            comment_form.save()
            return redirect(reverse("post-detail", kwargs={
                'id':post.id
            }))


    context = {
        "active_classes": get_language_classes(),
        'comment_form':comment_form,
        'post':post,
        "most_recent": most_recent,
        "category_count":category_count,

    }
    return render(request, 'post.html',context)

def post_create(request):
    title = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    blog = get_blog()
    if request.method == 'POST':
        if form.is_valid():
            form.instance.blog = blog
            form.instance.author = author
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'id':form.instance.id
            }))
    context = {
        "active_classes": get_language_classes(),
        'title':title,
        'form':form
    }
    return render(request, "post_create.html", context)

def post_update(request, id):
    title = 'Update'
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'id':form.instance.id
            }))
    context = {
        "active_classes": get_language_classes(),
        'title':title,
        'form':form
    }
    return render(request, "post_create.html", context)




def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse('post-list'))
