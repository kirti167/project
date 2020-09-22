from tkinter import*
import math,random
import os
from tkinter import messagebox


class Bill_App:
     def __init__(self,root):
        self.root = root
        self.root.geometry("1850x1200+0+0")

        self.root.title("cafe management system")
        
        
        bg_color = "#074463"
        fg_color = "white"
        lbl_color = 'white'
        #Title of App
        title = Label(self.root,text = "Cafe Management System",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)
        
        #=======================Varibles=====================#
        #=======================Coffee===================#
        self.latte=IntVar()
        self.espresso=IntVar()
        self.cappuccino=IntVar()
        self.hotcoffee=IntVar()
        
        self.coldcoffee=IntVar()
        self.cafemocha=IntVar()
        #=====================ice cream======================#
        self.blackberry=IntVar()
        self.vanilla=IntVar()
        self.chocochip=IntVar()
        self.caramelapple=IntVar()
        self.peanutbutter=IntVar()
        self.strawberry=IntVar()
        #=====================shakes======================#
        self.chocolate=IntVar()
        self.mango=IntVar()
        self.butterrum=IntVar()
        self.oreo=IntVar()
        self.straw=IntVar()
        self.banana=IntVar()
        #=====================total product price & tax variables======================#
        self.coffee_price=StringVar()
        self.icecream_price=StringVar()
        self.shakes_price=StringVar()
        
        self.coffee_tax=StringVar()
        self.icecream_tax=StringVar()
        self.shakes_tax=StringVar()
        #===================customer=========================#
        self.c_name=StringVar()
        self.c_phone=StringVar()
       
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        
        

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",15,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",18,"bold")).grid(row = 0,column = 0,padx = 20,pady = 5)
        cname_en = Entry(F1,width=15,textvariable= self.c_name, font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        

        #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",18,"bold")).grid(row = 0,column = 2,padx = 20,pady=5)
        cphon_en = Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        

        #====================Customer Bill No==================#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",18,"bold")).grid(row = 0,column = 4,padx = 20,pady=5)
        cbill_en = Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        
        
        #====================Bill Search Button===============#
        bill_btn = Button(F1,text = "search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)
        #==================Cosmetics Frame=====================#
        F2 = LabelFrame(self.root,text = 'Coffee',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",15,"bold"))
        F2.place(x = 5,y = 180,width = 325,height = 380)

        #===========Frame Content=========#
        coffee_lbl = Label(F2,font = ("times new roman",16,"bold"),fg = "lightgreen",bg = bg_color,text = "Latte")

        coffee_lbl.grid(row = 0,column = 0,padx = 10,pady = 10,sticky="w")
        coffee_en = Entry(F2,width=10,textvariable=self.latte,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        coffee_en.grid(row = 0,column = 1,pady = 10,padx = 10)

        #=======Face Cream
        es_lbl = Label(F2,font = ("times new roman",16,"bold"),fg = "lightgreen",bg = bg_color,text = "Espresso")
        es_lbl.grid(row = 1,column = 0,padx = 10,pady = 10,sticky="w")
        es_en = Entry(F2,width=10,textvariable=self.espresso,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        es_en.grid(row = 1,column = 1,pady = 10,padx = 10)

        #========Face Wash
        choc_lbl = Label(F2,font = ("times new roman",16,"bold"),fg ="lightgreen",bg = bg_color,text = "Cappuccino")
        choc_lbl.grid(row = 2,column = 0,padx = 10,pady = 10,sticky="w")
        choc_en = Entry(F2,width=10,textvariable=self.cappuccino,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        choc_en.grid(row = 2,column = 1,pady = 10,padx = 10)

        #========Hair Spray
        hot_lbl = Label(F2,font = ("times new roman",16,"bold"),fg = "lightgreen",bg = bg_color,text = "Hotcoffee")
        hot_lbl.grid(row = 3,column = 0,padx = 10,pady = 10,sticky="w")

        hot_en = Entry(F2,width=10,textvariable=self.hotcoffee,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        hot_en.grid(row = 3,column = 1,pady = 10,padx = 10)

        #============Body Lotion

        afr_lbl = Label(F2,font = ("times new roman",16,"bold"),fg ="lightgreen",bg = bg_color,text = "coldcoffee")
        afr_lbl.grid(row = 4,column = 0,padx = 10,pady = 10,sticky="w")
        afr_en = Entry(F2,width=10,textvariable=self.coldcoffee,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        afr_en.grid(row = 4,column = 1,pady = 10,padx = 10)

        #==============hair gel=======
        amer_lbl = Label(F2,font = ("times new roman",16,"bold"),fg ="lightgreen",bg = bg_color,text = "cafemocha")
        amer_lbl.grid(row = 5,column = 0,padx = 10,pady = 10,sticky="w")
        amer_en = Entry(F2,width=10,textvariable=self.cafemocha,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        amer_en.grid(row = 5,column = 1,pady = 10,padx = 10)



                #==================ice cream=====================#
        F3 = LabelFrame(self.root,text = 'Ice Cream',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",15,"bold"))
        F3.place(x = 340,y = 180,width = 325,height = 380)

        #===========Frame Content=========#
        bl_lbl = Label(F3,font = ("times new roman",16,"bold"),fg = "lightgreen",bg = bg_color,text = "Blackberry")

        bl_lbl.grid(row = 0,column = 0,padx = 10,pady = 10,sticky="w")
        bl_en = Entry(F3,width=10,textvariable=self.blackberry,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        bl_en.grid(row = 0,column = 1,pady = 10,padx = 10)

        #=======Food oil========#
        va_lbl = Label(F3,font = ("times new roman",16,"bold"),fg = "lightgreen",bg = bg_color,text = "Vanilla")
        va_lbl.grid(row = 1,column = 0,padx = 10,pady = 10,sticky="w")
        va_en = Entry(F3,width=10,textvariable=self.vanilla,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        va_en.grid(row = 1,column = 1,pady = 10,padx = 10)

        #======dall==============#
        ch_lbl = Label(F3,font = ("times new roman",16,"bold"),fg ="lightgreen",bg = bg_color,text = "Chocochip")
        ch_lbl.grid(row = 2,column = 0,padx = 10,pady = 10,sticky="w")
        ch_en = Entry(F3,width=10,textvariable=self.chocochip,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        ch_en.grid(row = 2,column = 1,pady = 10,padx = 10)

        #========wheat===========#
        g4_lbl = Label(F3,font = ("times new roman",16,"bold"),fg = "lightgreen",bg = bg_color,text = "Caramelapple")
        g4_lbl.grid(row = 3,column = 0,padx = 10,pady = 10,sticky="w")
        g4_en = Entry(F3,width=10,textvariable=self.caramelapple,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        g4_en.grid(row = 3,column = 1,pady = 10,padx = 10)

        #===========sugar===========#
        g5_lbl = Label(F3,font = ("times new roman",16,"bold"),fg ="lightgreen",bg = bg_color,text = "Peanutbutter")
        g5_lbl.grid(row = 4,column = 0,padx = 10,pady = 10,sticky="w")
        g5_en = Entry(F3,width=10,textvariable=self.peanutbutter,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        g5_en.grid(row = 4,column = 1,pady = 10,padx = 10)
       #=====================tea==================#

        g6_lbl = Label(F3,font = ("times new roman",16,"bold"),fg ="lightgreen",bg = bg_color,text = "strawberry")
        g6_lbl.grid(row = 5,column = 0,padx = 10,pady = 10,sticky="w")
        g6_en = Entry(F3,width=10,textvariable=self.strawberry,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        g6_en.grid(row = 5,column = 1,pady = 10,padx = 10)

        #==================shakes=====================#
        F4 = LabelFrame(self.root,text = 'Shakes',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",15,"bold"))
        F4.place(x = 670,y = 180,width = 325,height = 380)

        

        #===========Frame Content=========#
        c1_lbl = Label(F4,font = ("times new roman",16,"bold"),fg = "lightgreen",bg = bg_color,text = "Chocolate")
        c1_lbl.grid(row = 0,column = 0,padx = 10,pady = 10,sticky="w")
        c1_en = Entry(F4,width=10,textvariable=self.chocolate,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        c1_en.grid(row = 0,column = 1,pady = 10,padx = 10)

        #=======cock==============#
        c2_lbl = Label(F4,font = ("times new roman",16,"bold"),fg = "lightgreen",bg = bg_color,text = "Mango")
        c2_lbl.grid(row = 1,column = 0,padx = 10,pady = 10,sticky="w")
        c2_en = Entry(F4,width=10,textvariable=self.mango,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        c2_en.grid(row = 1,column = 1,pady = 10,padx = 10)

        #========frooti========#
        c3_lbl = Label(F4,font = ("times new roman",16,"bold"),fg ="lightgreen",bg = bg_color,text = "Butterrum")
        c3_lbl.grid(row = 2,column = 0,padx = 10,pady = 10,sticky="w")
        c3_en = Entry(F4,width=10,textvariable=self.butterrum,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        c3_en.grid(row = 2,column = 1,pady = 10,padx = 10)

        #========thumsup=======#
        c4_lbl = Label(F4,font = ("times new roman",16,"bold"),fg = "lightgreen",bg = bg_color,text = "Oreo")
        c4_lbl.grid(row = 3,column = 0,padx = 10,pady = 10,sticky="w")
        c4_en = Entry(F4,width=10,textvariable=self.oreo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        c4_en.grid(row = 3,column = 1,pady = 10,padx = 10)

        #============limca=======#
        c5_lbl = Label(F4,font = ("times new roman",16,"bold"),fg ="lightgreen",bg = bg_color,text = "Strawberry")
        c5_lbl.grid(row = 4,column = 0,padx = 10,pady = 10,sticky="w")
        c5_en = Entry(F4,width=10,textvariable=self.straw,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        c5_en.grid(row = 4,column = 1,pady = 10,padx = 10)

        #===========sprite================#
        c6_lbl = Label(F4,font = ("times new roman",16,"bold"),fg ="lightgreen",bg = bg_color,text = "Banana")
        c6_lbl.grid(row = 5,column = 0,padx = 10,pady = 10,sticky="w")
        c6_en = Entry(F4,width=10,textvariable=self.banana,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN)
        c6_en.grid(row = 5,column = 1,pady = 10,padx = 10)

        #=========Bill Area====================#
        F5 =Frame(self.root,bd = 10,relief = GROOVE)
        F5.place(x = 1010,y = 180,width = 350,height = 380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)

        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill =BOTH, expand =1)

        #======BUTTONFRAME=====#
        F6 = LabelFrame(self.root,text = "Bill Menu",bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",15,"bold"))
        F6.place(x =0,y = 560,relwidth =1,height = 140)
        m1=Label(F6,text="Total Coffee Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.coffee_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2=Label(F6,text="Total Icecream Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.icecream_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3=Label(F6,text="Total Shakes Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.shakes_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1=Label(F6,text="Coffee Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.coffee_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2=Label(F6,text="Icecream Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.icecream_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3=Label(F6,text="Shakes Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.shakes_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
        
    #Function to get total prices
     def total(self):
          
          self.c_l_p=self.latte.get()*100
          self.c_e_p=self.espresso.get()*120
          self.c_ch_p=self.cappuccino.get()*120
          self.c_h_p=self.hotcoffee.get()*80
          self.c_c_p=self.coldcoffee.get()*90
          self.c_ca_p=self.cafemocha.get()*120
          
          
          
     
        #=================Total Cosmetics Prices
          self.total_coffee_price=float(
            self.c_l_p+
            self.c_e_p+
            self.c_ch_p+
            self.c_h_p+
            self.c_c_p+
            self.c_ca_p
            
        )
          self.coffee_price.set("Rs. "+str(self.total_coffee_price))
          self.c_tax=round((self.total_coffee_price*0.05),2)
          self.coffee_tax.set("Rs. "+str(self.c_tax))

          self.i_b_p=self.blackberry.get()*120
          self.i_v_p=self.vanilla.get()*80
          self.i_c_p=self.chocochip.get()*100
          self.i_ca_p=self.caramelapple.get()*120
          self.i_p_p=self.peanutbutter.get()*120
          self.i_s_p=self.strawberry.get()*120
        






        
       #=================Total Cosmetics Prices
          self.total_icecream_price=float(
          self.i_b_p+
          self.i_v_p+
          self.i_c_p+
          self.i_ca_p+
          self.i_p_p+
          self.i_s_p
          )         
          self.icecream_price.set("Rs. "+str(self.total_icecream_price))
          self.i_tax=round((self.total_icecream_price*0.05),2)                              
          self.icecream_tax.set("Rs. "+str(self.i_tax))
          self.s_cho_p=self.chocolate.get()*100
          self.s_m_p=self.mango.get()*90
          self.s_b_p=self.butterrum.get()*180
          self.s_o_p=self.oreo.get()*120
          self.s_st_p=self.straw.get()*80
          self.s_ba_p=self.banana.get()*80
        






        
          self.total_shakes_price=float(
             self.s_cho_p+
             self.s_m_p+
             self.s_b_p+
             self.s_o_p+
             self.s_st_p+
             self.s_ba_p
            
        )
          self.shakes_price.set("Rs. "+str(self.total_shakes_price))
          self.s_tax=round((self.total_shakes_price*0.05),2)                    
          self.shakes_tax.set("Rs. "+str(self.s_tax))
          self.Total_bill=float(self.total_coffee_price+self.total_icecream_price+self.total_shakes_price+self.c_tax+self.i_tax+self.s_tax)
    
     def welcome_bill(self):
          self.txtarea.delete('1.0',END)
          self.txtarea.insert(END,"\t ....CRAVINGS CURE...\n")
          self.txtarea.insert(END,f"\n Bill Number :{self.bill_no.get()}")
          self.txtarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
          self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
          self.txtarea.insert(END,f"\n**************************************")
          self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrrice")
          self.txtarea.insert(END,f"\n**************************************")

     def bill_area(self):
          if self.c_name.get()=="" or self.c_phone.get()=="":
               messagebox.showerror("Error","customer details are must")
          elif self.coffee_price.get()=="Rs. 0.0" and self.icecream_price.get()=="Rs. 0.0" and self.shakes_price.get()=="Rs. 0.0":
               messagebox.showerror("Error","No Product Purchased")

          else:
              self.welcome_bill()     

            

         #========coffee==========#
              if self.latte.get()!=0:
                  self.txtarea.insert(END,f"\n latte\t\t{self.latte.get()}\t\t{self.c_l_p}")
              
              if self.espresso.get()!=0:
                  self.txtarea.insert(END,f"\n espresso\t\t{self.espresso.get()}\t\t{self.c_e_p}")
              if self.cappuccino.get()!=0:
                  self.txtarea.insert(END,f"\n cappucino\t\t{self.cappuccino.get()}\t\t{self.c_ch_p}")
              if self.hotcoffee.get()!=0:
                  self.txtarea.insert(END,f"\n hotcoffee\t\t{self.hotcoffee.get()}\t\t{self.c_h_p}")
              if self.coldcoffee.get()!=0:
                  self.txtarea.insert(END,f"\n coldcoffee\t\t{self.coldcoffee.get()}\t\t{self.c_c_p}")
              if self.cafemocha.get()!=0:
                  self.txtarea.insert(END,f"\n cafemocha\t\t{self.cafemocha.get()}\t\t{self.c_ca_p}")
         #========ice cream==========#
              if self.blackberry.get()!=0:
                  self.txtarea.insert(END,f"\n blackberry\t\t{self.blackberry.get()}\t\t{self.i_b_p}")
              
              if self.vanilla.get()!=0:
                  self.txtarea.insert(END,f"\n vanilla\t\t{self.vanilla.get()}\t\t{self.i_v_p}")
              if self.chocochip.get()!=0:
                  self.txtarea.insert(END,f"\n chocochip\t\t{self.chocochip.get()}\t\t{self.i_c_p}")
              if self.caramelapple.get()!=0:
                  self.txtarea.insert(END,f"\n caramelapple\t\t{self.caramelapple.get()}\t\t{self.i_ca_p}")
              if self.peanutbutter.get()!=0:
                  self.txtarea.insert(END,f"\n \t\t{self.peanutbutter.get()}\t\t{self.i_p_p}")
              if self.strawberry.get()!=0:
                  self.txtarea.insert(END,f"\n stawberry icecream\t\t{self.strawberry.get()}\t\t{self.i_s_p}")
          #========shakes==========#
              if self.chocolate.get()!=0:
                  self.txtarea.insert(END,f"\n chocolateshake\t\t{self.chocolate.get()}\t\t{self.s_cho_p}")
              
              if self.mango.get()!=0:
                  self.txtarea.insert(END,f"\n mangoshake\t\t{self.mango.get()}\t\t{self.s_m_p}")
              if self.butterrum.get()!=0:
                  self.txtarea.insert(END,f"\n butterrumshake\t\t{self.butterrum.get()}\t\t{self.s_b_p}")
              if self.oreo.get()!=0:
                  self.txtarea.insert(END,f"\n oreoshake\t\t{self.oreo.get()}\t\t{self.s_o_p}")
              if self.straw.get()!=0:
                  self.txtarea.insert(END,f"\n strawberryshake\t\t{self.straw.get()}\t\t{self.s_st_p}")
              if self.banana.get()!=0:
                  self.txtarea.insert(END,f"\n bananashake\t\t{self.banana.get()}\t\t{self.s_ba_p}")
                  self.txtarea.insert(END,f"\n--------------------------------------")
              if self.coffee_tax.get()!="Rs. 0.0":
                  self.txtarea.insert(END,f"\n coffee Tax\t\t\t{self.coffee_tax.get()}")
                  self.txtarea.insert(END,f"\n--------------------------------------")
              if self.icecream_tax.get()!="Rs. 0.0":
                  self.txtarea.insert(END,f"\nIcecreamTax\t\t\t{self.icecream_tax.get()}")
                  self.txtarea.insert(END,f"\n--------------------------------------")
              if self.shakes_tax.get()!="Rs. 0.0":
                  self.txtarea.insert(END,f"\n shakes Tax\t\t\t{self.shakes_tax.get()}")
              self.txtarea.insert(END,f"\n Total Bill: \t\t\t Rs. {self.Total_bill}")     
              self.txtarea.insert(END,f"\n--------------------------------------")
              self.save_bill()
     def save_bill(self):
          op=messagebox.askyesno("Save Bill","do you want to save the bill?")
          if op>0:
               self.bill_data=self.txtarea.get('1.0',END)
               f1=open("Desktop\\file save\\"+str(self.bill_no.get())+".txt",'r')
               f1.write(self.bill_data)
               f1.close()
               messagebox.showinfo("saved",f"Bill no. : {self.bill_no.get()} saved successfully")
          else:
               return     
                  
     def clear_data(self):
          op=messagebox.askyesno("Clear","Do you really want to clear?")
          if op>=0:
               
           #=======================Coffee===================#
               self.latte.set(0)
               self.espresso.set(0)
               self.cappuccino.set(0)
               self.hotcoffee.set(0)
        
               self.coldcoffee.set(0)
               self.cafemocha.set(0)
        #=====================ice cream======================#
               self.blackberry.set(0)
               self.vanilla.set(0)
               self.chocochip.set(0)
               self.caramelapple.set(0)
               self.peanutbutter.set(0)
               self.strawberry.set(0)
        #=====================shakes======================#
               self.chocolate.set(0)
               self.mango.set(0)
               self.butterrum.set(0)
               self.oreo.set(0)
               self.straw.set(0)
               self.banana.set(0)
        #=====================total product price & tax variables======================#
               self.coffee_price.set("")
               self.icecream_price.set("")
               self.shakes_price.set("")
        
               
               self.coffee_tax.set("")
               self.icecream_tax.set("")
               self.shakes_tax.set("")
        #===================customer=========================#
               self.c_name.set("")
               self.c_phone.set("")
       
               self.bill_no.set("")
               x=random.randint(1000,9999)
               self.bill_no.set(str(x))
               self.search_bill.set("")
               self.welcome_bill()
     def Exit_app(self):
          op=messagebox.askyesno("Exit","Do you really want to exit?")
          if op>=0:
               self.root.destroy()


    
              





root =Tk()
object = Bill_App(root)
root.mainloop()
