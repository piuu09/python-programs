from abc import ABC,abstractmethod
class A(ABC):


    def xyz(self):
     print(" hello xyz")


    @abstractmethod
    def show(self):
        print(" hi show")    


