from tkinter import *
import tkinter
import pandas as pd
from arval_main import arval_single_loop
from alphabet_main import alphabet_single_loop
from hitatchi_main import hitatchi_single_loop
from multiprocessing import Process, Manager , freeze_support





# double check everything for reliability
# create better explanations
# delete redundant stuff 

class a_car():
    def __init__(self,capcode,make, model, deriv, blp):
        self.capcode = capcode
        self.make = make
        self.model = model
        self.deriv = deriv
        self.blp = blp

def get_make(row):# for sort func
    return row.make
def get_model(row):# for sort func
    return row.model
def get_deriv(row):# for sort func
    return row.deriv



def otr():
    # ((((List price – (manufacturer discount percentage + dealer discount percentage)) – additional discount) + delivery) * 1.2) + RFL + 55 = OTR
    our_otr = input_otr
    our_blp = input_blp.get("1.0","end-1c")
    if len(our_blp)< 2:
        our_otr.delete('1.0',"end")
        our_otr.insert('1.0',"choose a car")
        return;
    our_blp = float(input_blp.get("1.0","end-1c").replace(",",""))

    if man_discount_percentage_elem.get("1.0","end-1c") == "":
        man_discount_percentage = 0
    else:
        man_discount_percentage = float(man_discount_percentage_elem.get("1.0","end-1c").replace(",",""))

    if dealer_discount_percentage_elem.get("1.0","end-1c") == "":
        dealer_discount_percentage = 0
    else:
        dealer_discount_percentage = float(dealer_discount_percentage_elem.get("1.0","end-1c").replace(",",""))



    if addition_discount_elem.get("1.0","end-1c") == "":
        addition_discount = 0
    else:
        addition_discount = float(addition_discount_elem.get("1.0","end-1c").replace(",",""))

    if delivery_elem.get("1.0","end-1c") == "":
        delivery = 0
    else:
        delivery = float(delivery_elem.get("1.0","end-1c").replace(",",""))

    if RFL_elem.get("1.0","end-1c") == "":
        RFL = 0
    else:
        RFL = float(RFL_elem.get("1.0","end-1c").replace(",",""))



    this_otr = (((our_blp-(our_blp*((man_discount_percentage + dealer_discount_percentage)/100)) - addition_discount)+ delivery )*1.2) + RFL + 55
    this_otr = round(this_otr , 2)
    our_otr.delete('1.0',"end")
    our_otr.insert('1.0',str(this_otr))





    

def deriv_selected_func(der):
    deriv_top_label_object.set(der)
    for o in (all_options):
        if o.deriv == der:
            input_capcode.delete('1.0',"end")
            input_capcode.insert('1.0',o.capcode)
            input_blp.delete('1.0',"end")
            input_blp.insert('1.0',o.blp)


def make_selected_func(make_selected):
    print("make selected " +str(make_selected))
 #   make_object['menu'].delete(0, 'end')
    model_object['menu'].delete(0, 'end')
    good_models = []


  #  employees.sort(key=get_name)
   # print(employees, end='\n\n')

    all_options.sort(key=get_model)
    for o in (all_options):
        if o.make == make_selected:
            mo = o.model
            allready_used = False
            for gm in good_models:
                if gm == mo:
                    allready_used = True
            if allready_used:
                pass
            else:
                good_models.append(mo)
                model_object['menu'].add_command(label=mo, command=lambda mo = mo: model_selected_func(mo))   ## command=lambda a    <- this is the problem it doesnt know what a is      , but i need to pass a into it or its useless 
    make_top_label_object.set(make_selected)
    model_top_label_object.set(" choose a model ")
    deriv_top_label_object.set(" choose a deriv ")

def model_selected_func(model_selected):
    print("model selected")
  #  model_object['menu'].delete(0, 'end')
    deriv_object['menu'].delete(0, 'end')
    good_derivs = []
    all_options.sort(key=get_deriv)
    our_make = make_top_label_object.get()
    for o in (all_options):
        if o.model == model_selected and our_make == o.make:
            der = o.deriv
            allready_used = False
            for gm in good_derivs:
                if gm == der:
                    allready_used = True
            if allready_used:
                pass
            else:
                good_derivs.append(der)
                deriv_object['menu'].add_command(label=der, command=lambda der = der: deriv_selected_func(der))   ## command=lambda a    <- this is the problem it doesnt know what a is      , but i need to pass a into it or its useless 
    model_top_label_object.set(model_selected)
    deriv_top_label_object.set(" choose a deriv ")

class password():
    def __init__(self , website , login, passw):
        self.website = website
        self.login = login
        self.password = passw


def get_passwords():
    thedb = pd.read_csv("passwords.csv" , dtype = str)
    for col in thedb.columns:
        print(col)
    passwords = []
    for i in range(thedb.shape[0]):
        if str(thedb.iloc[i]['website']) == "arval":
            passwords.append(password("arval" , str(thedb.iloc[i]['login']), str(thedb.iloc[i]['password'])))
        if str(thedb.iloc[i]['website']) == "alphabet":
            passwords.append(password("alphabet " , str(thedb.iloc[i]['login']), str(thedb.iloc[i]['password'])))
        if str(thedb.iloc[i]['website']) == "hitatchi":
            passwords.append(password("hitatchi" , str(thedb.iloc[i]['login']), str(thedb.iloc[i]['password'])))
    return passwords

def get_local_file():
    thedb = pd.read_csv("car_names.csv" , dtype = str)
    cars = []
    for i in range(thedb.shape[0]):
        try:
            make = str(thedb.iloc[i][' Manufacture'])
        except:
            make = str(thedb.iloc[i]['Manufacturer'])
        try:
            model = str(thedb.iloc[i][' Model Name'])
        except:
            try:
                model = str(thedb.iloc[i]['Model Name'])
            except:
                model = str(thedb.iloc[i]['Model'])
        try:
            deriv = str(thedb.iloc[i][' Variant'])
        except:
            deriv = str(thedb.iloc[i]['Variant'])

        try:
            capcode = str(thedb.iloc[i]['capcode'])
        except:
            try:
                capcode = str(thedb.iloc[i]['CapCode'])
            except:
                try:
                    capcode = str(thedb.iloc[i]['Cap_Code'])
                except:
                    try:
                        capcode = str(thedb.iloc[i]['Cap Code'])
                    except:
                        capcode = str(thedb.iloc[i]['CAP CODE'])
        try:
            blp = str(thedb.iloc[i]['blp'])
        except:
            try:
                blp = str(thedb.iloc[i]['Basic List'])
            except:
                try:
                    blp = str(thedb.iloc[i]['Basic List Price'])
                except:
                    blp = str(thedb.iloc[i][' Basic List Price'])
        blp = blp.strip().replace(",","").replace("'","")
        
        cars.append(a_car(capcode,make, model, deriv, blp))

    return cars


def go():
    our_miles = [input_miles.get("1.0","end-1c")]
    our_months = [input_months.get("1.0","end-1c")]
    our_otr = input_otr.get("1.0","end-1c")
    our_months_up = input_months_up.get("1.0","end-1c")
    our_capcode = input_capcode.get("1.0","end-1c")
    our_blp = input_blp.get("1.0","end-1c")
    our_maint = maint_var.get()
    if our_maint == 0:
        our_maint = [False]
        
    if our_maint == 1:
        our_maint = [True]

    if metallic_var.get() == 1:
        our_metallic = True
    else:
        our_metallic = False
        
    if all_terms_var.get() == 1:
        our_miles = [5000, 8000, 10000 , 15000, 20000, 25000, 30000]
        our_months = [24, 36, 48]
        our_maint = [True , False]
        input_miles.delete('1.0',"end")
        input_miles.insert('1.0',"irellevent")
        input_months.delete('1.0',"end")
        input_months.insert('1.0',"irellevent")

    for p, n in zip(answers_prices , answers_names):
        p.delete('1.0',"end")
        n.delete('1.0',"end")
        # refresh
       # Tk.update()
        


    our_make = make_top_label_object.get()
    our_model = model_top_label_object.get()
    our_deriv = deriv_top_label_object.get()
    check_boxes = [c1 , c3 , c4 ]
    the_vars = [var1, var3, var4]
    ticked_boxes = []
    passwords = get_passwords()
    for p in passwords:
        if p.website == "arval":
            our_arval_login = p.login
            our_arval_password = p.password
        if p.website.strip().lower() == "alphabet".strip().lower():
            our_alphabet_login = p.login
            our_alphabet_password = p.password
        if p.website.strip().lower() == "hitatchi".strip().lower():
            our_hitatchi_login = p.login
            our_hitatchi_password = p.password
        else:
            print("noooooooooooooooooooooooooooooo")

    no_funders_chosen = True
    for cb, v in zip(check_boxes , the_vars):
        if (v.get() == 1):
            print(cb.cget("text"))
            ticked_boxes.append(cb.cget("text"))
            no_funders_chosen = False



#    for tb in ticked_boxes:
 #       if tb == "alphabet":            
  #          alphabet_single_loop(our_capcode, our_make, our_model, our_deriv , our_months, our_miles, our_months_up, our_otr,our_blp, our_maint , our_alphabet_login, our_alphabet_password, "" , 0  ,False , our_metallic)
   #     if tb == "hitatchi":            
    #        hitatchi_single_loop(our_capcode, our_make, our_model, our_deriv , our_months, our_miles, our_months_up, our_otr,our_blp, our_maint , our_hitatchi_login, our_hitatchi_password, "" , 0  ,False, our_metallic)
     #   if tb == "arval":            
      #      arval_single_loop(our_capcode, our_make, our_model, our_deriv , our_months, our_miles, our_months_up, our_otr,our_blp, our_maint , our_arval_login, our_arval_password, "" , 0 ,False, our_metallic)
            
    proc_num = 0
    processes = []
    manager = Manager()
    d = manager.dict()


    if just_open_var.get() == 1:
        our_just_open = True
    else:
        our_just_open = False

    otr_bool = True
    if our_otr== '':
        otr_bool = False
    
    if otr_bool == False:
        currently_doing_info.delete('1.0',"end")
        currently_doing_info.insert('1.0'," no otr ")
        window.update()
    elif no_funders_chosen == True:
        currently_doing_info.delete('1.0',"end")
        currently_doing_info.insert('1.0'," no funders chosen ")
        window.update()
    else:
        currently_doing_info.delete('1.0',"end")
        currently_doing_info.insert('1.0',"getting prices for "+str(our_deriv))
        window.update()
    if no_funders_chosen == False and otr_bool == True:
        for tb in ticked_boxes:
            print(str(tb)+ "     =    tb ")
            d[proc_num] = []
            if tb == "arval":
                p1 = Process( target = arval_single_loop , args = (our_capcode, our_make, our_model, our_deriv , our_months, our_miles, our_months_up, our_otr,our_blp, our_maint , our_arval_login, our_arval_password , d , proc_num , our_just_open  , our_metallic))
            if tb == "alphabet":            
                p1 = Process( target = alphabet_single_loop , args = (our_capcode, our_make, our_model, our_deriv , our_months, our_miles, our_months_up, our_otr,our_blp, our_maint , our_alphabet_login, our_alphabet_password , d , proc_num , our_just_open  , our_metallic))
            if tb == "hitatchi":            
                p1 = Process( target = hitatchi_single_loop , args = (our_capcode, our_make, our_model, our_deriv , our_months, our_miles, our_months_up, our_otr,our_blp, our_maint , our_hitatchi_login, our_hitatchi_password , d , proc_num , our_just_open  , our_metallic))
            processes.append(p1)
            proc_num+= 1;
        for proc in processes:
            proc.start()    
        for proc in processes:
            proc.join()
        print("ans                ooooooooo   ")
        print(d)
        currently_doing_info.delete('1.0',"end")
        currently_doing_info.insert('1.0',"got prices for "+str(our_deriv))

        for ans in range(len(d)):
            print(d)
            print(ans)
            try:
                print(d[ans]+"      d[ans]")
            except:
                print("nope 1")
            try:
                print(d[0]+"      d[0]")
            except:
                print("nope 2")
            try:
                print(d[1]+"      d[1]")
            except:
                print("nope 3")
            try:
                print(d[0]+"      d[0]")
            except:
                print("nope 2")
            answers_prices[ans].delete('1.0',"end")
            answers_names[ans].delete('1.0',"end")
            try:
                answers_prices[ans].insert('1.0',d[ans][1])
                answers_names[ans].insert('1.0',d[ans][0])
            except:
                answers_prices[ans].insert('1.0',"collection error")
                answers_names[ans].insert('1.0',"collection error")

        if all_terms_var.get() == 1:
            finaldf = pd.DataFrame({'capcode':[], 'funders':[], 'make':[], 'model':[], 'deriv':[] , 'mles':[], 'months':[], 'months up':[], 'cm':[], 'fm':[]})
            for ans in d:
                
                for price in range(21):
                    print(price)
                    if price == 0:
                        miles = 5000;
                        months = 24;
                    if price == 1:
                        miles = 5000;
                        months = 36;
                    if price == 2:
                        miles = 5000;
                        months = 48;
                    if price == 3:
                        miles = 8000;
                        months = 24;
                    if price == 4:
                        miles = 8000;
                        months = 36;
                    if price == 5:
                        miles = 8000;
                        months = 48;
                    if price == 6:
                        miles = 10000;
                        months = 24;
                    if price == 7:
                        miles = 10000;
                        months = 36;
                    if price == 8:
                        miles = 10000;
                        months = 48;
                    if price == 9:
                        miles = 15000;
                        months = 24;
                    if price == 10:
                        miles = 15000;
                        months = 36;
                    if price == 11:
                        miles = 15000;
                        months = 48;
                    if price == 12:
                        miles = 20000;
                        months = 24;
                    if price == 13:
                        miles = 20000;
                        months = 36;
                    if price == 14:
                        miles = 20000;
                        months = 48;
                    if price == 15:
                        miles = 25000;
                        months = 24;
                    if price == 16:
                        miles = 25000;
                        months = 36;
                    if price == 17:
                        miles = 25000;
                        months = 48;
                    if price == 18:
                        miles = 30000;
                        months = 24;
                    if price == 19:
                        miles = 30000;
                        months = 36;
                    if price == 20:
                        miles = 30000;
                        months = 48;


                    if price != 21:    
                        print(d[ans][1][price])
                        try:
                            if type(d[ans][1]) == type(['lol', 'list']):
                                df_1_deal = pd.DataFrame({'capcode':[our_capcode], 'funders':[d[ans][0]], 'make':[our_make], 'model':[our_model], 'deriv':[our_deriv] , 'mles':[miles], 'months':[months], 'months up':[our_months_up], 'cm':[d[ans][1][price]], 'fm':[d[ans][1][price+21]]}) 
                            else:
                                df_1_deal = pd.DataFrame({'capcode':[our_capcode], 'funders':[d[ans][0]], 'make':[our_make], 'model':[our_model], 'deriv':[our_deriv] , 'mles':[miles], 'months':[months], 'months up':[our_months_up], 'cm':["fail"], 'fm':["fail"]})
                        except:
                            df_1_deal = pd.DataFrame({'capcode':[our_capcode], 'funders':["fail"], 'make':[our_make], 'model':[our_model], 'deriv':[our_deriv] , 'mles':[miles], 'months':[months], 'months up':[our_months_up], 'cm':["fail"], 'fm':["fail"]})
                    finaldf = finaldf.append(df_1_deal)
            try:
                finaldf.to_csv("your prices.csv")
            except:
                try:
                    finaldf.to_csv("your prices spare cant save cos you have other open.csv")
                except:
                    try:
                        finaldf.to_csv("your prices spare cant save cos you have other open 2 .csv")
                    except:
                        print("failed to save")
        print("saved 309")


print("getting files ")
our_options = get_local_file()
all_options = our_options
print("got files ")


all_options.sort(key=get_make)


unique_makes = []
for o in our_options:
    make = o.make
    if make not in unique_makes:
        unique_makes.append(make)
print(unique_makes)
unique_models = []
for o in our_options:
    model = o.model
    if model not in unique_models:
        unique_models.append(model)
print(unique_models)

global chromedriversl;
chromedriversl = []
if __name__ == '__main__':
    freeze_support()
    window=Tk()
   # chromedrivers.pack()
    window.title('choose a car')
    window.geometry("820x520+10+20")
    canvas=Canvas(window, width=360, height=300)
    canvas.pack()
    canvas.create_line(0,0,0,300, fill="green", width=5)
    canvas.create_line(200,0,200,300, fill="green", width=5)

    make_top_label_object = StringVar(window)
    make_top_label_object.set("choose a make")


    model_top_label_object = StringVar(window)
    model_top_label_object.set("choose a model") # default value



    deriv_top_label_object = StringVar(window)
    deriv_top_label_object.set("choose a deriv") # default value
                                                                                         #   (make_chosen , make_object, make_top_label_object , model_object , deriv_object, all_options)
    empty_values = ["empty 1" , "empty 2"]

    ##################################
    input_capcode = tkinter.Text(window, height = 1, width = 24);
    input_capcode.pack()
    input_capcode.place(x=25, y=150)

    input_blp = tkinter.Text(window, height = 1, width = 12);
    input_blp.pack()
    input_blp.place(x=50, y=100)
    blp_label = Label(window, text = "blp").place(x=25, y=100);

    input_miles = tkinter.Text(window, height = 1, width = 8);
    input_miles.pack()
    input_miles.place(x=325, y=100)
    input_miles.insert('1.0',"5000")
    miles_label = Label(window, text = "miles").place(x=235, y=100);

    #input_miles.pack()
    input_months = tkinter.Text(window, height = 1, width = 8)
    input_months.pack()
    input_months.place(x=325, y=160);
    input_months.insert('1.0',"24")
    months_label = Label(window, text = "months").place(x=235, y=160);
    input_months_up = tkinter.Text(window, height = 1, width = 8)
    input_months_up.pack();
    input_months_up.place(x=325, y=220);
    input_months_up.insert('1.0',"3")
    months_up_label = Label(window, text = "months up").place(x=235, y=220);
    #months_up_label.pack()

    input_otr = tkinter.Text(window, height = 1, width = 15)
    input_otr.pack();
    input_otr.place(x=525, y=300);


    
    otr_label = Label(window, text = "otr").place(x=500, y=300);
    #otr_label.pack()
    maint_var = tkinter.BooleanVar()
    maint = tkinter.Checkbutton(window, text='maintenance' , variable=maint_var)
    maint.pack()
    maint.place(x=305, y=50);
    #######################################
    # , input_capcode , input_blp

    deriv_object = OptionMenu(window, deriv_top_label_object, *empty_values , command= lambda deriv_c: deriv_selected(deriv_c  ))
    deriv_object.pack();
    deriv_object.place(x=25, y=300);

    #model_c: model_selected(model_c , models , def_model  , unique_models  , window 
    model_object = OptionMenu(window, model_top_label_object, *unique_models , command= lambda model_c: model_selected(model_c ))
    model_object.pack();
    model_object.place(x=25, y=250);


    make_object = OptionMenu(window, make_top_label_object , *unique_makes , command= lambda make_c: make_selected_func(make_c  ))# , model_top_label_object, deriv_object , deriv_top_label_object ))
    make_object.pack();
    make_object.place(x=25, y=200);
     #   (make_chosen , make_object, make_top_label_object , model_object , deriv_object, all_options)

    B = Button(window, text ="go", command = go)
    B.place(x=565, y=380);

    man_discount_percentage_elem = tkinter.Text(window, height = 1, width = 12);
    man_discount_percentage_elem.pack()
    man_discount_percentage_elem.place(x=600, y=30)
    man_discount_percentage_elem.insert('1.0',"0")
    man_disc_label = Label(window, text = "man_discount_percentage").place(x=435, y=30);

    dealer_discount_percentage_elem = tkinter.Text(window, height = 1, width = 12);
    dealer_discount_percentage_elem.pack()
    dealer_discount_percentage_elem.place(x=600, y=60)
    dealer_discount_percentage_elem.insert('1.0',"0")
    dealer_disc_label = Label(window, text = "dealer_discount_percentage").place(x=435, y=60);
    
    delivery_elem = tkinter.Text(window, height = 1, width = 12);
    delivery_elem.pack()
    delivery_elem.place(x=600, y=90)
    delivery_elem.insert('1.0',"0")
    delivery_label = Label(window, text = "delivery").place(x=435, y=90);

    addition_discount_elem = tkinter.Text(window, height = 1, width = 12);
    addition_discount_elem.pack()
    addition_discount_elem.place(x=600, y=120)
    addition_discount_elem.insert('1.0',"0")
    addition_discount_label = Label(window, text = "addition_discount").place(x=435, y=120);

    RFL_elem = tkinter.Text(window, height = 1, width = 12);
    RFL_elem.pack()
    RFL_elem.place(x=600, y=150)
    RFL_elem.insert('1.0',"0")
    RFL_label = Label(window, text = "RFL").place(x=435, y=150);

    set_otr = Button(window, text ="set otr", command = otr)
    set_otr.place(x=505, y=250);

    metallic_var = tkinter.BooleanVar()
    metallic = tkinter.Checkbutton(window, text='metallic ' , variable=metallic_var)
    metallic.pack()
    metallic.place(x=305, y=280);

    all_terms_var = tkinter.BooleanVar()
    all_terms = tkinter.Checkbutton(window, text='all_terms' , variable=all_terms_var)
    all_terms.pack()
    all_terms.place(x=305, y=310);



    just_open_var = tkinter.BooleanVar()
    just_open = tkinter.Checkbutton(window, text='just open to this car' , variable=just_open_var)
    just_open.pack()
    just_open.place(x=305, y=340);



    var1 = tkinter.IntVar()
    c1 = tkinter.Checkbutton(window, text='arval' , variable=var1)
    c1.pack()
    c1.place(x=225, y=370);

    #var2 = tkinter.IntVar()
    #c2 = tkinter.Checkbutton(window, text='lex', variable=var2)
    #c2.pack()
    #c2.place(x=75, y=270);

    var3 = tkinter.IntVar()
    c3 = tkinter.Checkbutton(window, text='alphabet', variable=var3)
    c3.pack()
    c3.place(x=300, y=370);

    var4 = tkinter.IntVar()
    c4 = tkinter.Checkbutton(window, text='hitatchi' , variable=var4)
    c4.pack()
    c4.place(x=365, y=370);


    currently_doing_info = tkinter.Text(window, height = 1, width = 58)
    currently_doing_info.pack()
    currently_doing_info.place(x=275, y=420);


    anwers_name_1 = tkinter.Text(window, height = 1, width = 8)
    anwers_name_1.pack()
    anwers_name_1.place(x=275, y=440);
    anwers_name_2 = tkinter.Text(window, height = 1, width = 8)
    anwers_name_2.pack()
    anwers_name_2.place(x=275, y=460);
    anwers_name_3 = tkinter.Text(window, height = 1, width = 8)
    anwers_name_3.pack()
    anwers_name_3.place(x=275, y=480);
    answers_names = [anwers_name_1 , anwers_name_2 , anwers_name_3]
    anwers_price_1 = tkinter.Text(window, height = 1, width = 18)
    anwers_price_1.pack()
    anwers_price_1.place(x=375, y=440);
    anwers_price_2 = tkinter.Text(window, height = 1, width = 18)
    anwers_price_2.pack()
    anwers_price_2.place(x=375, y=460);
    anwers_price_3 = tkinter.Text(window, height = 1, width = 18)
    anwers_price_3.pack()
    anwers_price_3.place(x=375, y=480);
    answers_prices = [anwers_price_1 , anwers_price_2 , anwers_price_3]

    



    window.mainloop();
