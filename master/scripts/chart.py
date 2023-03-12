import mysql.connector
import webbrowser
import sys

# inp1 = sys.argv[1] 
# inp2 = sys.argv[2]

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='railway',
                                         user='root',
                                         password='root')

    sql_result = """select * from passenger"""

    
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

    tbl = "<tr><td>PNR</td><td>TRAIN NO</td></tr>"
    p.append(tbl)

    for row in result:
        a = "<tr><td>%s</td>"%row[0]
        p.append(a)
        b = "<td>%s</td>"%row[1]
        p.append(b)
        # c = "<td>%s</td>"%row[2]
        # p.append(c)
        # d = "<td>%s</td></tr>"%row[3]
        # p.append(d)
    contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
    <html>
    <head>
    <meta content="text/html; charset=ISO-8859-1"
    http-equiv="content-type">
    <title>Python Webbrowser</title>
    </head>
    <body>
    <table>
    %s
    </table>
    </body>
    </html>
    '''%(p)

    filename = 'chart.html'

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