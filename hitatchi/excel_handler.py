import pandas as pd
import datetime
class deal_pair():
    def __init__(self,capcode,months,miles,maintprice, nomaintprice, options):
        self.capcode = capcode
        self.months = months
        self.miles = miles
        self.maintprice = maintprice
        self.nomaintprice = nomaintprice
        self.options = options


class deal_pair_qn():
    
    def __init__(self,capcode,months,miles,maintprice, nomaintprice, options , qn , deriv , otr , van, blp):
        self.capcode = capcode
        self.months = months
        self.miles = miles
        self.maintprice = maintprice
        self.nomaintprice = nomaintprice
        self.options = options
        self.qn = qn
        self.deriv = deriv
        self.otr = otr
        self.van = van
        self.blp = blp

class cap_n_otr():
    def __init__(self,capcode, otr):
        self.capcode = capcode
        self.otr = otr

class cap_n_stuff():
    def __init__(self,capcode,model,deriv, otr, blp):
        self.capcode = capcode
        self.model = model
        self.deriv = deriv
        self.otr = otr
        self.blp = blp


def get_excel_file():
    print("oi")
    old_arval_deals = []
    thedb = pd.read_csv("OTRs 2.0 aa.csv")
    print("oi2")

    for i in range(thedb.shape[0]):
    #    print("for a thing")
        raw_otr = str(thedb.iloc[i]['OTR'])
        otr = "";
        for j in raw_otr:
            if j.isnumeric() or j == '.':
                otr += j
        old_arval_deals.append(cap_n_otr(thedb.iloc[i]["Cap Code"] , otr ))
    return(old_arval_deals)

class diy():
    def __init__(self,capcode, make, model, deriv , my , blp, cap_id):
        self.capcode = capcode
        self.make = make
        self.model = model
        self.deriv = deriv
        self.my = my
        self.blp = blp
        self.cap_id = cap_id

class acar():
    def __init__(self,capcode, blp, otr):
        self.capcode = capcode
        self.blp = blp
        self.otr = otr




def get_cars():
    final= []
    for i in range(30):
        try:
            thedb = pd.read_csv(str(i)+".csv"  ,  dtype = str)
        except:
            pass

    for i in range(thedb.shape[0]):
        capcode = str(thedb.iloc[i]['Cap Code'])
        try:
            blp = str(thedb.iloc[i][' Basic List Price'])
        except:
            blp = str(thedb.iloc[i]['Basic List'])

        otr = str(thedb.iloc[i]['OTR'])


        final.append(acar(capcode,blp,otr))
    return(final)

def not_match_save(new_deals):
    finaldf = pd.DataFrame({'capcode':[]})

    for c in new_deals:
        df_1_deal = pd.DataFrame({'capcode':[c.capcode]})
        finaldf = finaldf.append(df_1_deal)

    try:
        finaldf.to_csv("no comparison match, hitatchi might not have these   .csv")
    except:
        finaldf.to_csv("no comparison match, hitatchi might not have these  spare close main .csv")


def get_comp():
    thedb = pd.read_csv("hit_comp.csv", dtype = str)
    final = []
    for i in range(thedb.shape[0]):

  #      print("for a thing")
        capcode = str(thedb.iloc[i]['CAP Code'])
        make = str(thedb.iloc[i]['Make'])
        model = str(thedb.iloc[i]['Model'])
        deriv = str(thedb.iloc[i]['Variant Full Description'])
        my = str(thedb.iloc[i]['Model Year'])
        blp = str(thedb.iloc[i]['Vehicle List Price'])
        try:
            cap_id = str(thedb.iloc[i]['CAP ID'])
        except:
            cap_id = str(thedb.iloc[i]['Variant'])
        blp2 = ""
        counter = 0
        for char in blp:
            if counter == 2:
                blp2 += ","
            blp2+=char
            counter +=1

        if make.lower() in deriv.lower():
            deriv2 = deriv.replace(make , "")

        final.append(diy(capcode , make, model , deriv2 , my , blp2, cap_id))
    return(final)


def get_excel_file_with_model_and_deriv():
    print("oi   sttttt")
    old_arval_deals = []
    thedb = pd.read_csv("OTRs 2.0 aa.csv")

    print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
    print(thedb.shape[0])
    print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")

    for i in range(thedb.shape[0]-1):
        print("oi prob")
        otr = float((thedb.iloc[i]['OTR']))
        print("hah")
   #     otr = "";
    #    for j in raw_otr:
     #       if j.isnumeric() or j == '.':
      #          otr += j
      
        model  = thedb.iloc[i][' Model Name']
        deriv  = thedb.iloc[i][' Variant']
        blp = float(thedb.iloc[i][' Basic List Price'])
        print("oi pro fuck   767676")
        old_arval_deals.append(cap_n_stuff(thedb.iloc[i]["Cap Code"], model , deriv , otr, blp ))
    print("oi prob   fuck")
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

def save(stuff, price):
    finaldf = pd.DataFrame({'stuff':[],'price':[]})

    for c in range(len(stuff)-1):
        df_1_deal = pd.DataFrame({'stuff':[stuff[c]],'price':[price[c]]})
        finaldf = finaldf.append(df_1_deal)

    finaldf.to_csv(" stuff you need n prices .csv")
    print("oi weve finally done")

def save2(stuff , name):
    finaldf = pd.DataFrame({'stuff':[]})

    for c in range(len(stuff)-1):
        df_1_deal = pd.DataFrame({'stuff':[stuff[c]]})
        finaldf = finaldf.append(df_1_deal)

    finaldf.to_csv(str(name)+".csv")
    print("oi weve finally done")


def save_what_we_got_qn(name,info_to_save):
    finaldf = pd.DataFrame({'capcode':[],'miles':[], 'months':[], 'cm':[], 'fm':[], 'options':[], 'quote num for 24m 10k cm':[], 'car nam':[], 'otr':[], 'is van':[], 'blp':[]})
    for c in info_to_save:
        print(type(c))
        print(c.capcode)
        df_1_deal = pd.DataFrame({'capcode':[c.capcode],'miles':[c.miles], 'months':[c.months], 'cm':[c.nomaintprice], 'fm':[c.maintprice], 'options':[c.options], 'quote num for 24m 10k cm':[c.qn] , 'car nam':[c.deriv], 'otr':[c.otr] , 'is van':[c.van] , 'blp':[c.blp]})
        finaldf = finaldf.append(df_1_deal)

    finaldf.to_csv(str(name)+".csv")
    print("saved")

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
    cols = pd.read_csv(" hitatchi prices round = 1.csv", dtype = str).columns;
    finaldf = pd.DataFrame(data = None , columns = cols)
    for i in range(5):
        try:
            thedb = pd.read_csv(" hitatchi prices round = "+str(i)+".csv", dtype = str)
            finaldf = finaldf.append(thedb)
        except:
            pass
    finaldf.to_csv("final combined.csv")
