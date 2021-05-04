#!/usr/bin/env python
# coding: utf-8

# In[5]:


# import modules
from tkinter import *
import tkinter.messagebox
import sqlite3
from db import *


# create the class for front end ui(user interface)
class product:
# defult constructor  
    def __init__(self,root):  

        p = Database()
        p.conn()


        self.root=root 
        self.root.title("Sales purchase management system")
        self.root.geometry('1325x690')
        self.root.config(bg='grey')
# after creating the body to need to get the values thats why create the variables after then add the labels
        pId=StringVar()
        pName=StringVar()
        pPrice=StringVar()
        pQty=StringVar()
        pCompany=StringVar()
        pContact=StringVar()
#calls the method to perform database operation:-
# The function to close the main frame:-

        def close():
            print("product:close method called")
            close=tkinter.messagebox.askyesno("Sales purchase management system","Really.....Do you want to close the system")
            if close>0:
                root.destroy()
                print("product:close method finished\n")
                return  
# The function perform clear or reset
        def clear():
            print("product:clear method called")
            self.txtpID.delete(0,END)
            self.txtpName.delete(0,END)
            self.txtpPrice.delete(0,END)
            self.txtpQty.delete(0,END)
            self.txtpCompany.delete(0,END)
            self.txtpContact.delete(0,END)
            print("Product:clear method finished\n")
# insert function to save the data in database
        def insert():
            print("product:insert method called")
            if(len(pId.get())!=0):
                p.insert(pId.get(),pName.get(),pQty.get(),pPrice.get(),pCompany.get(),pContact.get())
                productList.delete(0,END)
                productList.insert(END,pId.get(),pName.get(),pQty.get(),pPrice.get(),pCompany.get(),pContact.get())
                showInProductList()
            else:
                tkinter.messagebox.askyesno("Sales purchase management system","Really.....Enter Product id")
            print("product:insert method finished\n")

        def showInProductList():
            print("Product:showInProductList method called")
            productList.delete(0,END)
            for row in p.show():
                productList.insert(END,row,str(""))
            print("product: showInProductList method finished\n")
        def productRec(event):
            print("product:porductRec method called")
            global pd
            searchPd = productList.curselection()[0]
            pd = productList.get(searchPd)

            self.txtpID.delete(0,END)
            self.txtpID.insert(END,pd[0])

            self.txtpName.delete(0,END)
            self.txtpName.insert(END,pd[1])

            self.txtpPrice.delete(0,END)
            self.txtpPrice.insert(END,pd[2])

            self.txtpQty.delete(0,END)
            self.txtpQty.insert(END,pd[3])

            self.txtpCompany.delete(0,END)
            self.txtpCompany.insert(END,pd[4])

            self.txtpContact.delete(0,END)
            self.txtpContact.insert(END,pd[5])

            print("product : productRec method finished\n")
        def delete():
            print("product:porductRec method called")
            if(len(pId.get())!=0):
                p.delete(pd[0])
                clear()
                showInProductList()
            print("product:porductRec method finished\n")
        def serach():
            print("product:search method called")
            productList.delete(0,END)
            for row in p.search(pId.get(),pName.get(),pQty.get(),pPrice.get(),pCompany.get(),pContact.get()):
                productList.insert(END,row,str(" "))
            print("product:search method finished\n")
        def update():
            print("product:search method called")
            if (len(pId.get())!=0):
                print(pd[0],pd[1])
                p.delete(pd[0])
            if (len(pId.get())!=0):
                p.insert(pId.get(),pName.get(),pQty.get(),pPrice.get(),pCompany.get(),pContact.get())
                productList.delete(0,END)
                productList.insert(END,(pId.get(),pName.get(),pQty.get(),pPrice.get(),pCompany.get(),pContact.get()))
            #p.update(pd[0],pName.get(),pQty.get(),pPrice.get(),pCompany.get(),pContact.get())
            print("product:update method finished")

# lets all the database methods to perform database operations
# create the title frame of project
        MainFrame=Frame(self.root,bg='Grey')
#grid() - grid allocates the rows and column forms        
        MainFrame.grid()
# Now i want to divide whole page into three parts
#create title frame calls the mainframe
#bd means border
        HeadFrame =Frame(MainFrame,bd=2,padx=50,pady=10,bg='#a7c5eb',relief=RIDGE)
#to put head head frame at the top
#then head frame is adding to the main frame
        HeadFrame.pack(side= TOP)
# here we add just title of project with decoration part menas fg four ground text color    
        self.ITitle = Label(HeadFrame,font=('arial',50,'bold'),fg='white',text = 'Sales purchase management system  ',bg='#413c69')  
        self.ITitle.grid()
#OperationFrame to perform the operation put it into mainframe
        OperationFrame = Frame(MainFrame,bd=1,width=1320,height=60,padx=50,pady=20,bg='#a7c5eb',relief=RIDGE)
        OperationFrame.pack(side=BOTTOM)
#Then we have to add the body frame below the in betn main and operational frame
        BodyFrame = Frame(MainFrame,bd=2,width=1290,height=400,padx=30,pady=20,bg='Tan',relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)
#The body frame contains the two body right body for slider and left for entry and labels
        LeftBodyFrame =LabelFrame(BodyFrame,bd=2,width=600,height=500,padx=20,pady=10,bg='#eaffd0',relief=RIDGE,font=('Cambria',15,'bold'),
                        text='Product Item details:')
        LeftBodyFrame.pack(side=LEFT)
        RightBodyFrame =LabelFrame(BodyFrame,bd=2,width=400,height=380,padx=20,pady=10,bg='#eaffd0',relief=RIDGE,font=('Cambria',15,'bold'),
                        text='Product Item details:')
        RightBodyFrame.pack(side=RIGHT)
#Add the labels and entry to the left body W-west aglin
        self.labelpID=Label(LeftBodyFrame,font=('Cambria',14,'bold'),text = "Product Id:-",padx=2,pady=2,bg='Tan',width=15)
        self.labelpID.grid(row=0,column=0,sticky=W)

        self.txtpID=Entry(LeftBodyFrame,font=('Cambria',12,'bold'),textvariable=pId,width=35)
        self.txtpID.grid(row=0,column=1,sticky=W)


        self.labelpName=Label(LeftBodyFrame,font=('Cambria',14,'bold'),text = "Product Name:-",padx=2,pady=2,bg='Tan',width=15)
        self.labelpName.grid(row=1,column=0,sticky=W)

        self.txtpName=Entry(LeftBodyFrame,font=('Cambria',12,'bold'),textvariable=pName,width=35)
        self.txtpName.grid(row=1,column=1,sticky=W)


        self.labelpPrice=Label(LeftBodyFrame,font=('Cambria',14,'bold'),text = "Product Price:-",padx=2,pady=2,bg='Tan',width=15)
        self.labelpPrice.grid(row=2,column=0,sticky=W)

        self.txtpPrice=Entry(LeftBodyFrame,font=('Cambria',12,'bold'),textvariable=pPrice,width=35)
        self.txtpPrice.grid(row=2,column=1,sticky=W)


        self.labelpQty=Label(LeftBodyFrame,font=('Cambria',14,'bold'),text = "Product Qty:-",padx=2,pady=2,bg='Tan',width=15)
        self.labelpQty.grid(row=3,column=0,sticky=W)

        self.txtpQty=Entry(LeftBodyFrame,font=('Cambria',12,'bold'),textvariable=pQty,width=35)
        self.txtpQty.grid(row=3,column=1,sticky=W)


        self.labelpCompany=Label(LeftBodyFrame,font=('Cambria',14,'bold'),text = "Product Company:-",padx=2,pady=2,bg='Tan',width=15)
        self.labelpCompany.grid(row=4,column=0,sticky=W)

        self.txtpCompany=Entry(LeftBodyFrame,font=('Cambria',12,'bold'),textvariable=pCompany,width=35)
        self.txtpCompany.grid(row=4,column=1,sticky=W)


        self.labelpContact=Label(LeftBodyFrame,font=('Cambria',14,'bold'),text = "Product Contact:-",padx=2,pady=2,bg='Tan',width=15)
        self.labelpContact.grid(row=5,column=0,sticky=W)

        self.txtpContact=Entry(LeftBodyFrame,font=('Cambria',12,'bold'),textvariable=pContact,width=35)
        self.txtpContact.grid(row=5,column=1,sticky=W)
# To add dummy spaces to equl both left and right frames
        self.labelpC1=Label(LeftBodyFrame,padx=2,pady=2)
        self.labelpC1.grid(row=6,column=0,sticky=W)

        self.labelpC2=Label(LeftBodyFrame,padx=2,pady=2)
        self.labelpC2.grid(row=7,column=0,sticky=W)

        self.labelpC3=Label(LeftBodyFrame,padx=2,pady=2)
        self.labelpC3.grid(row=8,column=0,sticky=W)

        self.labelpC4=Label(LeftBodyFrame,padx=2,pady=2)
        self.labelpC4.grid(row=9,column=0,sticky=W)

        self.labelpC5=Label(LeftBodyFrame,padx=2,pady=2)
        self.labelpC5.grid(row=10,column=0,sticky=W)

        self.labelpC6=Label(LeftBodyFrame,padx=2,pady=2)
        self.labelpC6.grid(row=11,column=0,sticky=W)



# adding the scroll bar to rightbosy frame
        scroll = Scrollbar(RightBodyFrame)
        scroll.grid(row=0,column=1,sticky='ns')

# To set the scroll bar to product where we show the details to show listbox like "Listbox"      
        productList=Listbox(RightBodyFrame,width=40,height=16,font=('Cambria',12,'bold'),yscrollcommand=scroll.set)
        productList.bind('<<ListboxSelect>>',productRec)          

#To set the scroll bar to list
        productList.grid(row=0,column=0,padx=8)
        scroll.config(command=productList.yview)
# Now we add the buttons on the operational frame
        self.buttonSaveData = Button(OperationFrame,text='Save',font=('arial',18,'bold'),height=1,width='10',bg='#eff0b6',bd=4,command=insert)
        self.buttonSaveData.grid(row=0,column=0)
# The button for showdata        
        self.buttonShowData = Button(OperationFrame,text='Show Data',font=('arial',18,'bold'),height=1,width='10',bg='#eff0b6',bd=4,command=showInProductList)
        self.buttonShowData .grid(row=0,column=1)
# The button for cleardata        
        self.buttonClearData = Button(OperationFrame,text='Reset',font=('arial',18,'bold'),height=1,width='10',bg='#eff0b6',bd=4,command=clear)
        self.buttonClearData.grid(row=0,column=2)
# The button for deletedata        
        self.buttonDeleteData= Button(OperationFrame,text='Delete',font=('arial',18,'bold'),height=1,width='10',bg='#eff0b6',bd=4,command=delete)
        self.buttonDeleteData.grid(row=0,column=3)
# The button for searchdata        
        self.buttonSearchData = Button(OperationFrame,text='Search',font=('arial',18,'bold'),height=1,width='10',bg='#eff0b6',bd=4,command=serach)
        self.buttonSearchData .grid(row=0,column=4)
# The button for updatedata        
        self.buttonUpdateData = Button(OperationFrame,text='Update',font=('arial',18,'bold'),height=1,width='10',bg='#eff0b6' ,bd=4,command=update)
        self.buttonUpdateData.grid(row=0,column=5)
# The button for closedata        
        self.buttonCloseData = Button(OperationFrame,text='Close',font=('arial',18,'bold'),height=1,width='10',bg='#eff0b6',bd=4,command=close)
        self.buttonCloseData.grid(row=0,column=6)
if __name__=='__main__':
    root=Tk()
application = product(root)
root.mainloop()


# In[3]:





# In[ ]:




