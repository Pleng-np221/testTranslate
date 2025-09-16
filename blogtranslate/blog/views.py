from django.shortcuts import render
from django.http import JsonResponse
from google.cloud import translate_v2 as translate
from .models import Blog

translate_client = translate.Client()

def home(request):
    blogs = Blog.objects.all()
    return render(request, "blog/home.html", {"blogs": blogs})

def translate_blog(request, blog_id):
    target_lang = "en"  # always translate to English
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return JsonResponse({"error": "Blog not found"}, status=404)

    translated_header = translate_client.translate(blog.header, target_language=target_lang)["translatedText"]
    translated_body = translate_client.translate(blog.body, target_language=target_lang)["translatedText"]

    return JsonResponse({
        "blog_id": blog.id,
        "header": translated_header,
        "body": translated_body,
    })
