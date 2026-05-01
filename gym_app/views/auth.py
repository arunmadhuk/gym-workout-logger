from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse


def user_login(request):
    print("Login view called")
    print(f"Request : {request}")
    template_name = 'auth/login.html'
    context = {'title': 'Login'}
    if request.method == 'POST':
        print("Login form submitted with data:")
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Email: {email}")
        print(f"Password: {password}")
        # Here you would typically authenticate the user and log them in

        # Authenticate using the custom backend
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print(f" user :'{email}' logged in succesfully")
            return JsonResponse({"message": "Login successful", "user": user.email}, status=200)
        else:
            print(f" user :'{email}' log in attempt failed")
            return JsonResponse({"error": "Invalid credentials"}, status=200)
  
    return render(request, template_name, context)

def user_logout(request):
    print("Logout view called")
    print(f"Request : {request}")
    template_name = 'auth/logout.html'
    context = {'title': 'Logout'}
    return render(request, template_name, context)