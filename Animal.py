class Animal:
    pass
    type="Animaltype"


    # default constructor
    def  __init__(self):
        print("default animal constructor")

    # parametrized constructor
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight

    # methods
    def xyz(self):
        print("hello i am  from parent class")


    def greet(self):
        print("hello is animal !")
