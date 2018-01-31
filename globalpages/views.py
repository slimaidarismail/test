from django.shortcuts import render
from django.views import View

# Create your views here.
class HomePage(View):
    template_name = 'globalpages/home.html'
    def get(self, request):
        return render(request, 'globalpages/home.html')