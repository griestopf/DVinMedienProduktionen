# a = 3
# if a == 1:
#      print('eins')
# elif a == 2:
#      print('zwei')
# else:
#      print('viele')
# 
# 
# alter = 17
# status = "erwachsen" if alter >= 18 else "minderjährig"
# 
# a = 0
# while a < 10:
# 	print(a)
# 	a = a+1

class Person:
	def __init__(self, name, alter):
		self.Name = name
		self.Alter = alter
	def StellDichVor(self):
		print("Ich bin " + self.Name + " und bin " + str(self.Alter) + " Jahre alt.")

p = Person("Horst", 42)
p.Hubraum = 1990
p.StellDichVor()
