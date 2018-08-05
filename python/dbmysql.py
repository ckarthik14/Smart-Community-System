import urllib.request
from urllib.parse import urlencode
from datetime import datetime
import MySQLdb
import ast
from time import sleep

db = MySQLdb.connect("localhost","root","1","scs")
pi = 0
po = 0

try:
    cursor = db.cursor()

    device = "[DEVICE_NAME]@[USERNAME].[USERNAME]"
    apikey = "[CARRIOTS_APIKEY]"
    params = urlencode({'max' : 1, 'sort': 'at','order':-1})
    url = 'https://api.carriots.com/devices/{device}/streams/'.format(device=device)
    url = url+'?'+params
    headers = {
        'Carriots.apiKey': apikey,
        'Accept-Type': 'application/json'
    }
    req = urllib.request.Request(url, headers=headers)

    while True:
        sleep(5)
        response = urllib.request.urlopen(req)
        
        information = response.read().decode('utf-8')
        
        data = ast.literal_eval(information)

        if (data["total_documents"] != 0):
            result = data['result']
            data = result[0]
            data = data['data']

            people_in = data['entered']
            time_of_entry = data['time_of_entry']
            people_out = data['exited']
            time_of_exit = data['time_of_exit']
            count = data['count']

            stmt = "insert into people_data (people_entered, time_of_entry, \
                    people_exited, time_of_exit, no_of_people, distance) values \
                    (\'%d\',\'%s\',\'%d\',\'%s\',\'%d\')" \
                    % (people_in, time_of_entry, people_out, time_of_exit, \
                       count)

            max_no = "select MAX(no) as max from people_data"
            cursor.execute(max_no)
            res = cursor.fetchone()
            last_row = res[0]
            print (last_row)
            
            if last_row != None:
                record = "select * from people_data where no = %d" % (last_row)
                cursor.execute(record)
                results = cursor.fetchone()
                print (results)
                pi = results[1]
                po = results[3]

            if (pi != people_in or po != people_out):  
                cursor.execute(stmt)
        
            print (data, last_row, pi, po)
    
except Exception as e:
    print (e)
    db.rollback()

db.close()
