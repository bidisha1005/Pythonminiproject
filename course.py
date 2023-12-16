from tkinter import *
from PIL import Image,ImageTk  #importing pillow module
from tkinter import ttk
class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title('Student Result Management System')
        self.root.geometry('1200x480+80+170')
        self.root.config(bg='white')
        self.root.focus_force()

        # title
        title = Label(self.root, text='Manage Course Details',font=('Arial Rounded MT Bold', 20, 'bold'), bg='#190482', fg='white').place(x=10,y=15,width=1180,height=35)

        #variables
        self.var_course=StringVar()
        self.var_duration = StringVar()
        self.var_charges= StringVar()

        #widgets
        lbl_courseName=Label(self.root,text='Course Name',font=('Founders Grostesk Text',15,'bold'),bg='white').place(x=10,y=60)
        lbl_duration= Label(self.root, text='Duration', font=('Founders Grostesk Text', 15, 'bold'),bg='white').place(x=10, y=100)
        lbl_charges= Label(self.root, text='Charges', font=('Founders Grostesk Text', 15, 'bold'),bg='white').place(x=10, y=140)
        lbl_description= Label(self.root, text='Description', font=('Founders Grostesk Text', 15, 'bold'),bg='white').place(x=10, y=180)

        #entry fields
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=('Founders Grostesk Text',15,'bold'),bg='#C2D9FF').place(x=150,y=60,width=200)
        txt_duration= Entry(self.root,textvariable=self.var_duration, font=('Founders Grostesk Text', 15, 'bold'),bg='#C2D9FF').place(x=150, y=100,width=200)
        txt_charges= Entry(self.root,textvariable=self.var_charges, font=('Founders Grostesk Text', 15, 'bold'),bg='#C2D9FF').place(x=150, y=140,width=200)
        self.txt_description= Text(self.root, font=('Founders Grostesk Text', 15, 'bold'),bg='#C2D9FF').place(x=150, y=180,width=500,height=130)

        #buttons
        self.btn_add=Button(self.root,text='Save',font=('Founders Grostesk Text',15,'bold'),bg='#8E8FFA',fg='black',cursor='hand 2').place(x=150,y=400,width=110,height=40)
        self.btn_update= Button(self.root, text='Update', font=('Founders Grostesk Text', 15, 'bold'), bg='#8E8FFA',fg='black', cursor='hand 2').place(x=270,y=400, width=110, height=40)
        self.btn_delete= Button(self.root, text='Delete', font=('Founders Grostesk Text', 15, 'bold'), bg='#8E8FFA',fg='black', cursor='hand 2').place(x=390,y=400, width=110, height=40)
        self.btn_clear= Button(self.root, text='Clear', font=('Founders Grostesk Text', 15, 'bold'), bg='#8E8FFA',fg='black', cursor='hand 2').place(x=510,y=400, width=110, height=40)

        #search panel
        self.var_search=StringVar()
        lbl_search_courseName = Label(self.root, text='Course Name', font=('Founders Grostesk Text', 15, 'bold'), bg='white').place(x=720, y=60)
        txt_search_courseName = Entry(self.root, textvariable=self.var_search,font=('Founders Grostesk Text', 15, 'bold'), bg='#C2D9FF').place(x=860, y=60,width=180)
        btn_search= Button(self.root, text='Search', font=('Founders Grostesk Text', 15, 'bold'), bg='#8E8FFA',fg='black', cursor='hand 2').place(x=1070, y=60, width=120, height=28)

        #content
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=('cid','name','duration','charges','description'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading('cid',text='Course ID')
        self.CourseTable.heading('name', text='Name')
        self.CourseTable.heading('duration', text='Duration')
        self.CourseTable.heading('charges', text='Charges')
        self.CourseTable.heading('description', text='Description')

        self.CourseTable['show']='headings'

        self.CourseTable.column('cid',width=100)
        self.CourseTable.column('name',width=100)
        self.CourseTable.column('duration',width=100)
        self.CourseTable.column('charges',width=100)
        self.CourseTable.column('description',width=150)

        self.CourseTable.pack(fill=BOTH,expand=1)

if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()