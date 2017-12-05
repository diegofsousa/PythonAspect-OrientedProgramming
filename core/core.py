# Core of a software product line. Theme: Residential automation.

class Singleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class House(object):
	"""
	In this class the assignments related to the environments are inserted.
	The design pattern strategy is used.
	"""
	def __init__(self, name, open_door, manager, residents):
		self.__name = name
		self.__open_door = open_door
		self.__manager = manager
		self.__residents = residents

	def __repr__(self):
		return "<house: {}, open_door: {}, manager: {}>".format(
								self.__name, self.__open_door, self.__manager)

	def manager(self):
		return self.__manager

	def open_door(self):
		self.__open_door = True

	def close_door(self):
		self.__open_door = False

	def door(self):
		return self.__open_door

	def residents(self):
		return self.__residents

class Person(object):
	"""
	In this class are entered the assignments relative to users. The design
	pattern strategy is used.
	"""
	def __init__(self, name, age, gender):
		self.__name = name
		self.__age = age
		self.__gender = gender

	def __repr__(self):
		return "<name: {}, age: {}, gender: {}>".format(
								self.__name, self.__age, self.__gender)

	def age(self):
		return self.__age



# diego = Person("Diego", 21, "Male")
# fernando = Person("Fernando", 19, "Male")

# ap201 = House("AP 201", False, diego, [fernando])

# print(ap201)
