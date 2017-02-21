#!/usr/bin/python

class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    # nepouziva self, no instance as the first parameter
    @staticmethod
    def make_car_sound():
        print 'VRoooom!'


class Vechicle(object)

     def __init__(self, make, model):
         self.make = make
         self.model = model

    @classmethod
    def is_motorcycle(cls):
        return cls.wheels == 2
