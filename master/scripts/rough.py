
import webbrowser
contents = '''''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
    {\% load static %}
    <html>
    <head>
    <title>
        eTicketing Platform
    </title>
    <link rel="stylesheet" href="{\% \static 'style.css' \%}">
    <link rel="icon" type="image/x-icon" href="{\% \static 'favicon.png' \%}">
    </head>
    <BODY>
    <div class="navi">
    <ul>
        <li><a onclick= "location.href='{\% \url 'home' \%}'">Home</a></li>
        <li><a href="Login.html">Login</a></li>
        <li><a href="#">Register</a></li>
        <li><a onclick= "location.href='{\% \url 'search' \%}'">Search Train</a></li>
        <li><a onclick= "location.href='{\% \url 'about' %}'">About</a></li>
        <li><a onclick= "location.href='{% url 'help' %}'">Help</a>
      </ul>
    </div>
    <div class="sectionLeft">
    <h1>INDIAN RAILWAYS</h1>
    <br>
    <h2>SAFETY | SECURITY | PUNCTUALITY</h2>
    </div>
    <div class="sectionLeft">
    <img src="{% static 'index_bg.jpg' %}" >
    </div>
    <div class="belowImage">
        <marquee>Welcome to Indian Railways</marquee>
    </div>
    <table>
    </table>
    </BODY>
    </html>'''''

filename = 'train_status.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

    main(contents, filename)    
    webbrowser.open(filename)