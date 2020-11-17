#! /usr/bin/env python3

import Object
import Point

import Vector2
import Camera
import Text
import WorldSpace
import MouseFollower

import OpenGL.GLUT



class Controller:
	''' This function controls the interaction with the user '''
	
	STEP_WIDTH: 		float = 10
	DX: 				float = .5
	MARGIN: 			float = 2
	STEP_WIDTH_SCROLL: 	float = .02
	STEP_PARAM:			float = .1
	
	
	def __init__(self, wspace: WorldSpace.WorldSpace):
		
		self.ws = wspace
		
		self.drag = False
		self.paramIndex = 0
		
		self.ws.objList.append(MouseFollower.Mouse())
		
		self.n: int = 0
	
	
	
	def specialKeys(self, key: int, x: int, y: int) -> None:
		''' Give it to glutSpecialFunc '''
		
		if key == OpenGL.GLUT.GLUT_KEY_LEFT:		self.ws.camPosition += Vector2.Vector2(-self.ws.camDeltaX / self.STEP_WIDTH, .0)
		                                            
		elif key == OpenGL.GLUT.GLUT_KEY_RIGHT:	    self.ws.camPosition += Vector2.Vector2(self.ws.camDeltaX / self.STEP_WIDTH, .0)
			                                        
		elif key == OpenGL.GLUT.GLUT_KEY_UP:        self.ws.camPosition += Vector2.Vector2(.0, self.ws.camDeltaY / self.STEP_WIDTH)
			                                        
		elif key == OpenGL.GLUT.GLUT_KEY_DOWN:      self.ws.camPosition += Vector2.Vector2(.0, -self.ws.camDeltaY / self.STEP_WIDTH)
			
		
		self.ws.render()	
			
		OpenGL.GLUT.glutPostRedisplay()
	
		
		
	
	
	def keyboardKeys(self, key: int ,x: int, y: int) -> None:
		''' Give it glutKeyboardFunc '''
		
		if key == b'q':
			
			N = (self.n + 1) % len(self.ws.objList)
			
			while not self.ws.objList[N].movable:
				N = (N + 1) % len(self.ws.objList)
			
			self.n = N
		
		elif key == b'+':
			
			if self.ws.camDeltaX - self.DX > 0:		self.ws.camDeltaX -= self.DX
			
		elif key == b'-':			self.ws.camDeltaX += +self.DX
		
		elif key == b'c':
			
			newList = [OBJ for OBJ in self.ws.objList if str(OBJ) != 'Point']
			
			self.ws.objList = newList.copy()
		
		
		for OBJ in self.ws.objList:
			
			if str(OBJ) == 'Parametric':
				
				if key == b'd':		OBJ.params[self.paramIndex] += self.STEP_PARAM
		
				elif key == b'a':		OBJ.params[self.paramIndex] -= self.STEP_PARAM
		
				elif key == b'w':		self.paramIndex = (self.paramIndex + 1) % len(OBJ.params)
		
			
		
		self.ws.render()

		OpenGL.GLUT.glutPostRedisplay()



	def mousePassive(self,x: int, y: int) -> None:
		''' What to do when I move the mouse over the screen '''
		
		
		for OBJ in self.ws.objList:
			
			if str(OBJ) == 'Mouse':
				
				OBJ.screenPosition = self.ws.mouseToScreen(x, y)
				worldPosition = self.ws.mouseToWorld(x, y)
				OBJ.string = f'({worldPosition.x: .1f},{worldPosition.y: .1f})'
					
		
		OpenGL.GLUT.glutPostRedisplay()



	def mouseActive(self, key: int, state: int, x: int, y: int) -> None:
		''' What to do when I move the mouse over the screen '''
		
		if key == 4 and state:
			
			if self.ws.camDeltaX - self.DX > 0:		self.ws.camDeltaX -= self.DX
	
		elif key == 3 and state:					self.ws.camDeltaX += +self.DX
		
		elif key == 0 and state:
			
			worldPosition = self.ws.mouseToWorld(x, y)
			self.ws.objList.append(Point.Point(Vector2.Vector2(worldPosition.x, worldPosition.y)))		


			
		
	
	
