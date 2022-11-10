# Central Legitimization Agency Code
import random
import time


class CLA:
    def __init__(self, name):
        self.name = name

    def generate_validation_num(self):
        random.seed(time.time())
        validID = random.randint(0, 10000000000000)
        return validID














