# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-08-25 12:33:01
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-08-25 17:35:33

from stepper import Stepper

def main():
	leftMotor = stepper([17, 18, 27, 22])
	leftMotor.step(2, 'Left')
	leftMotor.cleanGPIO()

if __name__ == '__main__':
	main()