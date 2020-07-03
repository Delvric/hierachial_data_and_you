from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, reverse
from file_system.models import File_System
from file_system.forms import AddFilesForm
# Create your views here.


def show_files_system(request):
    return render(request, 'files.html', {'files': File_System.objects.all()})


def add_files_view(request):
    html = 'genericforms.html'

    if request.method == 'POST':
        form = AddFilesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File_System.objects.create(
                name=data['name'],
                parent=data['parent']
            )
        return HttpResponseRedirect(reverse('homepage'))

    form = AddFilesForm()
    return render(request, html, {'form': form})
# Create your views here.
