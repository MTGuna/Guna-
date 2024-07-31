import time
print("time tuple")
localtime=time.localtime(time.time())
print("Local time:",localtime)
localtime=time.asctime(time.localtime(time.time()))
print("Formatted time:",localtime)
