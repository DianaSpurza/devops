from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime


def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    date = datetime.now().strftime("%Y-%m-%D %H:%M:%S")
    page = request.path
    sinfo = os.uname()
    cinfo = request.META['HTTP_USER_AGENT']
    response = {'date': date, 'current_page': page, 'server_info': sinfo, 'client_info': cinfo}
    return JsonResponse(response)

