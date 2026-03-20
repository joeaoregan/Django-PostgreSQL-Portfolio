from django.shortcuts import render, get_object_or_404
from .models import Job
from django.db import OperationalError

def home(request):
    try:
        jobs = Job.objects.all()
        # Force the query to execute here to catch the error early
        list(jobs) 
    except OperationalError:
        jobs = []  # Fallback to an empty list
        
    return render(request, 'jobs/home.html', {'jobs': jobs, 'db_error': not jobs})
	
def detail(request, job_id):
	# print(job_id) # show job id in console
	job_detail = get_object_or_404(Job, pk=job_id)
	# return render(request, 'jobs/home.html')
	return render(request, 'jobs/detail.html', {'job':job_detail})