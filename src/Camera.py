#! /usr/bin/env python3

import Vector2
import OpenGL.GLUT


class Camera:
	
	def __init__(self, position: Vector2.Vector2 = Vector2.Vector2(.0, .0),
					   deltaX: float = 10):
		
		self.position = position										# in world coordinates
		self.deltaX = deltaX											# width of the camera
		self.deltaY = deltaX											# height of the camera
		
	
		
	def updateZoom(self, dx):
		''' Similar to update position '''
		
		self.width = OpenGL.GLUT.glutGet(OpenGL.GLUT.GLUT_WINDOW_WIDTH)
		self.height = OpenGL.GLUT.glutGet(OpenGL.GLUT.GLUT_WINDOW_HEIGHT)		
		
		if self.deltaX + dx > 0:
			self.deltaX += dx
			self.deltaY = self.height / self.width * self.deltaX
