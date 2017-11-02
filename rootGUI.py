# Unsupervised Learning GUI

# Headers
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np


class graph:

	# Initialisation function
	def __init__(self,master,title):

		# Set the title
		self.master = master
		master.title(title)

		# Figure canvas
		self.fig = Figure()
		self.plt = self.fig.add_subplot(111);
		
		self.canvas = FigureCanvasTkAgg(self.fig, master=master)
		self.canvas.show();
		self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		# Window settings
		master.resizable(True,True)
		master.update()

	# Functions for GUI
	def createButton(self,text,command):
		plotButton = tk.Button(self.master, text =text, command = command)
		plotButton.pack(in_=self.master, side=tk.LEFT)

	def checkBox(self,text):
		check = tk.IntVar()
		c = tk.Checkbutton(root, text=text, variable=check)
		c.pack(in_=root, side=tk.LEFT)
		return check;

	def createDropList(self,labels,ini):
		var = tk.StringVar(self.master)
		var.set(labels[ini]);
		drop = tk.OptionMenu(root,var,*labels)
		drop.pack(in_=self.master, side=tk.LEFT)      
		return var

	def createEntry(self,text,*argv):
		var = tk.StringVar();
		entry = tk.Entry(root,textvariable=var);
		tk.Label(root, text=text).pack(side=tk.LEFT)
		entry.pack(in_=root, side=tk.LEFT)  
		if argv:
			var.set(argv[0]); 
		return var;

# Create window  
root = tk.Tk()
g = graph(root,'GUI Time');

# Close the root loop
root.mainloop()