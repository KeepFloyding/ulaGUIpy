# Unsupervised Learning GUI

# Updates to perform:

# new class with inheritance
# automatically update dropdown list
# drop down menu for what colors of scatter plot should be
# restricting number of plotted points (sample)
# implementing additional windows



# Headers
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np

import pandas as pd

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


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

		# Creating buttons
		self.cluster_labels = [];

		self.csvFileName = self.createEntry('csv file')
		self.keys = ['Axis_1','Axis_2','PCA_1','PCA_2']

		loadButton = self.createButton('Load Data', self.loadData)
		self.drop1 = self.createDropList(self.keys,0)
		self.drop2 = self.createDropList(self.keys,1)
		plotButton = self.createButton('Plot!', self.plotFigure)
		clusterButton = self.createButton('Cluster',self.clusterData)
		pcaButton = self.createButton('Run PCA',self.runPCA)
        
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

	# Functions specific to a certain class

	def loadData(self):

		csvFile = self.csvFileName.get()

		self.data = pd.read_csv(csvFile)
		self.keys = self.data.keys();


	def plotFigure(self):

		self.plt.clear();

		choice_1 = self.drop1.get();
		choice_2 = self.drop2.get();

		x = self.data[choice_1]
		y = self.data[choice_2]

		if len(self.cluster_labels) == 0:
			c = np.random.rand(1, len(x)) 
		else:
			c = self.cluster_labels


		self.plt.scatter(x, y, c=c, picker=True);
		self.plt.set_xlabel(choice_1)
		self.plt.set_ylabel(choice_2)
		#self.fig.colorbar()        
		self.canvas.draw();

	def clusterData(self):

		kmeans = KMeans();
		kmeans.fit(self.data)

		self.cluster_labels = kmeans.labels_

	def runPCA(self):

		pca = PCA();
		scaler = StandardScaler()
		X = scaler.fit_transform(self.data)
		X_pca = pca.fit_transform(X)
		self.data['PCA_1'] = X_pca[:,0]
		self.data['PCA_2'] = X_pca[:,1]



# Create window  
root = tk.Tk()
g = graph(root,'GUI Time');

# Close the root loop
root.mainloop()