from django.shortcuts import render
from report import models
from django.shortcuts import get_object_or_404



def index(request):
    build_list=models.build.objects.all()
    return render(request,'index.html',locals())


def table(request):
    perform_list=models.Performset.objects.all()
    return render(request,'report.html',{'perform_list':perform_list})

def dashboard(request):
    pass
    return render(request, 'assets/dashboard.html', locals())


def detail(request, asset_id):
    asset = get_object_or_404(models.Asset, id=asset_id)
    return render(request, 'assets/detail.html', locals())