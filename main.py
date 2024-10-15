from tkinter import *
from tkinter import ttk
from db import Database
from tkinter import messagebox

db=Database("Employee.db")

root=Tk()
root.title('Employee Management System')
root.geometry('1920x1080+0+0')
root.config(bg='#2c3e50')
root.state('zoomed')

name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()
address=StringVar()

#Entries frame
entries_frame=Frame(root,bg='#535c68')
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text='Employee Management System',font=('Calibri',18,'bold'),bg='#535c68',fg='white')
title.grid(row=0,columnspan=2,padx=10,pady=20,sticky='w')

lblname=Label(entries_frame,text='Name',font=('Calibri',16),bg='#535c68',fg='white')
lblname.grid(row=1,column=0,padx=10,pady=10,sticky='w')
txtName=Entry(entries_frame,textvariable=name,font=('Calibri',16))
txtName.grid(row=1,column=1,padx=10,pady=10,sticky='w')

lblage=Label(entries_frame,text='Age',font=('Calibri',16),bg='#535c68',fg='white')
lblage.grid(row=1,column=2,padx=10,pady=10,sticky='w')
txtAge=Entry(entries_frame,textvariable=age,font=('Calibri',16))
txtAge.grid(row=1,column=3,padx=10,pady=10,sticky='w')

lbldoj=Label(entries_frame,text='D.O.J',font=('Calibri',16),bg='#535c68',fg='white')
lbldoj.grid(row=2,column=0,padx=10,pady=10,sticky='w')
txtdoj=Entry(entries_frame,textvariable=doj,font=('Calibri',16))
txtdoj.grid(row=2,column=1,padx=10,pady=10,sticky='w')

lblemail=Label(entries_frame,text='Email',font=('Calibri',16),bg='#535c68',fg='white')
lblemail.grid(row=2,column=2,padx=10,pady=10,sticky='w')
txtEmail=Entry(entries_frame,textvariable=email,font=('Calibri',16))
txtEmail.grid(row=2,column=3,padx=10,pady=10,sticky='w')

lblgender=Label(entries_frame,text='Gender',font=('Calibri',16),bg='#535c68',fg='white')
lblgender.grid(row=3,column=0,padx=10,pady=10,sticky='w')
comboGender=ttk.Combobox(entries_frame,font=('Calibri',16),textvariable=gender,state='readonly')
comboGender['values']=('Male','Female')
comboGender.grid(row=3,column=1,padx=10,sticky='w')

lblcontact=Label(entries_frame,text='Contact No',font=('Calibri',16),bg='#535c68',fg='white')
lblcontact.grid(row=3,column=2,padx=10,pady=10,sticky='w')
txtContact=Entry(entries_frame,textvariable=contact,font=('Calibri',16))
txtContact.grid(row=3,column=3,padx=10,pady=10,sticky='w')

lbladdress=Label(entries_frame,text='Address',font=('Calibri',16),bg='#535c68',fg='white')
lbladdress.grid(row=4,column=0,padx=10,pady=10,sticky='w')

txtAddress=Text(entries_frame,width=85,height=5,font=('Calibri',16))
txtAddress.grid(row=5,column=0,columnspan=4,padx=10,pady=10,sticky='w')

def getdata(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data['values']
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])

def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def add_employee():
    if txtName.get()=='' or txtAge.get()=='' or txtdoj.get()=='' or txtEmail.get()=='' or comboGender.get()=='' or txtContact.get()=='' or txtAddress.get(1.0,END)=='':
        messagebox.showerror('Error in Input','Please fill all the details')
        return
    db.insert(txtName.get(),txtAge.get(),txtdoj.get(),txtEmail.get(),comboGender.get(),txtContact.get(),txtAddress.get(1.0,END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    displayall()
def del_employee():
    db.remove(row[0])
    messagebox.showinfo("Deleted", "Deleted Sucessfully")
    clearAll()
    displayall()
def edit_employee():
    if txtName.get() == '' or txtAge.get() == '' or txtdoj.get() == '' or txtEmail.get() == '' or comboGender.get() == '' or txtContact.get() == '' or txtAddress.get(
            1.0, END) == '':
        messagebox.showerror('Error in Input', 'Please fill all the details')
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtdoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
              txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Updated Sucessfully")
    clearAll()
    displayall()
def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0,END)





btn_frame=Frame(entries_frame,bg='#535c68')
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky='w')
btnAdd=Button(btn_frame,command=add_employee,text="Add",width=15,
              font=('Calibri',16,'bold'),bg='#16a085',fg='white',bd=0).grid(row=0,column=0,padx=10)


btndelete=Button(btn_frame,command=del_employee,text="Delete",width=15,
              font=('Calibri',16,'bold'),bg='#2980b9',fg='white',bd=0).grid(row=0,column=1,padx=10)


btnEdit=Button(btn_frame,command=edit_employee,text="Edit",width=15,
              font=('Calibri',16,'bold'),bg='#c0392b',fg='white',bd=0).grid(row=0,column=2,padx=10)


btnclear=Button(btn_frame,command=clearAll,text="Clear",width=15,
              font=('Calibri',16,'bold'),bg='#f39c12',fg='white',bd=0).grid(row=0,column=3,padx=10)

#table frame
tree_frame=Frame(root,bg='#ecf0f1')
tree_frame.place(x=0,y=500,width=1980,height=520)
style=ttk.Style()
style.configure('mystyle.Treeview',font=('Calibri',18),
                rowheight=50)
style.configure('mystyle.Treeview.Heading',font=('Calibri',18),
                rowheight=50)
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")

tv.heading('1',text='ID')
tv.column('1',width=5)
tv.heading('2',text='Name')
tv.heading('3',text='Age')
tv.column('3',width=5)
tv.heading('4',text='D.O.J')
tv.column('4',width=10)
tv.heading('5',text='Email')
tv.heading('6',text='Gender')
tv.column('6',width=10)
tv.heading('7',text='Contact')
tv.heading('8',text='Adress')
tv['show']='headings'
tv.bind('<ButtonRelease-1>',getdata)
tv.pack(fill=X)

displayall()
displayall()
root.mainloop()
