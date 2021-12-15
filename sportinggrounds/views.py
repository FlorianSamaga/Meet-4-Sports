from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import GroundPictureForm, CreateGroundForm
from django.contrib import messages
from .models import Grounds
from django.contrib.auth.decorators import login_required

def show_ground(request):
    if request.method == 'GET':
        posts=[]
        rq = request.GET
        name = rq.__getitem__('name')
        qs = Grounds.objects.filter(name=name)
        for temp in qs:
            if temp.changingrooms == 'false':
                chRo = 'available'
            else:
                chRo = 'not available'

            dic = {'name': temp.name, 'type': temp.type, 'street': temp.street, 'postal': temp.postal, 'area': temp.area, 'country': temp.country, 'opens': temp.opens, 'closes': temp.closes, 'changingrooms': chRo, 'parkingsituation': temp.parkingsituation, 'publictransportation': temp.publictransportation, 'image': temp.image}
            posts.append(dic)

        context={
            'posts':posts
        }

        return render(request, 'ground.html', context)
    else:
        messages.success(request, f'Sportingground has not been found!')
    return home(request)



def home(request):
    posts = []
    qs = Grounds.objects.all()

    for temp in qs:
        dic = {'name': temp.name, 'image': temp.image, 'type': temp.type}
        posts.append(dic)

    context={
        'posts':posts
    }
    return render(request, 'home.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        info_form = CreateGroundForm(request.POST, request.FILES)
    
        if info_form.is_valid():
            messages.success(request, f'Sportingground has been created!')
            info_form.save()
        else:
            messages.error(request, f'Error while creating sportsground information.')
            return redirect('createSportingground')

        return redirect('sportinggrounds')   
    else:
        info_form = CreateGroundForm()
        return render(request, 'create.html', {'info_form': info_form})
