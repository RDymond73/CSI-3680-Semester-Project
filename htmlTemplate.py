#Template for creating html pages

import os, webbrowser

#create folder for html pages if it doesn't exist
def createFolder():
    if os.path.exists('.\\htmlPages') == False:
        os.makedirs('.\\htmlPages')

#create html file for an array of data
def createHTML(row):
    file = open('.\\htmlPages' + '\\' + row[0] + '.html', 'w')
    data = """<html>
    <head></head>
    <body>
        <h1 ALIGN=CENTER>""" + row[0] + """</h1>
        <h2 ALIGN=CENTER>""" + row[1] + """</h2>
        <p ALIGN=CENTER>""" + row[2] + """</p>
        <p ALIGN=CENTER>""" + row[3] + """</p>
        <p ALIGN=CENTER>""" + row[4] + """</p>
        <p ALIGN=CENTER>""" + row[5] + """</p>
        <p ALIGN=CENTER>""" + row[6] + """</p>
    </body>
    
    </html>"""

    file.write(data)
    file.close()
    path = '.\\htmlPages' + '\\' + row[0] + '.html'
    webbrowser.open_new_tab(path)


test = ['Rick Dymond', '11/10/99', 'Test1', 'Test2', 'Test3', 'Test4', 'Test5']

createTemplate()
createHTML(test)