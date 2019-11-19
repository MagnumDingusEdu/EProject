from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime, timezone
import csv
from .settings import BASE_DIR
import os

def home_view(request):
    if request.method == "GET":
        print(request.GET)
        if request.GET.get("triggerred") == "true":
            print("The alarm system has been triggered")
            with open(os.path.join(BASE_DIR, 'static', 'breach_log.csv'), mode='a') as breach_log:
                breachWwriter = csv.writer(breach_log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                list_list = []

                list_list.append(str(datetime.now().strftime('%I:%M %p')))
                list_list.append(str(datetime.now().strftime('%d %B %Y')))
                
                breachWwriter.writerow(list_list)
                
                breach_log.close()
    context = {
        "log": str(datetime.now().strftime('%I:%M %p %d %B %Y')),
    }
    return render(request, "index.html", context)

def clear_view(request):
    with open(os.path.join(BASE_DIR, 'static', 'breach_log.csv'), mode='w+') as breach_log:
        bwriter = csv.writer(breach_log)
        bwriter.writerow(['Date', 'Time'])
        breach_log.close()
    return redirect('/')