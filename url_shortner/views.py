from django.http import HttpResponse
from django.shortcuts import render,redirect
import random
from url.models import Url,Video
from datetime import datetime 

def index(request):
    if request.method == "POST":
        link = request.POST.get("link")
        short_link = ""

        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        url = Url.objects.all()
        
        for i in url:
            if i.link == link:
                short_link = i.short_link
                break

        else:
            for i in range(1, 7):
                letters = random.randint(1, len(alpha) - 1)
                let = alpha[letters]
                short_link += let

            current_datetime = datetime.now()
            url = Url(link=link, short_link=short_link,request_datetime=current_datetime)
            url.save()
            url.ip_address = get_client_ip(request)
            url.save(update_fields=['ip_address'])

        new_url = "http://127.0.0.1:8000/" + short_link

        if not new_url :
            return render(request,"index.html")
        return render(request, "index.html", {"new_url": new_url})

    return render(request, "index.html")

def shorten(request, id):
    url = Url.objects.filter(short_link=id)
    link = ""
    for i in url:
        link = i.link

    return redirect(link)

def url_history(request):
    urls = Url.objects.order_by('request_datetime')  
    return render(request, 'history.html', {'urls': urls})

def redirect_to_original(request, short_link):
    try:
        url_object = Url.objects.get(short_link=short_link)
        # Redirect to the original URL
        return redirect(url_object.link)
    except Url.DoesNotExist:
        # Handle the case where the short link is not found
        return HttpResponse("Short link not found.", status=404)
    
def get_client_ip(request):
    # Function to get the user's IP address from the request object
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def view_recent_youtube_videos(request):
    recent_youtube_videos = Video.objects.filter(embed_link__icontains='youtube.com').order_by('-id')[:10]
    # Filter videos containing 'youtube.com' in the embed_link field, sorted by id to get the latest

    # Extract YouTube video IDs from the embed links
    youtube_embeds = []
    for video in recent_youtube_videos:
        video_id = video.embed_link.split('/')[-1]  # Assuming YouTube video IDs are at the end of the URL
        youtube_embed_url = f"https://www.youtube.com/embed/{video_id}"
        youtube_embeds.append(youtube_embed_url)

    return render(request, 'recent_youtube_videos.html', {'youtube_embeds': youtube_embeds})