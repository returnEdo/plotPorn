#! /usr/bin/env python3

import Object
import Text
import Vector2
import Matrix2
import OpenGL.GL
import OpenGL.GLUT

RT = Vector2.Vector2(1, 1)
LT = Vector2.Vector2(-1, 1)
RL = Vector2.Vector2(1, -1)


		
		
	
class Axis(Object.Object):
	
	
	COLOR_AXIS = [.6, .6, .6]
	
	
	def __init__(self):
		
		
		super().__init__()
		
		self.movable = False
		self.verbose = True
	
	
	def render(self, Mcp: Matrix2.Matrix2,								# Camera to pixel matrix
					 Mps: Matrix2.Matrix2,								# Pixel to screen matrix
					 Mcs: Matrix2.Matrix2,								# Camera to screen matrix
					 camPosition: Vector2.Vector2) -> None:
		''' Draws on screen the position of an object
		globalPosition is a list of Vector2 '''
		
		test = self.Test(Mcs, camPosition)
		
		if test[0] != 'failed':														# we can draw the y-axis

			if self.verbose:	Text.renderToScreen(test[0] + .01, .9, 'Y')
			
			OpenGL.GL.glBegin(OpenGL.GL.GL_LINES)

			OpenGL.GL.glColor3d(self.COLOR_AXIS[0], self.COLOR_AXIS[1], self.COLOR_AXIS[2])
			
			OpenGL.GL.glVertex3d(test[0], -1, .1)
			OpenGL.GL.glVertex3d(test[0], 1, .1)
			
			OpenGL.GL.glEnd()
			
		if test[1] != 'failed':														# we can draw the x-axis

			if self.verbose:	Text.renderToScreen(.9, test[1] + .01, 'X')
			
			OpenGL.GL.glBegin(OpenGL.GL.GL_LINES)
			
			OpenGL.GL.glColor3d(self.COLOR_AXIS[0], self.COLOR_AXIS[1], self.COLOR_AXIS[2])
			
			OpenGL.GL.glVertex3d(-1, test[1], .1)
			OpenGL.GL.glVertex3d(1, test[1], .1)
			
			OpenGL.GL.glEnd()
	
	
	def Test(self, Mcs: Matrix2.Matrix2, camPosition: Vector2.Vector2) -> Vector2.Vector2:
		''' Check which axis and where it has to be drawn '''
		
		Mcs_inv = Mcs.inv(diag = True)
		
		worldRT = Mcs_inv * RT + camPosition
		worldLT = Mcs_inv * LT + camPosition
		worldRL = Mcs_inv * RL + camPosition
		
		screenO = -1 * Mcs * camPosition
		
		res = []
		
		if worldRT.x * worldLT.x < 0:		res.append(screenO.x)
		
		else:								res.append('failed')
		
		if worldRT.y * worldRL.y < 0:		res.append(screenO.y)
		
		else:								res.append('failed')
		
		return res
