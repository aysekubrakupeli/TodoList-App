from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoItemForm

# Create your views here.
def get_index(request):
    results = TodoItem.objects.all()
    return render(request, "index.html", {'items': results})
    
def get_item_form(request):

    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(get_index)
    else:

        form = TodoItemForm()
        
    return render(request, "item_form.html", { 'form': form })

    
def edit_item(request, id):
   
   item = get_object_or_404 (TodoItem, pk = id)
   
   if request.method == "POST":
       form = TodoItemForm(request.POST, instance=item)
       if form.is_valid():
           form.save()
           return redirect(get_index)
       
       
   else:
       form = TodoItemForm(instance=item)
       
       
   return render(request, "item_form.html", { 'form': form })

    
def toggle_status(request, id):    
   item = get_object_or_404(TodoItem, pk=id)
   item.done = not item.done
   item.save()
   
   return redirect(get_index)

