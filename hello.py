def myfunc(n):
    return lambda a:a*n

myDouble = myfunc(3)
print(myDouble(12))