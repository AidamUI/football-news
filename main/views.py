from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406404781',
        'name': 'Muhammad Kaila Aidam Riyan',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
