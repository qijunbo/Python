import os,time,datetime
file_date = os.path.getmtime("c:\Eclipse4.5.0.rar")
print file_date

timeStruct = time.localtime(file_date)
createDate = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)
print "File last modified on: " + str( createDate )
t =  datetime.datetime.now()
print "Today is " +  str(t)
df = t - datetime.datetime.fromtimestamp(time.mktime(timeStruct))  
print "Days to today " + str(df)
print  df.days , df.seconds
 
