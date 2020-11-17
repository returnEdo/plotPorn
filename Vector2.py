#! /usr/bin/env python3

from __future__ import annotations
import Matrix2
import typing



class Vector2:
	
	def __init__(self, x: float = 0, y: float = 0):
		
		self.x = x
		self.y = y
		
	def __add__(self, other: Vector2) -> Vector2:
		
		return Vector2(self.x + other.x, self.y + other.y)
		
		
	def __sub__(self, other: Vector2) -> Vector2:
		
		return Vector2(self.x - other.x, self.y - other.y)
		
		
	def __mul__(self, other):
		''' Scalar product and product by a constant'''
		
		if type(other) == Vector2:
		
			return self.x * other.x + self.y * other.y
		
		elif type(other) == Matrix2.Matrix2:
			
			xx = self.x * other.a + self.y * other.c
			yy = self.x * other.b + self.y * other.d
			
			return Vector2(xx, yy)
		
		else:
			try:					return Vector2(self.x * other, self.y * other)
	
			except TypeError:
				
				return None
	
	
	def __rmul__(self, other):
		
		if type(other) != Vector2 and type(other) != Matrix2.Matrix2:
			
			return Vector2(self.x * other, self.y * other)

	
	def __or__(self, other: Vector2) -> Matrix2.Matrix2:
		''' Outer product '''
		
		mat = [[self.x ** 2, self.x * self.y],
			   [self.y * self.x, self.y ** 2]]
		
		return Matrix2.Matrix2(mat)
		
	
	def __list__(self) -> typing.List[float]:
		
		return [self.x, self.y]
		
		
	
	def norm2(self) -> float:
		''' Square norm '''
		
		return self.x ** 2 + self.y ** 2
	
	
	def __str__(self):
		
		return " ({0}, {1}) ".format(self.x, self.y)
	
	
	def copy(self) -> Vector2:
		''' Returns a copy of the current vector '''
		
		return Vector2(self.x, self.y)


