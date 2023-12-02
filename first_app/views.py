from django.shortcuts import render
import datetime


# Create your views here.
def home(request):
    d = {
        "author": "Rahim",
        "age": 20,
        "list": ["python", "c", "c++"],
        "birthday": datetime.datetime.now(),
        "courses": [
            {id: 1, "name": "Python", "fee": 500},
            {id: 2, "name": "Django", "fee": 600},
            {id: 3, "name": "C++", "fee": 700},
        ],
    }
    return render(request, "home.html", d)
