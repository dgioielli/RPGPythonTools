from tkinter import *

root = Tk()

root.geometry("300x300")
root.minsize(height=250, width=350)
root.maxsize(height=250, width=350)
root.title("Notepad")

scrollbar = Scrollbar(root)

scrollbar.pack(side=RIGHT, fill=Y)

text_info = Text(root, yscrollcommand=scrollbar.set)
text_info.pack(fill=BOTH)

scrollbar.configure(command=text_info.yview)

root.mainloop()
