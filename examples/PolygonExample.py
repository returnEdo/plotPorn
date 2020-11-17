#! /usr/bin/env python3
''' Show the basic usage of the polygon classes '''

import Plot			# we need this to draw somenthing!!
import Polygon				# to create the polygon
import Vector2				# to place the polygons!


if __name__ == '__main__':
	
	''' We start by creating the polygons '''
	square = Polygon.Square(Vector2.Vector2(2, 2))
	circle = Polygon.Circle(Vector2.Vector2(0, -2))
	heptagon = Polygon.Polygon(Vector2.Vector2(-2, 2), 7)
	
	''' We then create our canvas '''
	canvas = Plot.Plot()
	
	''' We add the object to the canvas '''
	canvas.addObject(square)
	canvas.addObject(circle)
	canvas.addObject(heptagon)
	
	''' Enjoy math!! '''
	canvas.plot()
