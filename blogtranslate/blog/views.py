from django.http import JsonResponse
from google.cloud import translate_v2 as translate
from .models import Blog

# Create client once
translate_client = translate.Client()

def translate_blog(request, blog_id):
    target_lang = request.GET.get("lang", "en")  # default: English
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        return JsonResponse({"error": "Blog not found"}, status=404)

    # Translate fields
    translated_header = translate_client.translate(blog.header, target_language=target_lang)["translatedText"]
    translated_body = translate_client.translate(blog.body, target_language=target_lang)["translatedText"]

    return JsonResponse({
        "blog_id": blog.id,
        "target_lang": target_lang,
        "header": translated_header,
        "body": translated_body,
    })
