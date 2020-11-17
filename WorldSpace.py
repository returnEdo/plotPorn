#! /usr/bin/env pyton3

import Matrix2
import Vector2

import Object
import Camera

import typing

import OpenGL.GLUT




class WorldSpace:
	''' This class relates the objects to be rendered and the cam '''
	
	
	def __init__(self, objList: typing.List[Object.Object] = []):
		
		self.objList = objList
		
		self.camPosition = Vector2.Vector2()
		self.camDeltaX = 10
		self.camDeltaY = 10
		
	
	def render(self) -> None:
		''' Renders all the objects '''
		
		Mcp, Mps, Mcs = self.computeMatrices()
		
		for Obj in self.objList:

			Obj.render(Mcp, Mps, Mcs, self.camPosition)
	
	
	def updateAspectRatio(self) -> None:
		''' Updates self.camDeltaY to keep the aspect ratio '''
		
		self.camWidth = OpenGL.GLUT.glutGet(OpenGL.GLUT.GLUT_WINDOW_WIDTH)
		self.camHeight = OpenGL.GLUT.glutGet(OpenGL.GLUT.GLUT_WINDOW_HEIGHT)		
		
		self.camDeltaY = self.camHeight / self.camWidth * self.camDeltaX		
	
	
	
	def computeMatrices(self) -> typing.List[Matrix2.Matrix2]:
		''' Should be called after cam position and zoom have been adjusted '''
		
		self.updateAspectRatio()
		
		Mcp = Matrix2.Matrix2([[self.camWidth/ self.camDeltaX, 0],					# from camera to pixel frame
							  [0, self.camHeight / self.camDeltaY]])
		
		Mps = Matrix2.Matrix2([[2 / self.camWidth, .0],								# from pixel to screen frame
							   [.0, 2 / self.camHeight]])
		
		Mcs = Matrix2.Matrix2([[2 / self.camDeltaX, .0],							# from camera to screen frame
							   [.0, 2 / self.camDeltaY]])
		
		return [Mcp, Mps, Mcs]
	
	
	
	def mouseToWorld(self, x: int, y: int) -> Vector2.Vector2:
		''' Converts from mouse coordinates to world coordinates an screen coordinates'''

		# update aspect ratio
		
		Mmc = Matrix2.Matrix2([[self.camDeltaX / self.camWidth, 0],
							   [0, -self.camDeltaY / self.camHeight]])
							 
		return Mmc * Vector2.Vector2(x - self.camWidth / 2, y - self.camHeight / 2) + self.camPosition
	
	
	def mouseToScreen(self, x: int, y: int) -> Vector2.Vector2:
		''' Converts from mouse coordinates to screen coordinates '''
		
		Mms = Matrix2.Matrix2([[2 / self.camWidth, 0],
							   [0, -2 / self.camHeight]])
		
		return Mms * Vector2.Vector2(x - self.camWidth / 2, y - self.camHeight / 2)
	
	
