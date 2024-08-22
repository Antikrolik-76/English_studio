from django.shortcuts import render


def groups(request):
    return render(request, 'groups.html', {'title': 'groups'})
