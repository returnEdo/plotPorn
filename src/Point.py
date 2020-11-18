#! /usr/bin/env python3

import Vector2
import Matrix2

import Text
import Polygon

import typing


class Point(Polygon.Polygon):
	''' These are the points you can drop with the mouse '''
	
	RADIUS: float = .05
	N_SIDES: int = 8
	DIFF: float = .04
	POINT_COLOR: typing.List[float] = [.6, .98, .6]
	
	def __init__(self, position: Vector2.Vector2):
		
		super().__init__(position, self.N_SIDES, self.RADIUS)
		
		self.POL_COLOR = self.POINT_COLOR.copy()
		self.movable = False
	
	
	def render(self, Mcp: Matrix2.Matrix2,	
					 Mps: Matrix2.Matrix2,	
					 Mcs: Matrix2.Matrix2,	
					 camPosition: Vector2.Vector2) -> None:
	
		super().render(Mcp, Mps, Mcs, camPosition)
		
		screenPosition = Mcs * (self.position - camPosition)
		
		Text.renderToScreen(screenPosition.x + self.DIFF,
							screenPosition.y + 2 * self.DIFF,
							f'X:{self.position.x: .4f}')
							
		Text.renderToScreen(screenPosition.x + self.DIFF,
							screenPosition.y + self.DIFF,
							f'Y:{self.position.y: .4f}')
	
	def __str__(self) -> str:		return 'Point'
