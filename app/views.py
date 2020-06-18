from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *

def index(request):
    return render(request, 'index.html')

def listCategory(request):
    categoryList = Category.objects.all()
    return render(request, 'category/list.html', {'categoryList': categoryList})

def addCategory(request):
    form = CategoryForm()
    # success = False
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            # success = True
            return redirect('list-category')
    return render(request, 'category/form.html', {'form': form})
    # return render(request, 'category/form.html', {'form': form,'success' = success})
def editCategory(request,pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('list-category')

    return render(request, 'category/form.html',{'form':form})

def deleteCategory(request, pk):
    category = get_object_or_404(Category,pk=pk)