#Template for creating html pages

import os, webbrowser

#create folder for html pages if it doesn't exist
def createFolder():
    if os.path.exists('.\\htmlPages') == False:
        os.makedirs('.\\htmlPages')

#create html file for an array of data
def createHTML(row):
        # for i in row:
            file = open('.\\htmlPages' + '\\' + row[0] + '.html', 'w')
            data = """<html>
            <head></head>
            <body>
                <h1 ALIGN=CENTER>""" + row[0] + """</h1>
                <h2 ALIGN=CENTER>""" + "DOB: " + row[1] + """</h2>
                <p ALIGN=CENTER>""" + "Role: " + row[2] + """</p>
                <p ALIGN=CENTER>""" + "Favorite food: " + row[3] + """</p>
                <p ALIGN=CENTER>""" + "Favorite Sport: " + row[4] + """</p>
                <p ALIGN=CENTER>""" + "Favorite cars: " + row[5] + """</p>
                <p ALIGN=CENTER>""" + "Phone: " + row[6] + """</p>
            </body>
            
            </html>"""

            file.write(data)
            file.close()
            path = '.\\htmlPages' + '\\' + row[0] + '.html'
            webbrowser.open_new_tab(path)


#test = [['Rick Dymond', '11/10/99', 'Test1', 'Test2', 'Test3', 'Test4', 'Test5'], ['Rick Dymond', '11/10/99', 'Test1', 'Test2', 'Test3', 'Test4', 'Test5'], ['Rick Dymond', '11/10/99', 'Test1', 'Test2', 'Test3', 'Test4', 'Test5']]

# createFolder()
#createHTML(test)