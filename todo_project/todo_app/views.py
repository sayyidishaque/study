from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.
def index(request):
    disp_task = Todo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        pre = request.POST.get('priority')
        dt = request.POST.get('date')
        task = Todo(Name=name, Priority=pre, Date=dt)
        task.save()

    return render(request, 'index.html', {'task': disp_task})


def delete(request, tskid):
    if request.method == 'POST':
        task = Todo.objects.get(id=tskid)
        task.delete()
        return redirect('/')

    return render(request, 'delete.html')


def update(request, tskid):
    task = Todo.objects.get(id=tskid)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'task': task})
