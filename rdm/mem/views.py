from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
import mysql.connector
from datetime import datetime
from rest_framework import views
from rest_framework.response import Response
from .serializers import DataSerializer

class DataAPI(views.APIView):
    def get(self, request):
        your_data= [{
          "field1" : 'h',
          "field2" : 10
        }]
        serializer = DataSerializer(your_data, many=True)
        return Response(serializer.data)


connection = None

def establish_connection():
    global connection
    # if not connection:
    connection = mysql.connector.connect(
        host='localhost',
        database='railway',
        user='root',
        password='root'
    )

From = None
To = None

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def search(request) :
  return render(request, 'search.html')

# @requires_csrf_token
def searchres(request):
  global From
  global To
  From = request.POST.get('from')
  To = request.POST.get('to')
  global connection
  if not connection:
    establish_connection() 

  sql_result = """select L.train_no, L.train_name, R1.ar_time, R2.ar_time,seats
                  from trains as L, route as R1, route as R2
                  where L.train_no = R1.train_no and R1.train_no = R2.train_no and R1.st_id = '%s' and R2.st_id = '%s';""" % (
      From, To)

  cursor = connection.cursor()
  cursor.execute(sql_result)
  result = cursor.fetchall()

  context = {
      'result': result,
  }

  return render(request, 'searchres.html', context)

def book(request) :
  global From
  global To
  context =  {
      'from' : From ,
      'to' : To,
  } 
  return render(request,'book.html',context)

def chart(request) :
   return render(request,'chart.html')

def getchart(request) :
  train_no = request.POST.get('train_no')

  global connection
  if not connection:
    establish_connection() 

  sql_result = """select*from passengers as P
                  where P.train_no = %s;"""%(train_no)
  
  cursor = connection.cursor()
  cursor.execute(sql_result)
  result = cursor.fetchall()

  context = {
      'result': result,
  }

  return render(request, 'chartres.html', context)

def live(request) :
  return render(request,'status.html')

def status(request) :
  train_no = request.POST.get('train_no')
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")

  global connection
  if not connection:
    establish_connection() 

  sql_result = """select T.train_name, R.st_id , R.ar_time
                    from route as R,trains as T
                    where R.train_no = T.train_no and R.train_no = %s and R.ar_time < cast('%s' as time)
                    ORDER BY R.ar_time DESC
                    LIMIT 1  ;"""%(train_no,current_time)
  
  cursor = connection.cursor()
  cursor.execute(sql_result)
  result = cursor.fetchall()

  for row in result:
    x = row[0]
    a = row[1]
    b = row[2]

  context = {
      'train_name' : x,
      'st_id': a,
      'ar_time' : b,
      'train_no' : train_no,
  }

  return render(request, 'status_live.html', context)

def enquiry(request) :
  return render(request,'enquiry.html')

def getPNR(request) :
  PNR_no = request.POST.get('PNR')

  global connection
  if not connection:
    establish_connection() 
  sql_result = """select*from passengers as P
                  where P.pnr_no = %s;"""%(PNR_no)

  cursor = connection.cursor()
  cursor.execute(sql_result)
  result = cursor.fetchall()

  context = {
      'result': result,
  }

  return render(request, 'enquiryres.html', context)


# def book(request) :
# def confirm(request) :


