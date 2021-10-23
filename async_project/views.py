from django.shortcuts import render, redirect
from .models import Article, Registerdb
from django.core.mail import send_mail
from django.conf import settings
from asgiref.sync import sync_to_async
import asyncio

#Asyncronius send mail function
async def async_send_mail(subject,message,email_list):
    a_send_mail = sync_to_async(send_mail, thread_sensitive=False)
    await a_send_mail(subject, message, settings.EMAIL_HOST_USER, email_list, fail_silently = False)
    print('email send successfully')

def dashboard(request):
    article = Article.objects.all()
    return render (request, 'async_project/dashboard.html', {'articles': article})

async def registerview(request):
    if request.method == 'GET':
        return render (request, 'async_project/register.html')
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')

        await sync_to_async(Registerdb.objects.create)(name=name, email = email)
        
        subject = "Registration successful"
        message = f"Hello {name}, \n\n Thanks for choosing our services, We will notify you when ever a new article is uploaded. Stay tuned.."
        

        asyncio.create_task(async_send_mail(subject, message, [email]))
        
        return redirect('/')

async def article_create(request):
    if request.method == 'GET':
        return render (request, 'async_project/article.html')
    else:
        title = request.POST.get('title')
        description = request.POST.get('description')
        print('title', title)
        print('description', description)

        await sync_to_async(Article.objects.create)(title=title, description = description)
        
        subject = "New Article uploaded!"
        message = f"New article with a title '{title}' is uploaded now, \n\n Enjoy reading.."
        
        customers = await sync_to_async(list)(Registerdb.objects.all())
        email_list = [Registerdb.email for Registerdb in customers]

        asyncio.create_task(async_send_mail(subject, message, email_list))
        return redirect('/')

    # return redirect('/register/')