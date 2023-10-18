
from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.views import View





def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта ', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


 #def create(request):
  #  error = ''
   # if request.method == 'POST':
#
 #       form = TaskForm(request.POST)
  ##         form.save()
    #        return redirect('home')
     #   else:
      #      error = 'Форма не верна'
#
#
 #   form = TaskForm()
  #  context = {
   #     'form': form,
    #    'error': error
#
 #   }
  #  return render(request, 'main/create.html', context)

class TaskCreateView(View):
    template_name = 'main/create.html'

    def get(self, request):
        form = TaskForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = {'form': form, 'error': 'Форма не верна'}
            return render(request, self.template_name, context)

