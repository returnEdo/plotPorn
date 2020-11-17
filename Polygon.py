#! /usr/bin/env python3

import Vector2
import Matrix2

import Object

import OpenGL.GL

import typing
import math


def computeVertices(nSides: int, radius: float = 2) -> typing.List[Vector2.Vector2]:
	
	assert nSides != 0
	
	step: float = math.pi * 2 / nSides
	
	lst = []
	
	for i in range(nSides):
		
		lst.append(Vector2.Vector2(radius * math.cos(-step / 2 + step * i),
								   radius * math.sin(-step / 2 + step * i)))
	
	return lst



class Polygon(Object.Object):
	''' Parent class for polygons objects '''
	
	POL_COLOR = [.6, .6, .6]
	
	
	def __init__(self, position: Vector2.Vector2 = Vector2.Vector2(), nSides: int = 3, radius: float = 2):
		
		self.nSides = nSides 											# number of sides of the polygon
		
		super().__init__(position)
		
		self.copyMe = computeVertices(self.nSides, radius)
		
		self.vertices: 			typing.List[Vector2.Vector2] = self.copyMe.copy()
		self.globalVertices: 	typing.List[Vector2.Vector2] = self.copyMe.copy()
	
	
	def updateVertices(self) -> None:
		''' Updates all the verices after a translation (world frame) '''
		
		em = []
		
		for Vertex in self.copyMe:
			
			em.append(self.position + Vertex)							# traslation
			
		self.vertices = em.copy()
			
		
		
	def render(self, Mcp: Matrix2.Matrix2,								# Camera to pixel matrix
					 Mps: Matrix2.Matrix2,								# Pixel to screen matrix
					 Mcs: Matrix2.Matrix2,								# Camera to screen matrix
					 camPosition: Vector2.Vector2) -> None:
		''' Draws on screen the position of an object
		globalPosition is a list of Vector2 '''
		
		self.updateVertices()
		self.getGlobal(Mcs, camPosition)
		
		OpenGL.GL.glBegin(OpenGL.GL.GL_LINE_LOOP)
		OpenGL.GL.glColor3d(self.POL_COLOR[0], self.POL_COLOR[1], self.POL_COLOR[2])
		
		for Vertex in self.globalVertices:			OpenGL.GL.glVertex3d(Vertex.x, Vertex.y, .0)
		
		OpenGL.GL.glEnd()
		
		
	def getGlobal(self, Mcs: Matrix2.Matrix2, camPosition: Vector2.Vector2) -> None:
		
		self.globalVertices = []
		
		for  Vertex in self.vertices:
			
			self.globalVertices.append(Mcs * ( Vertex - camPosition ))
		


class Square(Polygon):
	
	def __init__(self, position: Vector2.Vector2 = Vector2.Vector2()):
		
		
		super().__init__(position, 4)
		
		self.POL_COLOR = [1, .63, .004]
	
	
	def __str__(self):		return 'Square'


class Circle(Polygon):
	
	def __init__(self, position: Vector2.Vector2 = Vector2.Vector2(), radius: float = 2):
		
		
		super().__init__(position, 50, radius)

		self.POL_COLOR = [.27, .93, .84]

	
	def __str__(self):		return 'Circle'
	

		
		
		
		
		
