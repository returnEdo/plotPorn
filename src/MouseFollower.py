#! /usr/bin/env python3

import Vector2
import Matrix2

import Text

import Object
import OpenGL.GL



class Mouse(Object.Object):
	
	
	def __init__(self, verbose: bool = True):
		
		super().__init__()
		
		self.verbose = verbose
		self.movable = False
		
		self.string: str = ''
		self.screenPosition = self.position.copy()
		
	
	def render(self, Mcp: Matrix2.Matrix2,					
					 Mps: Matrix2.Matrix2,									
					 Mcs: Matrix2.Matrix2,								
					 camPosition: Vector2.Vector2) -> None:
						 
		OpenGL.GL.glBegin(OpenGL.GL.GL_POINTS)
		OpenGL.GL.glColor3d(.6, .3, .0)
		OpenGL.GL.glVertex3d(self.screenPosition.x, self.screenPosition.y, -.01)
		OpenGL.GL.glEnd()
		
		Text.renderToScreen(self.screenPosition.x + .05, self.screenPosition.y + .05, self.string)
		
		OpenGL.GL.glBegin(OpenGL.GL.GL_LINES)
		
		OpenGL.GL.glColor3d(.2, .2, .2)
		
		OpenGL.GL.glVertex3d(self.screenPosition.x, 1, .2)
		OpenGL.GL.glVertex3d(self.screenPosition.x, -1, .2)
		
		OpenGL.GL.glVertex3d(1, self.screenPosition.y, .2)
		OpenGL.GL.glVertex3d(-1, self.screenPosition.y, .2)
		
		OpenGL.GL.glEnd()
		
		
		
		
	
	def __str__(self) -> str:		return 'Mouse'
