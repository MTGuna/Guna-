import time
t=time.time()
print("seconds:",t)
print("local time:",time.localtime())
print("asctime:",time.asctime(time.localtime(time.time())))
print("ctime:",time.ctime())
print("mktime:",time.mktime(time.localtime()))
print("timeclock:",time.perf_counter())
