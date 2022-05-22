from datetime import date, datetime, timedelta
from xml.dom.minidom import Element

print("While calling the function pass no of days value in x and y")

#i have creted the code in Pycharm, if you want to execute the code, you have to put test_payload1.xml
#in your current working directory, also output file will be saved there only

def add_data(x,y):
    import xml.etree.ElementTree as ET

    # parsing using the string.
    mytree = ET.parse('test_payload1.xml')

    root = mytree.getroot()

    print(root)

    for depart in root.iter('DEPART'):
        print(depart.text)

    for returnDate in root.iter('RETURN'):
        print(returnDate.text)

    today = date.today()
    #print("Today's date:", today)
    depart_date = today + timedelta(days=x)
    return_date = today + timedelta(days=y)
    #print(depart_date)
    #print(return_date)
    depart = depart_date.strftime("%Y%m%d")
    print("depart", depart)
    return_date_now = return_date.strftime("%Y%m%d")
    print("return_date_now", return_date_now)

    for departDate in root.iter('DEPART'):
        departDate.text = depart
        print("updated depart date",departDate.text)

    for returnDate in root.iter('RETURN'):
        returnDate.text = return_date_now
        print("updated return date",returnDate.text)

    mytree.write('output.xml')

    return x,y


add_data(10,20)

#I have set depart date as X and Return Date as Y,
#X is the first argument and Y is the Second Argument.


