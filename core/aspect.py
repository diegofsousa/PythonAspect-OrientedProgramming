import logging
from core.core import House, Person

'''
Patterns used:
Strategy,
Singleton,
Façade,
Iterator
'''

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh = logging.FileHandler('log_filename.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

# Pointcut
class Authenticate(object):
	def wrap(self, func):
		def wrapper(*args, **kwargs):
			self.before(args[0])
			if args[1].manager() != args[0] and args[0] not in args[1].residents():
				raise ValueError('Participant is not allowed.')
			else:
				func(*args, **kwargs)
				self.current()
			self.after()
		return wrapper

	def before(self, args):
		logging.debug("[{}] - Starting authentication...".format(args))

	def current(self):
		logging.debug("Authentication is happening...")

	def after(self):
		logging.debug("Ending authentication.")

# Pointcut
class OpenDoor(object):
	def wrap(self, func):
		def wrapper(*args, **kwargs):
			self.before()
			func(*args, **kwargs)
			self.after()
		return wrapper

	def before(self):
		logging.debug("Openning door...")

	def after(self):
		logging.debug("Door is open!")

# Pointcut
class CloseDoor(object):
	def wrap(self, func):
		def wrapper(*args, **kwargs):
			self.before()
			func(*args, **kwargs)
			self.after()
		return wrapper

	def before(self):
		logging.debug("Closing door...")

	def after(self):
		logging.debug("Door is close!")


# diego = Person("Diego", 21, "Male")
# fernando = Person("Fernando", 19, "Male")
# leo = Person("Leo", 21, "Male")

# ap201 = House("AP 201", False, diego, [fernando])

# auth = Authenticate().wrap
# opendoor = OpenDoor().wrap

# @auth
# def access_to_home(participant, house):
# 	logging.debug("Acesso Liberado")

# @auth
# @opendoor
# def get_home(participant, house):
# 	logging.debug("Entrando em casa")


# access_to_home(diego, ap201)
# get_home(fernando, ap201)
