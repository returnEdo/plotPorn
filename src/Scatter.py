
#! /usr/bin/env python3

from __future__ import annotations
import Object
import typing
import Vector2
import OpenGL.GL
import OpenGL.GLUT
import math
	
	
def createArray(x: typing.List[float], y: typing.List[float]) -> typing.List[Vector2.Vector2]:
	
	return [Vector2.Vector2(xx, yy) for xx, yy in zip(x, y)]



def sigmoid(y: float, minY: float, maxY: float) -> float:
	
	t = (y - minY) / (maxY - minY)
	
	return -2 * t ** 2 * ( t - 1.5)
	


class Scatter(Object.Object):
	''' Function object. You simply pass a function and an interval to it '''
	
	
	POINT_SIZE: float = 8.0
	CONNECT: bool = True
	CONNECT_COLOR: typing.List[float] = [.4, .4, .4]
	COLOR_MAP: str = 'colorful'										# other option is 'grey_scale'
	
	def __init__(self, x: typing.List[float], y: typing.List[float]):
		
		super().__init__() 
		
		assert len(x) == len(y)
		
		self.x, self.y = x, y
			
		self.maxX, self.minX = max(x), min(x)
		self.maxY, self.minY = max(y), min(y)
		self.n = len(x)
		
		self.connect = True
		self.movable = False
			
		
	
	def render(self, Mcp: Matrix2.Matrix2,		
	                 Mps: Matrix2.Matrix2,		
	                 Mcs: Matrix2.Matrix2,		
	                 camPosition: Vector2.Vector2) -> None:
		
		# Compute the vertices
		screenVertices = self.drawTest(Mcs, camPosition)
		
		if screenVertices == 'failed':
			
			return
		
		# Displays the points with a colormap
		OpenGL.GL.glPointSize(self.POINT_SIZE)
		OpenGL.GL.glBegin(OpenGL.GL.GL_POINTS)

		for yy, Vertex in zip(self.y, screenVertices):
			
			sig = sigmoid(yy, self.minY, self.maxY)

			if self.COLOR_MAP == 'colorful':		OpenGL.GL.glColor3d(sig, 1 - sig, .0)
			
			elif self.COLOR_MAP == 'grey_scale':	OpenGL.GL.glColor3d(sig, sig, sig)

			OpenGL.GL.glVertex3d(Vertex.x, Vertex.y, -.01)
		
		OpenGL.GL.glEnd()
		
		
		# Display the connections if required
		if self.connect:
			
			OpenGL.GL.glBegin(OpenGL.GL.GL_LINE_STRIP)
			
			OpenGL.GL.glColor3d(self.CONNECT_COLOR[0], self.CONNECT_COLOR[1], self.CONNECT_COLOR[2])

			for Vertex in screenVertices:		OpenGL.GL.glVertex3d(Vertex.x, Vertex.y, -.01)
			
			OpenGL.GL.glEnd()
					
		
		
	def toScreen(self, X: typing.List[float], 
				 	   F: typing.List[float], 
					   Mcs: Matrix2.Matrix2, 
					   camPosition: Vector2.Vector2) -> typing.List[Vector2.Vector2]:
		''' Converts to screen coordinates some stuff'''
		
		screenVertices = []
		
		for x, f in zip(X, F):
			
			screenVertices.append(Mcs * (Vector2.Vector2(x, f) - camPosition))
			
		return screenVertices
		


	
	def drawTest(self, Mcs: Matrix2.Matrix2,
					  camPosition: Vector2.Vector2) -> typing.List[Vector2.Vector2]:
		''' Computes the corner of the window in the world coordinates '''
					  
		worldTR = Mcs.inv(diag = True) * Vector2.Vector2(1, 1) + camPosition
		worldLL = Mcs.inv(diag = True) * Vector2.Vector2(-1, -1) + camPosition
		
		if (self.minX >= worldTR.x or
			self.maxX <= worldLL.x or
			self.minY >= worldTR.y or
			self.maxY <= worldLL.y):
		
			return 'failed'
		
		else:
			
			return self.toScreen(self.x, self.y, Mcs, camPosition)
	
		
	def __str__(self) -> str: 	return 'Scatter'
	
	
	
	
	
