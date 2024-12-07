import tkinter
import pyLaysWebhooker
import requests

window = tkinter.Tk()
def sendMessage(url,msg):
    if 'https://' in url:
        pyLaysWebhooker.pyInstantSend(url,msg)
window.wm_title('Lays Webhooker for Windows App')
window.geometry('722x416')
window.iconbitmap('icon.ico')
label1 = tkinter.Label(window,text='Webhook URL:')
label1.pack()
label1.place(x=325,y=20)
entry1 = tkinter.Entry(window)
entry1.pack()
entry1.place(x=310,y=50)
label2 = tkinter.Label(window,text="Message:")
label2.pack()
label2.place(x=335,y=100)
entry2 = tkinter.Entry(window)
entry2.pack()
entry2.place(x=310,y=130)
button = tkinter.Button(window,text="Speak!",command=lambda: sendMessage(entry1.get(),entry2.get()))
button.pack()
button.place(x=335,y=200)
window.resizable(False,False)
window.mainloop()