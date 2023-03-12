import mysql.connector
import webbrowser
import sys


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

    sql_result = """select pnr_no,train_no,boarding_st_id,dest_st_id
                    from passenger
                    where pnr_no = %s;"""%(inp1)

    
    cursor = connection.cursor()
    cursor.execute(sql_result)

    result = cursor.fetchall()
    print(result)



    for row in result:
        a = row[0]
        b = row[1]
        c = row[2]
        d = row[3]

    contents = '''%s
    <!DOCTYPE html>
    <html>
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
    <h2>PNR number : %s</h2>
    <h2>Train no : %s</h2>
    <h2>Boarding Station : %s</h2>
    <h2>Destination : %s</h2>
    <h2>Status : Confirmed </h2>

    </BODY>
    </html>'''%(st,st2,st3,home,search,about,help,st4,a,b,c,d)

    filename = 'pnr_result.html'

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