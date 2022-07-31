from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact,Blog,FAQ


def index(request):
    allBlogs = Blog.objects.all().order_by('-timestamp')
    blog = []
    for item in allBlogs:
        blog.append({'id':item.blog_id,'name':item.name,'message':item.message,'time':item.timestamp})
    return render(request, 'blog/index.html',{'blog':blog})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    thank = False
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, phone=phone, email=email, subject=subject, message=message)
        contact.save()
        thank = True
    return render(request, 'blog/contact.html',{'thank':thank})

def FAQs(request):
    allfaq = FAQ.objects.all()
    faq=[]
    for item in allfaq:
        faq.append({'id':item.FAQ_id,'question':item.question,'answer':item.answer})
    return render(request, 'blog/FAQs.html', {'faq':faq})


def post(request):
    thank = False
    if request.method == 'POST':
        name = request.POST.get('firstname', '') + " " + request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        blog = Blog(name=name, email=email, message=message)
        blog.save()
        thank = True
    return render(request, 'blog/post.html',{'thank':thank})


def blogView(request, myid):
    blog = Blog.objects.filter(blog_id=myid)
    return render(request, 'blog/blogview.html',{'blog':blog[0]})


def searchMatch(query, item):
    if query in item.name.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allBlogs = Blog.objects.filter(name__icontains=query).order_by('-timestamp')
    params = {'allBlogs': allBlogs, "msg": ""}
    if len(allBlogs) == 0 or len(query) > 50:
        params = {'msg': "There is no blog posted with the "+query+" name . Please enter a valid name !!!"}
    return render(request, 'blog/search.html', params)
