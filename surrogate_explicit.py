import numpy as np
import csdl


class Atm(csdl.Model):
    def initialize(self):
        self.parameters.declare('alt')
    def define(self):
        alt = self.parameters['alt']

        altitude = self.create_input('altitude', val=alt)

        # custom operation insertion
        p, d = csdl.custom(altitude, op=AtmExplicit())

        self.register_output('pressure', p)
        self.register_output('density', d)


class AtmExplicit(csdl.CustomExplicitOperation):
    def initialize(self):
        pass
    def define(self):

        # input: altitude
        self.add_input('altitude', shape=(1,))

        # output: pressure and density
        self.add_output('pressure', shape=(1,))
        self.add_output('density', shape=(1,))