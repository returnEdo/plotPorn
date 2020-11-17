#! /usr/bin/env python3

import Plot								# we need this to draw somenthing!!

from FunctionObj import linspace		# I use it to create the X list below


if __name__ == '__main__':
	
	''' Let's define 2 lists ... x: '''
	
	X = linspace(-4, 4, 20)
	
	''' ... and Y: '''
	
	Y = [-.2 * x ** 3 + 2 * x for x in X]
	
	''' Create the plot: '''

	plot = Plot.Plot()
	
	''' add the scatter '''
	
	plot.addScatter(X, Y)				# set connect = False if you don't want to connect the points
	
	''' and ... enjoy your scatter plot!! '''
	
	plot.plot()
	
