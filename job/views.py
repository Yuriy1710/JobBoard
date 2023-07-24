from django.shortcuts import render, redirect
from .models import Job
from .forms import AddJobForm, ApplicationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    return render(request, 'job-detail.html', {'job':job})



@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()
            
            return redirect('dashboard')
        
    else:
        form = ApplicationForm() 
        
    return render(request, 'apply-for-job.html', {'form': form, 'job': job})   


@login_required
def add_job(request):
    if request.method == "POST":
        form = AddJobForm(request.POST)
        
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            
            return redirect('dashboard')
        
    else:
        form = AddJobForm()
        
    return render(request, 'add-job.html', {'form': form})