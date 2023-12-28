from django.shortcuts import render

from django.views.generic import TemplateView

class IndexPageView(TemplateView):
    template_name = 'index.html'
    
def index(request):
    linkedin_profile_url = "https://www.linkedin.com/in/waigera-mwangi-995944223"
    return render(request, 'index.html', {'linkedin_profile_url': linkedin_profile_url})