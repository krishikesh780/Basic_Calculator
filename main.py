import function_concept
import class_concept
import inheritance_concept

# Calling function
function_concept.add()
function_concept.sub()
function_concept.mul()
function_concept.div()

print("Succesfullly running function concept")
# create object of class and calling the function
e=class_concept.myClass(10,20)
e.add()
e.mult()
print("Succesfullly running class concept")

# creating object of class (inheritance) and calling fun
multi_level=inheritance_concept.multi_level3()
multi_level.method1()
multi_level.method2()
multi_level.method3()
print("Succesfullly running Inheritance concept")
