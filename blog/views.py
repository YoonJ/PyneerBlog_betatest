from django.shortcuts import render, get_object_or_404
from .models import Project
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User

#메인 페이지
def index_page(request):
    return render(request, 'blog/index.html')

#동그라미 버튼을 누르면 들어오는 프로젝트 상세 페이지
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'blog/project_detail.html', {'project':project})