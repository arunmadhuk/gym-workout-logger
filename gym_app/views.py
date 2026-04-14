from django.shortcuts import render

# Create your views here.
def home(request):
    print("Home view called")
    print(f"Request : {request}")
    template_name = 'dashboard.html'
    context = {'title': 'Home'}
    return render(request, template_name, context)