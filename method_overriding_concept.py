class overriding_concept1():
  def method1(self): 
    print("method1 from overriding_concept1")
    
# single inheritance method overring concept

class overriding_concept2(overriding_concept1):
  def method1(self):
    print("method2 from overriding_concept2")
    super().method1()