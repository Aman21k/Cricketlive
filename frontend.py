from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Cricinfo")
topframe=Frame(root)
topframe.pack()
two=Label(root,text="Welcome cricFreaks!!!")
two.pack(fill=X)
two=Label(root,text="Here you can see live cricket scores and list of cricket matches going around")
two.pack(fill=X)

two=Label(root,text="[Note: we gonna show live score of the top two cricket games]")
two.pack(fill=X)

two=Label(root,text="Please make your choice ....")
two.pack(fill=X)


middleframe=Frame(root)
middleframe.pack()

resultLabel1 = Label(root, text = "")
resultLabel1.pack(fill=X)
resultLabel2 = Label(root, text = "")
resultLabel2.pack(fill=X)
resultLabel3 = Label(root, text = "")
resultLabel3.pack(fill=X)


def clicked1():

    res1=first_match()
    resultLabel1.config(text=res1)
   

def clicked3():
    res2=second_match()
    resultLabel2.config(text=res2)
def clicked2():
    res3=live_matches()
    resultLabel3.config(text=res3)
    
button1=Button(middleframe,text="live scores(match1)",command=clicked1)
button3=Button(middleframe,text="live scores(match2)",command=clicked3)
button2=Button(middleframe,text="live matches",command=clicked2)

button1.pack(side=LEFT)
button3.pack(side=LEFT)
button2.pack(side=RIGHT)

root.mainloop()


