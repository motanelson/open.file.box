import tkinter as tk
from tkinter import filedialog


a=filedialog.askopenfile(mode= "r" ,defaultextension="*.*")
f1=open(a.name,"r")
print(f1.read())
f1.close()