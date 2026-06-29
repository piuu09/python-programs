from A import A 
class B(A):
    def abc(self):
        print(" from abc B")




    def __init__(self):
        print("from B ") 
        #A.__annotate__(self)  
        super().__init__() 



