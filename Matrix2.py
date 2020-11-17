#! /usr/bin/env python3

from __future__ import annotations
import Vector2


ID = [[1, 0], [0, 1]]



class Matrix2:
	
	def __init__(self, mat: list = ID):
		
		assert (len(mat) == 2 and len(mat[0]) == 2), "\n\tWrong dimensions!"
		
		self.a: float = mat[0][0]
		self.b: float = mat[0][1]
		self.c: float = mat[1][0]
		self.d: float = mat[1][1]
		
	def det(self) -> float:
		''' Determinant '''
		
		return self.a * self.d - self.b * self.c
		
	
	def isSingular(self) -> bool:
		
		return (self.det() == 0.0)
		
	
	def inv(self, diag = False) -> Matrix2:
		''' Returns the inverse '''
		
		if diag:
			
			return Matrix2([[1 / self.a, .0], [.0, 1 / self.d]])
			
			
		n = 1 / self.det()
		
		return Matrix2([[self.d * n, -self.b * n], [-self.c * n, self.a * n]])
		
	
	def __mul__(self, other):
		''' Multiple kinds of multiplication '''
		
		if type(other) == Matrix2:
			
			mat = [[self.a * other.a + self.b * other.c,
						self.a * other.b + self.b * other.d],
						[self.c * other.a + self.d * other.c, 
						self.c * other.b + self.d * other.d]]
			
			return Matrix2(mat)
		
		elif type(other) == Vector2.Vector2:
			
			x = self.a * other.x + self.b * other.y
			y = self.c * other.x + self.d * other.y
			
			return Vector2.Vector2(x, y)
		
		else:
			
			mat = [[self.a * other, self.b * other],
				   [self.c * other, self.d * other]]
				   
			return Matrix2(mat)
	
	
	def __rmul__(self, other):
		
		if type(other) == int or type(other) == float:
			
			
			return  self * other
	
	
		
	def __add__(self, other: Matrix2) -> Matrix2:
		
		mat = [[self.a + other.a, self.b + other.b],
			   [self.c + other.c, self.c + other.c]]
		
		return Matrix2(mat)
		
		
	def __sub__(self, other: Matrix2) -> Matrix2:
		
		mat = [[self.a - other.a, self.b - other.b],
			   [self.c - other.c, self.c - other.c]]
		
		return Matrix2(mat)
	
	
	def __invert__(self) -> Matrix2:
		''' Transposition '''
		
		mat = [[self.a, self.c], [self.b, self.d]]
		
		return Matrix2(mat)
	
	
	def __str__(self) -> str:
		
		return '\t | {0} {1} | \n\t | {2} {3} | '.format(self.a, self.b, self. c, self.d)




def det(Mat: Matrix2) -> float:
	''' Determinant '''
	
	return Mat.a * Mat.d - Mat.b * Mat.c
	

def isSingular(Mat) -> bool:
	
	return (Mat.det() == 0.0)
	

def inv(Mat) -> Matrix2:
	''' Returns the inverse '''
	
	n = 1 / Mat.det()
	
	return Matrix2([[Mat.d * n, -Mat.b * n], [-Mat.c * n, Mat.a * n]])





