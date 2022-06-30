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
            print(driver.page_source)


def remove_breakdown_ass(driver):
#    //*[@id="buttonContractServices"]/tbody/tr/td[2]/a
#    //*[@id="lstMotorClub"]/option[2]
#   //*[@id="btnUpdateServices"]/tbody/tr/td[2]/a
    try_accept_wltp(driver)
    try_dismiss_wltp(driver)
 #   print(driver.page_source)

    q_opts_xp = '//*[@id="buttonContractServices"]/tbody/tr/td[2]/a';
    no_recov_xp = '//*[@id="lstMotorClub"]/option[2]';
    close_xp = '//*[@id="btnUpdateServices"]/tbody/tr/td[2]/a';
    q_services_frame_xpath = '//*[@id="ifPopupInternalWindow"]'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,q_opts_xp)))
    q_opts = driver.find_element_by_xpath(q_opts_xp)
    click(q_opts)

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,q_services_frame_xpath)))
    frame2 = driver.find_element_by_xpath(q_services_frame_xpath)
    driver.switch_to.frame(frame2)


    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,no_recov_xp)))
    no_recov = driver.find_element_by_xpath(no_recov_xp)
    click(no_recov)

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,close_xp)))
    close_but = driver.find_element_by_xpath(close_xp)
    click(close_but)
    try_to_move_into_frame(driver)

    try_to_move_into_frame(driver)
    try_accept_wltp(driver)
    try_dismiss_wltp(driver)
 #   print(driver.page_source)




def enter_otr(driver, otr):

    print("entering otr")
    otr_xpath = '//*[@id="txtOnTheRoad"]';

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,otr_xpath)))
    otr_box = driver.find_element_by_xpath(otr_xpath)
    default_otr = otr_box.get_attribute("value");
    if default_otr < otr: # *0.8
        print("default otr is better")
        return True


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

  #  print(driver.page_source)
    try_to_move_into_frame(driver)
   # print(driver.page_source)

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

def double_check_terms(driver, milesata, thesemiles, monthsata, thesemonths ):

    monthsxpath = '//*[@id="txtTerm"]'
    milesxpath = '//*[@id="txtAnnualDistance"]'

    milesata = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,milesxpath))).get_attribute("value"))
    monthsata = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,monthsxpath))).get_attribute("value"))

    while (int(milesata) != int(thesemiles)) or (int(monthsata) != int(thesemonths)):
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
    print("terms are good")

def prove_we_can_interact_with_page():

    try:
        months_up_xp = '//*[@id="txtAdvancePayments"]'
        WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,months_up_xp)))
        months_up = driver.find_element_by_xpath(months_up_xp)
        months_up_txt = months_up.get_attribute("innerHTML")
        delete(months_up)
        months_up.send_keys(months_up_txt)
        return True
    except:
        return False


def do_new_manu(driver, this_manu_terms):
    #   //*[@id="btnUpdateServices"]/tbody/tr/td[2]/a
    try_accept_wltp(driver)
    try_dismiss_wltp(driver)
 #   print(driver.page_source)
    
    q_opts_xp = '//*[@id="buttonContractServices"]/tbody/tr/td[2]/a';
    no_recov_xp = '//*[@id="lstMotorClub"]/option[2]';
    close_xp = '//*[@id="btnUpdateServices"]/tbody/tr/td[2]/a';
    q_services_frame_xpath = '//*[@id="ifPopupInternalWindow"]'

             #    //*[@id="buttonContractServices"]/tbody/tr/td[2]/a
    
    opt1 = 'Breakdown Assistance'
    opt2 = 'No Breakdown Assistance'
    motor_club_xp = '//*[@id="lstMotorClub"]'

    
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,q_opts_xp)))
    q_opts = (driver.find_element_by_xpath(q_opts_xp))
    click(q_opts)
    


    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,q_services_frame_xpath)))
    frame2 = driver.find_element_by_xpath(q_services_frame_xpath)
    driver.switch_to.frame(frame2)


    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,motor_club_xp)))
    motor_club = Select(driver.find_element_by_xpath(motor_club_xp))

    motor_club_sorted = False

    while not motor_club_sorted:
        print("sorting motor club loop     " + str(this_manu_terms))
        print(type(this_manu_terms))
        try:
            if math.isnan(this_manu_terms):
                motor_club.select_by_visible_text(opt1)
                motor_club_sorted = True
        except:
            try:
                if this_manu_terms == "nan":
                    motor_club.select_by_visible_text(opt1)
                    motor_club_sorted = True
            except:
                print("smcl e1")

        try:    
            if this_manu_terms.lower().strip() == "inc":
                motor_club.select_by_visible_text(opt2)
                motor_club_sorted = True
        except:
            print("smcl e2")
    
    #
   #
  #
  
    for i in range(5):
        print(this_manu_terms)

    update_clicked = False
    while not update_clicked:
        print("update clicked loop 666")
        try:
            upate_serv_xp = '//*[@id="btnUpdateServices"]/tbody/tr/td[2]/a'
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,upate_serv_xp)))
            update = driver.find_element_by_xpath(upate_serv_xp)
            click(update)
        except:
            pass
        try:
            prove_we_can_interact_with_page()
            update_clicked = True
        except:
            print("bad prooooof 1")


#    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,close_xp)))
 #   close_but = driver.find_element_by_xpath(close_xp)
  #  click(close_but)
    try_to_move_into_frame(driver)

    try_to_move_into_frame(driver)
    try_accept_wltp(driver)
    try_dismiss_wltp(driver)
 #   print(driver.page_source)



def get_prices(driver , this_manu_terms):
    previous_price = 0
    print("oi")
    try:
        print("oi2")
        print(driver.page_source)
        print("oi3")
    except:
        print("oi4")
        try_dismiss_wltp(driver)
        print(driver.page_source)
        print("oi5")
    finally:
        print("oi6")
        pass
    print("oi7")


    monthsxpath = '//*[@id="txtTerm"]'
    milesxpath = '//*[@id="txtAnnualDistance"]'
    everything_is_screwed = False;


    prices = []

    try:
        delete(months)
    except:
        try:
            recalc_xpath='//*[@id="buttonSaveQuotation"]/tbody/tr/td[2]/a';
            WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,recalc_xpath)))
            recalc = driver.find_element_by_xpath(recalc_xpath)
            click(recalc)
            delete(months)
        except:
            print(" cant interact with months box ")



    if not everything_is_screwed:
        chose_maint_yet = False
        counter = 0
        moved_after_maint = False
        for maint in range(2):

            if maint == 1 and chose_maint_yet == False:
                print("w2323w choosing maint")
                choose_maint(driver, everything_is_screwed)
                try_dismiss_wltp(driver)
                try_accept_wltp(driver)
                chose_maint_yet = True;

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

                if chose_maint_yet == True and moved_after_maint == False:
                    try_to_move_into_frame(driver)

                try_dismiss_wltp(driver)
                try_accept_wltp(driver)
               # print(driver.page_source)

                try:
                    milesxpath = '//*[@id="txtAnnualDistance"]'
                    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,milesxpath)))
                    miles = driver.find_element_by_xpath(milesxpath)
                    delete(miles)
                    miles.send_keys(thesemiles)
                except:
                    print("2")
               #     print(driver.page_source)

                    driver.switch_to.default_content()

                    print("4")
              #      print(driver.page_source)

                    try_to_move_into_frame(driver)
                    print("55")
                #    print(driver.page_source)

                    milesxpath = '//*[@id="txtAnnualDistance"]'
                    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,milesxpath)))
                    miles = driver.find_element_by_xpath(milesxpath)
                    delete(miles)
                    miles.send_keys(thesemiles)




                month_counter = 0
                for month in range(3):
                    if month == 0:
                        this_manu_term_month = this_manu_terms.yrs2
                    if month == 1:
                        this_manu_term_month = this_manu_terms.yrs3
                    if month == 2:
                        this_manu_term_month = this_manu_terms.yrs4
                    do_new_manu(driver, this_manu_term_month)
                    try:
                        try_to_move_into_frame(driver)
                        try_dismiss_wltp(driver)
                        try_accept_wltp(driver)
                    except:
                        print("error shifting frame after do_new_manu")
                    month_counter+=1


                    if month == 0:
                        thesemonths = 24
                    if month == 1:
                        thesemonths = 36
                    if month == 2:
                        thesemonths = 48


                    try:
                        monthsxpath = '//*[@id="txtTerm"]';
                        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,monthsxpath)))
                        months = driver.find_element_by_xpath(monthsxpath)
                        delete(months)
                        months.send_keys(thesemonths)
                    except:
              #          print(driver.page_source)
                        print("months stuck ")
                        print(1/0)

                    try:
                        milesxpath = '//*[@id="txtAnnualDistance"]'
                        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,milesxpath)))
                        miles = driver.find_element_by_xpath(milesxpath)
                        delete(miles)
                        miles.send_keys(thesemiles)
                    except:
              #          print(driver.page_source)
                        print("miles stuck ")
                        print(1/0)



                    update_price_xpath = '//*[@id="buttonSaveQuotation"]/tbody/tr/td[2]/a'
                    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,update_price_xpath)))
                    update_price = driver.find_element_by_xpath(update_price_xpath)
                    print(" before clicking update")
                    wait_for_loading(driver)
                    print("just about to click")
                    click(update_price)
                    print("just clicked")
                    wait_for_loading(driver)
                    print("after clivcking")
                    print("update clicked")

        #            ###############
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

                    for i in range(2):
                        milesata = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,milesxpath))).get_attribute("value"))
                        monthsata = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,monthsxpath))).get_attribute("value"))
                        double_check_terms(driver, milesata, thesemiles, monthsata, thesemonths )

                    wait_for_loading(driver)

                    theprice = (WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,pricexpath))).get_attribute("value"))
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
                   # mkl knj
                   # time.sleep(30)
    return (prices, everything_is_screwed)



def wait_for_loading(driver):
    wait_div_xp = '//*[@id="divPleaseWait"]'
    wait_div_present = True
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    continuosly_clear = 0
    while wait_div_present:

        print("top of wait div loop")

        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,wait_div_xp)))
            wait = driver.find_element_by_xpath(wait_div_xp)
            if "display: inline;" in wait.get_attribute("style"):
                print(driver.page_source)
                print("yep were loading still ")
                continuosly_clear = 0
                print(1/0)
                #while 1==1:
                 #   print("ooooooooooooohhhhh maaaaaaaaayyyyyyyyyyyyy gooooooooooooood we caught it loading")
            else:
            #    print("done waiting")
            #    print(wait.get_attribute("style"))
            #    print(wait.get_attribute("innerHTML"))
                continuosly_clear+=1
        except:
            print(" failed to do wait loop ")

        if continuosly_clear > 30:
            wait_div_present= False
            print("done waiting for div ")

        if datetime.datetime.now() > future:
            print(1/0)


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
    username, password, x = read_txt_file()
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
    try_to_move_into_frame(driver)
    print("maint start ")
    try:
        services_xpath = '//*[@id="buttonContractServices"]/tbody/tr/td[2]/a';
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,services_xpath)))
        services = driver.find_element_by_xpath(services_xpath)
        click(services)
        print("clicked services  ############")
    except s_ex.UnexpectedAlertPresentException:
        try:
 #       driver.switch_to.alert.dismiss();
            #time.sleep(10)
            print(" agenda 22222")
                             #
            services_xpath = '//*[@id="buttonContractServices"]/tbody/tr/td[2]/a';
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,services_xpath)))
            services = driver.find_element_by_xpath(services_xpath)
            click(services)
            print("error 888 saved this")
        except s_ex.NoSuchWindowException:
            print("that error")
            f_xpath = '/html/frameset/frame'
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,f_xpath)))
            fg = driver.find_element_by_xpath(f_xpath)
            print("before")
   #         print(driver.page_source)
            driver.switch_to.frame(fg)
            print("after")
    #        print(driver.page_source)

            services_xpath = '//*[@id="buttonContractServices"]/tbody/tr/td[2]/a';
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,services_xpath)))
            services = driver.find_element_by_xpath(services_xpath)
            click(services)
            print("error 999 saved this")

            while(1<2):

                print("6666666666666666666666")

        except:
            try:
                print(" agenda 66666 ")
                driver.switch_to.alert.dismiss();
                services_xpath = '//*[@id="buttonContractServices"]/tbody/tr/td[2]/a';
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,services_xpath)))
                services = driver.find_element_by_xpath(services_xpath)
                click(services)
            except:
                pass
            finally:
                pass
        finally:
            pass
    except:
        try:
            print(" agenda 098765")
            driver.switch_to.alert.dismiss();
            services_xpath = '//*[@id="buttonContractServices"]/tbody/tr/td[2]/a';
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,services_xpath)))
            services = driver.find_element_by_xpath(services_xpath)
            click(services)
        except:
            pass
        finally:
            pass

    finally:
        pass
    #finally:
     #   pass
# //*[@id="lstMaintenance"]/option[1]

# //*[@id="lstMaintenance"]/option[1]

#####  switch to //*[@id="ifPopupInternalWindow"]
  #  print("also does this crash at 17 again")
   # print("before frame switch")
    #print(driver.page_source)

    #/html/frameset/frame
    try:
        print(" agenda  ##@@@@@@;;;;;;;; ")
        frame2_xpath = '//*[@id="ifPopupInternalWindow"]'  # new frame for changing thing
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,frame2_xpath)))
        frame2 = driver.find_element_by_xpath(frame2_xpath)
        driver.switch_to.frame(frame2)
        print("after of frame switch")
   #     print(driver.page_source)
   #     if (len(driver.page_source)<100):
    #        print("were doing this worked thing ")
     #       itworked = False
      #      for i in range(10):
       #         i+=1;
        #        if not itworked:
         #           try:
          #              print("3333333333333")
           #             driver.switch_to.window(driver.window_handles[i])
            #            print(driver.page_source)
             #           print(i)
              #          print("3333333333333")
               #         if (len(driver.page_source)>100):
                #            itworked = True
                 #   except:
                  #       pass
#            if not itworked:
 #               while(1<2):
  #                  print("this is why everything is screwed")
   #             full_reset(driver, everything_is_screwed)
    except:

        try:
            print(" 99+ aaaaaaaaaaaaaaaaaa")
            driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='ifPopupInternalWindow']"))
            print(" 99+ aaaaaaaaaaaaaaaaaa affftererere ")
        except:
            try:
                print(" 99+ aaaaaaaaaaaaaaaaaa")
                try_to_move_into_frame(driver)
                driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='ifPopupInternalWindow']"))
                print(" 99+ aaaaaaaaaaaaaaaaaa   affffft ")
            except:
                pass
            finally:
                pass
        finally:
            pass


#    if (len(driver.page_source) < 100):
 #       print("we need to switch back")
  #      frames = driver.find_elements_by_tag_name("frame");
   #     html_lens = []
    #    for i in frames:
     #       print(i)
      #  print("hhhhhhhhhhhhhhhhhhhhhhhhhhhh")
       # for i in frames:
        #    print(driver.page_source)
         #   driver.switch_to(i)
          #  qqq = len(driver.page_source)
           # html_lens.append(qqq)
#        biggest_int = 0
 #       the_index =0
  #      index_counter = 0
   #     for h in html_lens:
    #        if h>biggest_int:
     #           the_index = index_counter
      #          biggest_int = h
       #     index_counter +=1
        #driver.switch_to.frame(frames[the_index])

   # if (len(driver.page_source) <100):
    #    print(" heeeeelper ")
     #   refreshandtryagain()
  #      print(driver.page_source)
   #     frame_xpath = "/html/frameset/frame"
    #    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,frame_xpath)))
     #   frame55 = driver.find_element_by_xpath(frame_xpath)
      #  driver.switch_to.frame(frame55)
       # print(driver.page_source)
        #/html/frameset/frame

    # maybe build a while loop to get stuck in


    new_quote_xpath2 = '//*[@id="lstMotorClub"]/option[2]'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,new_quote_xpath2)))
    new_quote_button_2 = driver.find_element_by_xpath(new_quote_xpath2)
    click(new_quote_button_2)

    maint_option_xpath = '//*[@id="lstMaintenance"]/option[2]';
    try:
        print("mmm aaaa")
        WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,maint_option_xpath)))
        print("2   mmm aaaa")
    except s_ex.UnexpectedAlertPresentException:
        try:
            print("mmm bbbb")
            try_dismiss_wltp(driver)
            try_accept_wltp(driver)
            WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,maint_option_xpath)))
        except s_ex.TimeoutException:
            print("mmm ccccc")
            try_to_move_into_frame(driver)
            WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,maint_option_xpath)))
        finally:
            pass
    except s_ex.TimeoutException:

        print("mmm ddddddd")
    #    driver.execute_script('alert("Clearing out past dialogs.")')
     #   driver.switch_to.alert.accept()
      #  print(driver.page_source)
     #   try_to_move_into_frame(driver)
    #    print(driver.page_source)
        try:
            WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,maint_option_xpath)))
        except:
            alloptsxpth = '//*[@id="lstMaintenance"]'
            WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,alloptsxpth)))
            maint_options = driver.find_element_by_xpath(alloptsxpth)
            A = False
            for opt in maint_options:
                text = opt.get_attribute('innerHTML')
                if text == "Customer Maintained":
                    click(opt)
                    print("im a geeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeennnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnniiiiiiiiiiiiiiiiiiiiiiiiiiiiuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuussssssssssssssssssssssssss")
                    A = True
            if A == False:
                everything_is_screrwed=True



 #           while(1<2):

    #`           new_quote_xpath1 = '//*[@id="PMENULI1"]/a/div'
     #           WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,new_quote_xpath1)))
      #          new_quote_button_1 = driver.find_element_by_xpath(new_quote_xpath1)
       #         click(new_quote_button_1) ### now we open the arval website

        #        new_quote_xpath2 = '//*[@id="subPMENULI1"]/li[1]/a'
         #       WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,new_quote_xpath2)))
          #      new_quote_button_2 = driver.find_element_by_xpath(new_quote_xpath2)
           #     click(new_quote_button_2) ### now we open the arval website







    finally:
        pass
    if everything_is_screwed:
        print("wut")
    if not everything_is_screwed:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,maint_option_xpath)))
        maint_option = driver.find_element_by_xpath(maint_option_xpath)
        click(maint_option)


        update_services_xpath = '//*[@id="btnUpdateServices"]/tbody/tr/td[2]/a';
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,update_services_xpath)))
        update_services = driver.find_element_by_xpath(update_services_xpath)
        click(update_services)
        print(" yaaaaaaaaaay ")


def enter_this_capcode(capcode, driver, months_upfront, contract_profile_config):
    a,b, contract_profile_config = read_txt_file()
    capcode = capcode.strip()

    contract_profile_box_path = '//*[@id="lstMLA"]'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,contract_profile_box_path)))
    contract_profile_box = Select(driver.find_element_by_xpath(contract_profile_box_path))
    contract_profile_box.select_by_visible_text(contract_profile_config)



    #default_profile_box_path = '//*[@id="lstPP"]'

    #if months_upfront == 3:
   #     if contract_profile_config == "business_and_personal":
  #          default_profile_xpath = '//*[@id="lstPP"]/option[6]]'
 #       if contract_profile_config == "personal":
#            default_profile_xpath = '//*[@id="lstPP"]/option[5]]'

    #if months_upfront == 6:
   #     default_profile_xpath = '//*[@id="lstPP"]/option[8]'

 ##   if months_upfront == 9:
#        default_profile_xpath = '//*[@id="lstPP"]/option[10]'



    #
    #WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,default_profile_xpath)))
   # default_profile = driver.find_element_by_xpath(default_profile_xpath)
  #  print("      ")
 #   click(default_profile)


# //*[@id="txtAdvancePayments"]
    upfront_box_xpath = '//*[@id="txtAdvancePayments"]';
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,upfront_box_xpath)))
    upfront_box = driver.find_element_by_xpath(upfront_box_xpath)
    delete(upfront_box)
    upfront_box.send_keys(months_upfront)


#    postcode_xp = '//*[@id="txtOvernightPostcode"]'
 #   WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,postcode_xp)))
  #  postcode = driver.find_element_by_xpath(postcode_xp)
   # postcode.send_keys("pr1 3nt")

    select_vehicle_button_xpath = '//*[@id="allContractDetails"]/tbody/tr[23]/td/table/tbody/tr/td[2]/a'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,select_vehicle_button_xpath)))
    select_vehicle_button = driver.find_element_by_xpath(select_vehicle_button_xpath)
    click(select_vehicle_button)



    capcode_box_xpath = '//*[@id="txtExternalCode"]'
    capcode_search_xpath = '//*[@id="divMain"]/table/tbody/tr[1]/td/table/tbody/tr/td[3]/table/tbody/tr/td[2]/a'
    print("11111111111111111111111111111")

#09
    try_dismiss_wltp(driver)
    try_accept_wltp(driver)

 #   print(driver.page_source)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,capcode_box_xpath)))
    capcode_box = driver.find_element_by_xpath(capcode_box_xpath)
    click(capcode_box)


    capcode_box.send_keys(capcode)

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,capcode_search_xpath)))
    capcode_button = driver.find_element_by_xpath(capcode_search_xpath)
    click(capcode_button)

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
          #          print(driver.page_source)
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
 #   print(driver.page_source)

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,blpxpath)))
    blp1 = driver.find_element_by_xpath(blpxpath)
    blp2 = blp1.text
    return(blp2)




# this section navigates to the website in question via the intranet of our site and then clicks on a button to take us to the website in question
#############################
def setup():
    
    driver_xpath2 = "chromedriver.exe"
    chrome_options = Options.Options()     ### stop text alerts
    chrome_options.add_argument("--disable-popup-blocking")

    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(driver_xpath2)

    driver.get("https://arvalpartners.arval.co.uk/j2ee/arvaleb/ebroker.html")

    try_to_move_into_frame(driver)

#    print(driver.page_source)
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
        frame_xpath = '/html/frameset/frame'#    arval button
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,frame_xpath)))
        frame = driver.find_element_by_xpath(frame_xpath)
        driver.switch_to.frame(frame)
    except:
        pass
    finally:
        pass








