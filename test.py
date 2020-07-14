print("hello world")
name = "syed"
print("how are you {}".format(name))


def myfunc(name):
  print("Hello {}, how are you?".format(name))
  
myfunc("syed")

class Myclass:
  def __init__(self,name,age):
    self.name = name
    self.age = age
    
  def display(self):
    print("Hi {}, and your age is {}".format(self.name,self.age))
    
    
emp1 = Myclass("syed",35)

print(emp1.display())
