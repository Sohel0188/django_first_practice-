from django.shortcuts import render
import datetime

def about(request):
    return render(request,'first_app/about.html')

def contact(request):
    return render(request,'first_app/contact.html')
#dic = {}
def templatefilter(request):
    dic = {'Name' : 'sohel', 'age' : 24, 'phone' : '054522',
           'dob' : datetime.datetime.now(),
           'lst':['alu','potol','korola','lau'], 
           'numbers': [1,2,3,4,5,6,7,8],'course':[
        {'id' : 1,
         'course' : 'python',
         'fee' : '20000'
         },
        {'id' : 2,
         'course' : 'Data structure',
         'fee' : '20000'
         },
        {'id' : 3,
         'course' : 'django',
         'fee' : '15000'
         },
        {'id' : 4,
         'course' : 'Algorithm',
         'fee' : '10000'
         },
    ]}
    return render(request,'first_app/template_filtering.html',dic)
