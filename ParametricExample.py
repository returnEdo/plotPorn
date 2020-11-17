#! /usr/bin/env python3

import Plot			# we need this to draw!!!

import math			# need the sin() for the function below

import typing 		# needed only for type annotations...not necessary!!



def sineWithParams(x: float, params: typing.List[float]) -> float:
	''' Sine with parametric amplitude, frequency & phase '''
	
	return params[0] * math.sin(x * params[1] + params[2])



if __name__ == '__main__':
	
	
	''' Create the canvas: '''
	
	plot = Plot.Plot()
	
	''' Decide the initial value of the parameters...this is not so important
	since you can change them afterwards '''
	initialParams = [1, 1, 0]
	
	''' Add the parametric function ...'''
	
	plot.addParametric(sineWithParams, initialParams)
	
	'''...and plot it: '''
	
	plot.plot()
	
	''' To change the parameters use the key w, increase the value of the
		parameter with d and decrease it with a!!! '''
