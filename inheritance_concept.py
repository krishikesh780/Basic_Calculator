'''
1. Single inheritance: A->B(A)
2. Multi level: A->B(A) and C(A)
3. heirarchy: A->B(A) & C(A)
4. multiple: A,B=> C(A,B)
'''
class multi_level1():
  a,b=100,200
  def method1(self):
    print(self.a+self.b)
class multi_level2(multi_level1):
  c,d=100,200
  def method2(self):
    print(self.c-self.d)
class multi_level3(multi_level2):
  x,y=100,200
  def method3(self):
    print(self.x*self.y)
