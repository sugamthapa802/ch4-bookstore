from django.shortcuts import render
from django.views.generic import TemplateView

# def home(request):
#     return render(request,'templates/home.html')
class HomePageView(TemplateView):
    template_name='home.html'

class AboutPageView(TemplateView):
    template_name="about.html"