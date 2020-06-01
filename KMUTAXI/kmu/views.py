from django.shortcuts import render, get_object_or_404, redirect
from .models import KMU
from .form import KmuForm
from django.utils import timezone

# Create your views here.

def kmu_station(request):
    kmuboards = KMU.objects.all()
    return render(request, 'kmu_station.html', {'kmuboards':kmuboards})

def detail(request, kmuboard_id):
    kmuboard = get_object_or_404(KMU, pk = kmuboard_id)
    return render(request, 'kmu_detail.html', {'kmuboard':kmuboard})

def new(request):
    if request.method == 'POST':
        form = KmuForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False) #임시저장
            content.pub_date = timezone.now()
            content.save()
            return redirect('kmu_station')
    else:
        form = KmuForm()
        return render(request, 'kmu_new.html', {'form':form})

def create(request):
    new_kmuboard = KMU()
    new_kmuboard.title = request.POST['title']
    new_kmuboard.body = request.POST['body']
    new_kmuboard.save()
    return redirect('kmu_detail', new_kmuboard.id)

def edit(request,kmuboard_id):
    edit_kmuboard = get_object_or_404(KMU, pk = kmuboard_id)
    return render(request, 'kmu_edit.html',{'kmuboard':edit_kmuboard})

def update(request,kmuboard_id):
    update_kmuboard = get_object_or_404(KMU, pk = kmuboard_id)
    update_kmuboard.title = request.POST['title']
    update_kmuboard.pub_date = timezone.datetime.now()
    update_kmuboard.body = request.POST['body']
    update_kmuboard.save()  
    return redirect('kmu_detail', update_kmuboard.id)

def delete(request,kmuboard_id):
    delete_kmuboard = get_object_or_404(KMU, pk = kmuboard_id)
    delete_kmuboard.delete()
    return redirect('kmu_station')
