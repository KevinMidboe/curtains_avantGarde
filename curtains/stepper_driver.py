#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-08-25 16:04:49
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-08-25 17:34:07

from time import sleep
import RPi.GPIO as gpio

class Stepper:
	# Initiate stepper
	# Pins = [pin1, pin2, pin3, pin4]
	def __init__(self, pins):
		self.pins = pins

		gpio.setmode(gpio.BCM)

		for pin in self.pins:
			gpio.setup(pin, gpio.OUT)
			gpio.output(pin, False)

	# Clears the GPIO settings
	def cleanGPIO(self):
		gpio.cleanup()

	def rotate(self, l, n=1):
		return l[n:] + l[:n]

	def togglePin(self, pins):
		for pin in self.pins:
			if pin in pins:
				gpio.output(pin, True)
			else:
				gpio.output(pin, False)

		sleep(0.001)

	def step(self, rotations, dir, speed=1, forever=False):
		for pin in self.pins:
			gpio.output(pin, True)

		turnLeft = True
		if (dir == 'right'):
			turnLeft = False
		elif (dir != 'left'):
			raise ValueError('STEPPER ERROR: no direction supplied')
			return False

		steps = rotations * 500
		pinState = self.pins

		while steps > 0:
			for i in range(2):
				self.togglePin([pinState[0]])
				self.togglePin([pinState[0], pinState[1]])
			
				pinState = self.rotate(pinState)


			steps -=1


if __name__ == '__main__':
	pins = [17, 18, 27, 22]
	stepper = Stepper(pins)
	stepper.step(10, 'left')
	stepper.cleanGPIO()
