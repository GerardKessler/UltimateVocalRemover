# -*- coding: utf-8 -*-
# Copyright (C) 2021 Gerardo Kessler <ReaperYOtrasYerbas@gmail.com>
# This file is covered by the GNU General Public License.

import appModuleHandler
import api
from ui import message
import winUser
from tones import beep

class AppModule(appModuleHandler.AppModule):

	CATEGORY= 'UltimateVoiceRemover'
	
	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		self.elements= None
		self.x= 0

	def createGui(self):
		if self.elements: return
		self.elements= [
			{'label': 'Archivo de entrada', 'path': api.getForegroundObject().firstChild.lastChild.children[8].children[3]},
			{'label': 'Carpeta de salida', 'path': api.getForegroundObject().firstChild.lastChild.children[8].children[1]},
			{'label': 'Modelo', 'path': api.getForegroundObject().firstChild.lastChild.children[5].children[26]},
			{'label': 'Método de procesamiento', 'path': api.getForegroundObject().firstChild.lastChild.children[5].children[42]},
			{'label': 'Elementos de extracción', 'path':  api.getForegroundObject().simpleFirstChild.simpleNext.simpleNext.simpleNext.simpleNext.simpleNext.simpleNext.simpleNext.simpleNext.simpleNext.simpleNext.simpleNext},
			{'label': 'Iniciar proceso', 'path': api.getForegroundObject().firstChild.lastChild.children[4]}
		]

	def script_press(self, gesture):
		self.createGui()
		api.moveMouseToNVDAObject(self.elements[self.x]['path'])
		winUser.mouse_event(winUser.MOUSEEVENTF_LEFTDOWN,0,0,None,None)
		winUser.mouse_event(winUser.MOUSEEVENTF_LEFTUP,0,0,None,None)
		beep(220, 15, 15, 15)

	def script_next(self, gesture):
		self.createGui()
		if self.x < len(self.elements) - 1:
			self.x+=1
			message(self.elements[self.x]['label'])
		else:
			self.x= 0
			message(self.elements[self.x]['label'])
		beep(220, 15, 1, 30)

	def script_previous(self, gesture):
		self.createGui()
		if self.x > 0:
			self.x-=1
			message(self.elements[self.x]['label'])
		else:
			self.x= len(self.elements) - 1
			message(self.elements[self.x]['label'])
		beep(220, 15, 30, 1)

	__gestures= {
		'kb:control+downArrow': 'next',
		'kb:control+upArrow': 'previous',
		'kb:control+enter': 'press'
	}
