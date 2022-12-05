#!/usr/bin/python

from tkinter import *
from tkinter import filedialog, messagebox

from markdown2 import Markdown
from tkhtmlview import HTMLLabel

class Main_win:
	def __init__(self, master):
		self.master = master
		self.file_name = 'test.md'
		self.init_win()
		
	def init_win(self):
		self.master.title('Редактор')
		self.master.geometry('700x600')
		
		self.main_menu = Menu(self.master)
		self.file_menu = Menu(self.main_menu, tearoff=0)
		self.file_menu.add_command(label='Open', command=self.open_file)
		self.file_menu.add_command(label='Save', command=self.save_file)
		self.file_menu.add_separator()
		self.file_menu.add_command(label='Exit', command=self.master.quit)
		self.main_menu.add_cascade(label='File', menu=self.file_menu)
		self.master.config(menu=self.main_menu)
		
		self.bar_frm = Frame(self.master)
		self.bar_frm.pack(fill=BOTH)
		self.bold_btn = Button(self.bar_frm, text='B', width=3, 
			command=lambda: self.tag_wrap('**'))
			#command=lambda: self.tag_ins(self.code_txt.index('insert'), '*'))
		self.bold_btn.pack(side=LEFT, padx=2)
		self.italic_btn = Button(self.bar_frm, text='I', width=3, 
			command=lambda: self.tag_wrap('_'))
		self.italic_btn.pack(side=LEFT, padx=2)
		
		
		self.frm = Frame(self.master, bg='#fcc')
		self.frm.pack(fill=BOTH, expand=1)
		
		self.code_txt = Text(self.frm, width=1)
		self.code_txt.bind('<<Modified>>', self.onInputChange)
		self.code_txt.pack(fill=BOTH, expand=1, side=LEFT)
		
		self.html_view = HTMLLabel(self.frm, width=1, background='#ffc', html='Привет')
		self.html_view.pack(fill=BOTH, expand=1, side=RIGHT)
		self.html_view.fit_height()
		
		self.master.mainloop()
		
	def onInputChange(self, event):
		self.code_txt.edit_modified(0)
		md2html = Markdown()
		self.html_view.set_html(md2html.convert(self.code_txt.get('1.0', END)))
	
	def tag_wrap(self, tag):
		selection = self.code_txt.tag_ranges(SEL)
		if selection:
			start_ins = selection[0]
			end_ins = selection[1]
		self.tag_ins(end_ins, tag)
		self.tag_ins(start_ins, tag)
	
	def tag_ins(self, index, tag):
		self.code_txt.insert(index, tag)
	
	def open_file(self):
		file_name = filedialog.askopenfilename(filetypes=(('Markdown File', '*.md'),
															('Text File', '*.txt'),
															('All Files', '*.*')))
		if file_name:
			try:
				self.code_txt.delete('1.0', END)
				with open (file_name) as file_object:
					self.code_txt.insert(END, file_object.read())
			except:
				messagebox.showerror('Ошибка', f'{file_name} Не открывается')
	
	def save_file(self):
		file_data = self.code_txt.get('1.0', END)
		file_name = filedialog.asksaveasfilename(filetypes = (('Markdown File', '*.md'),
							('Text File', '*.txt')), title='Save File', 
							defaultextension='md', initialfile=self.file_name)
		if file_name:
			try:
				with open(file_name, 'w') as f:
					f.write(file_data)
				self.file_name = file_name
			except:
				messagebox.showerror('Ошибка', f'Файл {file_name} не может быть сохранён')


root = Tk()
Main_win(root)

