from django.shortcuts import render

# Create your views here.
def clublist(request):
    return render(request, 'posts/club_list.html')