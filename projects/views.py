from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm,DocumentForm
from .models import Project
import os
from django.utils.html import format_html

# Create your views here.

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            return redirect(project_list)
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form':form,'project':None})

def project_list(request):
    status = request.GET.get('status')
    if status:
        projects = Project.objects.filter(status=status)
    else:
        projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

@login_required
def edit_project(request,pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance = project)
    if form.is_valid():
        form.save()
        return redirect ("project_list")
    return render(request,'projects/project_form.html',{'form':form, 'project':project})

@login_required
def delete_project(request,pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request,'projects/confirm_delete.html',{'project':project})


@login_required
def upload_document(request,project_id):
    project = get_object_or_404(Project, id = project_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.project = project
            document.save()
            return redirect ('project_list')
    else:
        form = DocumentForm()
    return render(request, 'projects/upload_document.html',{'form':form, 'project':project})


@login_required
def project_detail(request,pk):
    project = get_object_or_404(Project, pk=pk)
    documents = project.documents.all()
    return render(request, 'projects/project_detail.html',{
        'project':project,
        'documents':documents
    })