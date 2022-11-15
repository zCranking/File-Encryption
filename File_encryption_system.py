from tkinter import *
from tkinter import filedialog as fd
import hashlib

root=Tk()
root.geometry("250x190")
root.config(background="#0072BB")

def apply_md5():
    print("MD5 function")
    text_file = fd.askopenfilename()
    print(text_file)
    read_file = text_file.open("r")
    paragraph = read_file.read()
    byte = paragraph.encode()
    file_result = hashlib.md5(byte)
    file_hexd = file_result.hex()
    print(file_hexd)
    
    open(md5.txt, "w").write(file_hexd)
    print(file_hexd)
    close(md5.txt)
    
        
    
    
def apply_sha256():
    print("SHA function")   
    text_file = fd.askopenfilename()
    print(text_file)
    read_file = open(text_file, "r")
    paragraph = read_file.read()
    byte = paragraph.encode()
    file_result = hashlib.sha256(byte)
    file_hexd = byte.hex()
    print(file_hexd)
    
    open("sha256.txt", "w").write(file_hexd)
    print(file_hexd)
    close("sha256.txt") 
    
btn=Button(root, text="Apply MD5",command=apply_md5)
btn.place(relx=0.3,rely=0.5, anchor=CENTER)
btn1=Button(root, text="Apply SHA256",command=apply_sha256)
btn1.place(relx=0.7,rely=0.5, anchor=CENTER)
root.mainloop()