#! /usr/bin/env python3

import Plot			# we need this to draw somenthing!!

import math			# need the sin() for the function below


def sinc(x: float) -> float:
	''' Sine cardinal function '''
	
	if x == 0:		return 1
	
	return math.sin(10 * x) / (10 * x)


if __name__ == '__main__':
	
	
	''' Write whaterver function you like, may also be a lambda like: '''
	line = lambda x: 2 * x + 1
	''' ...or the cardinal sine above... '''
	
	''' ...feed it to the plot object '''
	plot = Plot.Plot(sinc)
	
	''' enjoy math !! '''
	plot.plot()
