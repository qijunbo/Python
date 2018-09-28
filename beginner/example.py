import os,time,datetime
file_date = os.path.getatime("c:\Eclipse4.5.0.rar")
print file_date
print type(file_date)
timeStruct = time.localtime(file_date)
t = datetime.datetime.now()
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)
print 
print otherStyleTime
df = datetime.datetime.fromtimestamp(time.mktime(timeStruct)) - t
print "=================days to today " + str(df)

print type(timeStruct)
print type( datetime.datetime.fromtimestamp(time.mktime(timeStruct)))
print "------------------"
print type(datetime.datetime.now().time())
print timeStruct
print "----------------"
print datetime.datetime.now().time()

print (t-datetime.datetime(1970,1,1)).total_seconds()
print t-datetime.datetime(1970,1,1)
 
t = datetime.datetime(2011, 10, 21, 0, 0)
print time.mktime(t.timetuple())

print '-----------'
print type(df)
print  datetime.timedelta(seconds=666)

print type( datetime.timedelta(seconds=666))

 
 

datetime1=datetime.datetime.strptime(otherStyleTime, "%Y-%m-%d %H:%M:%S")

