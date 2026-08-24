from django.shortcuts import render

def vista_principal(request):
    return render(request, 'pr_repaso/inicio.html')