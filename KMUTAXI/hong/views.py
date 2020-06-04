from django.shortcuts import render,get_object_or_404,redirect
from .models import HongdaeBoardModel,HongdaeComment
from django.utils import timezone
from .forms import HongdaeBoardModelForm,HongdaeCommentForm


# Create your views here.

#hong_station을 띄우는 views를 만들어주기
def hong(request):
    hongs = HongdaeBoardModel.objects.all()
    return render(request,'hong_station.html',{'hongs':hongs})
                   #=blog_id
def detail(request,taxi_id): #class이름
    hong = get_object_or_404(HongdaeBoardModel, pk = taxi_id)
    comment_form = HongdaeCommentForm() 
    comments = HongdaeComment.objects.all()
    return render(request, 'hong_detail.html',{'hong':hong, 'comment_form':comment_form,'comments':comments})
    #db에서 id를 가져옴

#새로작성할 글의 폼을 
def new(request):
    if request.method =='POST':
        form =HongdaeBoardModelForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False) #임시저장
            content.pud_date = timezone.now()
            content.save()
            return redirect('hong_station')

            
    else:
        form = HongdaeBoardModelForm()
        return render(request,'hong_new.html',{'form':form})

def create(request):
    new_hong = HongdaeBoardModel()
    new_hong.title = request.POST['title']
    new_hong.body=request.POST['body']
    new_hong.save()
    return redirect('hong_detail',new_hong.id)

def edit(request,taxi_id):
    edit_hong=get_object_or_404(HongdaeBoardModel,pk=taxi_id)
    return render(request,'hong_edit.html',{'hong':edit_hong})

def update(request,taxi_id):
    update_hong = get_object_or_404(HongdaeBoardModel,pk=taxi_id)
    update_hong.title = request.POST['title']
    update_hong.body=request.POST['body']
    update_hong.save()
    return redirect('hong_detail',update_hong.id)

def delete(request,texi_id):
    delete_hong = get_object_or_404(HongdaeBoardModel, pk = texi_id) 
    delete_hong.delete()
    return redirect('hong_station')


#새로작성할 글의 폼을 
def comment_create(request,texi_id):
    if request.method =='POST':
        form =HongdaeCommentForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False) #임시저장
            parents=get_object_or_404(HongdaeBoardModel, pk = texi_id)
            content.parents= parents
            content.save()
            return redirect('hong_detail',texi_id)
    else:
        form = HongdaeCommentForm()
        return render(request,'hong_new.html',{'form':form})


def comment_edit(request,comment_id):
    if request.method == "POST":
        update_hong = get_object_or_404(HongdaeComment,pk=comment_id)
        update_hong.title = request.POST['title']
        update_hong.body=request.POST['body']
        update_hong.save()
        return redirect('hong_detail', update_hong.parents.id)

    edit_hong=get_object_or_404(HongdaeComment,pk=comment_id)
    return render(request,'hong_edit.html',{'hong':edit_hong})
   
def comment_delete(request,comment_id):
    delete_hong = get_object_or_404(HongdaeComment, pk = comment_id) 
    delete_hong.delete()
    return redirect('hong_detail', delete_hong.parents.id)



