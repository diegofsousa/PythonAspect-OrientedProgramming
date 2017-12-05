from core.core import House, Person, Singleton
from core.aspect import Authenticate, OpenDoor, CloseDoor, logging

auth = Authenticate().wrap
opendoor = OpenDoor().wrap
closedoor = CloseDoor().wrap

class AutoHome(House, metaclass=Singleton):
	"""AutoHome Product"""
	def __init__(self, garage, tv, name, open_door, manager, residents):
		super(AutoHome, self).__init__(name, open_door, manager, residents)
		self.__garage = garage
		self.__tv = tv

	def save_car(self):
		self.__garage = True

	def watch_tv(self):
		self.__tv = True

diego = Person("Diego", 21, "Male")
fernando = Person("Fernando", 19, "Male")

casa = AutoHome(
				garage=False,
				tv = False,
				name = "Casa",
				open_door=False,
				manager=diego,
				residents=[fernando]
				)
@auth
@opendoor
def save_car(participante, house):
	logging.debug("Saving Car")
	house.save_car()

@auth
def watch_tv(participante, house):
	logging.debug("Watching tv")
	house.watch_tv()

@auth
def watch_tv(participante, house):
	logging.debug("Watching tv")
	house.watch_tv()

@auth
@closedoor
def take_care_of_the_garden(participante, house):
	logging.debug("Taking care of the garden")
	house.watch_tv()


save_car(diego, casa)
watch_tv(fernando, casa)
take_care_of_the_garden(fernando, casa)

#ap201 = House("AP 201", False, diego, [fernando])