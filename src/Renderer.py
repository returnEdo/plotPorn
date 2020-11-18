#! /usr/bin/env python3

import Camera
import Object
import Grid
import Matrix2
import Vector2
import typing

import OpenGL.GLUT





class Renderer:
	
	def __init__(self, objList: list, cam: Camera.Camera = Camera.Camera(), grid: Grid.Grid = Grid.Grid()):
		''' objList is list of Object.Object to be rendered '''
		
		self.objList = objList
		self.cam = cam
		self.grid = grid
		
		
		
	def computeGlobal(self):
		''' Computes the screen coordinates of the object '''
		
		self.cam.updateZoom(.0)
		self.grid.renderGrid(self.cam)

		for obj in self.objList:
			
			screenPosition = []
			obj.updateVertices()										# updates the vertices of the objects
			
			M = Matrix2.Matrix2([[2 / self.cam.deltaX, 0], 					# shear matrix: from world to screen coordinates
								 [0, 2 / self.cam.deltaY]])
			
			for Vertex in obj.vertices:
				
				screenPosition.append((M * (Vertex - self.cam.position)))	# translate the coordinates to the center of the cam
				
			obj.render(screenPosition)
	
	
	
	def computeGlobalSingle(self, obj: Object.Object) -> typing.List[Vector2.Vector2]:
		''' Computes the global coordinates of a single obj '''
	
	
		self.cam.updateZoom(.0)
		self.grid.renderGrid(self.cam)
		
		
		screenPosition = []
		obj.updateVertices()
		
		M = Matrix2.Matrix2([[2 / self.cam.deltaX, 0], 
							 [0, 2 / self.cam.deltaY]])
		
		for Vertex in obj.vertices:
			
			screenPosition.append((M * (Vertex - self.cam.position)))
			
		return screenPosition	
		
		
	# ~ def screenToWorld(self, x: float, y: float) -> Vector2.Vector2:
		# ~ ''' Traduces from screen to world '''
		
		
		
		
		
		
		
