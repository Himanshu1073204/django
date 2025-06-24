from django.http import HttpResponse
from django.shortcuts import render



# data= {'bdata': 'kya seen bhailog',
#        'clist':['php', 'java', 'Django'],
#        'student_detail': [
#         {'name': 'pardeep', 'phone': 756484985},
#         {'name': 'hello', 'phone': 95633785} 
#        ],
#        'number':[10, 20, 30, 50]  
#     }



def home(request):
    return render(request, "index.html")
def view_all(request):
    return render(request, 'all_blogs.html')

