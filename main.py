import function_concept
import class_concept
import inheritance_concept
import method_overriding_concept
import exceptional_handeling
# Calling function
function_concept.add()
function_concept.sub()
function_concept.mul()
function_concept.div()
print("Succesfullly running function concept")

# create object of class and calling the method
e=class_concept.myClass(10,20)
e.add()
e.mult()
print("Succesfullly running class concept")

# creating object of class (inheritance) and calling method
multi_level=inheritance_concept.multi_level3()
multi_level.method1()
multi_level.method2()
multi_level.method3()
print("Succesfullly running Inheritance concept")

# method overriding concept 
obj1=method_overriding_concept.overriding_concept2()
# line 2 and 5 method name same
obj1.method1() #by default local method
print("Succesfullly running method overriding concept")

# exceptional_handeling concept
excp=exceptional_handeling.exceptional(10,2)
print("Succesfully running exception handling concept: Info:",excp)