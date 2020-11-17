#! /usr/bin/env python3

import Matrix2
import Vector2

import Camera

import typing

''' The rendering pipeline is something like:
1) update positions and other stuff
2) update all the vertices of the Object.Object
3) update window dimension
4) compute the screen coordinates
5) render the object	'''


class Object:
	
	def __init__(self, position: Vector2.Vector2 = Vector2.Vector2()):
	
		self.position: Vector2.Vector2 = position											# this is the relative position of the cg
		
		self.color:	  typing.List[float] = [1.0, 1.0, 1.0]									# color of the object
		self.movable: bool = True
		
		self.vertices:			typing.List[Vector2.Vector2] = []
		self.globalVertices: 	typing.List[Vector2.Vector2] = []
		
	
	
	def __str__(self):		return "Object"
	
	
	def render(self, Mcp: Matrix2.Matrix2,								# Camera to pixel matrix
					 Mps: Matrix2.Matrix2,								# Pixel to screen matrix
					 Mcs: Matrix2.Matrix2,								# Camera to screen matrix
					 camPosition: Vector2.Vector2) -> None:
		''' Draws on screen the position of an object
		globalPosition is a list of Vector2 '''
		
		pass
	
	
	def updateVertices(self) -> None:
		''' Update all the vertices of an object. Has to be used prior to
		the computation of the screen coordinates '''
		
		pass
	
