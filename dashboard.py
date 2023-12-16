from tkinter import *
from PIL import Image,ImageTk  #importing pillow class
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title('Student Result Management System')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='white')

        #icons
        self.logo_dash=ImageTk.PhotoImage(file='images/student-with-graduation-cap.png')
        #title
        title=Label(self.root,text='Student Result Management System',image=self.logo_dash,font=('Arial Rounded MT Bold',20,'bold'),bg='#190482',fg='white').place(x=0,y=0,relwidth=1)


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
