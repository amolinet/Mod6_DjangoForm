from django.shortcuts import render
from .models import StudentForm
# Create your views here.

def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Process the form data
            return render(request, 'success.html', {'submitted_data': form.cleaned_data})
    else:
        form = StudentForm()
    
    return render(request, 'student_form.html', {'form': form})
