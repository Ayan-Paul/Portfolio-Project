from django.shortcuts import render
from .models import ProjectWebsite, ProjectWebpage, ProjectFunWebpage

def index(request):
    projects_website = ProjectWebsite.objects.all().order_by('project_type')
    projects_webpage = ProjectWebpage.objects.all().order_by('project_type')
    projects_fun_webpage = ProjectFunWebpage.objects.all().order_by('project_type')

    return render(request,'intro/index.html',{'projects_website':projects_website,
                                            'projects_webpage':projects_webpage,
                                            'projects_fun_webpage':projects_fun_webpage,
    })