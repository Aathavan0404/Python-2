x = 200

def greet():

    global x

    x = 100 #Value changed from 200 to 100
    
greet()

print(x)
