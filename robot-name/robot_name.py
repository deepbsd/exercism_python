from string import ascii_uppercase
import random
from datetime import datetime

class Robot(object):
    def __init__(self):
        self.name = self._create_name()

    def _create_name(self):
        random.seed(datetime.now())
        return ''.join(random.choice(ascii_uppercase) for i in range(2))+str(random.randint(100,999))

    def reset(self):
        self.name = self._create_name()
