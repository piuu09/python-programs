from abc import ABC,abstractmethod
from A import A
class B(A):
    pass
    def show(self):
        print(" hi im show from B")


obj=B()
obj.xyz() 
obj.show()       