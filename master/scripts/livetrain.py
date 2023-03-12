import mysql.connector
import webbrowser
import sys
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

inp1 = sys.argv[1] 
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

    sql_result = """select train_no,st_id , ar_time
                    from route
                    where train_no = %s and ar_time < cast('%s' as time)
                    ORDER BY ar_time DESC
                    LIMIT 1  ;"""%(inp1,current_time)

    
    cursor = connection.cursor()
    cursor.execute(sql_result)

    result = cursor.fetchall()
    print(result)

    p = []

    for row in result:
        a = row[0]
        p.append(a)
        b = row[1]
        p.append(b)
        c = row[2]
        p.append(c)
        # d = "<td>%s</td></tr>"%row[3]
        # p.append(d)
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
    <div class="liveTrain2">
        <h1 align="center">Live Train Status</h1>
        <table align="center"><tr>
            <th>Train no. : %s</th>
        </tr>
        <tr>
            <th>Last station : %s</th>
        </tr>
        <tr>
            <th>Last station Time : %s</th>
        </tr>
        </table>
    </div>'''%(st,st2,st3,home,search,about,help,st4,p[0],p[1],p[2])

    filename = 'train_status.html'

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