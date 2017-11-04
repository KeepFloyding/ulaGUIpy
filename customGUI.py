## Customised GUI
from rootGUI import graph
import tkinter as tk

# Create new class

class new(graph):

    def __init__(self, master,title):
        
        # Inherit the previous init class
        self.csvFileName = self.createEntry('csv file')
        graph.__init__(self,master, title)



# Create window  
root = tk.Tk()
g = new(root,'GUI Time');

# Close the root loop
root.mainloop()
