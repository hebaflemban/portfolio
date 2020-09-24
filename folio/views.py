from django.shortcuts import render, redirect
from .models import Project, Guest
from .forms import ContactForm

def home(request):
    context = {
        'homeMsg' : 'A Cool Qoute',
        "projects": Project.objects.all()
    }
    return render(request, 'home.html', context)

def project_list(request):
    context = {
        "projects": Project.objects.all()
    }
    return render(request, 'list.html', context)


def project_detail(request, project_id):
    context = {
        "project": Project.objects.get(id=project_id)
    }
    return render(request, 'detail.html', context)

def tag_list(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags
    }
    return render(request, 'tag_list.html', context)

#
# def project_create(request):
#     form = ProjectForm()
#     if request.method == "POST":
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('project-list')
#     context = {
#         "form": form,
#     }
#     return render(request, 'admin/project_create.html', context)
#
#
# def project_update(request, project_id):
#     project_obj = Project.objects.get(id=project_id)
#     form = ProjectForm(instance=project_obj)
#     if request.method == "POST":
#         form = ProjectForm(request.POST, instance=project_obj)
#         if form.is_valid():
#             form.save()
#             return redirect('project-list')
#     context = {
#         "project_obj": project_obj,
#         "form": form,
#     }
#     return render(request, 'admin/project_update.html', context)
#
#
# def project_delete(request, project_id):
#     project_obj = Project.objects.get(id=project_id)
#     project_obj.delete()
#     return redirect('project-list')

############################################################################################
#                                   Tags                                                   #
############################################################################################

#
# def tag_create(request):
#     if request.user.is_staff:
#         return redirect('404')
#     form = TagForm()
#     if request.method == "POST":
#         form = TagForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('tag_list')
#     context = {
#         'form': form
#     }
#     return render(request, 'admin/tag_create.html', context)
#
# def tag_update(request, tag_id):
#     if (not request.user.is_staff) or (request.user != library.manager):
#         return redirect('404')
#
#     tag = Tag.objects.get(id=tag_id)
#     if request.method == "POST":
#         form = TagForm(instance=tag)
#         if form.is_valid():
#             form.save()
#             return redirect('tag_list')
#     context = {
#         'form': form,
#         'tag': tag
#     }
#     return render(request, 'tag_list', context)
#
# def tag_delete(request, tag_id):
# 	Tag.objects.get(id=tag_id).delete()
# 	return redirect('tag_list')
