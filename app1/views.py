from django.shortcuts import render, redirect
from .models import Todo
from datetime import datetime

# 🔹 HOME (Add + Show + Search)
def home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')

        # ✅ Convert date safely
        if due_date:
            try:
                due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
            except:
                due_date = None
        else:
            due_date = None

        if title:
            Todo.objects.create(title=title, due_date=due_date)

        return redirect('/')

    query = request.GET.get('q')
    if query:
        todos = Todo.objects.filter(title__icontains=query)
    else:
        todos = Todo.objects.all()

    return render(request, 'home.html', {'todos': todos})


# 🔹 DELETE TASK
def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')


# 🔹 TOGGLE COMPLETE
def toggle(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('/')


# 🔹 EDIT TASK
def edit(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == "POST":
        todo.title = request.POST.get('title')
        todo.due_date = request.POST.get('due_date')
        if due_date =="":
            due_date = None
        todo.due_date = due_date   
        todo.save()
        if 'title':
            Todo.objects.create(title='title',due_date=due_date)
        return redirect('/')

    return render(request, 'edit.html', {'todo': todo})


# 🔹 CLEAR ALL TASKS
def clear_all(request):
    Todo.objects.all().delete()
    return redirect('/')