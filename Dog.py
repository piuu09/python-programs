from Animal import Animal
class Dog(Animal):
    
    
    def __init__(self):
        print("child constructor")


    def __init__(self,name,weight,colour):
        self.colour=colour
        super().__init__(name,weight)   

    def abc(self):
        print(" i am from child class")


    def dog_details(self):
        super().greet()
        print(f"{self.name}\n{self.colour}")


obj=Dog("lab","7kg","black")        
print(obj.type)
print(obj.name)
print(obj.weight)
obj.xyz()
obj.abc()
obj.dog_details()    

