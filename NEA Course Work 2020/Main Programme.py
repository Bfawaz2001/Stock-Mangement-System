import os
import smtplib, ssl
import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
from tkinter import Tk, StringVar, ttk
from tkinter import Toplevel
import tkinter.ttk as tkrtk
import tkinter as tkr
import csv
from csv import writer
import re
from datetime import datetime
import sqlite3
from sqlite3 import Error
import Stock_Managemnt_Database_File

#-----------UserNames and Passwords File Creation--------------#

#with open('Users.csv', 'w') as Users:
    
    #filewriter = csv.writer(Users, delimiter=',')
    #filewriter.writerow(['Usernames', 'Passwords'])
    #filewriter.writerow(['Bfawaz1','Bones471'])
    #filewriter.writerow(['Samir007','h20medicine'])
    #filewriter.writerow(['Bettybo99','AQAcp2020'])
    #filewriter.writerow(['Paul101','123!Paul?321'])
    #filewriter.writerow(['ADMIN','100001'])
    
#-------------Identifying User Names to Passwords--------------#
# create list holders for our data.

User_Names = []
Passes = []

# open file
with open('Users.csv', 'r') as f:

    reader = csv.reader(f, delimiter=',', quotechar='"')
    # read file row by row
    
    rowNr = 0
    for row in reader:
        if len(row) < 1:
            continue
        # Skip the header row
        
        if rowNr >= 1:
            User_Names.append(row[0])
            Passes.append(row[1])

        # Increase the row number
        rowNr = rowNr + 1

# Print data

#Zipped_Lists = zip(User_Names,Passes)

#Users_and_Passwords = (list(Zipped_Lists))


#--------------------For Admins Eyes Only----------------------#
#def admin(self):
        #with open('Users.csv', 'r') as a:
           # reader = csv.reader(a)
            
            # read file row by row
            #for row in reader:
               # Reveal.append(row)

def append_NewUser_CSV(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

#------------------------------Main Loop------------------------------#

def main():
    global root
    root = Tk()
    app = Login(root)
    
#-----------------------------Login Window-----------------------------#    
class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("User Login Page")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg ='Salmon')
        self.frame = Frame(self.master, bg='Salmon')
        self.frame.pack()

        self.Input_UserName = StringVar()
        self.Input_Password = StringVar()

        self.lblTitle = Label(self.frame, text = 'Login Window', font =('arial', 60, 'bold'),
                             bg='Salmon', fg='Cornsilk')
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=20)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        self.LoginFrame1 = LabelFrame(self.frame, width=1350,height=300
                                      ,text="Login",font=('arial',20,'bold'), relief='ridge',bg='SlateBlue2', bd=40)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1000,height=200
                                      ,font=('arial',20,'bold'), relief='ridge',bg='SlateBlue2', bd=40)
        self.LoginFrame2.grid(row=2, column=0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Inputs Entries UserName & Password~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        self.lblInput_UserName = Label(self.LoginFrame1, text = 'Username', font =('arial',30,'bold'),bd=22,
                                 bg = 'SlateBlue2', fg = 'Cornsilk')
        self.lblInput_UserName.grid(row=0,column=0)

        self.txtInput_UserName = Entry(self.LoginFrame1,font=('arial',30,'bold'),bd=7,textvariable=self.Input_UserName,
                                 width = 33)
        self.txtInput_UserName.grid(row=0,column=1,padx=88)

        self.lblInput_Password = Label(self.LoginFrame1,text='Password',font=('arial',30,'bold'),bd=22,
                                 bg='SlateBlue2', fg = 'Cornsilk')
        self.lblInput_Password.grid(row=1,column=0)

        self.txtInput_Password = Entry(self.LoginFrame1, font =('arial',30,'bold'), show='*',bd=7,textvariable=self.Input_Password,
                                 width=33)
        self.txtInput_Password.grid(row=1,column=1,columnspan=2,pady=30)
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Buttons~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        self.btnLogin = Button(self.LoginFrame2, text='Login', width=15,font=('arial',30,'bold'),
                               bg='SlateBlue2', fg='Cornsilk', command=self.Check_Login)
        self.btnLogin.grid(row=3,column=0,pady=20,padx=8)

        self.btnReset = Button(self.LoginFrame2, text='Reset', width=15,font=('arial',30,'bold'),
                               bg='SlateBlue2', fg='Cornsilk', command=self.Reset_Com)
        self.btnReset.grid(row=3,column=1,pady=20,padx=8)

        self.btnExit = Button(self.LoginFrame2, text='Exit', width=15,font=('arial',30,'bold'),
                               bg='SlateBlue2', fg='Cornsilk', command=self.Exit_Com)
        self.btnExit.grid(row=3,column=2,pady=20,padx=8)             
                     

    def Check_Login(self):
        Key = False

        #Gets the username and password that has just been entered
        
        try_User = (self.Input_UserName.get())
        try_Pass = (self.Input_Password.get())
        
        #Checks against the data base to see if there is a matching one in the lists.
        while Key == False:
            if (try_User in User_Names) and (try_Pass in Passes) and (try_User != "") and (try_Pass != ""):
                username_index_position = User_Names.index(try_User)
                password_index_position = Passes.index(try_Pass)
                if username_index_position == password_index_position:
                    Key = True
                    if (try_User == "ADMIN") and (try_Pass == "100001"):
                        self.Admin_window()
                    else:
                        self.Main_window()
                    #Display LOGIN Sucessfull on a pop up window that disapears after 5 secs
                    #Also display on same window what user you are signed in with
                        
                else:
                    Key = False
                    messagebox.showerror("Invalid Login Details", "Something Went Wrong Please Try Again!")
                    self.Input_UserName.set("") #Resets Username and Password Boxes
                    self.Input_Password.set("")
                    return

            else:
                Key = False
                messagebox.showerror("Invalid Login Details", "Incorrect Login Details! Try Again!")
                self.Input_UserName.set("") #Resets Username and Password Boxes
                self.Input_Password.set("")
                return
               
    def Reset_Com(self):
        self.Input_UserName.set("")
        self.Input_Password.set("")

    def Exit_Com(self):
        self.Exit_Com = tkinter.messagebox.askyesno("*!Quit System!*", "Confirm Exit")
        if self.Exit_Com > 0:
            self.master.destroy()
            return
        else:
            return
        
    def Main_window(self):
        self.master.destroy()
        Tk().withdraw()
        self.Home_Win = Toplevel()
        self.app = Main_Window(self.Home_Win)
        
    def Admin_window(self):
        self.master.destroy()
        Tk().withdraw()
        self.Admin_Window = Toplevel()
        self.app = Admin(self.Admin_Window)



#--------------------------------------------------Main/Home Window----=---------------------------------#
#-----------------------------------------------------------------------=--------------------------------#
PIP = []
Brand_Name = []
Product_Discription = []
Quantity = []

OrderID = []
Order_PIP = []
Order_Quantity = []
Total_Cost = []
Dates = []

Suppliers_Names = []
    
class Main_Window:

#---------------------------------------------- Initialisation ----------------------------------------------------#

    def __init__(self, master):
        
        self.master = master
        self.master.title("Main Page")
        self.master.geometry("1350x800+0+0")
        self.master.config(bg ='Peach Puff')
        #self.main_frame = Frame(self.master, bg='Peach Puff')
        #self.main_frame.pack()

        #self.btnDestroy = Button(self.frame, text='Destroy Window', width=15,font=('arial',25,'bold'),
                               #bg='SlateBlue2', fg='Cornsilk', command=self.Destroy_Window)
        #self.btnDestroy.grid(row=3,column=0,pady=20,padx=8)

        #a = tkrtk.Style()
        #a.configure('TNotebook.Tab', font=('arial','38'), height = 10, foreground='green')

        style = tkrtk.Style()
        
        style.theme_create( "Main_Theme", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [10, 5, 10, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [130, 5], "background": "white" },
            "map":       {"background": [("selected", "red")],
                          "expand": [("selected", [1, 1, 1, 10])] } } } )

        style.theme_use("Main_Theme")

        Tabs = tkrtk.Notebook(self.master)

        Stock_Manage_Frame = Frame(Tabs, bg='Peach Puff', width=1350, height=400)
        global Search_Frame
        Search_Frame = Frame(Tabs, bg='plum2', width=200, height=200)
        Orders_Frame = Frame(Tabs, bg='Thistle2', width=200, height=200)
        Suppliers_Frame = Frame(Tabs, bg='dark orchid', width=200, height=200)

        Tabs.add(Stock_Manage_Frame, text="   Stock Managment   " )
        Tabs.add(Search_Frame, text="   Search   " )
        Tabs.add(Orders_Frame, text="   Orders   " )
        Tabs.add(Suppliers_Frame, text="   Suppliers   " )
        Tabs.pack(fill = "both", expand = 1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#------------------------------------------- Stock Management Tab -----------------------------------------------------#
        
#------------------------------------------------- Frames -------------------------------------------------------------#

        StockManage_Frame0 = Frame(Stock_Manage_Frame, width=1350, height=25, bg = "Peach Puff")
        StockManage_Frame0.grid(row = 0, column =0, pady = 10)
        
        StockManage_Frame1 = Frame(Stock_Manage_Frame, width=1350, height=25, bg = "Peach Puff")
        StockManage_Frame1.grid(row = 1, column =0, padx = 100, pady = 10)
        
        StockManage_Frame2 = Frame(Stock_Manage_Frame, width=1350, height=400, bg = "Peach Puff")
        StockManage_Frame2.grid(row = 2, column =0, padx = 100)

        StockManage_Frame3 = Frame(Stock_Manage_Frame, width=1350, height=200, bg = "Peach Puff")
        StockManage_Frame3.grid(row = 3, column =0)
    
#--------------------------------------- Labels, Entry Boxes, and Buttons ---------------------------------------------#
    
        StockManage_Title = Label(StockManage_Frame0, text = "Stock Management", font=('arial',25,'bold'), bd = 25, relief='ridge',
                                 bg = 'Peach Puff', fg = 'Black')
        StockManage_Title.grid(row=0,column=0)

        

        Order_By_Label = Label(StockManage_Frame1, text = "Orber By", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 bg = 'Peach Puff', fg = 'Black')
        Order_By_Label.grid(row=0,column=0, padx = 5)
        

        PIP_Nummber_Button = Button(StockManage_Frame1,text='PIP', width=5,font=('arial',15,'bold'), bd = 5, relief='ridge',
                               bg='SlateBlue2', fg='Cornsilk', command = self.Display_Stock_PIP)
        PIP_Nummber_Button.grid(row = 0, column = 1, padx = 5)
        
        
        Highest_Stock_Button = Button(StockManage_Frame1,text='Highest Stock Quantity', width=20,font=('arial',15,'bold'), bd = 5, relief='ridge',
                               bg='SlateBlue2', fg='Cornsilk', command = self.Display_Stock_From_Highest)
        Highest_Stock_Button.grid(row = 0, column = 2, padx = 5)
        

        Lowest_Stock_Button = Button(StockManage_Frame1,text='Lowest Stock Quantity', width=20,font=('arial',15,'bold'), bd = 5, relief='ridge',
                               bg='SlateBlue2', fg='Cornsilk', command = self.Display_Stock_From_Lowest)
        Lowest_Stock_Button.grid(row = 0, column = 3, padx = 5)
        

        Brand_Name_A2Z_Button = Button(StockManage_Frame1,text='Brand Name A to Z', width=15,font=('arial',15,'bold'), bd = 5, relief='ridge',
                               bg='SlateBlue2', fg='Cornsilk', command = self.Display_Stock_A2Z)
        Brand_Name_A2Z_Button.grid(row = 0, column = 4, padx = 5)
        

        Brand_Name_Z2A_Button = Button(StockManage_Frame1,text='Brand Name Z to A', width=15,font=('arial',15,'bold'), bd = 5, relief='ridge',
                               bg='SlateBlue2', fg='Cornsilk', command = self.Display_Stock_Z2A)
        Brand_Name_Z2A_Button.grid(row = 0, column = 5, padx = 5)

        
        Stock_PIP_Label = Label(StockManage_Frame2, text = "PIP", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 10, bg = 'Peach Puff', fg = 'Black')
        Stock_PIP_Label.grid(row=0,column=0)

        Brand_Label = Label(StockManage_Frame2, text = "Brand", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 15, bg = 'Peach Puff', fg = 'Black')
        Brand_Label.grid(row=0,column=1)
        
        Stock_Product_Name_Label = Label(StockManage_Frame2, text = "Product Discription", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 25, bg = 'Peach Puff', fg = 'Black')
        Stock_Product_Name_Label.grid(row=0,column=2)

        Stock_Quantity_Label = Label(StockManage_Frame2, text = "Quantity", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 8, bg = 'Peach Puff', fg = 'Black')
        Stock_Quantity_Label.grid(row=0,column=3)
        
        self.scrollbar_V = Scrollbar(StockManage_Frame2)
        self.scrollbar_H_PIP = Scrollbar(StockManage_Frame2, orient=HORIZONTAL)
        self.scrollbar_H_Brand_Name = Scrollbar(StockManage_Frame2, orient=HORIZONTAL)
        self.scrollbar_H_Product_Discription = Scrollbar(StockManage_Frame2, orient=HORIZONTAL)
        self.scrollbar_H_Quantity = Scrollbar(StockManage_Frame2, orient=HORIZONTAL)
        self.scrollbar_V.grid(row = 1, column = 4, sticky=N+S+W)
        self.scrollbar_H_PIP.grid(row = 2, column = 0, sticky=N+E+S+W)
        self.scrollbar_H_Brand_Name.grid(row = 2, column = 1, sticky=N+E+S+W)
        self.scrollbar_H_Product_Discription.grid(row = 2, column = 2, sticky=N+E+S+W)
        self.scrollbar_H_Quantity.grid(row = 2, column = 3, sticky=N+E+S+W)
        
        self.lbPIP = Listbox(StockManage_Frame2, font=('arial',12,'bold'), width = 10, height = 20, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_PIP.set)
        self.lbPIP.grid(row=1,column=0)
        
        self.lbBrand_Name = Listbox(StockManage_Frame2, font=('arial',12,'bold'), width = 15, height = 20, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Brand_Name.set)
        self.lbBrand_Name.grid(row=1,column=1)
        
        self.lbProduct_Discription = Listbox(StockManage_Frame2, font=('arial',12,'bold'), width = 25, height = 20, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Product_Discription.set)
        self.lbProduct_Discription.grid(row=1,column=2)

        self.lbQuantity = Listbox(StockManage_Frame2, font=('arial',12,'bold'), width = 8, height = 20, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Quantity.set)
        self.lbQuantity.grid(row=1,column=3)

        self.Display_Stock_PIP()

        self.scrollbar_V.config(command=self.yview)
        self.scrollbar_H_PIP.config(command=self.lbPIP.xview)
        self.scrollbar_H_Brand_Name.config(command=self.lbBrand_Name.xview)
        self.scrollbar_H_Product_Discription.config(command=self.lbProduct_Discription.xview)
        self.scrollbar_H_Quantity.config(command = self.lbQuantity.xview)


        Edit_Button = Button(StockManage_Frame3,text='Edit Stock Quantity', width=15,font=('arial',15,'bold'), bd =10, relief='ridge',
                               bg='SlateBlue2', fg='Cornsilk', command = self.edit_stock)
        Edit_Button.grid(row = 0, column = 1, padx = 10, pady = 20)

        AddNew_Button = Button(StockManage_Frame3,text='Add New Products', width=15,font=('arial',15,'bold'), bd = 10, relief='ridge',
                               bg='SlateBlue2', fg='Cornsilk', command = self.New_Product)
        AddNew_Button.grid(row = 0, column = 2, padx = 10, pady = 20)

        Product_Info_Button = Button(StockManage_Frame3,text='Product Info', width=15,font=('arial',15,'bold'), bd = 10, relief='ridge',
                               bg='SlateBlue2', fg='Cornsilk', command = self.Product_Info)
        Product_Info_Button.grid(row = 0, column = 3, padx = 10, pady = 20)

        Delete_Button = Button(StockManage_Frame3,text='Delete Product', width=15,font=('arial',15,'bold'), bd = 10, relief='ridge',
                               bg='SlateBlue2', fg='Cornsilk', command = self.Delete_Product)
        Delete_Button.grid(row = 0, column = 4, padx = 10, pady = 20)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#-------------------------------------------------- Search Tab --------------------------------------------------------#

        Search_Frame0 = Frame(Search_Frame, width=1350, height=30, bg = "plum2")
        Search_Frame0.grid(row = 0, column = 0, pady = 3)
        
        Search_Frame1 = Frame(Search_Frame, width=1350, height=50, bg = "plum2",bd = 20, relief='ridge')
        Search_Frame1.grid(row = 1, column =0, padx = 350, pady = 3)

#--------------------------------------- Labels, Entry Boxes, and Buttons ---------------------------------------------#

        Search_Title = Label(Search_Frame0, text = "Search", font=('arial',25,'bold'), width = 15, bd = 25, relief='ridge',
                                 bg = 'Maroon3', fg = 'White')
        Search_Title.grid(row=0,column=0)


        Search_Label = Label(Search_Frame1, text = "Search Bar", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 bg = 'Maroon3', fg = 'White')
        Search_Label.grid(row=0,column=0)

        global Search_Bar_Entry
        Search_Bar_Entry = StringVar()

        global Search_Bar
        Search_Bar = Entry(Search_Frame1, font=('arial',20,'bold'),bd=7,textvariable = Search_Bar_Entry, width = 25, relief='ridge')
        Search_Bar.grid(row=0,column=1)

        global Search_By_Menu
        Search_By_Menu = StringVar()
        Search_By_Menu.set("Search By")
        Search_Option = ["Use", "Supplier", "PIP", "Brand"]
        
        Search_By_DropDownMenu = OptionMenu(Search_Frame1, Search_By_Menu,*Search_Option)
        Search_By_DropDownMenu.grid(row=0,column=2, padx = 15)


        Search_Button = Button(Search_Frame1,text='Start Search', width=15,font=('arial',15,'bold'), bd = 10, relief='ridge',
                               bg='Maroon3', fg='White', command = self.Start_Search)
        Search_Button.grid(row = 1, column = 1, pady = 5)

        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#-------------------------------------------------- Orders Tab --------------------------------------------------------#

        OrderTabs = tkrtk.Notebook(Orders_Frame)

        Place_Order_Tab = Frame(OrderTabs, bg='hotpink1', width=1000, height=500)
        Order_History_Tab = Frame(OrderTabs, bg='indian red', width=1000, height=500)
        
        OrderTabs.add(Place_Order_Tab, text=" Place Order " )
        OrderTabs.add(Order_History_Tab, text="   Order History   " )
        OrderTabs.pack(fill = "both", expand = 1)
        
        #-------------------------------------------------- Place Orders Tab --------------------------------------------------------#
        #-------------------------------------------------------- Frames ------------------------------------------------------------#

        Place_Order_Frame0 = Frame(Place_Order_Tab, width = 1350, height=25, bg = "hotpink1")
        Place_Order_Frame0.grid(row = 0, column =0, pady = 10)
        
        Place_Order_Frame1 = Frame(Place_Order_Tab,width = 1350, height=25, bg = "hotpink1")
        Place_Order_Frame1.grid(row =1, column =0, pady = 10)
        
        Place_Order_Frame2 = Frame(Place_Order_Tab, width = 1350, height=25, bg = "hotpink1")
        Place_Order_Frame2.grid(row = 2, column =0)

        Place_Order_Frame3 = Frame(Place_Order_Tab, width = 1350, height=25, bg = "hotpink1")
        Place_Order_Frame3.grid(row = 3, column =0)
        
        #--------------------------------------------------------- List -------------------------------------------------------------#

        Brands = [""]
        Order_BrandID = [""]
        Order_Product_Discription = [""]
        Order_Supplier_Name = [""]
        Order_Supplier_Email = [""]

        #-------------------------------------------- Place Order Tab Functions -----------------------------------------------------#
        def List_Brands():
            
            con = sqlite3.connect("Stock_Management_Database.db")
            cur = con.cursor()
            cur.execute('SELECT Brand_Name FROM "Brands"')
            Brands_rows = cur.fetchall()
            
            rowNr = 0
            
            for row in Brands_rows:
                if len(row) < 1:
                    continue

                if rowNr >= 0:
                    Brands.append(row[0])

                rowNr = rowNr + 1

            global Order_Brand_Menu
            Order_Brand_Menu = StringVar()
            Order_Brand_Menu.set("Pick a Brand")

            Place_Order_Brand_Label = Label(Place_Order_Frame1, text = "Brand", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                     width = 10, bg = 'Thistle2', fg = 'Black')
            Place_Order_Brand_Label.grid(row=0,column=0)

            global Brand_Name_DropDownMenu
            Brand_Name_DropDownMenu = OptionMenu(Place_Order_Frame1, Order_Brand_Menu, *Brands)
            Brand_Name_DropDownMenu.grid(row=1,column=0)

            Pick_Choice = Button(Place_Order_Frame3,text='Confirm Brand', width=20,font=('arial',15,'bold'), bd =10, relief='ridge',
                               bg='Thistle2', fg='Black', command = BrandID)
            Pick_Choice.grid(row = 0, column = 0, pady = 10)
                
        def BrandID():

            if Order_Brand_Menu.get() == "Pick a Brand":
                messagebox.showerror("No Brand Selected", "Please Select a Brand and Try Again")
            else:
                    Order_BrandID.clear()

                    global Order_Brand_Name_chosen
                    Order_Brand_Name_chosen = Order_Brand_Menu.get()
                    
                    con = sqlite3.connect("Stock_Management_Database.db")
                    cur = con.cursor()
                    cur.execute('SELECT BrandID FROM "Brands" WHERE Brand_Name = (:Brand_Name_Selected)',
                                {
                                    "Brand_Name_Selected" : Order_Brand_Name_chosen
                                })
                    OrderID_rows = cur.fetchall()
                    
                    rowNr = 0
                    
                    for row in OrderID_rows:
                        if len(row) < 1:
                            continue

                        if rowNr >= 0:
                            Order_BrandID.append(row[0])

                        rowNr = rowNr + 1

                    global Order_BrandID_chosen
                    Order_BrandID_chosen = Order_BrandID[0]

                    List_Product_Discription()


        def List_Product_Discription():

            Order_Product_Discription.clear()
                
            con = sqlite3.connect("Stock_Management_Database.db")
            cur = con.cursor()
            cur.execute('SELECT Product_Discription FROM "Product_Info" WHERE BrandID = (:BrandID_Selected)',
                        {
                            "BrandID_Selected" : Order_BrandID_chosen
                        })
            Product_Discription_rows = cur.fetchall()
            
            rowNr = 0
            
            for row in Product_Discription_rows:
                if len(row) < 1:
                    continue

                if rowNr >= 0:
                    Order_Product_Discription.append(row[0])

                rowNr = rowNr + 1

            global Place_Order_Product_Discription_Label
            Place_Order_Product_Discription_Label = Label(Place_Order_Frame1, text = "Product Discription", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                     width = 15, bg = 'Thistle2', fg = 'Black')
            Place_Order_Product_Discription_Label.grid(row=0,column=1, padx = 10)

            global Product_Discription_Menu
            Product_Discription_Menu = StringVar()
            Product_Discription_Menu.set("Pick a Product")

            global Product_Discription_DropDownMenu
            Product_Discription_DropDownMenu = OptionMenu(Place_Order_Frame1, Product_Discription_Menu, *Order_Product_Discription)
            Product_Discription_DropDownMenu.grid(row=1,column=1, padx = 10)

            Pick_Choice = Button(Place_Order_Frame3,text='Confirm Product', width=20,font=('arial',15,'bold'), bd =10, relief='ridge',
                               bg='Thistle2', fg='Black', command = Enter_Quantity)
            Pick_Choice.grid(row = 0, column = 0, pady = 10)

            
        def Enter_Quantity():

            if Product_Discription_Menu.get() == "Pick a Product" or (len(Product_Discription_Menu.get()) < 1):
                 messagebox.showerror("No Product Selected", "Please Select a Product and Try Again")
            else:
                global Place_Order_Quantity_Label
                Place_Order_Quantity_Label = Label(Place_Order_Frame1, text = "Quantity", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                     width = 10, bg = 'Thistle2', fg = 'Black')
                Place_Order_Quantity_Label.grid(row=0,column=2, padx = 10)

                global Place_Order_Quantity
                Place_Order_Quantity = StringVar()

                global Place_Order_Quantity_Entry
                Place_Order_Quantity_Entry = Entry(Place_Order_Frame1, font=('arial',20,'bold'),bd=7,textvariable = Place_Order_Quantity, width = 5)
                Place_Order_Quantity_Entry.grid(row=1,column=2, padx = 10)

                Pick_Choice = Button(Place_Order_Frame3,text='Confirm Quantity', width=20,font=('arial',15,'bold'), bd =10, relief='ridge',
                               bg='Thistle2', fg='Black', command = Total_Cost_Calculated)
                Pick_Choice.grid(row = 0, column = 0, pady = 10)

        def Total_Cost_Calculated():

            Total_Cost = []

            try:
                global Order_Quantity_chosen
                Order_Quantity_chosen = int(Place_Order_Quantity.get())
            except ValueError:
                messagebox.showerror("Invalid Data Entered!", "Please enter an integer value for the quantity! Try Again!")
                Quantity_Entry.set("")
            
            if Order_Quantity_chosen < 1:
                 messagebox.showerror("No Quantity Entered!", "Please select a Quantity and Try Again")
            else:
                global Total_Cost_Label
                Total_Cost_Label = Label(Place_Order_Frame2, text = "Total Cost", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                         width = 10, bg = 'Thistle2', fg = 'Black')
                Total_Cost_Label.grid(row=0,column=0, padx = 10)

                global Order_Total_Cost
                Order_Total_Cost = Listbox(Place_Order_Frame2, font=('arial',12,'bold'), width = 15, height = 1, bd = 10)
                Order_Total_Cost.grid(row=1, column=0, padx = 600)
                

                global Order_Product_Discription_chosen
                Order_Product_Discription_chosen = Product_Discription_Menu.get()
                
                
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('SELECT Product_Cost FROM "Product_Info" WHERE BrandID = (:BrandID_Selected) AND Product_Discription = (:Product_Discription_Selected) ',
                            {
                                "BrandID_Selected" : Order_BrandID_chosen,
                                "Product_Discription_Selected" : Order_Product_Discription_chosen
                            })
                
                Total_Cost = cur.fetchone()

                
                Final_Total_Cost = ((Order_Quantity_chosen) * float(Total_Cost[0]))

                global Calculated_Cost
                Calculated_Cost = round(Final_Total_Cost, 2)

                Order_Total_Cost.insert(0, Calculated_Cost)

                global Place_Order_Choice
                Place_Order_Choice = Button(Place_Order_Frame3,text='Place Order', width=20,font=('arial',15,'bold'), bd =10, relief='ridge',
                               bg='Thistle2', fg='Black', command = Place_Order)
                Place_Order_Choice.grid(row = 0, column = 1, padx = 10, pady = 10)

                global Clear_Order
                Clear_Order = Button(Place_Order_Frame3,text='Clear Current Order', width=20,font=('arial',15,'bold'), bd =10, relief='ridge',
                                     bg='Thistle2', fg='Black', command = Clear_Current)
                Clear_Order.grid(row = 0, column = 2, pady = 10)

        def Clear_Current():

            Total_Cost_Label.destroy()
            Order_Total_Cost.destroy()

            Place_Order_Quantity_Label.destroy()
            Place_Order_Quantity_Entry.destroy()
             
            Place_Order_Product_Discription_Label.destroy()
            Product_Discription_DropDownMenu.destroy()

            Brand_Name_DropDownMenu.destroy()

            Place_Order_Choice.destroy()

            Clear_Order.destroy()

            List_Brands()

        def Place_Order():
            
            if (Order_Brand_Menu.get() == "Pick a Brand") and (Product_Discription_Menu.get() == "Pick a Proudct") or (len(Product_Discription_Menu.get()) < 1) and (Order_Quantity_chosen < 1):
                 messagebox.showerror("Data Missing!", "Please entered all data and Try Agan!")
            else:
                Place_Order_Brand = Order_Brand_Menu.get()
                Place_Order_Product = Product_Discription_Menu.get()
                Place_Order_Quantity_Ordered = Order_Quantity_chosen

                Current_DateTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('SELECT PIP FROM "Product_Info" WHERE BrandID = (:BrandID_Selected) AND Product_Discription = (:Product_Discription_Selected) ',
                            {
                                "BrandID_Selected" : Order_BrandID_chosen,
                                "Product_Discription_Selected" : Order_Product_Discription_chosen
                            })

                Place_Order_PIP_Fetched = cur.fetchone()
                con.close()

                Place_PIP = int(Place_Order_PIP_Fetched[0])

                #-------------------------------- Send Supplier Email -------------------------------#

                Order_Supplier_Name.clear()
                Order_Supplier_Email.clear()
                
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('SELECT Supply_Name, Email FROM "Product_Info","Supplier" WHERE PIP = (:Order_Supplier_PIP) AND Product_Info.SupplyID = Supplier.SupplyID',
                            {
                                "Order_Supplier_PIP" : Place_PIP
                            })
                OrderID_rows = cur.fetchall()
                
                rowNr = 0
            
                for row in OrderID_rows:
                    if len(row) < 1:
                        continue

                    if rowNr >= 0:
                        Order_Supplier_Name.append(row[0])
                        Order_Supplier_Email.append(row[1])

                    rowNr = rowNr + 1

                port = 465

                smtp_server = "smtp.gmail.com"
                sender_email = os.environ.get('Pharmacy_Email')
                receiver_email = str(Order_Supplier_Email[0])
                password = os.environ.get('Pharmacy_Password')

                
                Email_Message =("""From: Sam
To: %s
Subject: %s
To Whom It May Concern,

We would like to place an order to purchase %s packages of %s, %s. With PIP Code - %s.

Our details are as follows

Pharmacy Name - Supercare Pharmacy
Phone Number - xxxxxxxxxxx
Fax - xxxxxxxxxxxx
Address - xxxxx, xxx xxxxxx, xxx xxxx

Many Thanks
    Supercare Pharmacy

Sent via Python! 
"""%(receiver_email, Place_PIP, Place_Order_Quantity_Ordered, Order_Brand_Name_chosen, Order_Product_Discription_chosen, Place_PIP))


                try:
                   context = ssl.create_default_context()
                   with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                      server.login(sender_email, password)
                      server.sendmail(sender_email, receiver_email, Email_Message)
                   messagebox.showinfo("Email","Successfully sent email to %s, %s"%(Order_Supplier_Email[0],Order_Supplier_Name[0]))  
                except Exception:  
                   messagebox.showerror("Email Error!","Error: unable to send email")  

                #------------------------------------------------------------------------------------#
                
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('INSERT INTO "Place_Order"(PIP,Order_Quantity,Total_Cost,Date_Placed) VALUES (:Order_Place_PIP_Selected, :Order_Place_Order_Quantity_Selected, :Order_Place_Total_Cost, :Order_Place_DateTime)',
                            {
                                "Order_Place_PIP_Selected" : Place_PIP,
                                "Order_Place_Order_Quantity_Selected" : Place_Order_Quantity_Ordered,
                                "Order_Place_Total_Cost" : Calculated_Cost,
                                "Order_Place_DateTime" : Current_DateTime
                            })
                con.commit()
                con.close()

                
                messagebox.showinfo("New Order Placed!", "A new order has been placed sucessfully!")
                
                Order_Brand_Menu.set("Pick a Brand")

                #----------- Reset ---------#
                
                Clear_Current()


        #------------------------------------------- Labels, Entry Boxes, and Buttons -----------------------------------------------#
        
        Place_Order_Title = Label(Place_Order_Frame0, text = "Place Order", font=('arial',25,'bold'), bd = 25, relief='ridge',
                                 bg = 'Thistle2', fg = 'Black')
        Place_Order_Title.grid(row=0,column=0, pady = 50)

        List_Brands()

        #-------------------------------------------------- Orders History Tab ------------------------------------------------------#
        #-------------------------------------------------------- Frames ------------------------------------------------------------#


        Order_History_Frame0 = Frame(Order_History_Tab, width=1350, height=25, bg = "indian red")
        Order_History_Frame0.grid(row = 0, column =0, pady = 5)
        
        Order_History_Frame1 = Frame(Order_History_Tab, width=1350, height=25, bg = "indian red")
        Order_History_Frame1.grid(row = 1, column =0, padx = 200, pady = 5)
        
        Order_History_Frame2 = Frame(Order_History_Tab, width=1350, height=400, bg = "indian red")
        Order_History_Frame2.grid(row = 2, column =0, padx = 200, pady = 5)

        Order_History_Frame3 = Frame(Order_History_Tab, width=1350, height=200, bg = "indian red")
        Order_History_Frame3.grid(row = 3, column =0, pady = 5)

        #------------------------------------------- Labels, Entry Boxes, and Buttons -----------------------------------------------#

        Order_History_Title = Label(Order_History_Frame0, text = "Order History", font=('arial',25,'bold'), bd = 25, relief='ridge',
                                 bg = 'gold', fg = 'Black')
        Order_History_Title.grid(row=0,column=0)

        

        Sort_By_Label = Label(Order_History_Frame1, text = "Sort By", font=('arial',15,'bold'), width = 15, bd = 10, relief='ridge',
                                 bg = 'indian red', fg = 'White')
        Sort_By_Label.grid(row=0,column=0, padx = 5)
        

        Newest_Sort_Button = Button(Order_History_Frame1,text='Newest', width=10,font=('arial',15,'bold'), bd = 5, relief='ridge',
                               bg='gold', fg='Black', command = self.Display_Newest)
        Newest_Sort_Button.grid(row = 0, column = 1, padx = 5)
        
        
        Oldest_Sort_Button = Button(Order_History_Frame1,text='Oldest', width=10,font=('arial',15,'bold'), bd = 5, relief='ridge',
                               bg='gold', fg='Black', command = self.Display_Oldest)
        Oldest_Sort_Button.grid(row = 0, column = 2, padx = 5)
        

        
        OrderID_Label = Label(Order_History_Frame2, text = "OrderID", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 10, bg = 'gold', fg = 'Black')
        OrderID_Label.grid(row=0,column=0)

        Order_PIP_Label = Label(Order_History_Frame2, text = "PIP", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 10, bg = 'gold', fg = 'Black')
        Order_PIP_Label.grid(row=0,column=1)
        
        Order_Quantity_Label = Label(Order_History_Frame2, text = "Order Quantity", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 15, bg = 'gold', fg = 'Black')
        Order_Quantity_Label.grid(row=0,column=2)

        Order_Total_Cost_Label = Label(Order_History_Frame2, text = "Order Cost", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 10, bg = 'gold', fg = 'Black')
        Order_Total_Cost_Label.grid(row=0,column=3)

        Order_Date_Label = Label(Order_History_Frame2, text = "Date & Time", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 25, bg = 'gold', fg = 'Black')
        Order_Date_Label.grid(row=0,column=4)
        
        self.scrollbar_V = Scrollbar(Order_History_Frame2)
        self.scrollbar_H_OrderID = Scrollbar(Order_History_Frame2, orient=HORIZONTAL)
        self.scrollbar_H_Order_PIP = Scrollbar(Order_History_Frame2, orient=HORIZONTAL)
        self.scrollbar_H_Order_Quantity = Scrollbar(Order_History_Frame2, orient=HORIZONTAL)
        self.scrollbar_H_Total_Cost = Scrollbar(Order_History_Frame2, orient=HORIZONTAL)
        self.scrollbar_H_Date = Scrollbar(Order_History_Frame2, orient=HORIZONTAL)
        self.scrollbar_V.grid(row = 1, column = 5, sticky=N+S+W)
        self.scrollbar_H_OrderID.grid(row = 2, column = 0, sticky=N+E+S+W)
        self.scrollbar_H_Order_PIP.grid(row = 2, column = 1, sticky=N+E+S+W)
        self.scrollbar_H_Order_Quantity.grid(row = 2, column = 2, sticky=N+E+S+W)
        self.scrollbar_H_Total_Cost.grid(row = 2, column = 3, sticky=N+E+S+W)
        self.scrollbar_H_Date.grid(row = 2, column = 4, sticky=N+E+S+W)
        
        
        self.lbOrderID = Listbox(Order_History_Frame2, font=('arial',12,'bold'), width = 5, height = 20, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_OrderID.set)
        self.lbOrderID.grid(row=1,column=0)
        
        self.lbOrder_PIP = Listbox(Order_History_Frame2, font=('arial',12,'bold'), width = 10, height = 20, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Order_PIP.set)
        self.lbOrder_PIP.grid(row=1,column=1)
        
        self.lbOrder_Quantity = Listbox(Order_History_Frame2, font=('arial',12,'bold'), width = 15, height = 20, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Order_Quantity.set)
        self.lbOrder_Quantity.grid(row=1,column=2)

        self.lbTotal_Cost = Listbox(Order_History_Frame2, font=('arial',12,'bold'), width = 10, height = 20, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Total_Cost.set)
        self.lbTotal_Cost.grid(row=1,column=3)

        self.lbDate = Listbox(Order_History_Frame2, font=('arial',12,'bold'), width = 20, height = 20, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Date.set)
        self.lbDate.grid(row=1,column=4)
        

        self.Display_Newest()


        self.scrollbar_V.config(command=self.yview)
        self.scrollbar_H_OrderID.config(command=self.lbOrderID.xview)
        self.scrollbar_H_Order_PIP.config(command=self.lbOrder_PIP.xview)
        self.scrollbar_H_Order_Quantity.config(command=self.lbOrder_Quantity.xview)
        self.scrollbar_H_Total_Cost.config(command = self.lbTotal_Cost.xview)
        self.scrollbar_H_Date.config(command = self.lbDate.xview)


        Edit_Button = Button(Order_History_Frame3,text='Show Order Information', width=20,font=('arial',15,'bold'), bd =10, relief='ridge',
                               bg='gold', fg='Black', command = self.Show_Order_Info)
        Edit_Button.grid(row = 0, column = 2, padx = 10, pady = 10)

        Cancel_Order_Button = Button(Order_History_Frame3,text='Cancel Order', width=20,font=('arial',15,'bold'), bd =10, relief='ridge',
                               bg='gold', fg='Black', command = self.Delete_Order)
        Cancel_Order_Button.grid(row = 0, column = 3, padx = 10, pady = 10)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#------------------------------------------------- Suppliers Tab ------------------------------------------------------#

#----------------------------------------------------- Frames ---------------------------------------------------------#

        Suppliers_Frame0 = Frame(Suppliers_Frame, width=150, height=25, bg = "dark orchid")
        Suppliers_Frame0.grid(row = 0, column = 0, pady = 35)

        Suppliers_Frame1 = Frame(Suppliers_Frame, width=150, height=25, bg = "dark orchid")
        Suppliers_Frame1.grid(row = 1, column = 0, padx = 35, pady = 5)

        Suppliers_Frame2 = Frame(Suppliers_Frame, width=150, height=25, bg = "dark orchid")
        Suppliers_Frame2.grid(row = 2, column = 0, padx = 35, pady = 5)
        
        Suppliers_Frame3 = Frame(Suppliers_Frame, width=100, height=25, bg = "dark orchid")
        Suppliers_Frame3.grid(row = 0, column = 1, pady = 10)
                
        Suppliers_Frame4 = Frame(Suppliers_Frame, width=100, height=50, bg = "dark orchid")
        Suppliers_Frame4.grid(row = 1, column = 1, padx = 35, pady = 5)

        Suppliers_Frame5 = Frame(Suppliers_Frame, width=500, height=25, bg = "dark orchid")
        Suppliers_Frame5.grid(row = 0, column = 2, padx = 35, pady = 5)

        Suppliers_Frame6 = Frame(Suppliers_Frame, width=500, height=25, bg = "dark orchid")
        Suppliers_Frame6.grid(row = 1, column = 2, padx = 35, pady = 5)

        Suppliers_Frame7 = Frame(Suppliers_Frame, width=500, height=25, bg = "dark orchid")
        Suppliers_Frame7.grid(row = 2, column = 2, padx = 35, pady = 5)


#--------------------------------------- Labels, Entry Boxes, and Buttons ---------------------------------------------#

        Suppliers_Information_Title = Label(Suppliers_Frame0, text = "Supplier Information", font=('arial',25,'bold'), bd = 20, relief='ridge',
                                 bg = 'Cadet Blue', fg = 'Black')
        Suppliers_Information_Title.grid(row=0,column=0)
        

        Chosen_Suppliers_Name_Label = Label(Suppliers_Frame1, text = "Supplier Name", font=('arial',15,'bold'), width = 15, bd = 15, relief='ridge',
                                 bg = 'Cadet Blue', fg = 'Black')
        Chosen_Suppliers_Name_Label.grid(row = 0,column=0, padx = 5)

        Chosen_Suppliers_Phone_Label = Label(Suppliers_Frame1, text = "Phone Number", font=('arial',15,'bold'), width = 15, bd = 15, relief='ridge',
                                 bg = 'Cadet Blue', fg = 'Black')
        Chosen_Suppliers_Phone_Label.grid(row = 2,column=0, padx = 5)

        Choesen_Suppliers_Email_Label = Label(Suppliers_Frame1, text = "Email", font=('arial',15,'bold'), width = 20, bd = 15, relief='ridge',
                                 bg = 'Cadet Blue', fg = 'Black')
        Choesen_Suppliers_Email_Label.grid(row = 4,column=0, padx = 5)

        Chosen_Suppliers_Address_Label = Label(Suppliers_Frame1, text = "Address", font=('arial',15,'bold'), width = 20, bd = 15, relief='ridge',
                                 bg = 'Cadet Blue', fg = 'Black')
        Chosen_Suppliers_Address_Label.grid(row = 6,column=0, padx = 5)


        global Chosen_Suppliers_Name_Display
        global Chosen_Suppliers_Phone_Display
        global Choesen_Suppliers_Email_Display
        global Chosen_Suppliers_Address_Display
        

        Chosen_Suppliers_Name_Display = Listbox(Suppliers_Frame1, font=('arial',15,'bold'), width = 20, height = 1, bd = 10, relief='ridge',
                                 bg = 'White', fg = 'Black')
        Chosen_Suppliers_Name_Display.grid(row = 1,column=0, padx = 5, pady = 10)

        Chosen_Suppliers_Phone_Display = Listbox(Suppliers_Frame1, font=('arial',15,'bold'), width = 15, height = 1, bd = 10, relief='ridge',
                                 bg = 'White', fg = 'Black')
        Chosen_Suppliers_Phone_Display.grid(row = 3,column=0, padx = 5, pady = 10)

        Choesen_Suppliers_Email_Display = Listbox(Suppliers_Frame1, font=('arial',15,'bold'), width = 25, height = 1, bd = 10, relief='ridge',
                                 bg = 'White', fg = 'Black')
        Choesen_Suppliers_Email_Display.grid(row = 5,column=0, padx = 5, pady = 10)

        Chosen_Suppliers_Address_Display = Listbox(Suppliers_Frame1, font=('arial',15,'bold'), width = 30, height = 1, bd = 10,relief='ridge',
                                 bg = 'White', fg = 'Black')
        Chosen_Suppliers_Address_Display.grid(row = 7,column=0, padx = 5, pady = 10)


        Display_Suppliers_Informaton_Button = Button(Suppliers_Frame2,text='Display Supplier Information', width=25,font=('arial',20,'bold'), bd =10, relief='ridge',
                               bg='Cadet Blue', fg='Cornsilk', command = self.Supplier_Details)
        Display_Suppliers_Informaton_Button.grid(row = 0, column = 0)



        def Display_Suppliers_Name():
         
            Suppliers_Names.clear()
            
            self.Suppliers_Listbox.delete(0, END)
            
            con = sqlite3.connect("Stock_Management_Database.db")
            cur = con.cursor()
            cur.execute('SELECT Supply_Name FROM "Supplier"')
            rows = cur.fetchall()
            con.close()
            
            rowNr = 0
            
            for row in rows:
                if len(row) < 1:
                    continue

                if rowNr >= 0:
                    Suppliers_Names.append(row[0])
                rowNr = rowNr + 1

            self.Suppliers_Listbox.insert("end", *Suppliers_Names)

            

        Suppliers_Title = Label(Suppliers_Frame3, text = "List Of Suppliers", font=('arial',25,'bold'), bd = 25, relief='ridge',
                                 bg = 'Cadet Blue', fg = 'Black')
        Suppliers_Title.grid(row=0,column=0)

        Suppliers_Name_Label = Label(Suppliers_Frame4, text = "Suppliers", font=('arial',25,'bold'), bd = 25, relief='ridge',
                                 bg = 'Cadet Blue', fg = 'Black')
        Suppliers_Name_Label.grid(row = 0,column=0)

        scrollbar_V = Scrollbar(Suppliers_Frame4)
        scrollbar_H_Suppliers = Scrollbar(Suppliers_Frame4, orient=HORIZONTAL)
        scrollbar_V.grid(row = 1, column = 1, sticky=N+S+W)
        scrollbar_H_Suppliers.grid(row = 2, column = 0, sticky=N+E+S+W)

        
        self.Suppliers_Listbox = Listbox(Suppliers_Frame4, font=('arial',15,'bold'), width = 25
                                         , height = 15, bg ='Cadet Blue', bd = 10, yscrollcommand=scrollbar_V.set, xscrollcommand=scrollbar_H_Suppliers.set)
        self.Suppliers_Listbox.grid(row=1,column=0,pady = 5)
        scrollbar_V.config(command=self.Suppliers_Listbox.yview)
        scrollbar_H_Suppliers.config(command=self.Suppliers_Listbox.xview)


        Display_Suppliers_Name()


        Add_New_Supplier_Title = Label(Suppliers_Frame5, text = "Add New Supplier", font=('arial',25,'bold'), bd = 25, relief='ridge',
                                 bg = 'Cadet Blue', fg = 'Black')
        Add_New_Supplier_Title.grid(row = 2,column=0, padx = 5)
        

        Add_Suppliers_Name_Label = Label(Suppliers_Frame6, text = "Supplier Name", font=('arial',15,'bold'), width = 15, bd = 15, relief='ridge',
                                 bg = 'Cadet Blue', fg = 'Black')
        Add_Suppliers_Name_Label.grid(row = 0,column=0, padx = 5)

        Add_Suppliers_Phone_Label = Label(Suppliers_Frame6, text = "Phone Number", font=('arial',15,'bold'), width = 15, bd = 15, relief='ridge',
                                 bg = 'Cadet Blue', fg = 'Black')
        Add_Suppliers_Phone_Label.grid(row = 2,column=0, padx = 5)

        Add_Suppliers_Email_Label = Label(Suppliers_Frame6, text = "Email", font=('arial',15,'bold'), width = 20, bd = 15, relief='ridge',
                                 bg = 'Cadet Blue', fg = 'Black')
        Add_Suppliers_Email_Label.grid(row = 4,column=0, padx = 5)

        Add_Suppliers_Address_Label = Label(Suppliers_Frame6, text = "Address", font=('arial',15,'bold'), width = 20, bd = 15, relief='ridge',
                                 bg = 'Cadet Blue', fg = 'Black')
        Add_Suppliers_Address_Label.grid(row = 6,column=0, padx = 5)


        global Add_Suppliers_Name
        global Add_Suppliers_Phone
        global Add_Suppliers_Email
        global Add_Suppliers_Address

        global Supplier_Name_Entered 
        global Phone_Entered
        global Email_Entered
        global Address_Entered

        Supplier_Name_Entered = StringVar()
        Phone_Entered = StringVar()
        Email_Entered = StringVar()
        Address_Entered = StringVar()
        

        Add_Suppliers_Name = Entry(Suppliers_Frame6, font=('arial',15,'bold'), textvariable = Supplier_Name_Entered, width = 20, bd = 10, relief='ridge',
                                 bg = 'White', fg = 'Black')
        Add_Suppliers_Name.grid(row = 1,column=0, padx = 5, pady = 10)

        Add_Suppliers_Phone = Entry(Suppliers_Frame6, font=('arial',15,'bold'), textvariable = Phone_Entered, width = 15, bd = 10, relief='ridge',
                                 bg = 'White', fg = 'Black')
        Add_Suppliers_Phone.grid(row = 3,column=0, padx = 5, pady = 10)

        Add_Suppliers_Email = Entry(Suppliers_Frame6, font=('arial',15,'bold'), textvariable = Email_Entered, width = 25, bd = 10, relief='ridge',
                                 bg = 'White', fg = 'Black')
        Add_Suppliers_Email.grid(row = 5,column=0, padx = 5, pady = 10)

        Add_Suppliers_Address = Entry(Suppliers_Frame6, font=('arial',15,'bold'), textvariable = Address_Entered, width = 30, bd = 10,relief='ridge',
                                 bg = 'White', fg = 'Black')
        Add_Suppliers_Address.grid(row = 7,column=0, padx = 5, pady = 10)
        

        Add_New_Supplier_Button = Button(Suppliers_Frame7,text='Add New Supplier', width=20,font=('arial',20,'bold'), bd =10, relief='ridge',
                               bg='Cadet Blue', fg='Cornsilk', command = self.Add_New_Supplier)
        Add_New_Supplier_Button.grid(row = 0, column = 0)
        
#--------------------------------------------------- Functions --------------------------------------------------------#
#------------------------------------------ Stock Management Tab Functions --------------------------------------------#

    def Clear_List(self):
        self.lbPIP.delete(0, END)
        self.lbBrand_Name.delete(0, END)
        self.lbProduct_Discription.delete(0, END)
        self.lbQuantity.delete(0, END)


    def Display_Stock_PIP(self):
        
        PIP.clear()
        Brand_Name.clear()
        Product_Discription.clear()
        Quantity.clear()

        self.Clear_List()
        
        con = sqlite3.connect("Stock_Management_Database.db")
        cur = con.cursor()
        cur.execute('SELECT PIP, Brand_Name, Product_Discription, Quantity FROM "Product_Info", "Brands" WHERE Product_Info.BrandID = Brands.BrandID')
        rows = cur.fetchall()
        con.close()
        
        rowNr = 0
        
        for row in rows:
            if len(row) < 1:
                continue

            if rowNr >= 0:
                PIP.append(row[0])
                Brand_Name.append(row[1])
                Product_Discription.append(row[2])
                Quantity.append(row[3])

            rowNr = rowNr + 1
            

        self.lbPIP.insert("end", *PIP)
        self.lbBrand_Name.insert("end", *Brand_Name)
        self.lbProduct_Discription.insert("end", *Product_Discription)
        self.lbQuantity.insert("end", *Quantity)

    def Display_Stock_From_Lowest(self):
        
        PIP.clear()
        Brand_Name.clear()
        Product_Discription.clear()
        Quantity.clear()
        
        self.Clear_List()
        
        con = sqlite3.connect("Stock_Management_Database.db")
        cur = con.cursor()
        cur.execute('SELECT PIP, Brand_Name, Product_Discription, Quantity FROM "Product_Info", "Brands" WHERE Product_Info.BrandID = Brands.BrandID ORDER BY Quantity')
        rows = cur.fetchall()
        con.close()
        
        rowNr = 0
        
        for row in rows:
            if len(row) < 1:
                continue

            if rowNr >= 0:
                PIP.append(row[0])
                Brand_Name.append(row[1])
                Product_Discription.append(row[2])
                Quantity.append(row[3])

            rowNr = rowNr + 1

        self.lbPIP.insert("end", *PIP)
        self.lbBrand_Name.insert("end", *Brand_Name)
        self.lbProduct_Discription.insert("end", *Product_Discription)
        self.lbQuantity.insert("end", *Quantity)

    def Display_Stock_From_Highest (self):

        PIP.clear()
        Brand_Name.clear()
        Product_Discription.clear()
        Quantity.clear()
        
        self.Clear_List()
        
        con = sqlite3.connect("Stock_Management_Database.db")
        cur = con.cursor()
        cur.execute('SELECT PIP, Brand_Name, Product_Discription, Quantity FROM "Product_Info", "Brands" WHERE Product_Info.BrandID = Brands.BrandID ORDER BY Quantity desc')
        rows = cur.fetchall()
        con.close()
        
        rowNr = 0
        
        for row in rows:
            if len(row) < 1:
                continue

            if rowNr >= 0:
                PIP.append(row[0])
                Brand_Name.append(row[1])
                Product_Discription.append(row[2])
                Quantity.append(row[3])

            rowNr = rowNr + 1

        self.lbPIP.insert("end", *PIP)
        self.lbBrand_Name.insert("end", *Brand_Name)
        self.lbProduct_Discription.insert("end", *Product_Discription)
        self.lbQuantity.insert("end", *Quantity)

    def Display_Stock_A2Z(self):

        PIP.clear()
        Brand_Name.clear()
        Product_Discription.clear()
        Quantity.clear()

        self.Clear_List()
        
        con = sqlite3.connect("Stock_Management_Database.db")
        cur = con.cursor()
        cur.execute('SELECT PIP, Brand_Name, Product_Discription, Quantity FROM "Product_Info", "Brands" WHERE Product_Info.BrandID = Brands.BrandID ORDER BY Brand_Name')
        rows = cur.fetchall()
        con.close()
        
        rowNr = 0
        
        for row in rows:
            if len(row) < 1:
                continue

            if rowNr >= 0:
                PIP.append(row[0])
                Brand_Name.append(row[1])
                Product_Discription.append(row[2])
                Quantity.append(row[3])

            rowNr = rowNr + 1

        self.lbPIP.insert("end", *PIP)
        self.lbBrand_Name.insert("end", *Brand_Name)
        self.lbProduct_Discription.insert("end", *Product_Discription)
        self.lbQuantity.insert("end", *Quantity)

    def Display_Stock_Z2A(self):
        
        PIP.clear()
        Brand_Name.clear()
        Product_Discription.clear()
        Quantity.clear()
        
        self.Clear_List()
        
        con = sqlite3.connect("Stock_Management_Database.db")
        cur = con.cursor()
        cur.execute('SELECT PIP, Brand_Name, Product_Discription, Quantity FROM "Product_Info", "Brands" WHERE Product_Info.BrandID = Brands.BrandID ORDER BY Brand_Name desc')
        rows = cur.fetchall()
        con.close()
        
        rowNr = 0
        
        for row in rows:
            if len(row) < 1:
                continue

            if rowNr >= 0:
                PIP.append(row[0])
                Brand_Name.append(row[1])
                Product_Discription.append(row[2])
                Quantity.append(row[3])

            rowNr = rowNr + 1

        self.lbPIP.insert("end", *PIP)
        self.lbBrand_Name.insert("end", *Brand_Name)
        self.lbProduct_Discription.insert("end", *Product_Discription)
        self.lbQuantity.insert("end", *Quantity)
        
    def edit_stock(self):
        
        PIP.clear()
        Brand_Name.clear()
        Product_Discription.clear()
        Quantity.clear()
        
        try:
            PIP_chosen = self.lbPIP.get(self.lbPIP.curselection())
        except Exception:
             messagebox.showerror("No Product Chosen!", "Please select a PIP number and try again!")

        else:
            Edit_Quantity_Window = Toplevel()
            Edit_Quantity_Window.geometry("795x225")
            Edit_Quantity_Window.config(bg ='MediumOrchid2')

            Frame1 = Frame(Edit_Quantity_Window, bg = 'MediumOrchid2')
            Frame1.grid(row = 0, column = 0)

            Frame2 = Frame(Edit_Quantity_Window, bg = 'MediumOrchid2')
            Frame2.grid(row = 1, column = 0)

            Quantity_Label = Label(Frame1, text = "Enter Quantity", font =('arial',30,'bold'),bd=20, relief='ridge',
                                     bg = 'SlateBlue2', fg = 'Cornsilk')
            Quantity_Label.grid(row = 0 , column = 0)

            Quantity_Entry = StringVar()
            
            New_Quantity = Entry(Frame1, font =('arial',30,'bold'),bd=20, relief='ridge', textvariable = Quantity_Entry,
                                 bg = 'SlateBlue2', fg = 'Cornsilk')
            New_Quantity.grid(row = 0 , column = 1)

            def Update_Quantity():

                try:
                    Quantity_Entered = int(New_Quantity.get())
                except ValueError:
                    messagebox.showerror("Invalid Data Entered!", "Please enter an integer value for the quantity! Try Again!")
                    Quantity_Entry.set("")
                        
                    
                if (Quantity_Entered > -1) and (type(Quantity_Entered) == int):
                    con = sqlite3.connect("Stock_Management_Database.db")
                    cur = con.cursor()
                    cur = con.execute('UPDATE "Product_Info" SET Quantity=? WHERE PIP=?',\
                                      (Quantity_Entered, PIP_chosen))
                    con.commit()
                    con.close()

                    Edit_Quantity_Window.destroy()

                    self.Clear_List()
                    
                    con = sqlite3.connect("Stock_Management_Database.db")
                    cur = con.cursor()
                    cur.execute('SELECT PIP, Brand_Name, Product_Discription, Quantity FROM "Product_Info", "Brands" WHERE Product_Info.BrandID = Brands.BrandID')
                    rows = cur.fetchall()
                    con.close()
                    
                    rowNr = 0
                    
                    for row in rows:
                        if len(row) < 1:
                            continue

                        if rowNr >= 0:
                            PIP.append(row[0])
                            Brand_Name.append(row[1])
                            Product_Discription.append(row[2])
                            Quantity.append(row[3])

                        rowNr = rowNr + 1
                        

                    self.lbPIP.insert("end", *PIP)
                    self.lbBrand_Name.insert("end", *Brand_Name)
                    self.lbProduct_Discription.insert("end", *Product_Discription)
                    self.lbQuantity.insert("end", *Quantity)

                else:
                    messagebox.showerror("Invalid data entered", "Please enter a valid quantity amount! Try Again!")
                    Quantity_Entry.set("")

            Update_Quantity_Button = Button (Frame2,text='Update Quantity', width=15,font=('arial',30,'bold'), bd = 10, relief='ridge',
                                   bg='SlateBlue2', fg='Cornsilk', command = Update_Quantity)
            Update_Quantity_Button.grid(row = 0 , column = 0, padx = 100, pady = 25)

    def Product_Info(self):

        PIP_Info = []
        Brand_Name_Info = []
        Product_Discription_Info = []
        Pack_Size_Info = []
        Product_Cost_Info = []
        Use_Info = []
        Supply_Name_Info = []
        Quantity_Info = []

        try:
            PIP_chosen = self.lbPIP.get(self.lbPIP.curselection())
        except Exception:
             messagebox.showerror("No Product Chosen!", "Please select a PIP number and try again!")
        else:
            
            PIP_Info.clear()
            Brand_Name_Info.clear()
            Product_Discription_Info.clear()
            Pack_Size_Info.clear()
            Product_Cost_Info.clear()
            Use_Info.clear()
            Supply_Name_Info.clear()
            Quantity_Info.clear()
        
            con = sqlite3.connect("Stock_Management_Database.db")
            cur = con.cursor()
            cur.execute('SELECT PIP, Product_Discription, Pack_Size, Product_Cost, Quantity FROM "Product_Info" WHERE (PIP = (:PIP_Selected))',
                        {
                            'PIP_Selected' : PIP_chosen
                        })
            
            Product_Info_Rows = cur.fetchall()
            con.close()

            
            rowNr = 0
            
            for row in Product_Info_Rows:
                if len(row) == 0:   
                    continue

                if rowNr >= 0:
                    PIP_Info.append(row[0])
                    Product_Discription_Info.append(row[1])
                    Pack_Size_Info.append(row[2])
                    Product_Cost_Info.append(row[3])
                    Quantity_Info.append(row[4])

                rowNr = rowNr + 1

            con = sqlite3.connect("Stock_Management_Database.db")
            cur = con.cursor()
            cur.execute('SELECT Brand_Name,Use,Supply_Name FROM "Product_Info","Brands","Uses","Supplier" WHERE (PIP = (:PIP_Selected)) AND Product_Info.BrandID = Brands.BrandID AND Product_Info.UseID = Uses.UseID AND Product_Info.SupplyID = Supplier.SupplyID',
                        {
                            'PIP_Selected' : PIP_chosen
                        })
            
            Other_Rows = cur.fetchall()
            con.close()

            
            rowNr = 0
            
            for row in Other_Rows:
                if len(row) < 1:
                    continue

                if rowNr >= 0:
                    Brand_Name_Info.append(row[0])
                    Use_Info.append(row[1])
                    Supply_Name_Info.append(row[2])

                rowNr = rowNr + 1
            
            
            Product_Information = Toplevel()

            Product_Information.geometry("895x380")
            Product_Information.config(bg ='Cadet Blue')

            Frame0 = Frame(Product_Information, bg = "Cadet Blue")
            Frame0.grid(row = 0, column = 0, pady = 5)

            Frame1 = Frame(Product_Information, bg = "Cadet Blue")
            Frame1.grid(row = 1, column = 0, padx = 5, pady = 5)

            Frame2 = Frame(Product_Information, bg = "Cadet Blue")
            Frame2.grid(row = 2, column = 0, pady = 5)

            Frame3 = Frame(Product_Information, bg = "Cadet Blue")
            Frame3.grid(row = 3, column = 0, pady = 5)



            Product_Info_Title = Label(Frame0, text = "Product Information", width = 30, font =('arial',25,'bold'), bd=15, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Product_Info_Title.grid(row = 0, column = 0)

            

            PIP_Label = Label(Frame1, text = "PIP", width = 15, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            PIP_Label.grid(row = 0, column = 0)

            PIP_Display = Listbox(Frame1, width = 15,  height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            PIP_Display.grid(row = 1, column = 0)
            
            
            Brand_Name_Label = Label(Frame1, text = "Brand Name", width = 15, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Brand_Name_Label.grid(row = 0, column = 1)
            
            Brand_Name_Display = Listbox(Frame1, width = 15, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Brand_Name_Display.grid(row = 1, column = 1)


            Product_Discription_Label = Label(Frame1, text = "Product Discription", width = 20, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Product_Discription_Label.grid(row = 0, column = 2)

            Product_Discription_Display = Listbox(Frame1, width = 20, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                        bg = 'White', fg = 'Black')
            Product_Discription_Display.grid(row = 1, column = 2)
            

            Quantity_Label = Label(Frame2, text = "Quantity", width = 25, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Quantity_Label.grid(row = 0, column = 0)

            Quantity_Display = Listbox(Frame2, width = 25, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Quantity_Display.grid(row = 1, column = 0)


            Product_Cost_Label = Label(Frame2, text = "Product Cost", width = 25, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Product_Cost_Label.grid(row = 0, column = 1)

            Product_Cost_Display = Listbox(Frame2, width = 25, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Product_Cost_Display.grid(row = 1, column = 1)
            

            Use_Label = Label(Frame3, text = "Use", width = 25, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Use_Label.grid(row = 0, column = 0)

            Use_Display = Listbox(Frame3, width = 25, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Use_Display.grid(row = 1, column = 0)
            

            Supply_Name_Label = Label(Frame3, text = "Supplier", width = 25, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Supply_Name_Label.grid(row = 0, column = 1)

            Supply_Name_Display = Listbox(Frame3, width = 25, height = 1, font =('arial',20,'bold'), bd=5,
                                         bg = 'White', fg = 'Black')
            Supply_Name_Display.grid(row = 1, column = 1)

            PIP_Display.insert(0,PIP_Info[0])
            Brand_Name_Display.insert(0,Brand_Name_Info[0])
            Product_Discription_Display.insert(0,Product_Discription_Info[0])
            Quantity_Display.insert(0,Quantity_Info[0])
            Product_Cost_Display.insert(0,Product_Cost_Info[0])
            Use_Display.insert(0,Use_Info[0])
            Supply_Name_Display.insert(0,Supply_Name_Info[0])
            
                
    def New_Product(self):

        self.Clear_List()
        
        self.New_Product = Toplevel()
        self.app = New_Product_Window(self.New_Product)

    def Delete_Product(self):

        Brand_Name_Chosen = []
        Product_Discription_Chosen = []
        
        PIP_Chosen = self.lbPIP.get(ACTIVE)

        try:
            PIP_chosen = self.lbPIP.get(self.lbPIP.curselection())
        except Exception:
             messagebox.showerror("No Product Chosen!", "Please select a PIP number and try again!")
        else:
            
            Delete_Product_Win = Toplevel()

            Delete_Product_Win.geometry("785x280")
            Delete_Product_Win.config(bg ='Cadet Blue')

            Frame0 = Frame(Delete_Product_Win, bg = "Cadet Blue")
            Frame0.grid(row = 0, column = 0, pady = 5)

            Frame1 = Frame(Delete_Product_Win, bg = "Cadet Blue")
            Frame1.grid(row = 1, column = 0, padx = 5, pady = 5)

            Frame2 = Frame(Delete_Product_Win, bg = "Cadet Blue")
            Frame2.grid(row = 2, column = 0, pady = 5)
            

            Title = Label(Frame0, text = "Delete Product", width = 25, font =('arial',25,'bold'), bd=15, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Title.grid(row = 0, column = 0)
            

            Delete_PIP_Display_Label = Label(Frame1, text = "PIP", width = 10, font =('arial',20,'bold'), bd=15, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Delete_PIP_Display_Label.grid(row = 0, column = 0)

            Delete_Brand_Display_Label = Label(Frame1, text = "Brand", width = 10, font =('arial',20,'bold'), bd=15, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Delete_Brand_Display_Label.grid(row = 0, column = 1)

            Delete_Product_Discription_Display_Label = Label(Frame1, text = "Product Discription", width = 20, font =('arial',20,'bold'), bd=15, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Delete_Product_Discription_Display_Label.grid(row = 0, column = 2)

            def Selected_Product():
                
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('SELECT Brand_Name, Product_Discription FROM "Product_Info","Brands" WHERE (PIP = (:PIP_Selected)) AND Product_Info.BrandID = Brands.BrandID',
                            {
                                'PIP_Selected' : PIP_Chosen
                            })
                
                rows = cur.fetchall()
                con.close()
                
                rowNr = 0
                
                for row in rows:
                    if len(row) < 1:   
                        continue

                    if rowNr >= 0:
                        Brand_Name_Chosen.append(row[0])
                        Product_Discription_Chosen.append(row[1])
                        
                    rowNr = rowNr + 1

                Delete_PIP_Display.insert(0,PIP_Chosen)
                Delete_Brand_Name_Display.insert(0,*Brand_Name_Chosen)
                Delete_Product_Discription_Display.insert(0,*Product_Discription_Chosen)
            

            Delete_PIP_Display = Listbox(Frame1, width = 10, height = 1, font =('arial',15,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Delete_PIP_Display.grid(row = 1, column = 0)

            Delete_Brand_Name_Display = Listbox(Frame1, width = 15, height = 1, font =('arial',15,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Delete_Brand_Name_Display.grid(row = 1, column = 1)
            
            Delete_Product_Discription_Display = Listbox(Frame1, width = 30, height = 1, font =('arial',15,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Delete_Product_Discription_Display.grid(row = 1, column = 2)


            Selected_Product()

            def Delete():
                
                self.confirm = tkinter.messagebox.askyesno("Confirm Deletion of Data!", "Are you sure you want to delete this record?")

                if self.confirm > 0:
                    
                    con = sqlite3.connect("Stock_Management_Database.db")
                    cur = con.cursor()
                    cur.execute('DELETE FROM "Product_Info" WHERE (PIP = (:PIP_Selected))',
                                {    
                                   'PIP_Selected' : PIP_Chosen
                                })
                    con.commit()
                    con.close()
                    
                    Delete_Product_Win.destroy()

                    PIP.clear()
                    Brand_Name.clear()
                    Product_Discription.clear()
                    Quantity.clear()

                    self.Clear_List()
                        
                    con = sqlite3.connect("Stock_Management_Database.db")
                    cur = con.cursor()
                    cur.execute('SELECT PIP, Brand_Name, Product_Discription, Quantity FROM "Product_Info", "Brands" WHERE Product_Info.BrandID = Brands.BrandID')
                    rows = cur.fetchall()
                    con.close()
                    
                    rowNr = 0
                    
                    for row in rows:
                        if len(row) < 1:
                            continue

                        if rowNr >= 0:
                            PIP.append(row[0])
                            Brand_Name.append(row[1])
                            Product_Discription.append(row[2])
                            Quantity.append(row[3])

                        rowNr = rowNr + 1
                        
                    self.lbPIP.insert("end", *PIP)
                    self.lbBrand_Name.insert("end", *Brand_Name)
                    self.lbProduct_Discription.insert("end", *Product_Discription)
                    self.lbQuantity.insert("end", *Quantity)


                else:
                    Delete_Product_Win.destroy()
            

            Delete_Button = Button(Frame2,text='Delete Product', width=15,font=('arial',20,'bold'), bd = 10, relief='ridge',
                                   bg='SeaGreen3', fg='Cornsilk', command = Delete)
            Delete_Button.grid(row = 0, column = 0)


#---------------------------------------------- Search Tab Functions --------------------------------------------------#

    def Start_Search(self):

        Searched_PIP = []
        Searched_Brand = []
        Searched_Product_Discription = []
        Searched_Use = []
        Searched_Supplier = []
        Searched_Quantity = []

        Similar_PIP = []
        Similar_Brand = []
        Similar_Product_Discription = []
        Similar_Use = []
        Similar_Supplier = []
        Similar_Quantity = []

        def Clear_Search_Lists():
            Searched_PIP.clear()
            Searched_Brand.clear()
            Searched_Product_Discription.clear()
            Searched_Use.clear()
            Searched_Supplier.clear()
            Searched_Quantity.clear()

            Similar_PIP.clear()
            Similar_Brand.clear()
            Similar_Product_Discription.clear()
            Similar_Use.clear()
            Similar_Supplier.clear()
            Similar_Quantity.clear()
        
        if Search_By_Menu.get() == "Search By":
            
            messagebox.showerror("No Search Filter Selected!","Please select a Search By option to filter your search before countinuing! Try Again!")
            
        else:
            
            def Frames_Labels_and_Lists():
                
                
                Search_Frame2 = LabelFrame(Search_Frame, width = 500, height=150, text = "Search Results", font=('arial',25,'bold'), bd = 20, relief='ridge', bg = "plum2")
                Search_Frame2.grid(row = 2, column =0, pady = 5)
                
                
                self.scrollbar_V = Scrollbar(Search_Frame2)
                self.scrollbar_H_Search_PIP = Scrollbar(Search_Frame2, orient=HORIZONTAL)
                self.scrollbar_H_Search_Brand = Scrollbar(Search_Frame2, orient=HORIZONTAL)
                self.scrollbar_H_Search_Product_Discription = Scrollbar(Search_Frame2, orient=HORIZONTAL)
                self.scrollbar_H_Search_Use = Scrollbar(Search_Frame2, orient=HORIZONTAL)
                self.scrollbar_H_Search_Supplier = Scrollbar(Search_Frame2, orient=HORIZONTAL)
                self.scrollbar_H_Search_Quantity = Scrollbar(Search_Frame2, orient=HORIZONTAL)
                self.scrollbar_V.grid(row = 1, column = 6, sticky=N+S+W, padx = 5)
                self.scrollbar_H_Search_PIP.grid(row = 2, column = 0, sticky=N+E+S+W)
                self.scrollbar_H_Search_Brand.grid(row = 2, column = 1, sticky=N+E+S+W)
                self.scrollbar_H_Search_Product_Discription.grid(row = 2, column = 2, sticky=N+E+S+W)
                self.scrollbar_H_Search_Use.grid(row = 2, column = 3, sticky=N+E+S+W)
                self.scrollbar_H_Search_Supplier.grid(row = 2, column = 4, sticky=N+E+S+W)
                self.scrollbar_H_Search_Quantity.grid(row = 2, column = 5, sticky=N+E+S+W)
            
                Searched_PIP_Label = Label(Search_Frame2, text = "PIP", font=('arial',15,'bold'), width = 15, bd = 10, relief='ridge',
                                     bg = 'Maroon3', fg = 'White')
                Searched_PIP_Label.grid(row=0,column=0, padx = 5)

                self.Searched_PIP_List = Listbox(Search_Frame2, font=('arial',15,'bold'), height = 4, width = 15, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Search_PIP.set)
                self.Searched_PIP_List.grid(row=1, column=0, padx = 5)

                
                Searched_Brand_Label = Label(Search_Frame2, text = "Brand", font=('arial',15,'bold'), width = 15, bd = 10, relief='ridge',
                                         bg = 'Maroon3', fg = 'White')
                Searched_Brand_Label.grid(row=0,column=1, padx = 5)

                self.Searched_Brand_List = Listbox(Search_Frame2, font=('arial',15,'bold'), height = 4, width = 15, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Search_Brand.set)
                self.Searched_Brand_List.grid(row=1, column=1, padx = 5)
                

                Searched_Product_Discription_Label = Label(Search_Frame2, text = "Product Discription", width = 15, font=('arial',15,'bold'), bd = 10, relief='ridge',
                                         bg = 'Maroon3', fg = 'White')
                Searched_Product_Discription_Label.grid(row=0,column=2, padx = 5)

                
                self.Searched_Product_Discription_List = Listbox(Search_Frame2, font=('arial',15,'bold'), height = 4, width = 15, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Search_Product_Discription.set)
                self.Searched_Product_Discription_List.grid(row=1, column=2, padx = 5)
                

                Searched_Use_Label = Label(Search_Frame2, text = "Use", font=('arial',15,'bold'), width = 15, bd = 10, relief='ridge',
                                         bg = 'Maroon3', fg = 'White')
                Searched_Use_Label.grid(row=0,column=3, padx = 5)

                self.Searched_Use_List = Listbox(Search_Frame2, font=('arial',15,'bold'), height = 4, width = 15, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Search_Use.set)
                self.Searched_Use_List.grid(row=1, column=3, padx = 5)
                

                Searched_Supplier_Label = Label(Search_Frame2, text = "Supplier", font=('arial',15,'bold'),width =15, bd = 10, relief='ridge',
                                         bg = 'Maroon3', fg = 'White')
                Searched_Supplier_Label.grid(row=0,column=4, padx = 5)

                self.Searched_Supplier_List = Listbox(Search_Frame2, font=('arial',15,'bold'), height = 4, width = 15, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Search_Supplier.set)
                self.Searched_Supplier_List.grid(row=1, column=4, padx = 5)
                

                Searched_Quantity_Label = Label(Search_Frame2, text = "Quantity", font=('arial',15,'bold'), width =10, bd = 10, relief='ridge',
                                         bg = 'Maroon3', fg = 'White')
                Searched_Quantity_Label.grid(row=0,column=5, padx = 5)

                self.Searched_Quantity_List = Listbox(Search_Frame2, font=('arial',15,'bold'), height = 4, width = 5, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Search_Quantity.set)
                self.Searched_Quantity_List.grid(row=1, column=5, padx = 5)


                self.scrollbar_V.config(command=self.yview)
                self.scrollbar_H_Search_PIP.config(command=self.Searched_PIP_List.xview)
                self.scrollbar_H_Search_Brand.config(command=self.Searched_Brand_List.xview)
                self.scrollbar_H_Search_Product_Discription.config(command=self.Searched_Product_Discription_List.xview)
                self.scrollbar_H_Search_Use.config(command = self.Searched_Use_List.xview)
                self.scrollbar_H_Search_Supplier.config(command = self.Searched_Supplier_List.xview)
                self.scrollbar_H_Search_Quantity.config(command = self.Searched_Quantity_List.xview)


            def Similar_Labels_and_Lists():
                

                Search_Frame3 = LabelFrame(Search_Frame, width=1350, height=150, text = "Similar Products", font=('arial',25,'bold'), bd = 20, relief='ridge', bg = "plum2")
                Search_Frame3.grid(row = 4, column =0, pady = 3)


                self.scrollbar_V = Scrollbar(Search_Frame3)
                self.scrollbar_H_Similar_PIP = Scrollbar(Search_Frame3, orient=HORIZONTAL)
                self.scrollbar_H_Similar_Brand = Scrollbar(Search_Frame3, orient=HORIZONTAL)
                self.scrollbar_H_Similar_Product_Discription = Scrollbar(Search_Frame3, orient=HORIZONTAL)
                self.scrollbar_H_Similar_Use = Scrollbar(Search_Frame3, orient=HORIZONTAL)
                self.scrollbar_H_Similar_Supplier = Scrollbar(Search_Frame3, orient=HORIZONTAL)
                self.scrollbar_H_Similar_Quantity = Scrollbar(Search_Frame3, orient=HORIZONTAL)
                self.scrollbar_V.grid(row = 1, column = 6, sticky=N+S+W, padx = 5)
                self.scrollbar_H_Similar_PIP.grid(row = 2, column = 0, sticky=N+E+S+W)
                self.scrollbar_H_Similar_Brand.grid(row = 2, column = 1, sticky=N+E+S+W)
                self.scrollbar_H_Similar_Product_Discription.grid(row = 2, column = 2, sticky=N+E+S+W)
                self.scrollbar_H_Similar_Use.grid(row = 2, column = 3, sticky=N+E+S+W)
                self.scrollbar_H_Similar_Supplier.grid(row = 2, column = 4, sticky=N+E+S+W)
                self.scrollbar_H_Similar_Quantity.grid(row = 2, column = 5, sticky=N+E+S+W)

                Similar_PIP_Label = Label(Search_Frame3, text = "PIP", font=('arial',15,'bold'), width = 15, bd = 10, relief='ridge',
                                         bg = 'Maroon3', fg = 'White')
                Similar_PIP_Label.grid(row=0,column=0, padx = 10)

                global Similar_PIP_List
                self.Similar_PIP_List = Listbox(Search_Frame3, font=('arial',15,'bold'), height = 4, width = 15, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Similar_PIP.set)
                self.Similar_PIP_List.grid(row=1, column=0, padx = 10)
                

                Similar_Brand_Label = Label(Search_Frame3, text = "Brand", font=('arial',15,'bold'), width = 15, bd = 10, relief='ridge',
                                         bg = 'Maroon3', fg = 'White')
                Similar_Brand_Label.grid(row=0,column=1, padx = 10)

                global Similar_Brand_List
                self.Similar_Brand_List = Listbox(Search_Frame3, font=('arial',15,'bold'), height = 4, width = 15, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Similar_Brand.set)
                self.Similar_Brand_List.grid(row=1, column=1, padx = 10)
                

                Similar_Product_Discription_Label = Label(Search_Frame3, text = "Product Discription", width = 15, font=('arial',15,'bold'), bd = 10, relief='ridge',
                                         bg = 'Maroon3', fg = 'White')
                Similar_Product_Discription_Label.grid(row=0,column=2, padx = 10)

                global Similar_Product_Discription_List
                self.Similar_Product_Discription_List = Listbox(Search_Frame3, font=('arial',15,'bold'), height = 4, width = 15, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Similar_Product_Discription.set)
                self.Similar_Product_Discription_List.grid(row=1, column=2, padx = 10)
                

                Similar_Use_Label = Label(Search_Frame3, text = "Use", font=('arial',15,'bold'), width = 15, bd = 10, relief='ridge',
                                         bg = 'Maroon3', fg = 'White')
                Similar_Use_Label.grid(row=0,column=3, padx = 10)

                global Similar_Use_List
                self.Similar_Use_List = Listbox(Search_Frame3, font=('arial',15,'bold'), height = 4, width = 15, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Similar_Use.set)
                self.Similar_Use_List.grid(row=1, column=3, padx = 10)
                

                Similar_Supplier_Label = Label(Search_Frame3, text = "Supplier", font=('arial',15,'bold'),width =15, bd = 10, relief='ridge',
                                         bg = 'Maroon3', fg = 'White')
                Similar_Supplier_Label.grid(row=0,column=4, padx = 10)

                global Similar_Supplier_List
                self.Similar_Supplier_List = Listbox(Search_Frame3, font=('arial',15,'bold'), height = 4, width = 15, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Similar_Supplier.set)
                self.Similar_Supplier_List.grid(row=1, column=4, padx = 10)
                

                Similar_Quantity_Label = Label(Search_Frame3, text = "Quantity", font=('arial',15,'bold'), width =10, bd = 10, relief='ridge',
                                         bg = 'Maroon3', fg = 'White')
                Similar_Quantity_Label.grid(row=0,column=5, padx = 10)

                global Similar_Quantity_List
                self.Similar_Quantity_List = Listbox(Search_Frame3, font=('arial',15,'bold'), height = 4, width = 5, bd = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Similar_Quantity.set)
                self.Similar_Quantity_List.grid(row=1, column=5, padx = 10)


                self.scrollbar_V.config(command=self.yview)
                self.scrollbar_H_Similar_PIP.config(command=self.Similar_PIP_List.xview)
                self.scrollbar_H_Similar_Brand.config(command=self.Similar_Brand_List.xview)
                self.scrollbar_H_Similar_Product_Discription.config(command=self.Similar_Product_Discription_List.xview)
                self.scrollbar_H_Similar_Use.config(command = self.Similar_Use_List.xview)
                self.scrollbar_H_Similar_Supplier.config(command = self.Similar_Supplier_List.xview)
                self.scrollbar_H_Similar_Quantity.config(command = self.Similar_Quantity_List.xview)


            if Search_By_Menu.get() == "Use":

                All_Uses = []
                
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('SELECT Use FROM "Uses"')
                rows = cur.fetchall()
                con.close()
                
                rowNr = 0
                
                for row in rows:
                    if len(row) < 1:
                        continue

                    if rowNr >= 0:
                        All_Uses.append(row[0])

                    rowNr = rowNr + 1
                    

                All_Uses_lower = [x.lower() for x in All_Uses]
                 
                Search_By_Use = Search_Bar_Entry.get()
                
                if Search_By_Use.lower() not in All_Uses_lower:

                    messagebox.showerror("No Use Exists!", "This Pharmacy does not have any products with this Use! Try Again!")
                    Search_Bar_Entry.set("")
                    
                else:

                    New_Search_By_Use = All_Uses[All_Uses_lower.index(Search_By_Use.lower())]
                    
                    Frames_Labels_and_Lists()
                    
                    Clear_Search_Lists()

                    Search_By_Use = Search_Bar_Entry.get()
                    
                    con = sqlite3.connect("Stock_Management_Database.db")
                    cur = con.cursor()
                    cur.execute('''SELECT PIP, Brand_Name, Product_Discription, Use, Supply_Name, Quantity FROM "Product_Info", "Brands", "Uses", "Supplier"
                                    WHERE Use = (:Searching_Use) AND Product_Info.BrandID = Brands.BrandID AND Product_Info.UseID = Uses.UseID AND Product_Info.SupplyID = Supplier.SupplyID''',
                                {
                                    "Searching_Use" : New_Search_By_Use

                                })
                    rows = cur.fetchall()
                    con.close()
                    
                    rowNr = 0
                    
                    for row in rows:
                        if len(row) < 1:
                            continue

                        if rowNr >= 0:
                            Searched_PIP.append(row[0])
                            Searched_Brand.append(row[1])
                            Searched_Product_Discription.append(row[2])
                            Searched_Use.append(row[3])
                            Searched_Supplier.append(row[4])
                            Searched_Quantity.append(row[5])

                        rowNr = rowNr + 1
                        
                    self.Searched_PIP_List.insert(0,*Searched_PIP)
                    self.Searched_Brand_List.insert(0,*Searched_Brand)
                    self.Searched_Product_Discription_List.insert(0,*Searched_Product_Discription)
                    self.Searched_Use_List.insert(0,*Searched_Use)
                    self.Searched_Supplier_List.insert(0,*Searched_Supplier)
                    self.Searched_Quantity_List.insert(0,*Searched_Quantity)
                    
            elif Search_By_Menu.get() == "Supplier":

                All_Suppliers = []
                
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('SELECT Supply_Name FROM "Supplier"')
                rows = cur.fetchall()
                con.close()
                
                rowNr = 0
                
                for row in rows:
                    if len(row) < 1:
                        continue

                    if rowNr >= 0:
                        All_Suppliers.append(row[0])

                    rowNr = rowNr + 1

                All_Suppliers_lower = [x.lower() for x in All_Suppliers]
                
                Search_By_Suppliers = Search_Bar_Entry.get()
                
                if Search_By_Suppliers.lower() not in All_Suppliers_lower:

                    messagebox.showerror("No supplier!", "This Pharmacy does not currently use this supplier! Try Again!")
                    Search_Bar_Entry.set("")
                    
                else:
                    
                    New_Search_By_Suppliers = All_Suppliers[All_Suppliers_lower.index(Search_By_Suppliers.lower())]

                    Frames_Labels_and_Lists()
            
                    Clear_Search_Lists()
                    
                    con = sqlite3.connect("Stock_Management_Database.db")
                    cur = con.cursor()
                    cur.execute('''SELECT PIP, Brand_Name, Product_Discription, Use, Supply_Name, Quantity FROM "Product_Info", "Brands", "Uses", "Supplier"
                                    WHERE Supply_Name = (:Searching_Supplier) AND Product_Info.BrandID = Brands.BrandID AND Product_Info.UseID = Uses.UseID AND Product_Info.SupplyID = Supplier.SupplyID''',
                                {
                                    "Searching_Supplier" : New_Search_By_Suppliers

                                })
                    rows = cur.fetchall()
                    con.close()
                    
                    rowNr = 0
                    
                    for row in rows:
                        if len(row) < 1:
                            continue

                        if rowNr >= 0:
                            Searched_PIP.append(row[0])
                            Searched_Brand.append(row[1])
                            Searched_Product_Discription.append(row[2])
                            Searched_Use.append(row[3])
                            Searched_Supplier.append(row[4])
                            Searched_Quantity.append(row[5])

                        rowNr = rowNr + 1
                        
                    self.Searched_PIP_List.insert(0,*Searched_PIP)
                    self.Searched_Brand_List.insert(0,*Searched_Brand)
                    self.Searched_Product_Discription_List.insert(0,*Searched_Product_Discription)
                    self.Searched_Use_List.insert(0,*Searched_Use)
                    self.Searched_Supplier_List.insert(0,*Searched_Supplier)
                    self.Searched_Quantity_List.insert(0,*Searched_Quantity)
                
            elif Search_By_Menu.get() == "PIP":

                All_PIPs = []
                
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('SELECT PIP FROM "Product_Info"')
                rows = cur.fetchall()
                con.close()
                
                rowNr = 0
                
                for row in rows:
                    if len(row) < 1:
                        continue

                    if rowNr >= 0:
                        All_PIPs.append(row[0])

                    rowNr = rowNr + 1
                    
                try:
                    Search_By_PIP = int(Search_Bar_Entry.get())
                except ValueError:
                    messagebox.showerror("PIP Does Not Exist!", "This Pharmacy does not currently have a product with that PIP Code! Try Again!")
                    Search_Bar_Entry.set("")
                
                
                if Search_By_PIP not in All_PIPs:

                    messagebox.showerror("PIP Does Not Exist!", "This Pharmacy does not currently have a product with that PIP Code! Try Again!")
                    Search_Bar_Entry.set("")
                    
                else:
                    
                    Frames_Labels_and_Lists()

                    Similar_Labels_and_Lists()
                
                    Clear_Search_Lists()

                    con = sqlite3.connect("Stock_Management_Database.db")
                    cur = con.cursor()
                    cur.execute('''SELECT PIP, Brand_Name, Product_Discription, Use, Supply_Name, Quantity FROM "Product_Info", "Brands", "Uses", "Supplier"
                                    WHERE PIP = (:Searching_PIP) AND Product_Info.BrandID = Brands.BrandID AND Product_Info.UseID = Uses.UseID AND Product_Info.SupplyID = Supplier.SupplyID''',
                                {
                                    "Searching_PIP" : Search_By_PIP

                                })
                    rows = cur.fetchall()
                    con.close()
                    
                    rowNr = 0
                    
                    for row in rows:
                        if len(row) < 1:
                            continue

                        if rowNr >= 0:
                            Searched_PIP.append(row[0])
                            Searched_Brand.append(row[1])
                            Searched_Product_Discription.append(row[2])
                            Searched_Use.append(row[3])
                            Searched_Supplier.append(row[4])
                            Searched_Quantity.append(row[5])

                        rowNr = rowNr + 1
                        
                    self.Searched_PIP_List.insert(0,*Searched_PIP)
                    self.Searched_Brand_List.insert(0,*Searched_Brand)
                    self.Searched_Product_Discription_List.insert(0,*Searched_Product_Discription)
                    self.Searched_Use_List.insert(0,*Searched_Use)
                    self.Searched_Supplier_List.insert(0,*Searched_Supplier)
                    self.Searched_Quantity_List.insert(0,*Searched_Quantity)

                    con = sqlite3.connect("Stock_Management_Database.db")
                    cur = con.cursor()
                    cur.execute('''SELECT PIP, Brand_Name, Product_Discription, Use, Supply_Name, Quantity FROM "Product_Info", "Brands", "Uses", "Supplier"
                                    WHERE Use = (:Similar_Use) AND Product_Info.BrandID = Brands.BrandID AND Product_Info.UseID = Uses.UseID AND Product_Info.SupplyID = Supplier.SupplyID''',
                                {
                                    "Similar_Use" : Searched_Use[0]

                                })
                    rows = cur.fetchall()
                    con.close()
                    
                    rowNr = 0
                    
                    for row in rows:
                        if len(row) < 1:
                            continue

                        if rowNr >= 0:
                            Similar_PIP.append(row[0])
                            Similar_Brand.append(row[1])
                            Similar_Product_Discription.append(row[2])
                            Similar_Use.append(row[3])
                            Similar_Supplier.append(row[4])
                            Similar_Quantity.append(row[5])

                        rowNr = rowNr + 1

                    self.Similar_PIP_List.insert(0,*Similar_PIP)
                    self.Similar_Brand_List.insert(0,*Similar_Brand)
                    self.Similar_Product_Discription_List.insert(0,*Similar_Product_Discription)
                    self.Similar_Use_List.insert(0,*Similar_Use)
                    self.Similar_Supplier_List.insert(0,*Similar_Supplier)
                    self.Similar_Quantity_List.insert(0,*Similar_Quantity)
                    
                
            elif Search_By_Menu.get() == "Brand":
                
                All_Brands = []
                
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('SELECT Brand_Name FROM "Brands"')
                rows = cur.fetchall()
                con.close()
                
                rowNr = 0
                
                for row in rows:
                    if len(row) < 1:
                        continue

                    if rowNr >= 0:
                        All_Brands.append(row[0])

                    rowNr = rowNr + 1
                    

                All_Brands_lower = [x.lower() for x in All_Brands]
                
                    
                Search_By_Brand = Search_Bar_Entry.get()
                
                if Search_By_Brand.lower() not in All_Brands_lower:

                    messagebox.showerror("Brand Does not Exist!", "This Pharmacy does not current have any Products of the selected Brand! Try Again!")
                    Search_Bar_Entry.set("")
                    
                else:

                    New_Search_By_Brand = All_Brands[All_Brands_lower.index(Search_By_Brand.lower())]
                    
                    Frames_Labels_and_Lists()

                    Clear_Search_Lists()

                    con = sqlite3.connect("Stock_Management_Database.db")
                    cur = con.cursor()
                    cur.execute('''SELECT PIP, Brand_Name, Product_Discription, Use, Supply_Name, Quantity FROM "Product_Info", "Brands", "Uses", "Supplier"
                                    WHERE Brand_Name = (:Searching_Brand) AND Product_Info.BrandID = Brands.BrandID AND Product_Info.UseID = Uses.UseID AND Product_Info.SupplyID = Supplier.SupplyID''',
                                {
                                    "Searching_Brand" : New_Search_By_Brand

                                })
                    rows = cur.fetchall()
                    con.close()
                    
                    rowNr = 0
                    
                    for row in rows:
                        if len(row) < 1:
                            continue

                        if rowNr >= 0:
                            Searched_PIP.append(row[0])
                            Searched_Brand.append(row[1])
                            Searched_Product_Discription.append(row[2])
                            Searched_Use.append(row[3])
                            Searched_Supplier.append(row[4])
                            Searched_Quantity.append(row[5])

                        rowNr = rowNr + 1
                        
                    self.Searched_PIP_List.insert(0,*Searched_PIP)
                    self.Searched_Brand_List.insert(0,*Searched_Brand)
                    self.Searched_Product_Discription_List.insert(0,*Searched_Product_Discription)
                    self.Searched_Use_List.insert(0,*Searched_Use)
                    self.Searched_Supplier_List.insert(0,*Searched_Supplier)
                    self.Searched_Quantity_List.insert(0,*Searched_Quantity)

#------------------------------------------- Order History Tab Functions ----------------------------------------------#

    def Clear_Order_History_List(self):
        
        self.lbOrderID.delete(0,END)
        self.lbOrder_PIP.delete(0,END)
        self.lbOrder_Quantity.delete(0,END)
        self.lbTotal_Cost.delete(0,END)
        self.lbDate.delete(0,END)
        

        
    def Display_Newest(self):
        
        OrderID.clear()
        Order_PIP.clear()
        Order_Quantity.clear()
        Total_Cost.clear()
        Dates.clear()
        
        self.Clear_Order_History_List()
        
        con = sqlite3.connect("Stock_Management_Database.db")
        cur = con.cursor()
        cur.execute('SELECT OrderID, PIP, Order_Quantity, Total_Cost, Date_Placed FROM "Place_Order" ORDER BY Date_Placed desc')
        rows = cur.fetchall()
        con.close()
        
        rowNr = 0
        
        for row in rows:
            if len(row) < 1:
                continue

            if rowNr >= 0:
                OrderID.append(row[0])
                Order_PIP.append(row[1])
                Order_Quantity.append(row[2])
                Total_Cost.append(row[3])
                Dates.append(row[4])

            rowNr = rowNr + 1

        self.lbOrderID.insert("end", *OrderID)
        self.lbOrder_PIP.insert("end", *Order_PIP)
        self.lbOrder_Quantity.insert("end", *Order_Quantity)
        self.lbTotal_Cost.insert("end", *Total_Cost)
        self.lbDate.insert("end", *Dates)
        

    def Display_Oldest(self):
        
        OrderID.clear()
        Order_PIP.clear()
        Order_Quantity.clear()
        Total_Cost.clear()
        Dates.clear()
        
        self.Clear_Order_History_List()
        
        con = sqlite3.connect("Stock_Management_Database.db")
        cur = con.cursor()
        cur.execute('SELECT OrderID, PIP, Order_Quantity, Total_Cost, Date_Placed FROM "Place_Order"')
        rows = cur.fetchall()
        con.close()
        
        rowNr = 0
        
        for row in rows:
            if len(row) < 1:
                continue

            if rowNr >= 0:
                OrderID.append(row[0])
                Order_PIP.append(row[1])
                Order_Quantity.append(row[2])
                Total_Cost.append(row[3])
                Dates.append(row[4])

            rowNr = rowNr + 1

        self.lbOrderID.insert("end", *OrderID)
        self.lbOrder_PIP.insert("end", *Order_PIP)
        self.lbOrder_Quantity.insert("end", *Order_Quantity)
        self.lbTotal_Cost.insert("end", *Total_Cost)
        self.lbDate.insert("end", *Dates)



    def Show_Order_Info(self):
        
        Chosen_Order_PIP = []
        Chosen_Order_Brand_Name = []
        Chosen_Order_Product_Discription = []
        Chosen_Order_Quantity = []
        Chosen_Order_Total_Cost = []
        Chosen_Order_Date = []
        
        Chosen_Order = self.lbOrderID.get(ACTIVE)


        try:
            
            OrderID_Chosen = self.lbOrderID.get(self.lbOrderID.curselection())
            
        except Exception:
            
            messagebox.showerror("No Order Chosen!", "Please select an Order and try again!")

        else:
            con = sqlite3.connect("Stock_Management_Database.db")
            cur = con.cursor()
            cur.execute('SELECT PIP, Order_Quantity, Total_Cost, Date_Placed FROM "Place_Order" WHERE OrderID = (:OrderID_Selected)',
                        {
                            "OrderID_Selected" : Chosen_Order

                        })
            Order_rows = cur.fetchall()
            con.close()
            
            rowNr = 0
            
            for row in Order_rows:
                if len(row) < 1:
                    continue

                if rowNr >= 0:
                    Chosen_Order_PIP.append(row[0])
                    Chosen_Order_Quantity.append(row[1])
                    Chosen_Order_Total_Cost.append(row[2])
                    Chosen_Order_Date.append(row[3])

                rowNr = rowNr + 1
                
                
            con = sqlite3.connect("Stock_Management_Database.db")
            cur = con.cursor()
            cur.execute('SELECT Product_Discription, Brand_Name FROM "Product_Info", "Brands" WHERE PIP = (:Order_PIP_Selected) AND Product_Info.BrandID = Brands.BrandID',
                        {
                            "Order_PIP_Selected" : Chosen_Order_PIP[0]
                        })
            PIP_row = cur.fetchall()
            con.close()
            
            rowNr = 0
            
            for row in PIP_row:
                if len(row) < 1:
                    continue

                if rowNr >= 0:
                    Chosen_Order_Product_Discription.append(row[0])
                    Chosen_Order_Brand_Name.append(row[1])

                rowNr = rowNr + 1
                
            
            
            Order_Information = Toplevel()

            Order_Information.geometry("890x380")
            Order_Information.config(bg ='Cadet Blue')

            Frame0 = Frame(Order_Information, bg = "Cadet Blue")
            Frame0.grid(row = 0, column = 0, pady = 5)

            Frame1 = Frame(Order_Information, bg = "Cadet Blue")
            Frame1.grid(row = 1, column = 0, padx = 5, pady = 5)

            Frame2 = Frame(Order_Information, bg = "Cadet Blue")
            Frame2.grid(row = 2, column = 0, pady = 5)

            Frame3 = Frame(Order_Information, bg = "Cadet Blue")
            Frame3.grid(row = 3, column = 0, pady = 5)



            Order_Info_Title = Label(Frame0, text = "Order Information", width = 30, font =('arial',25,'bold'), bd=15, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Order_Info_Title.grid(row = 0, column = 0)


            Chosen_OrderID_Label = Label(Frame1, text = "OrderID", width = 25, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Chosen_OrderID_Label.grid(row = 0, column = 1)

            Chosen_OrderID_Display = Listbox(Frame1, width = 25, height = 1, font =('arial',20,'bold'), bd=5,
                                         bg = 'White', fg = 'Black')
            Chosen_OrderID_Display.grid(row = 1, column = 1)
            

            Chosen_PIP_Label = Label(Frame2, text = "PIP", width = 15, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Chosen_PIP_Label.grid(row = 0, column = 0)

            Chosen_PIP_Display = Listbox(Frame2, width = 15,  height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Chosen_PIP_Display.grid(row = 1, column = 0)
            
            
            Chosen_Brand_Name_Label = Label(Frame2, text = "Brand Name", width = 15, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Chosen_Brand_Name_Label.grid(row = 0, column = 1)
            
            Chosen_Brand_Name_Display = Listbox(Frame2, width = 15, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Chosen_Brand_Name_Display.grid(row = 1, column = 1)


            Chosen_Product_Discription_Label = Label(Frame2, text = "Product Discription", width = 20, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Chosen_Product_Discription_Label.grid(row = 0, column = 2)

            Chosen_Product_Discription_Display = Listbox(Frame2, width = 20, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                        bg = 'White', fg = 'Black')
            Chosen_Product_Discription_Display.grid(row = 1, column = 2)
            

            Chosen_Quantity_Label = Label(Frame3, text = "Quantity", width = 25, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Chosen_Quantity_Label.grid(row = 0, column = 0)

            Chosen_Quantity_Display = Listbox(Frame3, width = 25, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Chosen_Quantity_Display.grid(row = 1, column = 0)


            Chosen_Total_Cost_Label = Label(Frame3, text = "Total Cost", width = 25, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Chosen_Total_Cost_Label.grid(row = 0, column = 1)

            Chosen_Total_Cost_Display = Listbox(Frame3, width = 25, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Chosen_Total_Cost_Display.grid(row = 1, column = 1)
            

            Chosen_Date_Label = Label(Frame3, text = "Date and Time", width = 25, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Chosen_Date_Label.grid(row = 0, column = 0)

            Chosen_Date_Display = Listbox(Frame3, width = 25, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Chosen_Date_Display.grid(row = 1, column = 0)
            

            Chosen_OrderID_Display.insert(0,Chosen_Order)
            Chosen_PIP_Display.insert(0,Chosen_Order_PIP[0])
            Chosen_Brand_Name_Display.insert(0,Chosen_Order_Brand_Name[0])
            Chosen_Product_Discription_Display.insert(0,Chosen_Order_Product_Discription[0])
            Chosen_Quantity_Display.insert(0,Chosen_Order_Quantity[0])
            Chosen_Total_Cost_Display.insert(0,Chosen_Order_Total_Cost[0])
            Chosen_Date_Display.insert(0,Chosen_Order_Date[0])


    def Delete_Order(self):

        Order_Brand_Name_Chosen = []
        Order_Product_Discription_Chosen = []
        Order_Quantity_Chosen = []
        Order_Total_Cost_Chosen = []
        Order_Supplier_Chosen = []
        Order_Date_and_Time_Chosen = []


        try:
            
            OrderID_Chosen = self.lbOrderID.get(self.lbOrderID.curselection())
            
        except Exception:
            
            messagebox.showerror("No Order Chosen", "Please select a OrderID and try again!")

        else:

            Order_Brand_Name_Chosen.clear()
            Order_Product_Discription_Chosen.clear()
            Order_Quantity_Chosen.clear()
            Order_Total_Cost_Chosen.clear()
            Order_Supplier_Chosen.clear()
            Order_Date_and_Time_Chosen.clear()
            
            Delete_Order_Win = Toplevel()

            Delete_Order_Win.geometry("1145x500")
            Delete_Order_Win.config(bg ='Cadet Blue')

            Frame0 = Frame(Delete_Order_Win, bg = "Cadet Blue")
            Frame0.grid(row = 0, column = 0, pady = 5)

            Frame1 = Frame(Delete_Order_Win, bg = "Cadet Blue")
            Frame1.grid(row = 1, column = 0, padx = 5, pady = 5)

            Frame2 = Frame(Delete_Order_Win, bg = "Cadet Blue")
            Frame2.grid(row = 2, column = 0, pady = 5)

            Frame3 = Frame(Delete_Order_Win, bg = "Cadet Blue")
            Frame3.grid(row = 3, column = 0, pady = 5)
            

            Title = Label(Frame0, text = "Cancel Order", width = 30, font =('arial',25,'bold'), bd=15, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Title.grid(row = 0, column = 0)


            Delete_OrderID_Display_Label = Label(Frame1, text = "Order ID", width = 10, font =('arial',25,'bold'), bd=15, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Delete_OrderID_Display_Label.grid(row = 0, column = 0)

            Delete_Brand_Display_Label = Label(Frame1, text = "Brand", width = 10, font =('arial',25,'bold'), bd=15, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Delete_Brand_Display_Label.grid(row = 0, column = 1)

            Delete_Product_Display_Label = Label(Frame1, text = "Product", width = 20, font =('arial',25,'bold'), bd=15, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Delete_Product_Display_Label.grid(row = 0, column = 2)

            Delete_Quantity_Display_Label = Label(Frame1, text = "Quantity", width = 10, font =('arial',25,'bold'), bd=15, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Delete_Quantity_Display_Label.grid(row = 0, column = 3)

            Delete_Total_Cost_Display_Label = Label(Frame2, text = "Total Cost", width = 10, font =('arial',25,'bold'), bd=15, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Delete_Total_Cost_Display_Label.grid(row = 0, column = 0)

            Delete_Supplier_Display_Label = Label(Frame2, text = "Supplier", width = 15, font =('arial',25,'bold'), bd=15, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Delete_Supplier_Display_Label.grid(row = 0, column = 1)

            Delete_Date_Display_Label= Label(Frame2, text = "Date Place", width = 20, font =('arial',25,'bold'), bd=15, relief='ridge',
                                         bg = 'SeaGreen3', fg = 'Cornsilk')
            Delete_Date_Display_Label.grid(row = 0, column = 2)
            

            def Selected_Product():
                
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('''SELECT Brand_Name, Product_Discription, Order_Quantity, Total_Cost, Supply_Name, Date_Placed
                               FROM "Place_Order","Product_Info","Brands","Supplier"
                               WHERE (OrderID = (:Order_Selected)) AND Place_Order.PIP = Product_Info.PIP AND Product_Info.BrandID = Brands.BrandID AND Product_Info.SupplyID = Supplier.SupplyID''',
                            {
                                'Order_Selected' : OrderID_Chosen
                            })
                
                rows = cur.fetchall()
                con.close()
                
                rowNr = 0
                
                for row in rows:
                    if len(row) < 1:   
                        continue

                    if rowNr >= 0:
                        Order_Brand_Name_Chosen.append(row[0])
                        Order_Product_Discription_Chosen.append(row[1])
                        Order_Quantity_Chosen.append(row[2])
                        Order_Total_Cost_Chosen.append(row[3])
                        Order_Supplier_Chosen.append(row[4])
                        Order_Date_and_Time_Chosen.append(row[5])
        
                        
                    rowNr = rowNr + 1


                Delete_OrderID_Display.insert(0,OrderID_Chosen)
                Delete_Brand_Display.insert(0,*Order_Brand_Name_Chosen)
                Delete_Product_Display.insert(0,*Order_Product_Discription_Chosen)
                Delete_Quantity_Display.insert(0,*Order_Quantity_Chosen)
                Delete_Cost_Display.insert(0,*Order_Total_Cost_Chosen)
                Delete_Supplier_Display.insert(0,*Order_Supplier_Chosen)
                Delete_Date_Display.insert(0,*Order_Date_and_Time_Chosen)
                

            Delete_OrderID_Display = Listbox(Frame1, width = 10, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Delete_OrderID_Display.grid(row = 1, column = 0)
            
            Delete_Brand_Display = Listbox(Frame1, width = 10, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Delete_Brand_Display.grid(row = 1, column = 1)

            Delete_Product_Display = Listbox(Frame1, width = 20, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Delete_Product_Display.grid(row = 1, column = 2)
            
            Delete_Quantity_Display = Listbox(Frame1, width = 5, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Delete_Quantity_Display.grid(row = 1, column = 3)

            Delete_Cost_Display = Listbox(Frame2, width = 10, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Delete_Cost_Display.grid(row = 1, column = 0)

            Delete_Supplier_Display = Listbox(Frame2, width = 15, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Delete_Supplier_Display.grid(row = 1, column = 1)

            Delete_Date_Display = Listbox(Frame2, width = 20, height = 1, font =('arial',20,'bold'), bd=5, relief='ridge',
                                         bg = 'White', fg = 'Black')
            Delete_Date_Display.grid(row = 1, column = 2)


            Selected_Product()

            def Delete():

                Cancel_Order_PIP = []
                Cancel_Order_Supplier_Name = []
                Cancel_Order_Supplier_Email = []

                self.confirm = tkinter.messagebox.askyesno("Confirm Deletion of Data!", "Are you sure you want to cancel this order")

                if self.confirm > 0:

                    Cancel_Order_PIP.clear()
                    Cancel_Order_Supplier_Name.clear()
                    Cancel_Order_Supplier_Email.clear()

                    con = sqlite3.connect("Stock_Management_Database.db")
                    cur = con.cursor()
                    cur.execute('SELECT PIP FROM "Place_Order" WHERE (OrderID = (:OrderID_PIP))',
                                {
                                    "OrderID_PIP" : OrderID_Chosen
                                })
                    Order_PIP_Fetched = cur.fetchone()
                    Cancel_Order_PIP.append(Order_PIP_Fetched[0])

                    con = sqlite3.connect("Stock_Management_Database.db")
                    cur = con.cursor()
                    cur.execute('SELECT Supply_Name, Email FROM "Place_Order","Product_Info","Supplier" WHERE (OrderID = (:OrderID_Email)) AND (Place_Order.PIP = Product_Info.PIP) AND (Product_Info.SupplyID = Supplier.SupplyID)',
                                {
                                    "OrderID_Email" : OrderID_Chosen
                                })
                    OrderID_rows = cur.fetchall()
                
                    rowNr = 0
            
                    for row in OrderID_rows:
                        if len(row) < 1:
                            continue

                        if rowNr >= 0:
                            Cancel_Order_Supplier_Name.append(row[0])
                            Cancel_Order_Supplier_Email.append(row[1])

                        rowNr = rowNr + 1

                    Cancel_Order_Date = Order_Date_and_Time_Chosen[0]
                    Cancel_OrderID = (OrderID_Chosen)

                    port = 465

                    smtp_server = "smtp.gmail.com"
                    sender_email = os.environ.get('Pharmacy_Email')
                    receiver_email = str(Cancel_Order_Supplier_Email[0])
                    password = os.environ.get('Pharmacy_Password')

                    
                    Email_Message =("""From: Sam
To: %s
Subject: %s
To Whom It May Concern,

We would like to CANCEL an order placed on %s, with OrderID - %s.
The order was to purchase %s packages of %s, %s. With PIP Code - %s.

Our details are as follows

Pharmacy Name - Supercare Pharmacy
Phone Number - xxxxxxxxxxx
Fax - xxxxxxxxxxxx
Address - xxxxx, xxx xxxxxx, xxx xxxx

Many Thanks

Supercare Pharmacy

Sent via Python! 
"""%(receiver_email,Cancel_Order_PIP[0],Cancel_Order_Date,Cancel_OrderID,int(Order_Quantity_Chosen[0]),Order_Brand_Name_Chosen[0],Order_Product_Discription_Chosen[0],Cancel_Order_PIP[0]))

                    try:
                       context = ssl.create_default_context()
                       with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                          server.login(sender_email, password)
                          server.sendmail(sender_email, receiver_email, Email_Message)
                       messagebox.showinfo("Email","Successfully sent cancelation email to %s, %s"%(Cancel_Order_Supplier_Email[0],Cancel_Order_Supplier_Name[0]))  
                    except Exception:  
                       messagebox.showerror("Email Error!","Error: unable to send cancelation email")  
                        
                    con = sqlite3.connect("Stock_Management_Database.db")
                    cur = con.cursor()
                    cur.execute('DELETE FROM "Place_Order" WHERE (OrderID = (:OrdeID_To_Delete))',
                                {    
                                   'OrdeID_To_Delete' : OrderID_Chosen
                                })
                    con.commit()
                    con.close()
                    
                    Delete_Order_Win.destroy()

                    Order_Brand_Name_Chosen.clear()
                    Order_Product_Discription_Chosen.clear()
                    Order_Quantity_Chosen.clear()
                    Order_Total_Cost_Chosen.clear()
                    Order_Supplier_Chosen.clear()
                    Order_Date_and_Time_Chosen.clear()

                    self.Clear_Order_History_List()

                    OrderID.clear()
                    Order_PIP.clear()
                    Order_Quantity.clear()
                    Total_Cost.clear()
                    Dates.clear()
        
                    con = sqlite3.connect("Stock_Management_Database.db")
                    cur = con.cursor()
                    cur.execute('SELECT OrderID, PIP, Order_Quantity, Total_Cost, Date_Placed FROM "Place_Order" ORDER BY Date_Placed desc')
                    rows = cur.fetchall()
                    con.close()
                    
                    rowNr = 0
                    
                    for row in rows:
                        if len(row) < 1:
                            continue

                        if rowNr >= 0:
                            OrderID.append(row[0])
                            Order_PIP.append(row[1])
                            Order_Quantity.append(row[2])
                            Total_Cost.append(row[3])
                            Dates.append(row[4])

                        rowNr = rowNr + 1

                    self.lbOrderID.insert("end", *OrderID)
                    self.lbOrder_PIP.insert("end", *Order_PIP)
                    self.lbOrder_Quantity.insert("end", *Order_Quantity)
                    self.lbTotal_Cost.insert("end", *Total_Cost)
                    self.lbDate.insert("end", *Dates)

                else:
                    Delete_Order_Win.destroy()
            

            Delete_Button = Button(Frame3,text='Delete Product', width=15,font=('arial',15,'bold'), bd = 10, relief='ridge',
                                   bg='SeaGreen3', fg='Cornsilk', command = Delete)
            Delete_Button.grid(row = 0, column = 0)
        
#-------------------------------------------- Suppliers Tab Functions -------------------------------------------------#

    def Supplier_Details(self):
        
        Supplier_Name_Info = []
        Supplier_Phone = []
        Supplier_Email = []
        Supplier_Address = []


        try:
            
            Supplier_chosen = self.Suppliers_Listbox.get(self.Suppliers_Listbox.curselection())
            
        except Exception:
            
            messagebox.showerror("No Supplier Chosen!", "Please select a Supplier and try again!")

        else:
        
            con = sqlite3.connect("Stock_Management_Database.db")
            cur = con.cursor()
            cur.execute('SELECT Supply_Name, Phone, Email, Address FROM "Supplier" WHERE (Supply_Name = (:Supplier_Selected))',
                        {
                            'Supplier_Selected' : Supplier_chosen
                        })
            
            Supplier_Info_Rows = cur.fetchall()
            con.close()
            
            rowNr = 0
            
            for row in Supplier_Info_Rows:
                if len(row) < 1:
                    continue

                if rowNr >= 0:
                    Supplier_Name_Info.append(row[0])
                    Supplier_Phone.append(row[1])
                    Supplier_Email.append(row[2])
                    Supplier_Address.append(row[3])

                rowNr = rowNr + 1
                
            Chosen_Suppliers_Name_Display.insert(0,Supplier_Name_Info[0])
            Chosen_Suppliers_Phone_Display.insert(0,Supplier_Phone[0])
            Choesen_Suppliers_Email_Display.insert(0,Supplier_Email[0])
            Chosen_Suppliers_Address_Display.insert(0,Supplier_Address[0])
            

    def Add_New_Supplier(self):

            Continue = True

            # or (not any(l in Email_Domain for l in (Add_Suppliers_Email.get())))

            Email_Domain = ('.com','.ac.uk','.co.uk','.gov','.edu','.net','.org','.biz','.gov')
            Email_Domain_re = re.compile("|".join(Email_Domain))

            if (len(Add_Suppliers_Name.get()) < 1):
                messagebox.showerror("Information Error!","Please enter a Supplier Name! Try Again!")
                Continue = False
                Supplier_Name_Entered.set("")

            try:
                Phone_Number = int(Add_Suppliers_Phone.get())
            except ValueError:
                    messagebox.showerror("Invalid Data Entered!", "Please enter a valid Phone Number and try again!")
                    Continue = False
                    Phone_Entered.set("")


            if (len(Add_Suppliers_Email.get()) < 1) or ("@" not in Add_Suppliers_Email.get()) or (not Email_Domain_re.search(Add_Suppliers_Email.get())):
                messagebox.showerror("Information Error!","Please enter a valid email address! Try Again!")
                Continue = False
                Email_Entered.set("")

            if (len(Add_Suppliers_Address.get()) < 1):
               messagebox.showerror("Information Error!","Please select a Use before submiting data! Try Again!")
               Continue = False
               Address_Entered.set("")
                
            if Continue is True:
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('INSERT INTO "Supplier"(Supply_Name,Phone,Email,Address) VALUES (:Supplier_Name_Value, :Phone_Value, :Email_Value, :Address_Value)',
                            {
                                'Supplier_Name_Value' : Add_Suppliers_Name.get(),
                                'Phone_Value' : Phone_Number,
                                'Email_Value' : Add_Suppliers_Email.get(),
                                'Address_Value' : Add_Suppliers_Address.get()
                            })

                con.commit()
                con.close()

                Supplier_Name_Entered.set("")
                Phone_Entered.set("")
                Email_Entered.set("")
                Address_Entered.set("")

                Suppliers_Names.clear()
        
                self.Suppliers_Listbox.delete(0, END)
        
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('SELECT Supply_Name FROM "Supplier"')
                rows = cur.fetchall()
                con.close()
                
                rowNr = 0
                
                for row in rows:
                    if len(row) < 1:
                        continue

                    if rowNr >= 0:
                        Suppliers_Names.append(row[0])
                    rowNr = rowNr + 1

                self.Suppliers_Listbox.insert("end", *Suppliers_Names)

#---------------------------------------------- Scrollbar Functions --------------------------------------------------#

    def yview(self, *args):
        
        self.lbPIP.yview(*args)
        self.lbBrand_Name.yview(*args)
        self.lbProduct_Discription.yview(*args)
        self.lbQuantity.yview(*args)

        self.Searched_PIP_List.yview(*args)
        self.Searched_Brand_List.yview(*args)
        self.Searched_Product_Discription_List.yview(*args)
        self.Searched_Use_List.yview(*args)
        self.Searched_Supplier_List.yview(*args)
        self.Searched_Quantity_List.yview(*args)

        try:
            self.Similar_PIP_List.yview(*args)
            self.Similar_Brand_List.yview(*args)
            self.Similar_Product_Discription_List.yview(*args)
            self.Similar_Use_List.yview(*args)
            self.Similar_Supplier_List.yview(*args)
            self.Similar_Quantity_List.yview(*args)
        except AttributeError:
            return

        self.lbOrderID.yview(*args)
        self.lbOrder_PIP.yview(*args)
        self.lbOrder_Quantity.yview(*args)
        self.lbTotal_Cost.yview(*args)
        self.lbDate.yview(*args)

    def xview(self, *args):
        self.lbPIP.xview(*args)
        self.lbBrand_Name.xview(*args)
        self.lbProduct_Discription.xview(*args)
        self.lbQuantity.xview(*args)

        self.lbOrderID.xview(*args)
        self.lbOrder_PIP.xview(*args)
        self.lbOrder_Quantity.xview(*args)
        self.lbTotal_Cost.xview(*args)
        self.lbDate.xview(*args)
            

#-----------------------------------------------New Product WIndow-----------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
        
class New_Product_Window:
    
    def __init__(self, master):
        self.master = master
        self.master.title(" Add New Product Page")
        self.master.geometry("1050x650+0+0")
        self.master.config(bg ='Cadet Blue')
        self.frame = Frame(self.master, bg='Cadet Blue')
        self.frame.pack()

        PIP_Entry = StringVar()
        Product_Discription_Entry = StringVar()
        Pack_Size_Entry = StringVar()
        Product_Cost_Entry= StringVar()
        Quantity_Entry = StringVar()

#-----------------------------------------------------Frames-------------------------------------------------------------#
        
        self.frame1 = Frame(self.frame, width=700,height=50 , relief='ridge',bg='MediumPurple2', bd=40)
        self.frame1.grid(row=0, column=0)

        self.frame2 = LabelFrame(self.frame, width=710,height=125
                                      ,font=('arial',20,'bold'), relief='ridge',bg='MediumPurple2', bd=40)
        self.frame2.grid(row=1, column=0)

        self.frame3 = LabelFrame(self.frame, width=710,height=125
                                      ,font=('arial',20,'bold'), relief='ridge',bg='MediumPurple2', bd=40)
        self.frame3.grid(row=2, column=0)

        self.frame4 = LabelFrame(self.frame, width=710,height=125
                                      ,font=('arial',20,'bold'), relief='ridge',bg='MediumPurple2', bd=40)
        self.frame4.grid(row=3, column=0)

#------------------------------------------------------Label-------------------------------------------------------------#

        Title_label = Label(self.frame1, text = "Add New Product", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 20, bg = 'MediumPurple2', fg = 'White')
        Title_label.grid(row = 0, column = 0, pady = 10)

        PIP_label = Label(self.frame2, text = "PIP", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 10, bg = 'MediumPurple2', fg = 'White')
        PIP_label.grid(row = 0, column = 0)

        BrandID_label = Label(self.frame2, text = "Brand Name", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 15, bg = 'MediumPurple2', fg = 'White')
        BrandID_label.grid(row = 0, column = 1)

        Product_Discription_label = Label(self.frame2, text = "Product Discription", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 25, bg = 'MediumPurple2', fg = 'White')
        Product_Discription_label.grid(row = 0, column = 2)

        UseID_label = Label(self.frame2, text = "Use", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 10, bg = 'MediumPurple2', fg = 'White')
        UseID_label.grid(row = 0, column = 3)

        Pack_Size_label = Label(self.frame3, text = "Pack Size", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 10, bg = 'MediumPurple2', fg = 'White')
        Pack_Size_label.grid(row = 0, column = 0)

        Product_Cost_label = Label(self.frame3, text = "Product Cost", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 15, bg = 'MediumPurple2', fg = 'White')
        Product_Cost_label.grid(row = 0, column = 1)

        SupplyID_label = Label(self.frame3, text = "Supplier", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 10, bg = 'MediumPurple2', fg = 'White')
        SupplyID_label.grid(row = 0, column = 2)

        Quantity_label = Label(self.frame3, text = "Quantity", font=('arial',15,'bold'), bd = 10, relief='ridge',
                                 width = 10, bg = 'MediumPurple2', fg = 'White')
        Quantity_label.grid(row = 0, column = 3)

#---------------------------------------------------------------Lists---------------------------------------------------------#

        Brands = []
        Uses = []
        Suppliers = []
        
#------------------------------------------------------------Entry Boxes------------------------------------------------------#

        PIP_Entrybox = Entry(self.frame2, font=('arial',20,'bold'),bd=7,textvariable=PIP_Entry, width = 10)
        PIP_Entrybox.grid(row=2,column=0)


        def List_Brands(): 
            con = sqlite3.connect("Stock_Management_Database.db")
            cur = con.cursor()
            cur.execute('SELECT Brand_Name FROM "Brands"')
            rows = cur.fetchall()
            
            rowNr = 0
            
            for row in rows:
                if len(row) < 1:
                    continue

                if rowNr >= 0:
                    Brands.append(row[0])

                rowNr = rowNr + 1

        def List_Uses(): 
            con = sqlite3.connect("Stock_Management_Database.db")
            cur = con.cursor()
            cur.execute('SELECT Use FROM "Uses"')
            rows = cur.fetchall()
            
            rowNr = 0
            
            for row in rows:
                if len(row) < 1:
                    continue

                if rowNr >= 0:
                    Uses.append(row[0])

                rowNr = rowNr + 1
                
        def List_Suppliers(): 
            con = sqlite3.connect("Stock_Management_Database.db")
            cur = con.cursor()
            cur.execute('SELECT Supply_Name FROM "Supplier"')
            rows = cur.fetchall()
            
            rowNr = 0
            
            for row in rows:
                if len(row) < 1:
                    continue

                if rowNr >= 0:
                    Suppliers.append(row[0])

                rowNr = rowNr + 1
                
        List_Brands()
        List_Uses()
        List_Suppliers()
        
        Brand_Menu = StringVar()
        Brand_Menu.set("Pick a Brand")

        Brand_Name_DropDownMenu = OptionMenu(self.frame2, Brand_Menu, *Brands)
        Brand_Name_DropDownMenu.grid(row=2,column=1)
        
        Product_Discription_Entrybox = Entry(self.frame2, font=('arial',20,'bold'),bd=7,textvariable = Product_Discription_Entry, width = 20)
        Product_Discription_Entrybox.grid(row=2,column=2)
        
        Use_Menu = StringVar()
        Use_Menu.set("Pick a Use")
        
        Use_DropDownMenu = OptionMenu(self.frame2, Use_Menu, *Uses)
        Use_DropDownMenu.grid(row=2,column=3)
        
        Pack_Size_Entrybox = Entry(self.frame3, font=('arial',20,'bold'),bd=7,textvariable = Pack_Size_Entry, width = 5)
        Pack_Size_Entrybox.grid(row=2,column=0)

        Product_Cost_Entrybox = Entry(self.frame3, font=('arial',20,'bold'),bd=7,textvariable = Product_Cost_Entry, width = 5)
        Product_Cost_Entrybox.grid(row=2,column=1)
        
        Supply_Menu = StringVar()
        Supply_Menu.set("Pick a Supplier")

        Supply_Name_DropDownMenu = OptionMenu(self.frame3, Supply_Menu, *Suppliers)
        Supply_Name_DropDownMenu.grid(row=2,column=2)

        Quantity_Entrybox = Entry(self.frame3, font=('arial',20,'bold'),bd=7,textvariable = Quantity_Entry, width = 5)
        Quantity_Entrybox.grid(row=2,column=3)

        def Reset():
            PIP_Entry.set("")
            Brand_Menu.set("Pick a Brand")
            Product_Discription_Entry.set("")
            Use_Menu.set("Pick a Use")
            Pack_Size_Entry.set("")
            Product_Cost_Entry.set("")
            Supply_Menu.set("Pick a Supplier")
            Quantity_Entry.set("")
        
        def add_new_product():

            Continue = True
            
            def BrandID_from_Brand_Name():
                global Fetched_BrandID
                Check_Brand_Name = Brand_Menu.get()
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('SELECT BrandID FROM "Brands" WHERE  Brand_Name = (:Brand_Name_Dic)',
                            {
                                'Brand_Name_Dic' : Check_Brand_Name

                            })
                Fetched_BrandID = cur.fetchone()
            
            def UseID_from_Uses():
                global Fetched_UseID
                Check_Uses = Use_Menu.get()
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('SELECT UseID FROM "Uses" WHERE  Use = (:Uses_Dic)',
                            {
                                'Uses_Dic' : Check_Uses
                            })
                Fetched_UseID = cur.fetchone()

            def SupplyID_from_Supply_Name():
                global Fetched_SupplyID
                Check_Supply_Name = Supply_Menu.get()
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('SELECT SupplyID FROM "Supplier" WHERE  Supply_Name = (:Supply_Name_Dic)',
                            {
                                'Supply_Name_Dic': Check_Supply_Name
                            })
                Fetched_SupplyID = cur.fetchone()
                
                
            BrandID_from_Brand_Name()
            UseID_from_Uses()
            SupplyID_from_Supply_Name()
            

            try:
                PIP_Entered = int(PIP_Entry.get())
            except ValueError:
                    messagebox.showerror("Invalid Data Entered!", "Please enter an integer value for the PIP number! Try Again!")
                    PIP_Entry.set("")
                    Continue = False
                    
                    
            try:
                BrandID = Fetched_BrandID[0]
            except TypeError:
                messagebox.showerror("Brand Name Error!", "Please select a Brand and try again!")
                Continue = False

            if (len(Brand_Menu.get()) < 1):
                messagebox.showerror("Information Error!","Please Select a Brand before submitting data! Try Again!")
                Continue = False
                Brand_Menu.set("Pick a Brand")
                

            if (len(Product_Discription_Entry.get()) < 1):
                messagebox.showerror("Information Error!","Please fill in a valid discription before submitting data! Try Again!")
                Continue = False
                Product_Discription_Entry.set("")
                

            try:
                UseID = Fetched_UseID[0]
            except TypeError:
                messagebox.showerror("Use Error!", "Please select a Use and try again!")
                Continue = False

            if (len(Use_Menu.get()) < 1):
               messagebox.showerror("Information Error!","Please select a Use before submitting data! Try Again!")
               Continue = False
               Use_Menu.set("Pick a Use")
               

            try:
                Pack_Size_Entered = int(Pack_Size_Entry.get())
            except ValueError:
                messagebox.showerror("Invalid Data Entered!", "Please enter an integer value for the Pack Size! Try Again!")
                Continue = False
                Pack_Size_Entry.set("")
                
            try:
                Product_Cost_Entered = (Product_Cost_Entry.get())
                integral, fractional = Product_Cost_Entered.split('.')
                Product_Cost_Entered = float(Product_Cost_Entered)
                if len(fractional) == 2 and Product_Cost_Entered > 0:
                    pass
                else:
                    messagebox.showerror("Invalid Data Entered!", "Please enter a float value for the Product Cost rounded to two decimal places! Try Again!")
                    Product_Cost_Entry.set("")
            except ValueError:
                messagebox.showerror("Invalid Data Entered!", "Please enter a float value for the Product Cost rounded to two decimal places! Try Again!")
                Continue = False
                Product_Cost_Entry.set("")
            
                    
            try:
                SupplyID = Fetched_SupplyID[0]
            except TypeError:
                messagebox.showerror("Supplier Error!", "Please select a Supplier and try again!")
                Continue = False

            if (len(Supply_Menu.get()) < 1):
                messagebox.showerror("Information Error!","Please select a Supplier before submitting data! Try Again!")
                Continue = False
                Supply_Menu.set("Pick a Supplier")
                

            try:
                Quantity_Entered = int(Quantity_Entry.get())
            except ValueError:
                messagebox.showerror("Invalid Data Entered!", "Please enter an integer value for the Quantity! Try Again!")
                Continue = False
                Quantity_Entry.set("")
                    

            if Continue is True:
                con = sqlite3.connect("Stock_Management_Database.db")
                cur = con.cursor()
                cur.execute('INSERT INTO "Product_Info" VALUES (:PIP_Value, :BrandID_Value, :Product_Discription_Value, :UseID_Value, :Pack_Size_Value, :Product_Cost_Value, :SupplyID_Value, :Quantity_Value)',
                            {
                                'PIP_Value' : PIP_Entry.get(),
                                'BrandID_Value' : BrandID,
                                'Product_Discription_Value' : Product_Discription_Entry.get(),
                                'UseID_Value' : UseID,
                                'Pack_Size_Value' : Pack_Size_Entry.get(),
                                'Product_Cost_Value' : Product_Cost_Entry.get(),
                                'SupplyID_Value' : SupplyID,
                                'Quantity_Value' : Quantity_Entry.get()
                            })

                con.commit()
                con.close()
                messagebox.showinfo("Entry Sucessful!", "The new product has been sucessfully entered!")
                Add_More = tkinter.messagebox.askyesno("Add More Data?", "Would you like to add another new product?")
                if Add_More > 0:
                    Reset()
                else:
                    self.master.destroy()


        Add_New_Data_Button = Button(self.frame4, text = "Add New Product", width=15,font=('arial',20,'bold'), bd =10, relief='ridge',
                               bg='SlateBlue2', fg='Cornsilk', command = add_new_product)
        Add_New_Data_Button.grid (row = 0, column = 0)

        Reset_Button = Button(self.frame4, text = "Reset", width=10,font=('arial',20,'bold'), bd =10, relief='ridge',
                               bg='SlateBlue2', fg='Cornsilk', command = Reset)
        Reset_Button.grid (row = 0, column = 1)

#--------------------------------------------------------------Fubctions---------------------------------------------------#


#-------------------------------------------------------------Admin Window-------------------------------------------------#
#------------------------------------------------------------------=-------------------------------------------------------#
     
class Admin:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin Page")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg ='Cadet Blue')
        self.frame = Frame(self.master, bg='Cadet Blue')
        self.frame.pack()
        
        self.New_User = StringVar()
        self.New_Pass = StringVar()
        self.Confirm_Pass = StringVar()
        
        self.lblTitle = Label(self.frame, text = 'Admin Page', font =('arial', 60, 'bold'),
                             bg='Cadet Blue', fg='Cornsilk')
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=20)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Frames~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        self.AdminFrame1 = LabelFrame(self.frame, width=1350,height=500
                                      ,text="ADMIN EYES ONLY",font=('arial',20,'bold'), relief='ridge',bg='SlateBlue2', bd=40)
        self.AdminFrame1.grid(row=1, column=0)

        self.AdminFrame2 = LabelFrame(self.frame, width=1000,height=200
                                      ,font=('arial',20,'bold'), relief='ridge',bg='SlateBlue2', bd=40)
        self.AdminFrame2.grid(row=2, column=0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Inputs Entries UserName & Password~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        self.lblNew_User = Label(self.AdminFrame1, text = 'Username', font =('arial',30,'bold'),bd=22,
                                 bg = 'SlateBlue2', fg = 'Cornsilk')
        self.lblNew_User.grid(row=0,column=0)

        self.txtNew_User = Entry(self.AdminFrame1,font=('arial',30,'bold'),bd=7,textvariable=self.New_User,
                                 width = 30)
        self.txtNew_User.grid(row=0,column=1,padx=88)

        self.lblNew_Pass = Label(self.AdminFrame1,text='Password',font=('arial',30,'bold'),bd=22,
                                 bg='SlateBlue2', fg = 'Cornsilk')
        self.lblNew_Pass.grid(row=1,column=0)

        self.txtNew_Pass = Entry(self.AdminFrame1, font =('arial',30,'bold'),bd=7,textvariable=self.New_Pass,
                                 width=30)
        self.txtNew_Pass.grid(row=1,column=1,columnspan=2,pady=30)
        
        self.lblConfirm_Pass = Label(self.AdminFrame1,text='Confirm Password',font=('arial',30,'bold'),bd=22,
                                 bg='SlateBlue2', fg = 'Cornsilk')
        self.lblConfirm_Pass.grid(row=2,column=0)

        self.txtConfirm_Pass = Entry(self.AdminFrame1, font =('arial',30,'bold'),bd=7,textvariable=self.Confirm_Pass,
                                 width=30)
        self.txtConfirm_Pass.grid(row=2,column=1,columnspan=2,pady=30)
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Buttons ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        self.btnUser_Info = Button(self.AdminFrame2, text='Create New User', width=15,font=('arial',25,'bold'),
                               bg='SlateBlue2', fg='Cornsilk', command=self.Checks)
        self.btnUser_Info.grid(row=3,column=0,pady=20,padx=8)

        self.btnReset = Button(self.AdminFrame2, text='Reset', width=10,font=('arial',25,'bold'),
                               bg='SlateBlue2', fg='Cornsilk', command=self.Reset_Com)
        self.btnReset.grid(row=3,column=1,pady=20,padx=8)

        self.btnDisplay = Button(self.AdminFrame2, text='Display Users', width=15,font=('arial',25,'bold'),
                               bg='SlateBlue2', fg='Cornsilk', command=self.Display_Users)
        self.btnDisplay.grid(row=3,column=2,pady=20,padx=8)

        self.btnExit = Button(self.AdminFrame2, text='Exit', width=10,font=('arial',25,'bold'),
                               bg='SlateBlue2', fg='Cornsilk', command=self.Exit_Com)
        self.btnExit.grid(row=3,column=3,pady=20,padx=8)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Subroutines ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
    def Password_Error_Message(self):
        self.Password_Error_Message = messagebox.showerror("Password Does Not Meet Criteria", """Please Make Sure your Password:
                                                          \n 1) Is at least 8 Characters long
                                                          \n 2) Has at least one number in it
                                                          \n 3) Has a Capital letter
                                                          \n 4) Has at least one Special Characters from: ($,#,@,!,*,.,_,&,!,£,^)
                                                          \n              Would you like to try again?                          """)
        return

    def Checks(self):
        Check_User = (self.New_User.get())
        Check_Pass = (self.New_Pass.get())
        Check_Confirm = (self.Confirm_Pass.get())

        Special_Characters = ['$', '#', '@', '!', '*', ".", "_", "&", "!", "£", "^"]
        

        if Check_User in User_Names:
            messagebox.showerror("Username Error!", "User Already Exists, Try again!")
            self.New_User.set("")
            self.New_Pass.set("")
            self.Confirm_Pass.set("")
        else:
            if Check_Pass != Check_Confirm:
                messagebox.showerror("Password Error!", "Passwords Do Not Match! , Try again!")
                self.New_Pass.set("")
                self.Confirm_Pass.set("")
                
            else:
                while True:
                    if (len(Check_Pass) < 8) or (re.search('[0-9]', Check_Pass) is None) or (re.search('[A-Z]',Check_Pass) is None) or (not any(c in Special_Characters for c in Check_Pass)):
                        messagebox.showerror("Password Does Not Meet Criteria", """Please make sure your password:
                                                                  \n 1) Is at least 8 Characters long
                                                                  \n 2) Has at least one number in it
                                                                  \n 3) Has a Capital letter
                                                                  \n 4) Has at least one Special Characters from: ($,#,@,!,*,.,_,&,!,£,^)
                                                                  \n              Please try again!                          """)
                        self.New_Pass.set("")
                        self.Confirm_Pass.set("")
                        return
                    else:
                        User_Names.append(Check_User)
                        Passes.append(Check_Pass)
                        Added_NewUser = [Check_User, Check_Pass]
                        append_NewUser_CSV('Users.csv', Added_NewUser)
                        self.New_User.set("")
                        self.New_Pass.set("")
                        self.Confirm_Pass.set("")
                        messagebox.showinfo("New User Added!","A New User Has Been Sucessfully Added!")
                        return
                        break
 
        
    def Reset_Com(self):
        self.New_User.set("")
        self.New_Pass.set("")
        self.Confirm_Pass.set("")

                
    def Display_Users(self):
        self.master.destroy()
        Tk().withdraw()
        self.Display_Users = Toplevel()
        self.app = Display_Window(self.Display_Users)

    def return_to_login(self):
        self.master.destroy()
        Tk().withdraw()
        self.return_to_login = Toplevel()
        self.app = Login(self.return_to_login)
        
    def Exit_Com(self):
        self.Exit_Com = tkinter.messagebox.askyesno("*!Quit System!*", "Confirm Exit")
        if self.Exit_Com > 0:
            self.return_to_login()
            return
        else:
            return

#------------------------------------------------Display Users Window---------------------------------------------#
#---------------------------------------------------------------=-------------------------------------------------#
     
class Display_Window:
    global User_Names
    global Passes
    
    def __init__(self, master):
        #Zipped_Lists = zip(User_Names,Passes)
        #Users_and_Passwords = (list(Zipped_Lists))
        self.master = master
        self.master.title("Display Users Page")
        self.master.geometry("950x650+275+0")
        self.master.config(bg ='Thistle2')
        self.frame = Frame(self.master, bg='Thistle2')
        self.frame.pack()
        
        self.New_User = StringVar()
        self.New_Pass = StringVar()
        self.Confirm_Pass = StringVar()
        
        self.lblTitle = Label(self.frame, text = 'Display Users Page', font =('arial', 40, 'bold'),
                             bg='Thistle2', fg='Cadet Blue')
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=5)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Frames~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        self.frame1 = LabelFrame(self.frame, width=1350,height=400
                                      ,text="UserNames and Passwords",font=('arial',20,'bold'), relief='ridge',bg='MediumPurple2', bd=40)
        self.frame1.grid(row=1, column=0)

        self.frame2 = LabelFrame(self.frame, width=500,height=150
                                      ,font=('arial',20,'bold'), relief='ridge',bg='MediumPurple2', bd=40)
        self.frame2.grid(row=2, column=0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Labels~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        self.scrollbar_V = Scrollbar(self.frame1)
        self.scrollbar_H_User = Scrollbar(self.frame1, orient=HORIZONTAL)
        self.scrollbar_H_Password = Scrollbar(self.frame1, orient=HORIZONTAL)
        self.scrollbar_V.grid(row = 0, column = 4, sticky=N+S+W)
        self.scrollbar_H_User.grid(row = 1, column = 1, sticky=N+E+S+W)
        self.scrollbar_H_Password.grid(row = 1, column = 2, sticky=N+E+S+W)
        
        def populateListbox(User,Pass):
            self.lbUser.insert("end", *User)
            self.lbPassword.insert("end", *Pass)

        self.lbUser = Listbox(self.frame1, font=('arial',12,'bold'), width = 20, height = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_User.set)
        self.lbUser.grid(row=0,column=1,pady=20,padx=8)

        self.lbPassword = Listbox(self.frame1, font=('arial',12,'bold'), width = 20, height = 10, yscrollcommand=self.scrollbar_V.set, xscrollcommand=self.scrollbar_H_Password.set)
        self.lbPassword.grid(row=0,column=2,pady=20,padx=8)

        self.scrollbar_V.config(command=self.yview)
        self.scrollbar_H_User.config(command=self.xview)
        self.scrollbar_H_Password.config(command = self.lbPassword.xview)

        populateListbox(User_Names, Passes)
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Buttons~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        self.btnExit = Button(self.frame2, text='Exit', width=10,font=('arial',25,'bold'),
                               bg='MediumPurple2', fg='Cornsilk', command=self.Exit_Com)
        self.btnExit.grid(row=3,column=3,pady=20,padx=8)

#--------------------------------------------------- Functions -------------------------------------------------------------#

    def yview(self, *args):
        self.lbUser.yview(*args)
        self.lbPassword.yview(*args)

    def xview(self, *args):
        self.lbUser.xview(*args)
        self.lbPassword.xview(*args)

    def return_to_admin(self):
        self.master.destroy()
        Tk().withdraw()
        self.return_to_admin = Toplevel()
        self.app = Admin(self.return_to_admin)
        
    def Exit_Com(self):
            self.Exit_Com = tkinter.messagebox.askyesno("*!Quit System!*", "Confirm Exit")
            if self.Exit_Com > 0:
                self.return_to_admin()
                return
            else:
                return

#----------------------------------------------------Main Loop------------------------------------------------------#

if __name__ == '__main__':
    main()
    
