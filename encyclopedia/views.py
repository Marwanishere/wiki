from django.shortcuts import render

from django.http import HttpResponse

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# psuedocode for function below provided by cs50.ai chatbot
def newfile(request):
    if request.method == 'POST':
        title = request.POST['newfilename']
        content = "#" + request.POST['newfilename'] + "\n" + request.POST['newpage']
        entries = util.list_entries()
        if title in entries:
            return render(request, "encyclopedia/errorpageexists.html")
        else:
            util.save_entry(title, content)
        return render(request, "encyclopedia/get.html", {
            "title": title,
            "get": content.lstrip("#" + title)
        })
    else:
        return render(request, "encyclopedia/newfile.html")
    
def editfile(request):
    # below line made using cs50.ai chatbot to get over
    # a techical error (multivaluedictkeyerror) and to get 
    #rid of errors due to filename containing newline characters
    title = request.POST.get('title').strip()
    # changed the line below to collect new content,
    #line made with cs50.ai chatbot assistance
    new_content = request.POST.get('editpage')
    if new_content != None:
        content =  "#" + title+ "\n" + new_content
        util.save_entry(title, content)
        return render(request, "encyclopedia/get.html", {
            "title": title,
            "get": new_content.lstrip("#" + title)
        })
    else:
        new_content = util.get_entry(title)
        return render(request, "encyclopedia/editfile.html",{
            "title":title,
            "old_content": new_content.lstrip("#" + title + "\n")
        })

def get(request):
    title = request.POST['title']
    # following six lines that allow for a title to be dictated 
    # were made with cs50.ai chatbot
    # I also learned how to use visual studio's python debugger
    # in the process
    markdown_text = util.get_entry(title)
    if markdown_text != None:
        lines = markdown_text.split('\n')
        title = title.lstrip('# '),
        title = lines[0] if lines else None
        markdown_text = markdown_text.lstrip(title)
        return render (request, "encyclopedia/get.html", {
            "title": title.lstrip('# '),
            "get": markdown_text
        })
    else :
        # following 4 lines made with assistance from cs50.ai chatbot
        all_entries = util.list_entries()
        matching_entries = [entry for entry in all_entries if title in entry]
        return render(request, "encyclopedia/searchlist.html", {
            "entries": matching_entries,
            "title" : title.lstrip('# ')
            })

#below function and import made with cs50.ai chatbot assistance
#below 2 lines acquired using cs50.ai chatbot
import random
from django.shortcuts import redirect
def randompage(request):
    entry = random.choice(util.list_entries())
    return redirect ("randomget", title= entry)

def randomget(request, title):
    # following six lines that allow for a title to be dictated 
    # were made with cs50.ai chatbot
    markdown_text = util.get_entry(title)
    lines = markdown_text.split('\n')
    title = title.lstrip('# '),
    title = lines[0] if lines else None
    markdown_text = markdown_text.lstrip(title)
    return render (request, "encyclopedia/randompage.html", {
        "title": title.lstrip('# '),
        "get": markdown_text
    })