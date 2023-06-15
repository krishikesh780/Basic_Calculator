import control_statement
import function_concept
import class_concept
import inheritance_concept
import method_overriding_concept
import exceptional_handeling

#Topic-1: Conrol Statement:
print("Topic-1: Conrol Statetment:")
check=control_statement.greatestNo(110,210,310)
print("greatestNo among 110,210 and 310 is:",check)
print("Input Number:  11 is : ",control_statement.even_odd(11))
print("input year 2021 is: ",control_statement.leap_year(2021))


#Topic-2 Function and Calling function
print("\nTopic-2: Function and Calling function:")
add=function_concept.add(10,20)
print("Addition of 10, 20:",add)
print("Subtraction of 10, 20:",function_concept.sub(10,20))
print("Multiplication of 10, 20:",function_concept.mul(10,20))
print("Division of 10, 20:",function_concept.div(10,20))
print("Succesfullly running function concept")


#Topic-3: Class, object and method
e=class_concept.myClass(10,20)
print("\nTopic-3: Class, object and Method Concept:")
print("Constructor method Addition of 10, 20 is :", e.add())
print("Constructor method Addition of 10, 20 is :", e.mult())
print("Succesfullly running class, object and method concept")


#Topic-4: Inheritance Concept
multi_level=inheritance_concept.multi_level3()
print("\nTopic-4: Inheritance Concept:")
print("Calling Method1:",multi_level.method1())
print("Calling Method2", multi_level.method2())
print("Calling Method3", multi_level.method3())
print("Succesfullly running Inheritance concept")

#Topic-5: method overriding concept 
obj1=method_overriding_concept.overriding_concept2()
print("\nTopic-5: method overriding concept :")
# line 2 and 5 method name same
print(obj1.method1()) #by default local method
print("Succesfullly running method overriding concept")


#Topic-6: exceptional_handeling Concept
excp=exceptional_handeling.exceptional(10,2)
print("\nTopic-6: Exceptional_handeling Concept :")
print("Succesfully running exception handling concept: Info:",excp)


