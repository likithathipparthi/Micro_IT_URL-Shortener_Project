from tkinter import *
import pyshorteners
import pyperclip 

root = Tk()
root.title("URL SHORTENER")
root.configure(bg = "light blue")

url=StringVar()
sortUrl= StringVar()

def urlshort():
    sortUrl.set(url.get())  
    generatedurl = pyshorteners.Shorteners().tinyurl.short(sortUrl.get())
    sortUrl.set(generatedurl)

def copy():
    generatedurl = sortUrl.get()
    pyperclip.copy(generatedurl)

Label(root, text="URL SHORTENER", font="Cambria").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate URL", command=urlshort).pack(pady=5)
Entry(root, textvariable=sortUrl).pack(pady=5)
Button(root, text="Copy URL", command=copy).pack(pady=5)  # Corrected typo here

root.mainloop()
