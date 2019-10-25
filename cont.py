
class Person:
    key=123
    

    def __init__(self,k):
        
          
       if Person.key==k:
              print("constructor accessed")
              self.name="Akshay"
       else:
           print("can't access the constructor")
                

    def printH(self):        
        print("Welcome")
        print(self.name)
        

abc=Person(12)
abc.printH()
    


