from django.shortcuts import redirect


def redirect_map(request):
    return redirect('root_page', permanent=True)
