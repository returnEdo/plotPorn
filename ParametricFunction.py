#! /usr/bin/env python3

from __future__ import annotations
import typing

import Object
import Vector2

import OpenGL.GL
import OpenGL.GLUT



def linspace(a: float, b: float, n: int) -> typing.List[float]:
	''' Linearly spaced from a to b '''
	
	step = (b - a) / n
	
	return [step * i + a for i in range(n)]




def computePointsParametric(fun: typing.Callable([float, typing.List[float]], float),
				  leftX: float,
				  rightX: float,
				  params: typing.List[float],
				  n: int):
	''' Evaluates the function '''

	X = linspace(leftX, rightX, n)
	
	return X, [fun(x, params) for x in X]
	
	


class Parametric(Object.Object):
	''' Function object. You simply pass a function and an interval to it '''
	
	FUN_COLOR = [.11, .74, .61]
	TEST_POINTS = 20
	EVAL_POINTS = 120
	
	def __init__(self, fun: typing.Callable([float, typing.List[float]], float),
					   params: typing.List[float]):
		
		super().__init__() 
		
		self.fun = fun
		self.params = params			# value of the parameters
		
		self.n = 1000
	
	
	
	def render(self, Mcp: Matrix2.Matrix2,		
	                 Mps: Matrix2.Matrix2,		
	                 Mcs: Matrix2.Matrix2,		
	                 camPosition: Vector2.Vector2) -> None:
		
		TR, LL = self.corners(Mcs, camPosition)												# find the corners of the cam
		
		_, evalFun = computePointsParametric(self.fun, LL.x, TR.x, self.params, self.TEST_POINTS)
		minX, maxX = min(evalFun), max(evalFun)
		
		if TR.y <= minX or LL.y >= maxX:		return										# this is a test eval to know wehter to plot or not
		
		X, F = computePointsParametric(self.fun, LL.x, TR.x, self.params, self.EVAL_POINTS)
		screenVertices = self.toScreen(X, F, Mcs, camPosition)

		OpenGL.GL.glBegin(OpenGL.GL.GL_LINE_STRIP)
		
		OpenGL.GL.glColor3d(self.FUN_COLOR[0], self.FUN_COLOR[1], self.FUN_COLOR[2])

		for Vertex in screenVertices:		OpenGL.GL.glVertex3d(Vertex.x, Vertex.y, -.01)
		
		OpenGL.GL.glEnd()
			
			
		
		
	
	def corners(self, Mcs: Matrix2.Matrix2,
					  camPosition: Vector2.Vector2) -> typing.List[Vector2.Vector2]:
		''' Computes the corner of the window in the world coordinates '''
					  
		worldTR = Mcs.inv(diag = True) * Vector2.Vector2(1, 1) + camPosition
		worldLL = Mcs.inv(diag = True) * Vector2.Vector2(-1, -1) + camPosition
		
		return worldTR, worldLL
	
	
	def toScreen(self, X: typing.List[float], 
				 	   F: typing.List[float], 
					   Mcs: Matrix2.Matrix2, 
					   camPosition: Vector2.Vector2) -> typing.List[Vector2.Vector2]:
		''' Converts to screen coordinates some stuff'''
		
		screenVertices = []
		
		for x, f in zip(X, F):
			
			screenVertices.append(Mcs * (Vector2.Vector2(x, f) - camPosition))
			
		return screenVertices
	
	
				 
						 
						 
	def __str__(self) -> str: 	return 'Parametric'
	
	
	
	
	

