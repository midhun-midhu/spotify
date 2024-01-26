from django.shortcuts import render,redirect
from .models import Movie
from .forms import MovieForm

def Home(req):
    movies=Movie.objects.all()
    return render(req,'index.html',{'movies':movies})
def Form(req):
    if req.method=="POST": 
        name=req.POST.get('name','')
        language=req.POST.get('language','')
        duration=req.POST.get('duration','')
        image=req.FILES['image']
        description=req.POST.get('description','')        
        movie=Movie(name=name,language=language,duration=duration,image=image,description=description)
        movie.save()
        return redirect('home')
    return render(req,'form.html')



def Details(req,id):
    movies=Movie.objects.get(id=id)
    return render(req,'details.html',{'movie':movies})
def Update(req,id):
    movies=Movie.objects.get(id=id)
    f=MovieForm(req.POST,req.FILES or None,instance=movies)
    if f.is_valid():
        f.save()
        return redirect('home')
    return render(req,'formUpdate.html',{"movie":movies,'f':f})

def Delete(req,id):
    movies=Movie.objects.get(id=id)
    if req.method=="POST":
        Movie.objects.filter(id=id).delete()
        return redirect('home')
    return render(req,'delete.html',{"movies":movies})