class Number():
	def __init__(self):
		self.num = 0
	def increase(self):
		self.num += 1
	def decrease(self):
		self.num -= 1

class NewNumber(Number):
	number_new = 11 # public variable
	_new = 12 # can be accessed by different classes
	__new = 11 # can be only accessed within NewNumber class
	def __init__(self):
		super().__init__()
	def sho_val(self):
		print("Value: "+ str(self.num))


if __name__ == "__main__":
	num = NewNumber()

	num.increase()
	num.increase()
	num.decrease()
	num.sho_val()