from django.shortcuts import render,get_object_or_404, redirect
from .models import *



# Create your views here.

def md_station(request):
    mockdongboards = MockdongBoard.objects.all()
    return render(request, 'md_station.html',{'mockdongboards':mockdongboards})

def detail(request,mockdongboard_id):
    mockdongboard = get_object_or_404(MockdongBoard, pk = mockdongboard_id)
    return render(request, 'md_detail.html', {'mockdongboard':mockdongboard})

def new(request):
    return render(request,'md_new.html')

def create(request):
    new_mockdongboard = MockdongBoard()
    new_mockdongboard.title = request.POST['title']
    new_mockdongboard.body = request.POST['body']
    new_mockdongboard.save()
    return redirect('md_detail', new_mockdongboard.id)

def edit(request,mockdongboard_id):
    mockdongboard = get_object_or_404(MockdongBoard, pk = mockdongboard_id)
    return render(request, 'md_edit.html',{'mockdongboard':mockdongboard})

def update(request,mockdongboard_id):
    edit_mockdongboard = get_object_or_404(MockdongBoard, pk = mockdongboard_id)
    edit_mockdongboard.title = request.POST['title']
    edit_mockdongboard.body = request.POST['body']
    edit_mockdongboard.save()
    return redirect('md_edit', edit_mockdongboard.id)

def delete(request,mockdongboard_id):
    delete_mockdongboard = get_object_or_404(MockdongBoard, pk = mockdongboard_id)
    delete_mockdongboard.delete()
    return redirect('md_station')
