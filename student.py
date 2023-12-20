from tkinter import *
from PIL import Image,ImageTk  #importing pillow module
from tkinter import ttk,messagebox
import sqlite3
class StudentClass:
    def __init__(self,root):
        self.root=root
        self.root.title('Student Result Management System')
        self.root.geometry('1200x480+80+170')
        self.root.config(bg='white')
        self.root.focus_force()

        # title
        title = Label(self.root, text='Manage Student Details',font=('Arial Rounded MT Bold', 20, 'bold'), bg='#190482', fg='white').place(x=10,y=15,width=1180,height=35)

        #variables
        self.var_roll=StringVar()
        self.var_Name = StringVar()
        self.var_Email= StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_a_date=StringVar()
        self.var_course=StringVar()
        # self.var_sate=StringVar()
        # self.var_city=StringVar()
        # self.var_pin=StringVar()

        #widgets

        # ====column 1====

        lbl_roll=Label(self.root,text='Roll no.',font=('Founders Grostesk Text',15,'bold'),bg='white').place(x=10,y=60)
        lbl_Name= Label(self.root, text='Name', font=('Founders Grostesk Text', 15, 'bold'),bg='white').place(x=10, y=100)
        lbl_Email= Label(self.root, text='Email', font=('Founders Grostesk Text', 15, 'bold'),bg='white').place(x=10, y=140)
        lbl_gender= Label(self.root, text='Gender', font=('Founders Grostesk Text', 15, 'bold'),bg='white').place(x=10, y=180)
        lbl_address = Label(self.root, text='Address', font=('Founders Grostesk Text', 15, 'bold'), bg='white').place(x=10, y=220)

        #entry fields

        self.txt_roll=Entry(self.root, textvariable=self.var_roll, font=('Founders Grostesk Text', 15, 'bold'), bg='#C2D9FF')
        self.txt_roll.place(x=150, y=60, width=200)
        txt_Name= Entry(self.root,textvariable=self.var_Name, font=('Founders Grostesk Text', 15, 'bold'),bg='#C2D9FF').place(x=150, y=100,width=200)
        txt_Email= Entry(self.root,textvariable=self.var_Email, font=('Founders Grostesk Text', 15, 'bold'),bg='#C2D9FF').place(x=150, y=140,width=200)
        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=('Select','Male','Female','Other'), font=('Founders Grostesk Text', 15, 'bold'),state='readonly',justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)

        #====column 2=====

        lbl_dob = Label(self.root, text='D.O.B', font=('Founders Grostesk Text', 15, 'bold'), bg='white').place(x=360, y=60)
        lbl_contact = Label(self.root, text='Contact', font=('Founders Grostesk Text', 15, 'bold'), bg='white').place(x=360,y=100)
        lbl_admission= Label(self.root, text='Admission', font=('Founders Grostesk Text', 15, 'bold'), bg='white').place(x=360,y=140)
        lbl_course= Label(self.root, text='Course', font=('Founders Grostesk Text', 15, 'bold'), bg='white').place(x=360, y=180)


        #entry fields column 2
        self.course_list=[]  #function call to update the list
        self.fetch_course()

        txt_dob = Entry(self.root, textvariable=self.var_dob, font=('Founders Grostesk Text', 15, 'bold'),bg='#C2D9FF').place(x=480, y=60, width=200)
        txt_contact= Entry(self.root, textvariable=self.var_contact, font=('Founders Grostesk Text', 15, 'bold'),bg='#C2D9FF').place(x=480, y=100, width=200)
        txt_admission= Entry(self.root, textvariable=self.var_a_date, font=('Founders Grostesk Text', 15, 'bold'),bg='#C2D9FF').place(x=480, y=140, width=200)
        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course,values=self.course_list,font=('Founders Grostesk Text', 15, 'bold'), state='readonly', justify=CENTER)
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.set('Select')

        #======text address====
        self.txt_Address= Text(self.root, font=('Founders Grostesk Text', 15, 'bold'),bg='#C2D9FF')
        self.txt_Address.place(x=150, y=220,width=540,height=100)

        #buttons
        self.btn_add=(Button(self.root,text='Save',font=('Founders Grostesk Text',15,'bold'),bg='#8E8FFA',fg='black',cursor='hand 2',command=self.add))
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update= Button(self.root, text='Update', font=('Founders Grostesk Text', 15, 'bold'), bg='#8E8FFA',fg='black', cursor='hand 2',command=self.update)
        self.btn_update.place(x=270,y=400, width=110, height=40)
        self.btn_delete= Button(self.root, text='Delete', font=('Founders Grostesk Text', 15, 'bold'), bg='#8E8FFA',fg='black', cursor='hand 2',command=self.delete)
        self.btn_delete.place(x=390,y=400, width=110, height=40)
        self.btn_clear= Button(self.root, text='Clear', font=('Founders Grostesk Text', 15, 'bold'), bg='#8E8FFA',fg='black', cursor='hand 2',command=self.clear)
        self.btn_clear.place(x=510,y=400, width=110, height=40)

        #search panel
        self.var_search=StringVar()
        lbl_search_roll = Label(self.root, text='Roll no', font=('Founders Grostesk Text', 15, 'bold'), bg='white').place(x=720, y=60)
        txt_search_roll = Entry(self.root, textvariable=self.var_search,font=('Founders Grostesk Text', 15, 'bold'), bg='#C2D9FF').place(x=860, y=60,width=180)
        btn_search= Button(self.root, text='Search', font=('Founders Grostesk Text', 15, 'bold'), bg='#8E8FFA',fg='black', cursor='hand 2',command=self.search).place(x=1070, y=60, width=120, height=28)

        #content
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)

        self.CourseTable=ttk.Treeview(self.C_Frame,columns=('roll','name','email','gender','dob','contact','admission','course','address'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("roll", text="Roll No.")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("dob", text="D.O.B")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("admission", text="Admission")
        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("address",text='Address')

        self.CourseTable['show']='headings'

        self.CourseTable.column('roll',width=100)
        self.CourseTable.column('name',width=100)
        self.CourseTable.column('email',width=100)
        self.CourseTable.column('gender',width=100)
        self.CourseTable.column('dob',width=100)
        self.CourseTable.column('contact', width=100)
        self.CourseTable.column('admission', width=100)
        self.CourseTable.column('course', width=100)
        self.CourseTable.column('address', width=200)

        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)   #bind hels in performaning an event
        self.show()

#======================================================================================

    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_Name.set(""),
        self.var_Email.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_a_date.set(""),
        self.var_course.set("Select"),
        self.txt_Address.get('1.0', END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")

    def delete(self):
        con = sqlite3.connect(database='Pythonminiproject')
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror('Error', 'Roll no should be required', parent=self.root)
            else:
                cur.execute('select * from student where roll=?', (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Please student from the list', parent=self.root)
                else:
                    op=messagebox.askyesno('Confirm','Do you want to proceed',parent=self.root)
                    if op ==True:
                        cur.execute('delete from student where roll=?', (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo('Delete','Student deleted successfully',parent=self.root)
                        self.clear()  #show function has been called in clear as well
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}')

    def get_data(self,ev):
        self.txt_roll.config(state='readonly')  #sets the coursename to read only mode
        self.txt_roll
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0]),
        self.var_Name.set(row[1]),
        self.var_Email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.txt_Address.delete('1.0', END)
        self.txt_Address.insert(END,row[8])

    def add(self):
        con = sqlite3.connect(database='Pythonminiproject')
        cur = con.cursor()
        try:
            if self.var_roll.get()== "":
                messagebox.showerror('Error','Roll Number should be required',parent=self.root)
            else:
                cur.execute('select * from student where name=?', (self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error', 'Roll No. already exists', parent=self.root)
                else:
                    cur.execute('insert into student (roll,name,email,gender,dob,contact,admission,course,address) values(?,?,?,?,?,?,?,?,?)',(
                                            self.var_roll.get(),
                                            self.var_Name.get(),
                                            self.var_Email.get(),
                                            self.var_gender.get(),
                                            self.var_dob.get(),
                                            self.var_contact.get(),
                                            self.var_a_date.get(),
                                            self.var_course.get(),
                                            self.txt_Address.get('1.0',END)
                    ))
                    con.commit()
                    messagebox.showinfo('Success','Student added successfully',parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}')

    def update(self):
        con = sqlite3.connect(database='Pythonminiproject')
        cur = con.cursor()
        try:
            if self.var_roll.get()== "":
                messagebox.showerror('Error','Roll no should be required',parent=self.root)
            else:
                cur.execute('select * from student where roll=?', (self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Select student from list', parent=self.root)
                else:
                    cur.execute('update student set roll=?,name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,address=? where roll=?',(
                        self.var_Name.get(),
                        self.var_Email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.txt_Address.get('1.0', END),
                        self.var_roll.get()

                    ))
                    con.commit()
                    messagebox.showinfo('Success','Student updated successfully',parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}')


    def show(self):
        con = sqlite3.connect(database='Pythonminiproject')
        cur = con.cursor()
        try:
            cur.execute('select * from student ')
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row) #all the data in rows will form in a list

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}')

    def fetch_course(self):
        con = sqlite3.connect(database='Pythonminiproject')
        cur = con.cursor()
        try:
            cur.execute('select name from course ')
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}')

    def search(self):
        con = sqlite3.connect(database='Pythonminiproject')
        cur = con.cursor()
        try:
            cur.execute("select * from student where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:

                self.CourseTable.delete(*self.CourseTable.get_children())

                self.CourseTable.insert('',END,values=row) #all the data in rows will form in a list
            else:
                messagebox.showerror('Error','No record found',parent=self.root)

        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}')


if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop()
