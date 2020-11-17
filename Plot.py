#! /usr/bin/env

import typing

import Axis
import Grid
import FunctionObj
import ParametricFunction
import Scatter
import Object

import Controller
import WorldSpace

import OpenGL.GL
import OpenGL.GLUT


class Plot:
	
	BKG_COLOR: typing.List[float] = [.12, .13, .12]
	ALPHA: float = .0
	WIDTH: float = 1200
	HEIGHT: float = 800
	
	
	def __init__(self, fun: typing.Callable = None):
		''' Function object '''
		
		self.ws = WorldSpace.WorldSpace([Axis.Axis(), Grid.Grid(),])
		
		if fun:		self.ws.objList.append(FunctionObj.Function(fun))
		
		self.ct = Controller.Controller(self.ws)
	
	
	def display(self) -> None:
		''' Main function that renders the objects '''
	
		OpenGL.GL.glClearColor(self.BKG_COLOR[0], self.BKG_COLOR[1], self.BKG_COLOR[2], self.ALPHA)
		OpenGL.GL.glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT | OpenGL.GL.GL_DEPTH_BUFFER_BIT)

		self.ws.render()

		OpenGL.GLUT.glutSwapBuffers()


	def keyboard(self, key: int, x: int, y: int) -> None:
		''' Keyboard event '''
		
		self.ct.keyboardKeys(key, x, y)
		OpenGL.GLUT.glutPostRedisplay()


	def special(self, key: int, x: int, y: int) -> None:
		''' Special keyboard events '''
		
		self.ct.specialKeys(key, x, y)
		OpenGL.GLUT.glutPostRedisplay()


	def mouseActive(self, key: int, state: int, x: int, y: int) -> None:
		''' Mouse wheel zoom '''
		
		self.ct.mouseActive(key, state, x, y)
		OpenGL.GLUT.glutPostRedisplay()


	def mousePassive(self, x: int, y: int) -> None:
		''' Mouse passive function '''
		
		self.ct.mousePassive(x, y)
		OpenGL.GLUT.glutPostRedisplay()
	
	
	def addFunction(self, fun) -> None:
		''' Add some functions to display '''
		
		self.ws.objList.append(FunctionObj.Function(fun))
		
		
	def addScatter(self, x: list, y: list, connect: bool = True) -> None:
		
		sct = Scatter.Scatter(x, y)
		sct.CONNECT = connect
		
		self.ws.objList.append(sct)
	
	
	def addParametric(self, fun,
							params: typing.List[float]) -> None:
		''' Adds parametric function to the plotter '''
		
		
		self.ws.objList.append(ParametricFunction.Parametric(fun, params))
	
	
	def addObject(self, obj: Object.Object) -> None:
		''' Adds generic object '''
		
		
		self.ws.objList.append(obj)
		
	
	
	def plot(self) -> None:
		''' Rendering and event loop '''
		
		OpenGL.GLUT.glutInit()														# create the window
		
		OpenGL.GLUT.glutInitDisplayMode(OpenGL.GLUT.GLUT_DOUBLE | OpenGL.GLUT.GLUT_RGB | OpenGL.GLUT.GLUT_DEPTH)		# window settings
		OpenGL.GLUT.glutInitWindowSize(self.WIDTH, self.HEIGHT)					
		OpenGL.GLUT.glutInitWindowPosition(20, 10)
		OpenGL.GLUT.glutCreateWindow("plotPorn")
		
		OpenGL.GL.glEnable(OpenGL.GL.GL_DEPTH_TEST)

		OpenGL.GLUT.glutDisplayFunc(self.display)									# callback functions
		OpenGL.GLUT.glutKeyboardFunc(self.keyboard)
		OpenGL.GLUT.glutSpecialFunc(self.special)
		OpenGL.GLUT.glutPassiveMotionFunc(self.mousePassive)
		OpenGL.GLUT.glutMouseFunc(self.mouseActive)
		
		OpenGL.GLUT.glutPostRedisplay()
		
		OpenGL.GLUT.glutMainLoop()
