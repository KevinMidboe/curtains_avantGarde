from time import sleep
import RPi.GPIO as gpio

class Stepper:
	# Initiate stepper
	# Pins = [pin1, pin2, pin3, pin4]
	def __init__(self, pins):
		self.pins = pins
		self.pin1 = self.pins[0]
		self.pin2 = self.pins[1]
		self.pin3 = self.pins[2]
		self.pin4 = self.pins[3]

		gpio.setmode(gpio.BCM)

		for pin in self.pins:
			gpio.setup(pin, gpio.OUT)
			gpio.output(pin, False)

	# Clears the GPIO settings
	def cleanGPIO(self):
		gpio.cleanup()

	def step(self, rotations, dir, speed=1, forever=False):
		StepSequence = range(0, 8)
		StepSequence[0] = [GpioPins[0]]
		StepSequence[1] = [GpioPins[0], GpioPins[1]]
		StepSequence[2] = [GpioPins[1]]
		StepSequence[3] = [GpioPins[1], GpioPins[2]]
		StepSequence[4] = [GpioPins[2]]
		StepSequence[5] = [GpioPins[2], GpioPins[3]]
		StepSequence[6] = [GpioPins[3]]
		StepSequence[7] = [GpioPins[3], GpioPins[0]]
		
		for pin in self.pins:
			gpio.output(pin, True)

		turnLeft = True
		if (dir == 'right'):
			turnLeft = False
		elif (dir != 'left'):
			raise ValueError('STEPPER ERROR: no direction supplied')
			return False

		steps = rotations * 500
		waitTime = 0.000001/speed

		while steps > 0:
			for pinList in stepSequence: 
				for pin in self.pins:
					if pin in pinList: 
						GPIO.output(pin, True)
					else:
						GPIO.output(pin, False)
				sleep(waitTime)

			steps -=1


if __name__ == '__main__':
	pins = [17, 18, 27, 22]
	stepper = new Stepper(pins)
	stepper.step(2, 'left')