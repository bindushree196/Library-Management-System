from django.shortcuts import render, redirect
from .models import Library

def library_list(request):
    data = Library.objects.all()
    return render(request, 'lmsapp/list.html',{'data': data})

def add_library(request):
    if request.method == 'POST':
            Library.objects.create(
            Student_Name = request.POST['Student_Name'],
            Title = request.POST['Title'],
            Quantity = request.POST['Quantity'],
            Author = request.POST['Author'],
            ISBN= request.POST['ISBN'],
            Published_Date = request.POST['Published_Date'],
            )
            return redirect('library_list')
    return render(request,'lmsapp/add.html')

def delete_library(request, id):
    lms = Library.objects.get(id=id)
    lms.delete()
    return redirect('library_list')

def update_library(request, id):
    lms = Library.objects.get(id=id)

    if request.method == 'POST':
        lms.Student_Name = request.POST['Student_Name']
        lms.Title = request.POST['Title']
        lms.Quantity = request.POST['Quantity']
        lms.Author= request.POST['Author']
        lms.ISBN=request.POST['ISBN']
        lms.published_date=request.POST['Published_Date']
        lms.save()
        return redirect('library_list')
    return render(request, 'lmsapp/update.html',{'lms':lms})

