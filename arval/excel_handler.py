import pandas as pd
import datetime
class deal_pair():
    def __init__(self,capcode,months,miles,nomaintprice, maintprice ,make,model,deriv,blp,otr):
        self.capcode = capcode
        self.months = months
        self.miles = miles
        self.maintprice = maintprice
        self.nomaintprice = nomaintprice
        self.make = make
        self.model = model
        self.deriv = deriv
        self.blp = blp
        self.otr=otr

class roadside_ass():
    def __init__(self,man, yrs2,yrs3,yrs4, cap):
        self.man = man
        self.yrs2 = yrs2
        self.yrs3 = yrs3
        self.yrs4 = yrs4
        self.cap = cap



class cap_n_otr():
    def __init__(self,capcode, otr):
        self.capcode = capcode
        self.otr = otr

class cap_n_otr_n_name():
    def __init__(self,capcode, otr , make, model, deriv, blp):
        self.capcode = capcode
        self.otr = otr
        self.make = make
        self.model = model
        self.deriv = deriv
        self.blp = blp

def get_excel_file():
    old_arval_deals = []
    for i in range(50):
        try:    
            thedb = pd.read_csv(str(i)+".csv" , dtype = str)    
        except:
            print(i)
 #   thedb = pd.read_csv("1.csv" , dtype = str)
    for i in range(thedb.shape[0]):
        raw_otr = str(thedb.iloc[i]['OTR'])
        otr = "";
        for j in raw_otr:
            if j.isnumeric() or j == '.':
                otr += j
        try:
            make = str(thedb.iloc[i][' Manufacture'])
        except:
            make = str(thedb.iloc[i]['Manufacturer'])
        try:
            model = str(thedb.iloc[i][' Model Name'])
        except:
            model = str(thedb.iloc[i]['Model Name'])
        try:
            deriv = str(thedb.iloc[i][' Variant'])
        except:
            deriv = str(thedb.iloc[i]['Variant'])

        old_arval_deals.append(cap_n_otr_n_name(thedb.iloc[i]["Cap Code"] , otr, make,model,deriv,thedb.iloc[i]["Basic List"] ))
    return(old_arval_deals)
    
def save_what_we_got23(name,info_to_save):
    finaldf = pd.DataFrame({'cap_code':[] ,'annual_mileage':[], 'contract_length':[], 'customer_maintained_rental':[], 'funer_maintained_rental':[]})
    for c in info_to_save:
        print(type(c))
        print(c.capcode)
        df_1_deal = pd.DataFrame({'cap_code':[c.capcode] ,'annual_mileage':[c.miles], 'contract_length':[c.months], 'customer_maintained_rental':[c.nomaintprice], 'funer_maintained_rental':[c.maintprice]}) 
        finaldf = finaldf.append(df_1_deal)
    
    finaldf.to_csv(str(name)+".csv")
    print("saved")




def save_what_we_got2(name,info_to_save):
    finaldf = pd.DataFrame({'cap_code':[] ,'annual_mileage':[], 'contract_length':[], 'customer_maintained_rental':[], 'funer_maintained_rental':[], 'make':[], 'model':[], 'deriv':[], 'blp':[], 'otr':[]})
    for c in info_to_save:
        print(type(c))
        print(c.capcode)
        df_1_deal = pd.DataFrame({'cap_code':[c.capcode] ,'annual_mileage':[c.miles], 'contract_length':[c.months], 'customer_maintained_rental':[c.nomaintprice], 'funer_maintained_rental':[c.maintprice] , 'make':[c.make], 'model':[c.model], 'deriv':[c.deriv], 'blp':[c.blp], 'otr':[c.otr]}) 
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


def save_what_we_got309(name,d1 , d2):
    finaldf = pd.DataFrame({'capcode':[], 'blp':[]})
    for jax in range(len(d1)-1):

        df_1_deal = pd.DataFrame({'capcode':[d1[jax]],'blp':[d2[jax]] }) 
        finaldf = finaldf.append(df_1_deal)
    finaldf.to_csv(str(name)+".csv")
    print("saved 309")

def final_save(new_deals):
    finaldf = pd.DataFrame({'capcode':[],'cm 9up 10k 24months':[],'blp':[], 'rv':[] })

    for c in new_deals:
        df_1_deal = pd.DataFrame({'capcode':[c.capcode],'cm 9up 10k 24months':[c.price],'blp':[c.blp], 'rv':[float(float(c.blp)/float(c.price))] }) 
        finaldf = finaldf.append(df_1_deal)
    
    finaldf.to_csv("first rv.csv")
    print("oi weve finally done")

def final_save2(new_deals):
    finaldf = pd.DataFrame({'capcode':[],'cm 9up 10k 24months':[],'blp':[], 'rv':[] })

    for c in new_deals:
        df_1_deal = pd.DataFrame({'capcode':[c.capcode],'cm 9up 10k 24months':[c.price],'blp':[c.blp], 'rv':[float(float(c.blp)/float(c.price))] }) 
        finaldf = finaldf.append(df_1_deal)
    
    finaldf.to_csv("first rv.csv")
    print("oi weve finally done")

def get_man_roadside_assistance():
    man_ass = []
    thedb = pd.read_csv("Manufacturer Roadside Assistance.csv")    

    for i in range(thedb.shape[0]):
        
        make = str(thedb.iloc[i]['Manufacturer'])
        yrs2 = str(thedb.iloc[i]['2 Years'])
        yrs3 = str(thedb.iloc[i]['3 Years'])
        yrs4 = str(thedb.iloc[i]['4 Years'])
        cap = str(thedb.iloc[i]['cap'])   
        man_ass.append(roadside_ass(make, yrs2, yrs3, yrs4, cap))

    return(man_ass)

    
def join_all():
    ################### hitatchi prices round = 1
    ####################hitatchi prices round = 1.csv
    import os
    cwd = os.getcwd()
    print(cwd)
    arr = os.listdir()
    print(arr)
    for a in arr:
        print(a)
    cols = pd.read_csv("current progress 1.csv", dtype = str).columns;
    finaldf = pd.DataFrame(data = None , columns = cols)            
    for i in range(5):
        try:
            thedb = pd.read_csv("current progress  "+str(i)+".csv", dtype = str)
            finaldf = finaldf.append(thedb)
        except:
            pass
    finaldf.to_csv("final combined.csv")
