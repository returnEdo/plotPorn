#! /usr/bin/env python3

import Matrix2
import numpy



class Rotation(Matrix2.Matrix2):
	
	def __init__(self, theta: float = numpy.pi, rad: bool = True):
		
		if not rad:	theta = theta / 180 * numpy.pi
		
		mat = [[numpy.cos(theta), numpy.sin(theta)],
			   [-numpy.sin(theta), numpy.cos(theta)]]
			   
		
		super().__init__(mat)
	
	
	def inv(self) -> Matrix2.Matrix2:				return ~self
	
	def det(self) -> float:							return 1.0
