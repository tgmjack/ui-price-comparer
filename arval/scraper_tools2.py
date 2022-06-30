import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions as s_ex
import pandas as pd
import pyautogui
import keyboard
import selenium.webdriver.chrome.options as Options
import pydirectinput
from selenium.webdriver.support.ui import Select
import datetime

def prove2(driver):
    print("big oldf fucking bread crum 99")
    cant_interact_with_months_box = True;
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while cant_interact_with_months_box:
        if datetime.datetime.now() > future:
            print(1/0)
        print("interact")
        try: #/html/body/div[8]/div[3]/div[2]/div[6]/div/table/tbody/tr[44]/td[2]/input
            monthsxpath = '//*[@id="txtTerm"]'
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,monthsxpath)))
            months = driver.find_element_by_xpath(monthsxpath)
            delete(months)
            cant_interact_with_months_box = False
       # except:
     #       try:
            recalc_xpath='//*[@id="buttonSaveQuotation"]/tbody/tr/td[2]/a';
            WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,recalc_xpath)))
            recalc = driver.find_element_by_xpath(recalc_xpath)
            click(recalc)
            delete(months)
            cant_interact_with_months_box = False
        except:
            #print(driver.page_source)
            try_accept_wltp(driver)
            try_dismiss_wltp(driver)
            driver.switch_to.default_content()
            try_to_move_into_frame(driver)
            #print(driver.page_source)

def get_this_price(driver , thesemonths, thesemiles, our_maint):
    time.sleep(0.5)
    wait_for_loading(driver)
    time.sleep(0.5)
    pricexpath = '//*[@id="txtPeriodicPayment"]'

    prove2(driver)

    if our_maint == False:
        choose_maint(driver, False)
    prove2(driver)

    monthsxpath = '//*[@id="txtTerm"]';
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,monthsxpath)))
    months = driver.find_element_by_xpath(monthsxpath)
    delete(months)
    months.send_keys(str(thesemonths))
    wait_for_loading(driver)
    print("prices bc 17")
    milesxpath = '//*[@id="txtAnnualDistance"]'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,milesxpath)))
    miles = driver.find_element_by_xpath(milesxpath)
    delete(miles)
    miles.send_keys(str(thesemiles))
    wait_for_loading(driver)

    update_price_xpath = '//*[@id="buttonSaveQuotation"]/tbody/tr/td[2]/a'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,update_price_xpath)))
    update_price = driver.find_element_by_xpath(update_price_xpath)
    wait_for_loading(driver)
    click(update_price)
    time.sleep(1)
    wait_for_loading(driver)

    theprice = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,pricexpath))).get_attribute("value"))

    return theprice;

def only_1_paint(driver):
    time.sleep(0.5)
    wait_for_loading(driver)
    time.sleep(0.5)

  #  try:
   #     #print(driver.page_source)
    #    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,extras_list_id)))
  #  except:
   #     driver.switch_to.parent_frame()
  #  #print(driver.page_source)

    try:
        extras_list_id = 'tblExtrasFactory';
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,extras_list_id)))
        q_opts = driver.find_element_by_id(extras_list_id)
        the_opts = q_opts.find_elements_by_tag_name("tr")
    except:
        print(9/0)
        return False

    cunter = 0
    wait_for_loading(driver)
    while(len(the_opts)>1):
        print(" opts removing loop")
        if len(the_opts)>1:
            names = []
            prices = []
            print("cleaned")
            for i in the_opts:
                print(i.get_attribute("innerHTML"))
                data = i.find_elements_by_tag_name("td")
                for d in data:
                    print(d.get_attribute("innerHTML"))
                    if (cunter % 2 == 0):
                        print("even = "+str(d.get_attribute("innerHTML")))
                        names.append(d.get_attribute("innerHTML"));
                    else:
                        prices.append(d.get_attribute("innerHTML"));
                        print("odd = "+str(d.get_attribute("innerHTML")))
                    cunter += 1;
        cheapest = prices[0]
        cheapest_add_on = names[0]


        for i in range(len(names)):
            if prices[i]<cheapest:
                cheapest = prices[i]
                cheapest_add_on = names[i]
            print(str(i)+" =extra_num    names    "+str(names[i]) + "       price    "+str(prices[i]))

        wait_for_loading(driver)

        amend_options_class = 'applicationbuildbutton';

        buttons = driver.find_elements_by_class_name(amend_options_class)

        amend_clicked = False
        for but in buttons:
            if not amend_clicked:
                if "Amend options" == but.get_attribute("innerHTML").strip():
                    but.click()
                    amend_clicked = True
        wait_for_loading(driver)

        extra_opts_body_xp = '/html/body/div[8]/div[3]/div[2]/div[6]/table[1]/tbody';

        internal_extra_opts_body_xp ='/html/body/div[8]/div[3]/div[2]/div[6]/table[1]/tbody/tr[6]/td/table/tbody';
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,internal_extra_opts_body_xp)))
        internal_extra_opts_body = driver.find_element_by_xpath(internal_extra_opts_body_xp)

        trs = internal_extra_opts_body.find_elements_by_tag_name("tr")

        for add in names:
            print("1a ")
            thisclicked = False
            for tr in trs:
                if not thisclicked:
                    print("2a ")
                    if add != cheapest_add_on:
                        print("3a ")
                        print(tr.get_attribute("innerHTML"))
                        if add in tr.get_attribute("innerHTML"):
                            print("4a ")
                            but = tr.find_element_by_tag_name("input");
                            but.click()
                            print("clickedy click click")
                            thisclicked = True
        print("the condition ")

        summary_class = 'applicationbuildbutton'
        buts = driver.find_elements_by_class_name(summary_class)
        for b in buts:
            if "Quotation summary" in b.get_attribute("innerHTML"):
                b.click()
        wait_for_loading(driver)
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,extras_list_id)))
        q_opts = driver.find_element_by_id(extras_list_id)
        the_opts = q_opts.find_elements_by_tag_name("tr")
        wait_for_loading(driver)

        for r in the_opts:
            print(r)


def make_finder(make):

    print("mmiimmii")
    og_capcode = "ff"
    if "land rover".lower() in make:
        og_capcode = 'LR'

    if "DS Automobiles".lower() in make:
        og_capcode = 'DS'

    if "Citroen".lower() in make:
        og_capcode = 'CI'

    if "Audi".lower() in make:
        og_capcode = 'AU'

    if "Seat".lower() in make:
        og_capcode = 'SE'

    if "Abarth".lower() in make:
        og_capcode = 'AB'

    if "ALFA ROMEO".lower() in make:
        og_capcode = 'AL'

    if "BMW".lower() in make:
        og_capcode = 'BM'


    if "DACIA".lower() in make:
        og_capcode = 'DA'


    if "FIAT".lower() in make:
        og_capcode = 'FI'


    if  "FORD".lower() in make:
        og_capcode = 'FO'


    if  "HONDA".lower()  in make:
        og_capcode = 'HO'

    if "HYUNDAI".lower() in make:
        og_capcode = 'HY'

    if  "ISUZU".lower() in make:
        og_capcode = 'IS'


    if  "ISUZU TRUCKS".lower() in make:
        og_capcode = 'IT'


    if "IVECO".lower() in make:
        og_capcode = 'IV'


    if "JAGUAR".lower() in make:
        og_capcode = 'JA'


    if "JEEP".lower() in make:
        og_capcode = 'JE'


    if "KIA".lower() in make:
        og_capcode = 'KI'


    if "LEXUS".lower() in make:
        og_capcode = 'LE'


    if "LOTUS".lower() in make:
        og_capcode = 'LS'
        #

    if "MAN".lower() in make:
        og_capcode = 'M3'

    if "MASERATI".lower() in make:
        og_capcode = 'MS'


    if "MAXUS".lower() in make:
        og_capcode = 'MX'


    if "MAZDA".lower() in make:
        og_capcode = 'MA'


    if "MERCEDES-BENZ".lower() in make:
        og_capcode = 'ME'


    if "MG MOTOR UK".lower() in make:
        og_capcode = 'NM'


    if "MINI".lower() in make:
        og_capcode = 'MN'


    if "MITSUBISHI".lower() in make:
        og_capcode = 'MI'


    if "NISSAN".lower() in make:
        og_capcode = 'NI'


    if "MGMOTORUK".lower() in make:
        og_capcode = 'NM'


    if "POLESTAR".lower() in make:
        og_capcode = 'PS'


    if "PORSCHE".lower() in make:
        og_capcode = 'PO'

    if "RENAULT".lower() in make:
        og_capcode = 'R1'

    if "PEUGEOT".lower() in make:
        og_capcode = 'PE'


    if "SEAT".lower() in make:
        og_capcode = 'SE'

    if "SKODA".lower() in make:
        og_capcode = 'SK'


    if "SSANGYONG".lower() in make:
        og_capcode = 'SS'


    if "SUBARU".lower() in make:
        og_capcode = 'SU'


    if "SUZUKI".lower() in make:
        og_capcode = 'SI'


    if "TESLA".lower() in make:
        og_capcode = 'TE'


    if "TOYOTA".lower() in make:
        og_capcode = 'TO'

    if "VAUXHALL".lower() in make:
        og_capcode = 'VA'

    if "VOLKSWAGEN".lower() in make:
        og_capcode = 'VW'


    if "VOLVO".lower() in make:
        og_capcode = 'VO'


    return og_capcode



def wait_for_delete():
    car_chosen = False
    while not car_chosen:
        if keyboard.is_pressed('q'):
            car_chosen = True
            print("were off :)")

def read_txt_file():
    with open('config.txt') as f:
        lines = f.readlines()
        pound_counter = 0
        username_got = False
        password_got = False
        doing_customer = False
        username = ""
        password = ""
        customer = ""
        for line in lines:
            for char in line:
                if password_got:
                    print("pg")
                print(char)
#                if char=="
                if pound_counter == 100 and char == '"':
                    pound_counter =-3
                    if not username_got:
                        username_got = True
                    else:
                        password_got = True

                if pound_counter == 100 and char != '"' and username_got and password_got:
                    customer += char



                if pound_counter == 100 and char != '"' and not username_got and not password_got:
                    username += char

                    print("appending char")
               #     pound_counter = 0
                if pound_counter == 100 and char != '"' and username_got and not password_got:
                    password += char
                    print("appending char")
#                    password_got = True
                #    pound_counter = 0
                if char == "£":
                    print("£")
                    pound_counter+=1
                if pound_counter == 3 and char == '"':
                    pound_counter = 100

    return username, password, customer

def website_down_for_maint_checker(driver):
    mnt = 'We are currently performing scheduled maintenance.'
    down_for_maint = True
    maint_waiter = 1
    while down_for_maint:
        print("m")
        if mnt in driver.page_source:
            print("maint is in html")
            maint_waiter += 1
            time.sleep(maint_waiter*30)
        else:
            down_for_maint = False
         #   #print(driver.page_source)


def remove_breakdown_ass(driver):
#    //*[@id="buttonContractServices"]/tbody/tr/td[2]/a
#    //*[@id="lstMotorClub"]/option[2]
#   //*[@id="btnUpdateServices"]/tbody/tr/td[2]/a
    print("remove brek 1 ")
    try_accept_wltp(driver)
    try_dismiss_wltp(driver)
 #   #print(driver.page_source)
    print("remove brek 2 ")
    q_opts_xp = '//*[@id="buttonContractServices"]/tbody/tr/td[2]/a';
    no_recov_xp = '//*[@id="lstMotorClub"]/option[2]';
    close_xp = '//*[@id="btnUpdateServices"]/tbody/tr/td[2]/a';
    q_services_frame_xpath = '//*[@id="ifPopupInternalWindow"]'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,q_opts_xp)))
    q_opts = driver.find_element_by_xpath(q_opts_xp)
    click(q_opts)
    print("remove brek 3")

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,q_services_frame_xpath)))
    frame2 = driver.find_element_by_xpath(q_services_frame_xpath)
    driver.switch_to.frame(frame2)
    print("remove brek 4 ")

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,no_recov_xp)))
    no_recov = driver.find_element_by_xpath(no_recov_xp)
    click(no_recov)
    print("remove brek 5")

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,close_xp)))
    close_but = driver.find_element_by_xpath(close_xp)
    click(close_but)
    try_to_move_into_frame(driver)
    print("remove brek 6 ")
    try_to_move_into_frame(driver)
    try_accept_wltp(driver)
    try_dismiss_wltp(driver)
    print("remove brek 7 ")
 #   #print(driver.page_source)




def enter_otr(driver, otr):

    print("entering otr")
    otr_xpath = '//*[@id="txtOnTheRoad"]';
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,otr_xpath)))
    otr_box = driver.find_element_by_xpath(otr_xpath)
    default_otr = otr_box.get_attribute("value");
 #   if default_otr < otr: # *0.8
  #      print("default otr is better")
   #     return True
    delete(otr_box)
    otr_box.send_keys(otr)
    recalc_xpath='//*[@id="buttonSaveQuotation"]/tbody/tr/td[2]/a';
    WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,recalc_xpath)))
    recalc = driver.find_element_by_xpath(recalc_xpath)
    click(recalc)
    print("finished entering otr")

def reset_1(driver):
#    //*[@id="subPMENULI1"]/li[1]/a
    try:
        new_quote_xpath2 = '//*[@id="subPMENULI1"]/li[1]/a'
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,new_quote_xpath2)))
        new_quote_button_2 = driver.find_element_by_xpath(new_quote_xpath2)
        click(new_quote_button_2)
    except:
        try_dismiss_wltp(driver)
        try_accept_wltp(driver)
        try_to_move_into_frame(driver)
        driver.execute_script('alert("Clearing out past dialogs.")')
        driver.switch_to.alert.accept()


def remove_breakdown(driver):

    #    //*[@id="buttonContractServices"]/tbody/tr/td[2]/a
    #     //*[@id="lstMotorClub"]/option[2]
    #    //*[@id="btnUpdateServices"]/tbody/tr/td[2]/a
    new_quote_xpath2 = '//*[@id="buttonContractServices"]/tbody/tr/td[2]/a'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,new_quote_xpath2)))
    new_quote_button_2 = driver.find_element_by_xpath(new_quote_xpath2)
    click(new_quote_button_2)

#//*[@id="lstMotorClub"]/option[2]

  #  #print(driver.page_source)
#  time.sleep(0.5)
 # wait_for_loading(driver)
  #time.sleep(0.5)
    try_to_move_into_frame(driver)
   # #print(driver.page_source)

#//*[@id="lstMotorClub"]/option[2]
    #//*[@id="lstMotorClub"]
    new_quote_xpath2 = '//*[@id="lstMotorClub"]'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,new_quote_xpath2)))
    new_quote_button_2 = driver.find_element_by_xpath(new_quote_xpath2)
    click(new_quote_button_2)



    new_quote_xpath2 = '//*[@id="lstMotorClub"]/option[2]'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,new_quote_xpath2)))
    new_quote_button_2 = driver.find_element_by_xpath(new_quote_xpath2)
    click(new_quote_button_2)


    new_quote_xpath2 = '//*[@id="btnUpdateServices"]/tbody/tr/td[2]/a'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,new_quote_xpath2)))
    new_quote_button_2 = driver.find_element_by_xpath(new_quote_xpath2)
    click(new_quote_button_2)

def double_check_terms(driver, milesata, thesemiles, monthsata, thesemonths, this_manu_terms, maint ):

    monthsxpath = '//*[@id="txtTerm"]'
    milesxpath = '//*[@id="txtAnnualDistance"]'

    milesata = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,milesxpath))).get_attribute("value"))
    monthsata = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,monthsxpath))).get_attribute("value"))
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)

    while (int(milesata) != int(thesemiles)) or (int(monthsata) != int(thesemonths)):
        if datetime.datetime.now() > future:
            print(1/0)
        print("miles ata thing")
        print("month 3 mile 0 extra click")
        print("miles in box currently == " + str(milesata))
        print("we want  == " + str(thesemiles))
        print("months in box currently == " + str(monthsata))
        print("we want  == " + str(thesemonths))

        months = driver.find_element_by_xpath(monthsxpath)
        delete(months)
        months.send_keys(thesemonths)

        recalc_xpath='//*[@id="buttonSaveQuotation"]/tbody/tr/td[2]/a';
        WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,recalc_xpath)))
        recalc = driver.find_element_by_xpath(recalc_xpath)
        click(recalc)

        miles = driver.find_element_by_xpath(milesxpath)
        delete(miles)
        miles.send_keys(thesemiles)

        recalc_xpath='//*[@id="buttonSaveQuotation"]/tbody/tr/td[2]/a';
        WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,recalc_xpath)))
        recalc = driver.find_element_by_xpath(recalc_xpath)
        click(recalc)
        wait_for_loading(driver)
        milesata = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,milesxpath))).get_attribute("value"))
        monthsata = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,monthsxpath))).get_attribute("value"))
        if int(milesata) != int(thesemiles):
            print("they still dont match")
        wait_for_loading(driver)


    error_counter = 0
    break_down_manu = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not break_down_manu:
        if datetime.datetime.now() > future:
            print(1/0)
        if maint == 0:
            error_counter+=1
            if error_counter > 7:
                do_new_manu(driver, this_manu_terms, maint)
            print("not manu dc doc func loop    ====================================================================================     yuyu")
      #      #print(driver.page_source)
            #          //*[@id="tblALSbody"]/tbody/tr/td[3]
            info_xp = '//*[@id="tblALSbody"]/tbody/tr/td[3]'
            WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,info_xp)))
            info = driver.find_element_by_xpath(info_xp).get_attribute("innerHTML")
            print(str(info)+"          info     mmmmmmmmmmmmmmmmm  ")


            try:
                print("dmanu loop t1")
                if math.isnan(this_manu_terms):
                    print("info loop t1")
                    info_xp = '//*[@id="tblALSbody"]/tbody/tr/td[3]'
                    WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,info_xp)))
                    info = driver.find_element_by_xpath(info_xp).get_attribute("innerHTML")
                    print(str(info)+"          info     t1  ")
                    if "Breakdown Assistance" in info:
                        break_down_manu = True
                        print(" break_down_manu  = true")
            except:
                try:
                    print("dmanu loop t2")
                    if this_manu_terms == "nan":
                        print("info loop t2")
                        info_xp = '//*[@id="tblALSbody"]/tbody/tr/td[3]'
                        WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,info_xp)))
                        info = driver.find_element_by_xpath(info_xp).get_attribute("innerHTML")
                        print(str(info)+"          info     t2  ")
                        if "Breakdown Assistance" in info:
                            break_down_manu = True
                            print(" break_down_manu  = true")
                except:
                    print("compare 1 error ")
                    print(1/0)

            try:
                print(" dmanu loop t3 ")

                if this_manu_terms.lower().strip() == "inc":
                    print("info loop t3")
                    info_xp = '//*[@id="tblALSbody"]/tbody/tr/td[3]'
                    WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,info_xp)))
                    info = driver.find_element_by_xpath(info_xp).get_attribute("innerHTML")
                    print(str(info)+"          info     t3  ")
                    if not "Breakdown Assistance" in info:
                        break_down_manu = True
                        print(" break_down_manu  = true")
            except:
                print("222")


        if maint == 1:
            print("cm loop")
            info_xp = '//*[@id="tblALSbody"]/tbody/tr/td[3]'
            WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,info_xp)))
            info = driver.find_element_by_xpath(info_xp).get_attribute("innerHTML")
            print(str(info)+"          info     t2  ")
            if not "Breakdown Assistance" in info:
                break_down_manu = True
                print(" break_down_manu  = true")
            else:
                do_new_manu(driver, this_manu_terms, maint)



    print("terms are good")
    return True

def prove_we_can_interact_with_page(driver, optional_time = 4):
    print("interact test start")
    counter = 0
    try:
        #print(driver.page_source)
        months_up_xp = '//*[@id="txtAdvancePayments"]'
        print("interact test start 2 ")
        WebDriverWait(driver,optional_time).until(EC.presence_of_element_located((By.XPATH,months_up_xp)))
        months_up = driver.find_element_by_xpath(months_up_xp)
        months_up_txt = str(months_up.get_attribute("value"))
        print("months_up_txt")
        print(months_up_txt)
        delete(months_up)
        months_up.send_keys(months_up_txt)
        print("interact test success")
        return True
    except:
        driver.switch_to.default_content()
        try_to_move_into_frame(driver)
        #print(driver.page_source)
        months_up_xp = '//*[@id="txtAdvancePayments"]'
        print("interact test start 2 ")
        WebDriverWait(driver,optional_time).until(EC.presence_of_element_located((By.XPATH,months_up_xp)))
        months_up = driver.find_element_by_xpath(months_up_xp)
        months_up_txt = str(months_up.get_attribute("value"))
        print("months_up_txt")
        print(months_up_txt)
        delete(months_up)
        months_up.send_keys(months_up_txt)
        print("interact test success")
        return True
    return False
 #       try:
  #          months_up_id = 'txtAdvancePayments'
   #         print("interact test start 2 ")
          #  #print(driver.page_source)
    #        WebDriverWait(driver,optional_time).until(EC.presence_of_element_located((By.ID,months_up_id)))
     #       months_up = driver.find_element_by_id(months_up_id)
      #      months_up_txt = str(months_up.get_attribute("value"))
       #     print("interact test fail")
        #    print(months_up_txt)
         #   delete(months_up)
          #  months_up.send_keys(months_up_txt)
           # return True
   #     except:
    #        print("cant fecking do it ")
     #       counter+=1
           # if counter % 2 == 0:
            #    driver.switch_to.default_content()
             #   try_to_move_into_frame(driver)

 #   frame_xp = '/html/frameset/frame'
  #  frame2 = driver.find_element_by_xpath(frame_xp)
   # driver.switch_to.frame(frame2)





def open_q_opts(driver, this_manu_terms):
    do_new_manu_stamp = datetime.datetime.now()
    print("manu terms im abart to do ================ "+str(this_manu_terms))
    try_accept_wltp(driver)
    try_dismiss_wltp(driver)
        #         /html/body/div[8]/div[3]/div[2]/div[6]/div/table/tbody/tr[79]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/a
        #         /html/body/div[8]/div[3]/div[2]/div[6]/div/table/tbody/tr[79]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/a
    q_opts_xp2 = '/html/body/div[8]/div[3]/div[2]/div[6]/div/table/tbody/tr[79]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/a'
    q_opts_xp = '//*[@id="buttonContractServices"]/tbody/tr/td[2]/a';

    no_recov_xp = '//*[@id="lstMotorClub"]/option[2]';
    close_xp = '//*[@id="btnUpdateServices"]/tbody/tr/td[2]/a';
    q_services_frame_xpath = '//*[@id="ifPopupInternalWindow"]'
    print("bout to open q")
    q_opts_opened = False
    wait_for_loading(driver)
    fail_counter = 0
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 300)
    while not q_opts_opened:
        print("bread crum do new manu 6 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
        if datetime.datetime.now() > future:
            print(1/0)
        wait_for_loading(driver)
        print("bread crum do new manu 7 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
        #print(driver.page_source)
        try:
            print("bread crum do new manu 8 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,q_opts_xp)))
            q_opts = (driver.find_element_by_xpath(q_opts_xp))
            click(q_opts)
            print("bread crum do new manu 9 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
        except:
            #print(driver.page_source)
            print("bad q open 1bbbbbbbbbbbb")
        #    try:
        #    print("bread crum do new manu 8 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
        #    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,q_opts_xp2)))
        #    q_opts = (driver.find_element_by_xpath(q_opts_xp2))
        #    click(q_opts)
        #    print("bread crum do new manu 9 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
        #    except:
        #        print("bad q open 1")
        print(str(fail_counter) + "     fail_counter   ")
        if fail_counter == 1:
            try:
                print("bread crum do new manu 10 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,q_services_frame_xpath)))
                frame2 = driver.find_element_by_xpath(q_services_frame_xpath)
                driver.switch_to.frame(frame2)
                print("bread crum do new manu 11 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
            except:
                print("bad q open move z")
        print( "    gggg    ++++++++++++++++++++ ")
        if fail_counter ==3 :
            try:
                print("bread crum do new manu 12 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,q_services_frame_xpath)))
                frame2 = driver.find_element_by_xpath(q_services_frame_xpath)
                driver.switch_to.frame(frame2)
                print("bread crum do new manu 13 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
            except:
                print("bad q open move zz")


        if fail_counter ==4 :
            try:
                print("bread crum do new manu 8 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,q_opts_xp2)))
                q_opts = (driver.find_element_by_xpath(q_opts_xp2))
                click(q_opts)
            except:
                print("bad q open move zz")

        if fail_counter == 5:
            #print(driver.page_source)
            driver.switch_to.default_content()
            print("js to df ")
            #print(driver.page_source)
        if fail_counter >7 :
            fail_counter = -1

        print( "   gsev     ++++++++++++++++++++ ")
    #    try:

#            print("bread crum do new manu 14 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
        try:
            rel_vechicle_xp = '//*[@id="lstReplacementVehicle"]' # bastard fucking problem hererereererererererrererrerererre
            motor_club_xp = '/html/body/div[7]/div[1]/div[3]/select'
            #print(driver.page_source)
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"lstMotorClub")))
            q_opts_obj = Select(driver.find_element_by_id("lstMotorClub"))
            og_opts = q_opts_obj.first_selected_option.text
            q_opts = Select(driver.find_element_by_id("lstMotorClub")).options
            good_change_counter = 0
            for opt in q_opts:
                print(opt.get_attribute("innerHTML"))
            for opt in q_opts:
                print("the opts herer 4444444444444444444")
                print(opt.text)
                q_opts_obj.select_by_visible_text(opt.text)
                print("br  after choosing de ting   ")
                if q_opts_obj.first_selected_option.text == opt.text:
                    print("br good up counter ")
                    good_change_counter+=1
            if good_change_counter> 1:
                q_opts_obj.select_by_visible_text(og_opts)
                time.sleep(0.5)
                if og_opts == q_opts_obj.first_selected_option.text:
                    print("  rate good ending vgvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
                    q_opts_opened = True
                    return True
        except:
            print("for fucking fuck hhhhhhhhhhhhhhhhhhhhhh")


       #     print("got you ")
        #    time.sleep(999)
 #           print("bread crum do new manu 15 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
    #    except:
    #        print("bad q open 2")
        print( str(fail_counter) +"    ++++++  bef  ++++++++++++++++++++ ")
        fail_counter+=1
        print( str(fail_counter) +"    ++++++  aft   ++++++++++++++++++++ ")
    return False

def check_q_opts_open(driver):
    opt1 = 'Breakdown Assistance'
    opt2 = 'No Breakdown Assistance'
    motor_club_xp = '//*[@id="lstMotorClub"]'
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,motor_club_xp)))
        motor_club = Select(driver.find_element_by_xpath(motor_club_xp))
        motor_club.select_by_visible_text(opt1)
        wait_for_loading(driver)
        motor_club.select_by_visible_text(opt2)
        wait_for_loading(driver)
        return True
    except:
        return False
def do_new_manu(driver, this_manu_terms, maint):
    do_new_manu_stamp = datetime.datetime.now()

 #   print("bread crum do new manu 1         "+str(datetime.datetime.now() - do_new_manu_stamp))
    print("manu terms im abart to do ================ "+str(this_manu_terms))
    #   //*[@id="btnUpdateServices"]/tbody/tr/td[2]/a
    try_accept_wltp(driver)
  #  print("bread crum do new manu 2         "+str(datetime.datetime.now() - do_new_manu_stamp))
    try_dismiss_wltp(driver)
   # print("bread crum do new manu 3         "+str(datetime.datetime.now() - do_new_manu_stamp))
  #  #print(driver.page_source)

    q_opts_xp = '//*[@id="buttonContractServices"]/tbody/tr/td[2]/a';
    no_recov_xp = '//*[@id="lstMotorClub"]/option[2]';
    close_xp = '//*[@id="btnUpdateServices"]/tbody/tr/td[2]/a';
    q_services_frame_xpath = '//*[@id="ifPopupInternalWindow"]'

             #    //*[@id="buttonContractServices"]/tbody/tr/td[2]/a

    print("bout to open q")
    q_opts_opened = False
   # print("bread crum do new manu 4         "+str(datetime.datetime.now() - do_new_manu_stamp))
    wait_for_loading(driver)
   # print("bread crum do new manu 5         "+str(datetime.datetime.now() - do_new_manu_stamp))
    fail_counter = 0

    open_q_opts(driver , this_manu_terms)
    print("q opts shjould be open now     ")
    opened_q = check_q_opts_open(driver)
    try_c = 0
    while not opened_q:
        print(str(try_c) +    "        try num              ")
        try_c+=1
        open_q_opts(driver , this_manu_terms)
        opened_q = check_q_opts_open(driver)
    opt1 = 'Breakdown Assistance'
    opt2 = 'No Breakdown Assistance'
    motor_club_xp = '//*[@id="lstMotorClub"]'


    print("bread crum do new manu 16         "+str(datetime.datetime.now() - do_new_manu_stamp))
    print("bout to sort motor club")
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,motor_club_xp)))
    motor_club = Select(driver.find_element_by_xpath(motor_club_xp))
   # print("bread crum do new manu 17         "+str(datetime.datetime.now() - do_new_manu_stamp))

    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    motor_club_sorted = False
    if maint == 0:
        if datetime.datetime.now() > future:
            print(1/0)
        while not motor_club_sorted:
            print("bread crum do new manu 18 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
            wait_for_loading(driver)
     #       print("sorting motor club loop     " + str(this_manu_terms))
            print(type(this_manu_terms))
            try:
                if math.isnan(this_manu_terms):
                    print("elper 1")
          #          print("bread crum do new manu 19 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))

                    motor_club.select_by_visible_text(opt1)
                    motor_club_sorted = True
            except:
                try:
                    if this_manu_terms == "nan":
                        print("elper 2")
           #             print("bread crum do new manu 20 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
                        motor_club.select_by_visible_text(opt1)
                        motor_club_sorted = True
                except:
                    print("smcl e1")

            try:
                if this_manu_terms.lower().strip() == "inc":
                    print("elper 3")
          #          print("bread crum do new manu 21 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
                    motor_club.select_by_visible_text(opt2)
                    motor_club_sorted = True
            except:
                print("smcl e2")
    elif maint == 1:
        motor_club.select_by_visible_text(opt2)
    else:
        print(" holy mother of fuck maint wasnt 0 or 1 ")
        print(1/0)


    for i in range(5):
        print(this_manu_terms)
 #   print("bread crum do new manu 21         "+str(datetime.datetime.now() - do_new_manu_stamp))
    wait_for_loading(driver)
    print("bout to click update")
    update_clicked = False
    fail_counter = 0
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not update_clicked:
        if datetime.datetime.now() > future:
            print(1/0)
        print("bread crum do new manu 22 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
        wait_for_loading(driver)
        print("bread crum do new manu 23 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
        print("update clicked loop 666")

 #       try:
  #          print("bread crum do new manu 24 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
   #         print("trying to click update")
        upate_serv_xp = '//*[@id="btnUpdateServices"]/tbody/tr/td[2]/a'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,upate_serv_xp)))
        update = driver.find_element_by_xpath(upate_serv_xp)
        click(update)
#            print("clicked update")
 #           print("bread crum do new manu 25 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
  #      except:
   #         pass

  #      try:
        print("bread crum do new manu 26 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
        update_clicked = prove_we_can_interact_with_page(driver)
        print("bread crum do new manu 27 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
       # except:
        #    print("bad prooooof 1")

        fail_counter+=1
        if not update_clicked:
            print("bread crum do new manu 28 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
            print("gunna try moving ")
            try_to_move_into_frame(driver)
            print("bread crum do new manu 29 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
            try_accept_wltp(driver)
            print("bread crum do new manu 30 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))
            try_dismiss_wltp(driver)
            print("bread crum do new manu 31 lloooooopp         "+str(datetime.datetime.now() - do_new_manu_stamp))





def get_prices(driver , this_manu_terms):
    #choose_maint(driver, False)
    previous_price = 0
    print("oi")
    try:
        print("oi2")
   #     #print(driver.page_source)
        print("oi3")
    except:
        print("oi4")
        try_dismiss_wltp(driver)
    #    #print(driver.page_source)
        print("oi5")
    finally:
        print("oi6")
        pass
    print("oi7")


    monthsxpath = '//*[@id="txtTerm"]'
    milesxpath = '//*[@id="txtAnnualDistance"]'
    everything_is_screwed = False;


    prices = []
    print("big oldf fucking bread crum 99")
    cant_interact_with_months_box = True;
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while cant_interact_with_months_box:
        if datetime.datetime.now() > future:
            print(1/0)
        print("interact")
        try: #/html/body/div[8]/div[3]/div[2]/div[6]/div/table/tbody/tr[44]/td[2]/input
            monthsxpath = '//*[@id="txtTerm"]'
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,monthsxpath)))
            months = driver.find_element_by_xpath(monthsxpath)
            delete(months)
            cant_interact_with_months_box = False
       # except:
     #       try:
            recalc_xpath='//*[@id="buttonSaveQuotation"]/tbody/tr/td[2]/a';
            WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,recalc_xpath)))
            recalc = driver.find_element_by_xpath(recalc_xpath)
            click(recalc)
            delete(months)
            cant_interact_with_months_box = False
        except:
            #print(driver.page_source)
            driver.switch_to.default_content()
            try_to_move_into_frame(driver)
            #print(driver.page_source)
  #          except Exception as e:
   #             print(e)
    #            print(" cant interact with months box   76767676")
     #           try_to_move_into_frame(driver)
      #          try_dismiss_wltp(driver)
       #         try_accept_wltp(driver)

    print("big oldf fucking bread crum 10")
    if not everything_is_screwed:
        chose_maint_yet = False
        counter = 0
        moved_after_maint = False
        for maint in range(2):
            loop_start = datetime.datetime.now()
    #        print("prices bc 1    "+str(datetime.datetime.now() - loop_start))

            if maint == 1 and chose_maint_yet == False:
                print("w2323w choosing maint")
                choose_maint(driver, everything_is_screwed)
                try_dismiss_wltp(driver)
                try_accept_wltp(driver)
                chose_maint_yet = True;
     #       print("prices bc 2    "+str(datetime.datetime.now() - loop_start))


            print("big oldf fucking bread crum 12")


            month_counter = 0
            for month in range(3):
                print("big oldf fucking bread crum 12 a ")

      #          print("prices bc 3    "+str(datetime.datetime.now() - loop_start))
                if month == 0:
                    this_manu_term_month = this_manu_terms.yrs2
                if month == 1:
                    this_manu_term_month = this_manu_terms.yrs3
                if month == 2:
                    this_manu_term_month = this_manu_terms.yrs4
       #         print("prices bc 4    "+str(datetime.datetime.now() - loop_start))
                do_new_manu(driver, this_manu_term_month, maint)
                print("big oldf fucking bread crum 12 b ")

        #        print("prices bc 5    "+str(datetime.datetime.now() - loop_start))
                try:
         #           print("prices bc 6    "+str(datetime.datetime.now() - loop_start))
                    try_to_move_into_frame(driver)
                    print("big oldf fucking bread crum 12c")

          #          print("prices bc 7    "+str(datetime.datetime.now() - loop_start))
                    try_dismiss_wltp(driver)
           #         print("prices bc 8    "+str(datetime.datetime.now() - loop_start))
                    try_accept_wltp(driver)
            #        print("prices bc 9    "+str(datetime.datetime.now() - loop_start))
                except:
                    print("error shifting frame after do_new_manu")
                month_counter+=1

         #       print("prices bc 10")
                if month == 0:
                    thesemonths = 24
                if month == 1:
                    thesemonths = 36
                if month == 2:
                    thesemonths = 48
          #      print("prices bc 11")
                print("big oldf fucking bread crum 13")

                try:
                    monthsxpath = '//*[@id="txtTerm"]';
                    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,monthsxpath)))
                    months = driver.find_element_by_xpath(monthsxpath)
                    delete(months)
                    months.send_keys(thesemonths)
                except:
          #          #print(driver.page_source)
                    print("months stuck ")
                    print(1/0)
          #      print("prices bc 12")

                print("big oldf fucking bread crum 14")
                for mile in range(7):
                    if mile == 0:
                        thesemiles = 5000
                    if mile == 1:
                        thesemiles = 8000
                    if mile == 2:
                        thesemiles = 10000
                    if mile == 3:
                        thesemiles = 15000
                    if mile == 4:
                        thesemiles = 20000
                    if mile == 5:
                        thesemiles = 25000
                    if mile == 6:
                        thesemiles = 30000
#                    print("prices bc 13")
                    print("big oldf fucking bread crum 15")
                    if chose_maint_yet == True and moved_after_maint == False:
                        try_to_move_into_frame(driver)
 #                   print("prices bc 14")
                    try_dismiss_wltp(driver)
  #                  print("prices bc 15")
                    try_accept_wltp(driver)
   #                 print("prices bc 16")
                   # #print(driver.page_source)
                    print("big oldf fucking bread crum 16")
                    try:
                        print("prices bc 17")
                        milesxpath = '//*[@id="txtAnnualDistance"]'
                        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,milesxpath)))
                        miles = driver.find_element_by_xpath(milesxpath)
                        delete(miles)
                        miles.send_keys(thesemiles)
                        print("prices bc 18")
                    except:
                        print("2")
                   #     #print(driver.page_source)

                        driver.switch_to.default_content()

                        print("4")
                  #      #print(driver.page_source)

                        try_to_move_into_frame(driver)
                        print("55")
                    #    #print(driver.page_source)

                        milesxpath = '//*[@id="txtAnnualDistance"]'
                        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,milesxpath)))
                        miles = driver.find_element_by_xpath(milesxpath)
                        delete(miles)
                        miles.send_keys(thesemiles)
          #          print("prices bc 19")

                    update_price_xpath = '//*[@id="buttonSaveQuotation"]/tbody/tr/td[2]/a'
                    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,update_price_xpath)))
                    update_price = driver.find_element_by_xpath(update_price_xpath)
                    print(" before clicking update")
           #         print("prices bc 20")
                    wait_for_loading(driver)
                    print("just about to click")
            #        print("prices bc 21")
                    click(update_price)
             #       print("prices bc 22")
                    print("just clicked")
                    wait_for_loading(driver)
              #      print("prices bc 23")
                    print("after clivcking")
                    print("update clicked")

        #                                                                      ##
        #            if mile == 0:
        #                if month == 0:
        #                    months = driver.find_element_by_xpath(monthsxpath)
        #                    delete(months)
        #                    months.send_keys(thesemonths)
        #                    miles = driver.find_element_by_xpath(milesxpath)
        #                    delete(miles)
        #                    miles.send_keys(thesemiles)
        #                    recalc_xpath='//*[@id="buttonSaveQuotation"]/tbody/tr/td[2]/a';
        #                    WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,recalc_xpath)))
        #                    recalc = driver.find_element_by_xpath(recalc_xpath)
        #                    click(recalc)
        #                    wait_for_loading(driver)
        #            if mile == 0:
        #                if month == 3:
        #                    print("month 3 mile 0 extra click")
        #                    thesemiles = 5000
        ##                    thesemonths = 48
        #                    months = driver.find_element_by_xpath(monthsxpath)
        #                    delete(months)
        #                    months.send_keys(thesemonths)
        #                    miles = driver.find_element_by_xpath(milesxpath)
        #                    delete(miles)
        #                    miles.send_keys(thesemiles)
        ##                    recalc_xpath='//*[@id="buttonSaveQuotation"]/tbody/tr/td[2]/a';
        #                    WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,recalc_xpath)))
        #                    recalc = driver.find_element_by_xpath(recalc_xpath)
        #                    click(recalc)
        #                    wait_for_loading(driver)




                    pricexpath = '//*[@id="txtPeriodicPayment"]'

          #          print("prices bc 24")
                    double_checked = False
                    while not double_checked:
                        print("prices bc 25")
                        milesata = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,milesxpath))).get_attribute("value"))
                        monthsata = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,monthsxpath))).get_attribute("value"))

                        double_checked = double_check_terms(driver, milesata, thesemiles, monthsata, thesemonths , this_manu_term_month , maint )

                        update_price_xpath = '//*[@id="buttonSaveQuotation"]/tbody/tr/td[2]/a'
                        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,update_price_xpath)))
                        update_price = driver.find_element_by_xpath(update_price_xpath)
                        print(" before clicking update   dc loop ")
                        wait_for_loading(driver)
                        print("just about to click   dc loop ")
                        click(update_price)
                        print("just clicked   dc loop ")
                        wait_for_loading(driver)
                        print("after clivcking   dc loop ")

              #      print("prices bc 26")
                    wait_for_loading(driver)

                    theprice = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,pricexpath))).get_attribute("value"))
                    print(theprice)
                    if previous_price == theprice:
                        print(1/0)
                    prices.append(float(theprice))

                    print(theprice)
                    print("###############")
                    print("################")
                    print("mile below ")
                    print(milesata)
                    print("month below ")
                    print(month_counter)
                    print("###############")
                    print("################")
                    print("maint below ")
                    print(maint)
                    print("###############")
                    print("################")
                    print("###############")
                    print("################")
                    print("price below ")
                    print(theprice)
                    previous_price = theprice
                  #  print("prices bc 27")
                   # mkl knj
                   # time.sleep(30)
    return (prices, everything_is_screwed)

def wait_for_loading(driver):
    wait_div_xp = '//*[@id="divPleaseWait"]'
    wait_div2_xp = '//*[@id="divPleaseWait2"]'
    wait_elemes_found = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not wait_elemes_found:
        if datetime.datetime.now() > future:
            print(1/0)
        print("wait elem loop")
        try:
            print("111111111")
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,wait_div_xp)))
            print("2222aa")
            wait = driver.find_element_by_xpath(wait_div_xp)
            style1 = wait.get_attribute("style")
            print("2222")
            print(style1)
            if len(style1)<5 or "display: inline" in style1 or "display: none" in style1:
                wait_elemes_found = True
                print("yep")
        except:
            try:
                driver.switch_to.default_content();
                print("uno")
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,wait_div_xp)))
                wait = driver.find_element_by_xpath(wait_div_xp)
                style1 = wait.get_attribute("style")
                print(style1)
                if len(style1)<5 or "display: inline;" in style1  or "display: none" in style1:
                    wait_elemes_found = True
                    print("yep 2")
            except:
                print("tttttt")
                try:
                    q_services_frame_xpath = '//*[@id="ifPopupInternalWindow"]'
                    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,q_services_frame_xpath)))
                    frame2 = driver.find_element_by_xpath(q_services_frame_xpath)
                    driver.switch_to.frame(frame2)
                    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,wait_div_xp)))
                    wait = driver.find_element_by_xpath(wait_div_xp)
                    style1 = wait.get_attribute("style")
                    print(style1)
                    if len(style1)<5 or "display: inline;" in style1  or "display: none" in style1:
                        wait_elemes_found = True
                        print("yep 3")
                except:
                    try:
                        try_to_move_into_frame(driver)
                        try_dismiss_wltp(driver)
                        try_accept_wltp(driver)
                        print("bad lc 3.a ")
                        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,wait_div_xp)))
                        wait = driver.find_element_by_xpath(wait_div_xp)
                        style1 = wait.get_attribute("style")
                        print(style1)
                        if len(style1)<5 or "display: inline;" in style1  or "display: none" in style1:
                            wait_elemes_found = True
                            print("yep 3  ggghhh ")
                    except:
                        print("arse")

    print(" 55555555555555555555555555555555 ")


def wait_for_loading666(driver):
    wait_div_xp = '//*[@id="divPleaseWait"]'
    wait_div2_xp = '//*[@id="divPleaseWait2"]'
    wait_div_present = True
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)

    continuosly_clear = 0
    continuosly_clear2 = 0
    loop_counter = 0
    while wait_div_present:
        if datetime.datetime.now() > future:
            print(1/0)
        print("top of wait div loop    "+str(continuosly_clear)+"       "+str(continuosly_clear2))
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,wait_div_xp)))
            wait = driver.find_element_by_xpath(wait_div_xp)
            if "display: inline;" in wait.get_attribute("style"):
            #    #print(driver.page_source)
                print("yep were loading still ")
                continuosly_clear = 0
                print(1/0)
            else:
                continuosly_clear+=1
        except:
            print(" failed to do wait loop 1 ")
            continuosly_clear = 0
    #        print(1/0)

        print("y 11")

        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,wait_div2_xp)))
            wait = driver.find_element_by_xpath(wait_div2_xp)
            if "display: inline;" in wait.get_attribute("style"):
            #    #print(driver.page_source)
                print("yep were loading still ")
                continuosly_clear2 = 0
                print(1/0)
                #while 1==1:
                 #   print("ooooooooooooohhhhh maaaaaaaaayyyyyyyyyyyyy gooooooooooooood we caught it loading")
            else:
                continuosly_clear2+=1
        except:

            print(" failed to do wait loop 2 ")
            continuosly_clear2 = 0

        print("y 12")

        if continuosly_clear > 6 and continuosly_clear2 > 6:
            wait_div_present= False
            print("done waiting for div ")

        if datetime.datetime.now() > future:
            print(1/0)


        print("y 13")


        try:
            print("y 1a")
            if loop_counter % 4 == 0:
                try:
                    try_to_move_into_frame(driver)
                except:
                    print("bad lc 4 ")

                try:
                    try_dismiss_wltp(driver)
                    try_accept_wltp(driver)
                except:
                    print("bad lc 3.a ")
            print("y 1b")
            if loop_counter % 2 == 0:
                try:
                    q_services_frame_xpath = '//*[@id="ifPopupInternalWindow"]'
                    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,q_services_frame_xpath)))
                    frame2 = driver.find_element_by_xpath(q_services_frame_xpath)
                    driver.switch_to.frame(frame2)
                except:
                    print("bad lc 4 ")
        except:
            print("failing to do lc shit")

        print("y 14")

def delete(box):
    box.send_keys(Keys.BACK_SPACE)
    box.send_keys(Keys.BACK_SPACE)
    box.send_keys(Keys.BACK_SPACE)
    box.send_keys(Keys.BACK_SPACE)
    box.send_keys(Keys.BACK_SPACE)
    box.send_keys(Keys.BACK_SPACE)
    box.send_keys(Keys.BACK_SPACE)
    box.send_keys(Keys.BACK_SPACE)
    box.send_keys(Keys.BACK_SPACE)
    box.send_keys(Keys.BACK_SPACE)
    box.send_keys(Keys.BACK_SPACE)
    box.send_keys(Keys.BACK_SPACE)
    box.send_keys(Keys.BACK_SPACE)
    box.send_keys(Keys.DELETE)
    box.send_keys(Keys.DELETE)
    box.send_keys(Keys.DELETE)
    box.send_keys(Keys.DELETE)
    box.send_keys(Keys.DELETE)
    box.send_keys(Keys.DELETE)
    box.send_keys(Keys.DELETE)
    box.send_keys(Keys.DELETE)

def loginandquote(driver, username, password, loginandquote):

   # username, password, x = read_txt_file()
    print("logging in 1")
    username_xpath = '//*[@id="p_username"]';
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,username_xpath)))
    username_box = driver.find_element_by_xpath(username_xpath)
  #  username = "FLAVELLJ"
    username_box.send_keys(username)

    print("logging in 2")
    password_xpath = '//*[@id="p_password"]';
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,password_xpath)))
    password_box = driver.find_element_by_xpath(password_xpath)
   # password = "Crocodile1in$"
    password_box.send_keys(password)

    print("logging in 3")
    login_button_xpath = '//*[@id="divMain"]/table/tbody/tr[4]/td[2]/table/tbody/tr/td[2]/a';
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,login_button_xpath)))
    login_button = driver.find_element_by_xpath(login_button_xpath)
    click(login_button) ### now we open the arval website

    print("logging in 4")
    continuepath = '//*[@id="divWelcomeContinue"]/a/img';
    website_down_for_maint_checker(driver)
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,continuepath)))
        continuebutton = driver.find_element_by_xpath(continuepath)
        click(continuebutton) ### now we open the arval website
    except:
        print(" no continue ")

    print("logging in 5")
    new_quote_xpath1 = '//*[@id="PMENULI1"]/a/div'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,new_quote_xpath1)))
    new_quote_button_1 = driver.find_element_by_xpath(new_quote_xpath1)
    click(new_quote_button_1) ### now we open the arval website

    print("logging in 6")
    new_quote_xpath2 = '//*[@id="subPMENULI1"]/li[1]/a'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,new_quote_xpath2)))
    new_quote_button_2 = driver.find_element_by_xpath(new_quote_xpath2)
    click(new_quote_button_2) ### now we open the arval website
    print("logging in 7")
    website_down_for_maint_checker(driver)

def full_reset(driver, username, password):
    driver.refresh()

    try_dismiss_wltp(driver)
    try_accept_wltp(driver)
    driver.execute_script('alert("Clearing out past dialogs.")')
    driver.switch_to.alert.accept()
    try_to_move_into_frame(driver)
    loginandquote(driver, username, password, loginandquote)

def fuller_reset(driver, username, password):

    try:
        driver.close();
    except:
        driver.quit();

    print("clsed driver ")
    driver = setup()
    print("open new browser")
    loginandquote(driver, username, password, loginandquote)
    print("logged in")
    for kk in range(100):
        print("HOLY MOTHER OF FUCK, IT WORKED. THEY CANT STOP YOU")
    return driver
def refresh_n_do_next_car(driver, username, password):
    try:
        full_reset(driver, username, password)
    except:
        fuller_reset(driver, username, password)


def choose_maint(driver, everything_is_screwed):

   # try_to_move_into_frame(driver)

    print("maint start ")

    services_open = False
    serv_open_errors = 0

    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not services_open:
        if datetime.datetime.now() > future:
            print(1/0)
        print(" services open  loop")
        try:
            print("clicking services  ############")

            services_xpath = '//*[@id="buttonContractServices"]/tbody/tr/td[2]/a';
            WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,services_xpath)))
            services = driver.find_element_by_xpath(services_xpath)
            click(services)
            wait_for_loading(driver)
            print("clicked services  ############")
        except:
            print("serv click err ")

        try:
            print("proving services open   ")
            maint_xpath = '//*[@id="lstMaintenance"]';
            WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH, maint_xpath )))
            maint = Select(driver.find_element_by_xpath(maint_xpath))
            maint.select_by_visible_text("Guaranteed Maintenance (Broker)")
            services_open = True
            print("proved services open     ############")
        except:
            try:
                q_services_frame_xpath = '//*[@id="ifPopupInternalWindow"]'
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,q_services_frame_xpath)))
                frame2 = driver.find_element_by_xpath(q_services_frame_xpath)
                driver.switch_to.frame(frame2)
            except:
                pass
            print("prov serv err ")

        serv_open_errors+=1


        if serv_open_errors % 3 == 0:
            try:
                try_to_move_into_frame(driver)
            except:
                print("bad serv open 3 ")

            try:
                try_dismiss_wltp(driver)
                try_accept_wltp(driver)
            except:
                print("bad serv open 3.a ")



        elif serv_open_errors % 4 == 0:
            try:
                q_services_frame_xpath = '//*[@id="ifPopupInternalWindow"]'
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,q_services_frame_xpath)))
                frame2 = driver.find_element_by_xpath(q_services_frame_xpath)
                driver.switch_to.frame(frame2)
            except:
                print("bad serv open 4 ")

############################################################################################################################################

    services_chosen = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not services_chosen:
        if datetime.datetime.now() > future:
            print(1/0)
        print(" services chosen  loop")
        try:
            print("choosing services  ############")
            maint_xpath = '//*[@id="lstMaintenance"]';
            WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, maint_xpath )))
            maint = Select(driver.find_element_by_xpath(maint_xpath))
            maint.select_by_visible_text("Customer Maintained")
            services_chosen = True
            print("chosen services  ############")
        except:
            print("serv chose err ")



    update_clicked = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not update_clicked:
        if datetime.datetime.now() > future:
            print(1/0)
        print("update clicked loop")
        try:
            up_xp = '//*[@id="btnUpdateServices"]/tbody/tr/td[2]/a'
            WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, up_xp)))
            update = driver.find_element_by_xpath(up_xp)
            click(update)
            update_clicked = True
            wait_for_loading(driver)
        except:
            pass


def enter_this_capcode(capcode, driver, months_upfront, contract_profile_config):
#    a,b, contract_profile_config = read_txt_file()

    contact_profile_sorted = False
    while not contact_profile_sorted:
        capcode = capcode.strip()
        contract_profile_box_path = '//*[@id="lstMLA"]'
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,contract_profile_box_path)))
        contract_profile_box = Select(driver.find_element_by_xpath(contract_profile_box_path))
        contract_profile_box.select_by_value("1");

        upfront_box_xpath = '//*[@id="txtAdvancePayments"]';
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,upfront_box_xpath)))
        upfront_box = driver.find_element_by_xpath(upfront_box_xpath)
        delete(upfront_box)
        upfront_box.send_keys(months_upfront)

        if str(upfront_box.get_attribute("innerHTML")).strip()==str(months_upfront).strip() or str(upfront_box.get_attribute("value")).strip()==str(months_upfront).strip():
            contact_profile_sorted = True
        else:
            print(upfront_box.get_attribute("innerHTML").strip())
            print(upfront_box.get_attribute("value").strip())
            print(str(months_upfront).strip()  + "=dis")
    try:
        select_vehicle_button_xpath = '//*[@id="allContractDetails"]/tbody/tr[23]/td/table/tbody/tr/td[2]/a'
        WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,select_vehicle_button_xpath)))
        select_vehicle_button = driver.find_element_by_xpath(select_vehicle_button_xpath)
        click(select_vehicle_button)
    except:
        try:
            select_vehicle_button_xpath = '/html/body/div[8]/div[3]/div[2]/div[6]/div/table/tbody/tr[24]/td/table/tbody/tr/td[2]/a'
            WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,select_vehicle_button_xpath)))
            select_vehicle_button = driver.find_element_by_xpath(select_vehicle_button_xpath)
            click(select_vehicle_button)
        except:
            try:
                select_vehicle_button_xpath = '/html/body/div[8]/div[3]/div[2]/div[6]/div/table/tbody/tr[25]/td/table/tbody/tr/td[2]/a'
                WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,select_vehicle_button_xpath)))
                select_vehicle_button = driver.find_element_by_xpath(select_vehicle_button_xpath)
                click(select_vehicle_button)
            except:
                select_vehicle_button_xpath = '//*[@id="allContractDetails"]/tbody/tr[23]/td/table/tbody/tr/td[2]/a'
                WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,select_vehicle_button_xpath)))
                select_vehicle_button = driver.find_element_by_xpath(select_vehicle_button_xpath)
                click(select_vehicle_button)


    capcode_box_xpath = '//*[@id="txtExternalCode"]'
    capcode_search_xpath = '//*[@id="divMain"]/table/tbody/tr[1]/td/table/tbody/tr/td[3]/table/tbody/tr/td[2]/a'
    print("11111111111111111111111111111")

#09
    try_dismiss_wltp(driver)
    try_accept_wltp(driver)

 #   #print(driver.page_source)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,capcode_box_xpath)))
    capcode_box = driver.find_element_by_xpath(capcode_box_xpath)
    click(capcode_box)


    capcode_box.send_keys(capcode)
    #print(driver.page_source)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,capcode_search_xpath)))
    capcode_button = driver.find_element_by_xpath(capcode_search_xpath)
    click(capcode_button)
    #print(driver.page_source)
    print(" spank you helpy helper ")
    summary_button_xpath = '//*[@id="divMain"]/table/tbody/tr[6]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/a'

    print("444 were ere")


    try_dismiss_wltp(driver)
    try_accept_wltp(driver)
    try_to_move_into_frame(driver)
    driver.execute_script('alert("Clearing out past dialogs.")')
    driver.switch_to.alert.accept()
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,summary_button_xpath)))
        summary_button = driver.find_element_by_xpath(summary_button_xpath)
        click(summary_button)
        try_dismiss_wltp(driver)
        try_accept_wltp(driver)
        try_to_move_into_frame(driver)
        driver.execute_script('alert("Clearing out past dialogs.")')
        driver.switch_to.alert.accept()
    except s_ex.UnexpectedAlertPresentException:

        next_car_works = False
        tstamp1 = datetime.datetime.now()
        future = tstamp1 +  datetime.timedelta(seconds = 130)
        while not next_car_works:
            try:
            #getting rid and moving on to next
                print("bad en      34 43 34 43 34 43 ")
                badcapcodes.append(this_car.capcode)
                click(capcode_box)
                rows_done_in_old_ratebook+=1
                this_car = old_arval_deals[rows_done_in_old_ratebook]
                delete(capcode_box)

                capcode_box.send_keys(this_car.capcode)
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,capcode_search_xpath)))
                capcode_button = driver.find_element_by_xpath(capcode_search_xpath)
                try:
                    print("22222222222222222222222222222222222")
          #          #print(driver.page_source)
                    click(capcode_button)
                    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,summary_button_xpath)))
                    summary_button = driver.find_element_by_xpath(summary_button_xpath)
                    click(summary_button)
                    next_car_works = True
                except:
                    pass
                finally:
                    pass
            finally:
                pass
    finally:
        pass

    a = prove_we_can_interact_with_page(driver, 25)
    return a







class deal():
    def __init__(self,capcode,months,miles,maint, price):
        self.capcode = capcode
        self.months = months
        self.miles = miles
        self.maint = maint
        self.price = price

class deal_with_rv():
    def __init__(self,capcode,months,miles, price,blp):
        self.capcode = capcode
        self.months = months
        self.miles = miles
        self.price = price
        self.blp = blp

class deal_pair():
    def __init__(self,capcode,months,miles,maintprice, nomaintprice):
        self.capcode = capcode
        self.months = months
        self.miles = miles
        self.maintprice = maintprice
        self.nomaintprice = nomaintprice

class better_prices():
    def __init__(self, old_deal, better_deal):
        self.old_deal = old_deal
        self.better_deal = better_deal


def click(button):
    try:
        button.click()
    except Exception as e:
        print(str(e))
        print(e)


first_time = 0



def get_blp(driver):
    # //*[@id="rowPaymentDetails"]/td[2]/table/tbody/tr[2]/td[1]
    blpxpath = '//*[@id="rowPaymentDetails"]/td[2]/table/tbody/tr[2]/td[1]'
    print("getting blp")
 #   #print(driver.page_source)

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,blpxpath)))
    blp1 = driver.find_element_by_xpath(blpxpath)
    blp2 = blp1.text
    return(blp2)




# this section navigates to the website in question via the intranet of our site and then clicks on a button to take us to the website in question
#############################
def setup():

    driver_xpath2 = "chromedriver.exe"
    chrome_options = Options.Options()
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(driver_xpath2 ,chrome_options=chrome_options)
    driver.get("https://arvalpartners.arval.co.uk/j2ee/arvaleb/ebroker.html")

    try_to_move_into_frame(driver)

#    #print(driver.page_source)
    return(driver);

def check_were_good(driver , everything_is_screwed):
    try:
        termsxp =  '//*[@id="txtTerm"]'
        yeardistxp= '//*[@id="txtAnnualDistance"]'
        totdistxp =  '//*[@id="txtContractDistance"]'
        monthsv = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,termsxp))).get_attribute("value"))
        yeardistv = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,yeardistxp))).get_attribute("value"))
        totdistv = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,totdistxp))).get_attribute("value"))
        if (yeardistv == totdist / (terms / 12)):
            pass
        else:
            while(1<2):
                print("why")

        theblp = get_blp(driver)


        if(theblp < 65000):
            return(everything_is_screwed)
        else:
            everything_is_screwed = True
            return(everything_is_screwed)


    except:
        try:
            try_dismiss_wltp(driver)
            try_accept_wltp(driver)
            try_to_move_into_frame(driver)


            summary_button_xpath = '//*[@id="divMain"]/table/tbody/tr[6]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/a'

            print("46666664 sorting some prob ")


            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,summary_button_xpath)))
            summary_button = driver.find_element_by_xpath(summary_button_xpath)
            click(summary_button)

            monthsv = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,termsxp))).get_attribute("value"))
            yeardistv = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,yeardistxp))).get_attribute("value"))
            totdistv = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,totdistxp))).get_attribute("value"))
            if (yeardistv == totdist / (terms / 12)):
                pass
            else:
                while(1<2):
                    print("why")

            theblp = get_blp(driver)


            if(theblp < 55000):
                return(everything_is_screwed)
            else:
                everything_is_screwed = True
                return(everything_is_screwed)

        except:
            wheverything_is_screwed = True
            return(everything_is_screwed)
    return(everything_is_screwed)








def try_dismiss_wltp(driver):
    try:
        driver.switch_to.alert.dismiss();
    except:
        pass
    finally:
        pass

def get_otr(driver):
    # //*[@id="txtOnTheRoad"]
    otr_xpath = '/html/frameset/frame'#    arval button
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,otr_xpath)))
    otr = driver.find_element_by_xpath(otr_xpath)
    otrprice = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,otr_xpath))).get_attribute("value"))
    return otrprice



def try_accept_wltp(driver):
    try:
        driver.switch_to.alert.accept();
    except:
        pass
    finally:
        pass


def try_to_move_into_frame(driver):
    try:
        time.sleep(0.5)
#        wait_for_loading(driver)
        time.sleep(0.5)
        frame_xpath = '/html/frameset/frame'#    arval button
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,frame_xpath)))
        frame = driver.find_element_by_xpath(frame_xpath)
        driver.switch_to.frame(frame)
    except:
        pass
    finally:
        pass
