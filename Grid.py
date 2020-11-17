#! /usr/bin/env python3

import Vector2
import Matrix2

import Object
import Text
import Camera

import math
import typing

import OpenGL.GL


screenLL: 	Vector2.Vector2 = Vector2.Vector2(-1, -1)
worldA:  	Vector2.Vector2 = Vector2.Vector2(1, 1)

class Grid(Object.Object):
	
	
	GRID_COLOR: typing.List[float] = [.3, .3, .3]
	
	def __init__(self, rho: int = 10):
		
		self.rho = rho
		self.movable = False
		self.verbose = True
		
	def __str__(self) -> str:		return 'Grid'
		
	def render(self, Mcp: Matrix2.Matrix2,			
    				 Mps: Matrix2.Matrix2,			
    				 Mcs: Matrix2.Matrix2,			
    				 camPosition: Vector2.Vector2) -> None:
		''' Renders the grid on screen '''
	
		Mcs_inv = Mcs.inv(diag = True)
	
		worldLL = Mcs.inv(diag = True) * screenLL + camPosition
		screenA = Mcs * worldA
		
		startX = (Mcs * (Vector2.Vector2(math.ceil(worldLL.x), worldLL.y) - camPosition)).x		# metti a posto ghisbiro
		startY = (Mcs * (Vector2.Vector2(worldLL.x, math.ceil(worldLL.y)) - camPosition)).y
		
		xA, yA = screenA.x, screenA.y									# this guys are x and y units in the screen reference

		currentPos: float = startX
		currentRealPos: float = math.ceil(worldLL.x)
		while currentPos <= 1:
			
			if self.verbose:	Text.renderToScreen(currentPos + .01, -.99, f'{currentRealPos}')
			
			
			OpenGL.GL.glBegin(OpenGL.GL.GL_LINES)
			
			OpenGL.GL.glColor3d(self.GRID_COLOR[0], self.GRID_COLOR[1], self.GRID_COLOR[2])
			
			OpenGL.GL.glVertex3d(currentPos, -1, .2)
			OpenGL.GL.glVertex3d(currentPos, 1, .2)
			
			OpenGL.GL.glEnd()
			
			currentPos += xA
			currentRealPos += 1
		
		currentPos = startY
		currentRealPos: float = math.ceil(worldLL.y)
		while currentPos <= 1:
			
			if self.verbose:	Text.renderToScreen(-.99, currentPos + .01, f'{currentRealPos}')
			
			OpenGL.GL.glBegin(OpenGL.GL.GL_LINES)
			
			OpenGL.GL.glColor3d(self.GRID_COLOR[0], self.GRID_COLOR[1], self.GRID_COLOR[2])
			
			OpenGL.GL.glVertex3d(-1, currentPos, .2)
			OpenGL.GL.glVertex3d(1, currentPos, .2)
			
			OpenGL.GL.glEnd()
			
			currentPos += yA
			currentRealPos += 1
		
