from datetime import date, datetime
from os import name, pipe, replace
from tkinter import*
from PIL import ImageTk
import pymysql
from tkinter import messagebox
import cv2 
from pyzbar.pyzbar import decode
from PIL import Image 



root = Tk()


name_of_user = ''


class Mainwindow:
    def __init__(self, root):
        self.root = root
        self.root.title('User Login')
        self.root.geometry('1200x700+200+70')
        self.root.resizable(False, False)

        #back_gorund
        self.image = ImageTk.PhotoImage(file = 'drugs_make_new_account.png')
        self.label = Label(self.root, image=self.image)
        self.label.pack()

        #Frame
        self.frame = Frame(self.root)
        self.frame.place(x=390, y=170, width=400, height=450)

        #Labels and Entries
        self.user_name = Label(self.frame, text='Username', font=('Andalus', 15, 'bold'), fg='black')
        self.user_name.place(x=80, y=50)

        self.entry1 = Entry(self.frame, font=('Andalus', 15))
        self.entry1.place(x=80, y=100, width=250)

        self.passlabel = Label(self.frame, text='Password', font=('Andalus', 15,  'bold'), fg='black')
        self.passlabel.place(x=80, y=150)

        self.entry2 = Entry(self.frame, show='*', font=('times new roman', 15), fg='black')
        self.entry2.place(x=80, y=200, width=250)

        self.button_login = Button(self.frame, text='Login', activebackground='#00B0F0', activeforeground='white',
                                    fg='black', font=('Arial', 15, 'bold'), command=lambda: self.logindata())
        self.button_login.place(x=80, y=250, width=250)


        self.button_create_new_user = Button(self.frame, text='Create Account', activebackground='#00B0F0', activeforeground='white',
                                             fg='black', font=('Arial', 15, 'bold'), command=lambda: Cenerate_New_User())
        self.button_create_new_user.place(x=80, y=300, width=250)

        self.button_reset_password = Button(self.frame, text='Forgot Password', activebackground='#00B0F0', activeforeground='white',
                                             fg='black', font=('Arial', 15, 'bold'))
        self.button_reset_password.place(x=80, y=350, width=250)



    def logindata(self):
        con = pymysql.connect(host='localhost', user='root', passwd='', database='drug_store')
        cur = con.cursor()
        cur.execute('use drug_store')
        cur.execute("Select * from user_information where Username=%s and Password=%s", (self.entry1.get(), self.entry2.get()))
        row = cur.fetchone()
        if row == None:
            messagebox.showerror('WARNING', 'USER NOT FOUND!')
        else:
            messagebox.showinfo('Succesfull', 'login')
            User_Interface(root)
        global name_of_user
        name_of_user = self.entry1.get()


class Cenerate_New_User:
    def __init__(self):
        self.root = root
        self.root.title('Create Account')
        self.root.geometry('1200x700+200+70')
        self.root.resizable(False, False)

        #back_gorund
        self.image = ImageTk.PhotoImage(file = 'drugs_make_new_account.png')
        self.label = Label(self.root, image=self.image)
        self.label.pack()

        #Frame
        self.frame = Frame(self.root)
        self.frame.place(x=390, y=170, width=400, height=450)

        #Labels and Entries
         

        self.user_name = Label(self.frame, text='Username:', font=('Andalus', 15, 'bold'), fg='black')
        self.user_name.place(x=80, y=50)

        
        self.entry1 = Entry(self.frame, font=('Andalus', 15))
        self.entry1.place(x=80, y=80, width=250)

        #global name_of_user
        #name_of_user = self.entry1.get()

        self.email = Label(self.frame, text='Email:', font=('Andalus', 15,  'bold'), fg='black')
        self.email.place(x=80, y=110)

        self.entry2 = Entry(self.frame, font=('times new roman', 15), fg='black')
        self.entry2.place(x=80, y=140, width=250)

        self.password = Label(self.frame, text='Password:', font=('Andalus', 15, 'bold'), fg='black')
        self.password.place(x=80, y=170)

        self.entry3 = Entry(self.frame, show='*', font=('Andalus', 15))
        self.entry3.place(x=80, y=200, width=250)

        self.repeat_password = Label(self.frame, text='Repete Password:', font=('Andalus', 15, 'bold'), fg='black')
        self.repeat_password.place(x=80, y=230)

        self.entry4 = Entry(self.frame, show='*', font=('Andalus', 15))
        self.entry4.place(x=80, y=260, width=250)

        self.address = Label(self.frame, text='Address:', font=('Andalus', 15,  'bold'), fg='black')
        self.address.place(x=80, y=290)

        self.entry5 = Entry(self.frame, font=('times new roman', 15), fg='black')
        self.entry5.place(x=80, y=320, width=250)

        self.age = Label(self.frame, text='Age', font=('Andalus', 15), fg='black')
        self.age.place(x=80, y=350)

        self.entry6 = Entry(self.frame, font=('times new roman', 15), fg='black')
        self.entry6.place(x=80, y=380, width=50)

        #set Gender
        self.Genders = ['m', 'f']
        self.varialbe = StringVar(self.frame)
        self.varialbe.set(self.Genders[0])
        self.gender = OptionMenu(self.frame, self.varialbe, *self.Genders)
        self.gender_lable = Label(self.frame, text='Gender:', font=('Andalus', 15,  'bold'), fg='black')
        self.gender_lable.place(x=80, y=410)
        self.gender.place(x=160, y=410)

        #Buttons
        self.button_create_account = Button(self.frame, text='Create', activebackground='#00B0F0', activeforeground='white',
                                    fg='black', font=('Arial', 10, 'bold'), command=lambda: self.create_user_account())
        self.button_create_account.place(x=300, y=410, width=50)

    def create_user_account(self):
        if self.entry3.get() != self.entry4.get():
            messagebox.showerror('Warning', 'Repeated Password is not like Password')
        con = pymysql.connect(host='localhost', user='root', passwd='', database='drug_store')
        cur = con.cursor()
        cur.execute('use drug_store')
        all_user_names = cur.fetchall()
        if (self.entry1.get(),) in all_user_names:
            messagebox.showerror('Warning', 'Username already taken')
        elif self.entry3.get() != self.entry4.get():
            messagebox.showerror('Warning', 'Repeted Password is not like Password')
        elif len(self.entry1.get()) == 0:
            messagebox.showerror('Warning','Please enter an Username')
        elif len(self.entry2.get()) == 0:
            messagebox.showerror('Warning','Please enter an Email')
        elif len(self.entry3.get()) == 0:
            messagebox.showerror('Warning','Please enter a Password')
        elif len(self.entry5.get()) == 0:
            messagebox.showerror('Warning','Please enter a Addresse')
        elif len(str(self.entry6.get())) == 0:
            messagebox.showerror('Warning','Please enter a name ')
        else: 
            cur.execute('SHOW TABLES')
            sqlFormula = 'INSERT INTO user_information(Username, Password, Email, Age, Gender, Address) VALUES (%s, %s, %s, %s, %s, %s)'
            user_to_add = (self.entry1.get(), self.entry3.get(), self.entry2.get(), self.entry6.get(), self.varialbe.get(), self.entry5.get())
            cur.execute(sqlFormula, user_to_add)
            con.commit()
            sqlFormula_Create_User_Table = 'CREATE TABLE `{user_name}` (drug_name VARCHAR(233) NOT NULL, purchase_date DATE NOT NULL, expiry_date DATE NOT NULL, dosis_per_day INT NOT NULL);'.format(user_name=self.entry1.get()) 
            #print(sqlFormula_Create_User_Table)
            cur.execute(sqlFormula_Create_User_Table)
            con.commit()
            Mainwindow(root)



class User_Interface:
    
    def __init__(self, root):
        self.root = root
        self.root.title('User Login')
        self.root.geometry('1200x700+200+70')
        self.root.resizable(False, False)
        

        #back_gorund
        self.image = ImageTk.PhotoImage(file = 'drugs.png')
        self.label = Label(self.root, image=self.image)
        self.label.pack()

        #Frame
        self.frame = Frame(self.root)
        self.frame.place(x=200, y=50, width=800, height=600)

        #Drug_Information
        self.drugs_list = ['Abilify', 'Aspirin', 'Berocca', 'Clamycin', 'Dafalgan', 'Diovan', 'Entresto', 'Ferriprox', 'Gracial', 'Haldol', 'Ibuprofen',	'Jakavi', 'Ketalgin', 'Lamotrin', 'Mebucaine', 'Neo-Angin', 'Oxycodon',	'Panadol', 'Pretuval',	
                        'Risperdal', 'Sifrol', 'Similasan', 'Targin', 'Trimipramine', 'Uptravi', 'Valium', 'Vitamin B1', 'Xanax', 'Yantil', 'Zestril']
        self.varialbe = StringVar(self.frame)
        self.varialbe.set(self.drugs_list[0])
        self.availabele_drugs = OptionMenu(self.frame, self.varialbe, *self.drugs_list)
        self.drugs_lable = Label(self.frame, text='Drugs:', font=('Andalus', 15,  'bold'), fg='black')
        self.drugs_lable.place(x=80, y=410)
        self.availabele_drugs.place(x=160, y=410)

        
        

        
        """
        con = pymysql.connect(host='localhost', user='root', passwd='', database='drug_store')
        cur =con.cursor()
        print(name_of_user)
        """
        #self.sql_formula = "SELECT * FROM {username}".format(username=name_of_user)
        
        #print(self.sql_formula)
        """
        cur.execute(self.sql_formula)
        self.fetched_inventory = cur.fetchall()
        print(self.fetched_inventory)
        """

        """
        self.list_of_inventory_of_user = []
        for user_drug in self.fetched_inventory:
            self.list_of_inventory_of_user.append(user_drug)
        
        self.varialbe_to_delete_inventory = StringVar(self.frame)
        self.varialbe.set(self.list_of_inventory_of_user[0])
        self.availabele_drugs_in_inventory = OptionMenu(self.frame, self.varialbe, *self.list_of_inventory_of_user)
        self.availabele_drugs_in_inventory.place(x=160, y=150)
        """
        

        #Buttons 
        self.show_drug_information = Button(self.frame, command= lambda: self.get_drug_info(), text='Info', activebackground='#00B0F0', activeforeground='white',
                                    fg='black', font=('Arial', 10, 'bold'),)
        self.show_drug_information.place(x=300, y=410, width=100)

        self.button_add_drug = Button(self.frame, text='Add Drug', activebackground='#00B0F0', activeforeground='white',
                                    fg='black', font=('Arial', 15, 'bold'), command= lambda: self.decode_QR_Code())
        self.button_add_drug.place(x=80, y=100, width=250)

        self.button_remove_drug = Button(self.frame, text='Remove Drug', activebackground='#00B0F0', activeforeground='white',
                                             fg='black', font=('Arial', 15, 'bold'), command=lambda: self.chose_drug_to_remove())
        self.button_remove_drug.place(x=80, y=150, width=250)

        self.button_show_expiry_dates = Button(self.frame, text='Show Expiry Dates', activebackground='#00B0F0', activeforeground='white',
                                             fg='black', font=('Arial', 15, 'bold'), command=lambda: self.expiry_date())
        self.button_show_expiry_dates.place(x=80, y=200, width=250)

        self.button_show_inventory_at_home = Button(self.frame, text='Show Inventory at Home', activebackground='#00B0F0', activeforeground='white',
                                             fg='black', font=('Arial', 15, 'bold'), command=lambda: self.show_inventory_at_home())
        self.button_show_inventory_at_home.place(x=80, y=250, width=250)

        self.button_exit = Button(self.frame, text='Exit Programm', activebackground='#00B0F0', activeforeground='white',
                                             fg='black', font=('Arial', 10, 'bold'), command=self.frame.quit)
        self.button_exit.place(x=600, y=550, width=100)

        """
        self.Genders = ['m', 'f']
        self.varialbe = StringVar(self.frame)
        self.varialbe.set(self.Genders[0])
        self.gender = OptionMenu(self.frame, self.varialbe, *self.Genders)
        self.gender_lable = Label(self.frame, text='Choose Drug:', font=('Andalus', 15,  'bold'), fg='black')
        self.gender_lable.place(x=500, y=100)
        self.gender.place(x=700, y=100)
        """



    def get_drug_info(self):
        con = pymysql.connect(host='localhost', user='root', passwd='', database='drug_store')
        cur = con.cursor()
        cur.execute('use drug_store')
        sql_Formula_to_see_drug_info = 'SELECT * FROM drug_information WHERE Name = ' + '"' + self.varialbe.get() + '"'
        cur.execute(sql_Formula_to_see_drug_info)
        fetched_drug_info = cur.fetchall()
        L = []
        for element_ in fetched_drug_info:
            for element_1 in element_:
                L.append(element_1)
        tuple_of_drug_elements = ('Name: ', 'Price: ', 'Pills per Box: ' , 'Storage Info: ', 'Desposal Info: ')
        index_of_list = 0
        str_with_all_info = ''
        for element_title in tuple_of_drug_elements:
            str_with_all_info += element_title + str(L[index_of_list]) + '\n'
            index_of_list += 1

        messagebox.showinfo(self.varialbe.get(), str_with_all_info)

    """
    def scan_QR_code (self):
        cap = cv2.VideoCapture(0) 
        cap.set (3,640) 
        cap.set (4,480) 
        camera = True  #mit Button verknüpfen --> scan QR Code --> dann settet der Button die Camera auf = true
        while camera == True:
            success, frame = cap.read()

            for code in decode(frame):
                x = list(code.data.decode("utf-8"))
                print(x)
                messagebox.showinfo('Your Drug Information', x)  
                con = pymysql.connect(host='localhost', user='root', passwd='', database='drug_store')
                cur = con.cursor()
                sql_formula = "INSERT INTO (drug_name, purchase_date, expiry_date, dosis_per_day) VALUES (%s, %s, %s, %s)"
                sql_formula_1 = sql_formula % x
                print(sql_formula_1)
                #print(sql_formula_1)
                #cur.execute(sql_formula % tuple(x))
            cv2.imshow("Testing-code-scan", frame) # definition of the Camera Window where the code can be scanned
            cv2.waitKey(1)
    """

    def decode_QR_Code(self):
        d = decode(Image.open("myQRcode5.png"))
        content_QR_code_str = (d[0].data.decode("ascii"))
        #print(type(content_QR_code_str))
        content_QR_code_list = content_QR_code_str.split()
        new_list = [s.replace("'", "") for s in content_QR_code_list]
        new_list_1 = [s.replace('"', "") for s in new_list]
        new_list_2 = [s.replace('[', "") for s in new_list_1]
        new_list_3 = [s.replace(']', '') for s in new_list_2]
        new_list_4 = [s.replace(',', '') for s in new_list_3]
        new_list_4[3] = int(new_list_4[3])
        con = pymysql.connect(host='localhost', user='root', passwd='', database='drug_store')
        cur =con.cursor()
        sql_formula = "INSERT INTO {username}(drug_name, purchase_date, expiry_date, dosis_per_day) VALUES ('%s', '%s', '%s', %s)".format(username=name_of_user)
        #print(name_of_user)
        #print(sql_formula % tuple(new_list_4))
        cur.execute(sql_formula % tuple(new_list_4))
        con.commit()
        messagebox.showinfo('User Info', 'Drug added to your database')

    def show_inventory_at_home(self):
        con = pymysql.connect(host='localhost', user='root', passwd='', database='drug_store')
        cur =con.cursor()
        sql_Formula_to_see_inventory = 'SELECT * FROM {username}'.format(username=name_of_user)
        cur.execute(sql_Formula_to_see_inventory)
        fetched_drug_user_info = cur.fetchall()
        str_with_all_info = ''
        for i in fetched_drug_user_info:
            list_with_user_information = []
            for a in i:
                list_with_user_information.append(str(a))
            new_list = [s.replace("datetime.date", "") for s in list_with_user_information]
            new_list_1 = [s.replace("datetime.date", "") for s in new_list]
            tuple_of_inventory_information = ('Drug Type: ', 'Purchase-Date: ', 'Expiry-Date: ' , 'Dosis-Per-Day: ')
            index_of_list = 0
            for element_title in tuple_of_inventory_information:
                if index_of_list <= 2:
                    str_with_all_info += element_title + str(new_list_1[index_of_list]) + '| '
                    index_of_list += 1
                else:
                    str_with_all_info += element_title + str(new_list_1[index_of_list]) 
            #print(str_with_all_info)
            str_with_all_info += '\n'
        root = Tk()
        S = Scrollbar(root)
        T = Text(root, height=4, width=100)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        T.insert(END, str_with_all_info)
        root.resizable(False, False)
        mainloop()
    

    def chose_drug_to_remove(self):
        con = pymysql.connect(host='localhost', user='root', passwd='', database='drug_store')
        cur =con.cursor()
        self.sql_formula = "SELECT * FROM {username}".format(username=name_of_user)
        cur.execute(self.sql_formula)
        user_list_information = cur.fetchall()
        self.list_of_user_drugs = []
        for i in user_list_information:
            self.list_of_user_drugs.append(i)
        self.varialbe_ = StringVar(self.frame)
        self.varialbe_.set(self.list_of_user_drugs[0])
        self.user_drugs = OptionMenu(self.frame, self.varialbe_, *self.list_of_user_drugs)
        #self.user_drugs_label = Label(self.frame, text='Choose Drug to remove:', font=('Andalus', 10,  'bold'), fg='black')
        #self.user_drugs_label.place(x=400, y=165)
        self.user_drugs.place(x=500, y=165)
        self.remoe = Button(self.frame, text='remove', activebackground='#00B0F0', activeforeground='white', fg='black', font=('Arial', 10, 'bold'), command=lambda: remove_drug())
        self.remoe.place(x=600, y=400, width=100)
        def remove_drug():
            a = self.varialbe_.get()
            s = a.split()
            print(s)
            print(s[1])
            con = pymysql.connect(host='localhost', user='root', passwd='', database='drug_store')
            cur =con.cursor()
            sql_command = "DELETE FROM {username} WHERE purchase_date={date};".format(username=name_of_user, date=s[1].removesuffix(','))
            cur.execute(sql_command)
            con.commit()
            messagebox.showinfo('', 'Drug has been deleted')
            User_Interface(root)

    def expiry_date(self):
        con = pymysql.connect(host='localhost', user='root', passwd='', database='drug_store')
        cur =con.cursor()
        self.sql_formula_dates = "Select expiry_date from {username}".format(username=name_of_user)
        cur.execute(self.sql_formula_dates)
        self.tuple_of_expiry_dates=cur.fetchall()
        list_of_expiry_dates = []
        for i in self.tuple_of_expiry_dates:
            for a in i:
                list_of_expiry_dates.append(str(a))
            new_list = [s.replace('date.time', '') for s in list_of_expiry_dates]
        str_for_out_put=''
        def days_between(d1, d2):
            d1 = datetime.strptime(d1, "%Y-%m-%d")
            d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)
        for date_ in new_list:
            transfered_date = datetime.strptime(date_, "%Y-%m-%d")
            print(transfered_date)
            today = date.today()
            str_for_out_put += 'Expiry Date: ' + date_ + 'Days till expriy:' + str(abs((str(today) - str(transfered_date)).days)) + '\n'

        root = Tk()
        S = Scrollbar(root)
        T = Text(root, height=4, width=100)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        T.insert(END, str_for_out_put)
        root.resizable(False, False)
        mainloop()

        print(list_of_expiry_dates[0])
        #new_list = [s.replace('date.time', '') for s in self.list_of_expiry_dates]
        print(new_list)
        




        

                                        





#class User_inventory:















main = Mainwindow(root)
root.mainloop()

