from tkinter import *
from PIL import Image,ImageTk  #importing pillow module
from course import CourseClass
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title('Student Result Management System')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='white')

        #icons
        self.logo_dash=ImageTk.PhotoImage(file='images/student-with-graduation-cap.png')
        #title
        title=Label(self.root,text='Student Result Management System',padx=10,compound=LEFT,image=self.logo_dash,font=('Arial Rounded MT Bold',20,'bold'),bg='#190482',fg='white').place(x=0,y=0,relwidth=1)
        #menu
        M_Frame=LabelFrame(self.root,text='Menus',font=('Founders Grotesk Text',15),bg='white')
        M_Frame.place(x=10,y=70,width=1340,height=80)

        #adding buttons
        btn_course=Button(M_Frame,text='Course',font=('Founders Grotesk Text',15,'bold'),bg='#190482',fg='black',cursor='hand 2',command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student = Button(M_Frame, text='Student', font=('Founders Grotesk Text', 15, 'bold'), bg='#190482',fg='black', cursor='hand 2').place(x=240, y=5, width=200, height=40)
        btn_result= Button(M_Frame, text='Result', font=('Founders Grotesk Text', 15, 'bold'), bg='#190482',fg='black', cursor='hand 2').place(x=460, y=5, width=200, height=40)
        btn_view = Button(M_Frame, text='View', font=('Founders Grotesk Text', 15, 'bold'), bg='#190482',fg='black', cursor='hand 2').place(x=680, y=5, width=200, height=40)
        btn_logout = Button(M_Frame, text='Logout', font=('Founders Grotesk Text', 15, 'bold'), bg='#190482', fg='black', cursor='hand 2').place(x=900, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text='Exit', font=('Founders Grotesk Text', 15, 'bold'), bg='#190482',fg='black', cursor='hand 2').place(x=1120, y=5, width=200, height=40)

        #content window
        self.bg_img=Image.open('images/uni.jpg')
        self.bg_img=self.bg_img.resize((920,350))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        #footer
        footer = Label(self.root, text='Policy Terms       Contact us       Help\n© 2023 Student Login',font=('Arial Rounded MT Bold', 12,), bg='black', fg='white').pack(side=BOTTOM,fill=X)

        #update details
        self.lbl_course=(Label(self.root,text='Total Courses\n[ 0 ]',font=('Founders Grotesk Text',20),bd=10,relief=RIDGE,bg='#7752FE',fg='white')
                         .place(x=400,y=530,width=300,height=100))

        self.lbl_student=(Label(self.root, text='Total Students\n[ 0 ]', font=('Founders Grotesk Text', 20), bd=10, relief=RIDGE, bg='#7752FE', fg='white')
                         .place(x=710, y=530, width=300, height=100))

        self.lbl_result=(Label(self.root, text='Total Results\n[ 0 ]', font=('Founders Grotesk Text', 20), bd=10, relief=RIDGE,bg='#7752FE', fg='white')
                         .place(x=1020, y=530, width=300, height=100))


    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win )

if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
