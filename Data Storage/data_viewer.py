from tkinter import *
import Pmw, sys
filename = "data.csv"
root = Tk()     
root.title("Data Viewer")       
top = Frame(root); top.pack(side='top')
text = Pmw.ScrolledText(top,
       borderframe=5, 
       vscrollmode='dynamic', 
       hscrollmode='dynamic',
       labelpos='n', 
       label_text='file %s' % filename,
       text_width=100, 
       text_height=10,
       text_wrap='none',
       )
text.pack()

text.insert('end', open(filename,'r').read())
Button(top, text='Quit', command=root.destroy).pack(pady=15)
root.mainloop()
