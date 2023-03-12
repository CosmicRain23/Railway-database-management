import mysql.connector
import webbrowser
import sys
import os

os.remove("D:\\Sem 3\\dbms project\\backend\\master\\search_result.html")

inp1 = sys.argv[1] 
inp2 = sys.argv[2]
st = '{% load static %}'
st2 = "{% static 'style.css' %}"
st3 = "{% static 'favicon.png'%}"
home = "{% url 'home' %}"
search = "{% url 'search' %}"
about = "{% url 'about' %}"
help = "{% url 'help' %}"
st4 = "{% static 'index_bg.jpg' %}"

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='railway',
                                         user='root',
                                         password='root')

    sql_result = """select L.train_no , L.train_name,R1.ar_time,R2.ar_time
                    from list_of_train as L,route as R1,route as R2
                    where L.train_no = R1.train_no and R1.train_no = R2.train_no and R1.st_id = %s and R2.st_id = %s ;"""%(inp1,inp2)

    
    cursor = connection.cursor()
    cursor.execute(sql_result)
    # print("EMPLOYEE Table created successfully ")
    # result2 = cursor.execute(mySql_Create_Table_Query2)
    # print("DEPARTMENT Table created successfully ")
    result = cursor.fetchall()
    # for row in result :
    #     print(row[0],row[1],row[2],sep=' ')
    #     print(row[1])

    p = []

    for row in result:
        a = "<tr><td>%s</td>"%row[0]
        p.append(a)
        b = "<td>%s</td>"%row[1]
        p.append(b)
        c = "<td>%s</td>"%row[2]
        p.append(c)
        d = "<td>%s</td></tr>"%row[3]
        p.append(d)
    contents = '''%s
    <!DOCTYPE html>
    <html lang = "en">
    <head>
    <title>
        eTicketing Platform
    </title>
    <link rel="stylesheet" href="%s">
    <link rel="icon" type="image/x-icon" href="%s">
    </head>
    <BODY>
    <div class="navi">
    <ul>
        <li><a onclick= "location.href='%s'">Home</a></li>
        <li><a href="Login.html">Login</a></li>
        <li><a href="#">Register</a></li>
        <li><a onclick= "location.href='%s'">Search Train</a></li>
        <li><a onclick= "location.href='%s'">About</a></li>
        <li><a onclick= "location.href='%s'">Help</a>
      </ul>
    </div>
    <div class="sectionLeft">
    <h1>INDIAN RAILWAYS</h1>
    <br>
    <h2>SAFETY | SECURITY | PUNCTUALITY</h2>
    </div>
    <div class="sectionLeft">
    <img src="%s" >
    </div>
    <div class="belowImage">
        <marquee>Welcome to Indian Railways</marquee>
    </div>
    <div class="searchTrain2">
        <h1>Search Train</h1>
    <table align="center" cellpadding="10px">
        <tr><th>Train number</th>
            <th>Train name</th>
            <th>Arrival</th>
            <th>Reach time</th>
            
        </tr>
        %s
    </table>
    </div>
    </BODY>
    </html>
    '''%(st,st2,st3,home,search,about,help,st4,p)

    filename = 'search_result.html'

    def main(contents, filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()

    main(contents, filename)    
    # webbrowser.open(filename)



finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

# <th>book now</th>         