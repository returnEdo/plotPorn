#! /usr/bn/env python3

import Object
import Vector2
import Matrix2
import typing
import OpenGL.GL
import OpenGL.GLUT


default = [.7, .7, .7]


def renderToScreen(x: int, y: int, string: str, TEXT_COLOR: typing.List[float] = default) -> None:
	''' Renders in Screen coordinates '''

	OpenGL.GL.glColor(TEXT_COLOR[0], TEXT_COLOR[1], TEXT_COLOR[2])

	OpenGL.GL.glRasterPos(x, y)		

	for character in string:

		OpenGL.GLUT.glutBitmapCharacter(OpenGL.GLUT.GLUT_BITMAP_9_BY_15, ord(character))


def fromScreenToWorld(position: Vector2.Vector2,
					  Mcs: Matrix2.Matrix2,
					  camPosition: Vector2.Vector2) -> typing.List[float]:
	''' Converts position from screen to world '''
	
	
	return list((Mcs * (position - camPosition)))
