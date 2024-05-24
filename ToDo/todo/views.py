from datetime import date

from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.shortcuts import redirect, render
from .models import ToDoItem
from .forms import ToDoForm


class AllToDos(ListView):
    model = ToDoItem
    template_name = "todo/base.html"

    def post(self, request, *args, **kwargs):
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the same page after adding task
        else:
            # Handle form errors if needed
            pass

    def get_queryset(self):
        return ToDoItem.objects.filter().order_by('due_date')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = ToDoForm()  # Add form to context for rendering in template
    #     return context


class TodayToDo(ListView):
    model = ToDoItem
    template_name = "todo/index.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(due_date=date.today())


def mark_complete(request, pk):
    task = ToDoItem.objects.get(pk=pk)
    task.is_complete = True
    task.save()

    referer_url = request.META.get('HTTP_REFERER', None)
    if referer_url and 'today' in referer_url:
        return redirect('today')
    else:
        return redirect('index')


def mark_incomplete(request, pk):
    task = ToDoItem.objects.get(pk=pk)
    task.is_complete = False
    task.save()

    referer_url = request.META.get('HTTP_REFERER', None)
    if referer_url and 'today' in referer_url:
        return redirect('today')
    else:
        return redirect('index')


def del_task(request, pk):
    task = ToDoItem.objects.get(pk=pk)
    task.delete()

    referer_url = request.META.get('HTTP_REFERER', None)
    if referer_url and 'today' in referer_url:
        return redirect('today')
    else:
        return redirect('index')


def edit_task(request, pk):
    task = ToDoItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            referer_url = request.META.get('HTTP_REFERER', None)
            if referer_url and 'today' in referer_url:
                return redirect('today')
            else:
                return redirect('index')
    else:
        form = ToDoForm(instance=task)

    return render(request, 'todo/edit.html', {'form': form})
