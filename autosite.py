from core.core import House, Person, Singleton
from core.aspect import Authenticate, OpenDoor, CloseDoor, logging
import copy

auth = Authenticate().wrap
opendoor = OpenDoor().wrap
closedoor = CloseDoor().wrap

class AutoSite(House, metaclass=Singleton):
	"""AutoSite Product"""
	def __init__(self, weed, to_work, name, open_door, manager, residents):
		super(AutoSite, self).__init__(name, open_door, manager, residents)
		self.__weed = weed
		self.__to_work = to_work

	def weed(self):
		self.__weed = True

	def to_work(self):
		self.__to_work = True

joao = Person("João", 21, "Male")
maria = Person("Maria", 19, "Female")
seu_antonio = Person("Seu Antonio", 40, "Male")

interior = AutoSite(
				weed=False,
				to_work = False,
				name = "Interior",
				open_door=False,
				manager=joao,
				residents=[maria, seu_antonio]
				)


@auth
@closedoor
def weed(participante, house):
	if participante.age() > 35:
		logging.debug("Not old enough to weed")
		house.weed()
	else:
		logging.debug("Weeding")

@auth
@closedoor
def work(participante, house):
	if participante.age() > 35:
		logging.debug("Not old enough to weed")
		house.to_work()
	else:
		logging.debug("Weeding")

weed(seu_antonio, interior)