import pandas as pd
import datetime
class deal_pair():
    def __init__(self,capcode,months,miles,maintprice, nomaintprice, make, model, deriv):
        self.capcode = capcode
        self.months = months
        self.miles = miles
        self.maintprice = maintprice
        self.nomaintprice = nomaintprice
        self.make = make
        self.model = model
        self.deriv = deriv
class cap_n_otr():
    def __init__(self,capcode, otr):
        self.capcode = capcode
        self.otr = otr

class cap_n_stuff():
    def __init__(self,capcode,model,make,deriv, otr, blp):
        self.capcode = capcode
        self.model = model
        self.deriv = deriv
        self.otr = otr
        self.blp = blp
        self.make = make

class deal_pair_final():
    def __init__(self,capcode,months,miles,cm, fm, make, model, deriv,otr,blp , months_up):
        self.capcode = capcode
        self.months = months
        self.miles = miles
        self.cm=cm
        self.fm=fm
        self.make = make
        self.model = model
        self.deriv = deriv
        self.blp = blp
        self.otr = otr
        self.months_up = months_up

def save_what_we_got444(name,info_to_save):
    finaldf = pd.DataFrame({'capcode':[],'make':[],'model':[],'deriv':[],'month':[],'mile':[],'cm':[],'fm':[],'otr':[],'blp':[],'months up':[] })
    for c in info_to_save:
        df_1_deal = pd.DataFrame({'capcode':[c.capcode],'make':[c.make],'model':[c.model],'deriv':[c.deriv],'month':[c.months],'mile':[c.miles],'cm':[c.cm],'fm':[c.fm],'otr':[c.otr],'blp':[c.blp] , 'months up':[c.months_up]})
        finaldf = finaldf.append(df_1_deal)

    finaldf.to_csv(str(name)+".csv")
    print("saved")


def get_excel_file():
    print("oi");
    print(" oi 1a ");
    old_arval_deals = []
    thedb = pd.read_csv("alf7.csv")
    print("oi2")

    for i in range(thedb.shape[0]):
        print("for a thing")  #############
        raw_otr = thedb.iloc[i]['OTR'].replace(",","")  ###
        otr = "";  ########################
        for j in raw_otr:
            if j.isnumeric() or j == '.':
                otr += j
        old_arval_deals.append(cap_n_otr(thedb.iloc[i]["CAP Code"] , otr ))
    return(old_arval_deals)

def get_diy_file():
    thedb = pd.read_csv("diy_alphabet.csv")
    return thedb

def get_excel_file_with_model_and_deriv():
    print("oi   sttttt")
    old_arval_deals = []
    for i in range(25):
        try:
            thedb = pd.read_csv(str(i)+".csv")
        except:
            print("naaaaaa" + str(i))


    print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
    print(thedb.shape[0])
    print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")

    for i in range(thedb.shape[0]-1):
     #   print("oi prob")

        try:
            otr = (thedb.iloc[i]['OTR']) #.replace(" GBP",""))
        except:
            try:
                otr = (thedb.iloc[i]['otr']) #.replace(" GBP",""))
            except:
                try:
                    otr = (thedb.iloc[i]['OTR Column'])
                except:
                    otr = (thedb.iloc[i]['real OTR']) #.replace(" GBP",""))

    #    otr = otr.replace(",","")
      #  print("hah")
   #     otr = "";
    #    for j in raw_otr:
     #       if j.isnumeric() or j == '.':
      #          otr += j
        try:
            make = thedb.iloc[i][' Manufacture']
        except:
            try:
                make = thedb.iloc[i]['Manufacturer']
            except:
                make = thedb.iloc[i]['make']
        try:
            model  = thedb.iloc[i][' Model Name']
        except:
            try:
                model  = thedb.iloc[i]['Model Name']
            except:
                model  = thedb.iloc[i]['model']

        try:
            deriv  = thedb.iloc[i][' Variant']
        except:
            try:
                deriv  = thedb.iloc[i]['Variant']
            except:
                deriv  = thedb.iloc[i]['deriv']

        try:
            blp = (thedb.iloc[i][' Basic List Price'])#.replace(" GBP",""))
        except:
            try:
                blp = (thedb.iloc[i]['Basic List'])
            except:
                blp = (thedb.iloc[i]['blp'])
        try:
            thecap = thedb.iloc[i]["Cap Code"]
        except:
            try:
                thecap = thedb.iloc[i]["capcode"]
            except:
                pass

        old_arval_deals.append(cap_n_stuff(thecap, model ,make, deriv , otr, blp ))

    print("oi prob  ")

    return(old_arval_deals)

def save_what_we_got(name,info_to_save):
    nar = str(datetime.datetime.now())
    nar = nar.replace(":", "-")
    print(str(nar))
    finaldf = pd.DataFrame({'capcode':[],'cm 9up 10k 24months':[],'blp':[], 'rv':[] })
    for c in info_to_save:
        df_1_deal = pd.DataFrame({'capcode':[],'cm 9up 10k 24months':[c.price],'blp':[c.blp], 'rv':[float(float(c.blp)/float(c.price))] })
        finaldf = finaldf.append(df_1_deal)
    finaldf.to_csv(str(name) + "    " + str(nar)+".csv")
    print("saved")

def save_what_we_got2(name,info_to_save):
    finaldf = pd.DataFrame({'capcode':[],'miles':[], 'months':[], 'cm':[], 'fm':[]})
    for c in info_to_save:
        print(type(c))
        print(c.capcode)
        df_1_deal = pd.DataFrame({'capcode':[c.capcode],'miles':[c.miles], 'months':[c.months], 'cm':[c.nomaintprice], 'fm':[c.maintprice]})
        finaldf = finaldf.append(df_1_deal)
    finaldf.to_csv(str(name)+".csv")
    print("saved")


def save_what_we_got3(name,info_to_save):
    finaldf = pd.DataFrame({'capcode':[],})
    for c in info_to_save:
        df_1_deal = pd.DataFrame({'capcode':[c],})
        finaldf = finaldf.append(df_1_deal)
    finaldf.to_csv(str(name)+".csv")
    print("saved")

def final_save(new_deals):
    finaldf = pd.DataFrame({'capcode':[],'cm 9up 10k 24months':[],'blp':[], 'rv':[] })
    for c in new_deals:
        df_1_deal = pd.DataFrame({'capcode':[c.capcode],'cm 9up 10k 24months':[c.price],'blp':[c.blp], 'rv':[float(float(c.blp)/float(c.price))] })
        finaldf = finaldf.append(df_1_deal)
    finaldf.to_csv("first rv.csv")
    print("oi weve finally done")
