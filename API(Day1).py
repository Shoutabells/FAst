def decorater(func):
    def wrapper():
        print("This  is before")
        func()
        print("after func  ")
    return wrapper

@decorater
def say_hello():
    print("Is the func working")

say_hello()        
