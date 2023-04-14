# Decorator
def decorator(to_be_decorated):

    def decorate():
        print('Extract code before the function being decorated')
        to_be_decorated()
        print('Extract code after the function being decorated')
    
    return decorate;


@decorator
def to_be_decorated():
    print("Function to be decorated")

to_be_decorated()