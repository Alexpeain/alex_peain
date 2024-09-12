from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Change index.html to your main HTML file
