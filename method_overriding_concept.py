class overriding_concept1():
  def method1(self): 
    return ("Partent Method: Method1 calling from overriding_concept1")
    
# single inheritance method overring concept

class overriding_concept2(overriding_concept1):
  def method1(self):
    print(super().method1())
    return ("By default: method2  calling from overriding_concept2")
