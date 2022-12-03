#!/usr/bin/python

from tkinter import *
from markdown2 import Markdown
from tkhtmlview import HTMLLabel

class Main_win:
	def __init__(self, master):
		self.master = master
		self.init_win()
		
	def init_win(self):
		self.master.title('Редактор')
		self.master.geometry('700x600')
		self.frm = Frame(self.master, bg='#fcc')
		self.frm.pack(fill=BOTH, expand=1)
		
		self.code_txt = Text(self.frm, width=1)
		self.code_txt.pack(fill=BOTH, expand=1, side=LEFT)
		
		self.html_view = HTMLLabel(self.frm, width=1, background='#ffc')
		self.html_view.pack(fill=BOTH, expand=1, side=RIGHT)
		
		self.master.mainloop()
		


root = Tk()
Main_win(root)

