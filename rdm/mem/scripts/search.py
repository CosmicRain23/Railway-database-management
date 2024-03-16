from django.shortcuts import render
import mysql.connector

def searchres(request):
    inp1 = request.POST.get('from')
    inp2 = request.POST.get('to')

    connection = mysql.connector.connect(host='localhost',
                                         database='railway',
                                         user='root',
                                         password='root')

    sql_result = """select L.train_no, L.train_name, R1.ar_time, R2.ar_time
                    from trains as L, route as R1, route as R2
                    where L.train_no = R1.train_no and R1.train_no = R2.train_no and R1.st_id = '%s' and R2.st_id = '%s';""" % (
        inp1, inp2)

    cursor = connection.cursor()
    cursor.execute(sql_result)
    result = cursor.fetchall()

    context = {
        'result': result,
    }

    return render(request, 'searchres.html', context)
