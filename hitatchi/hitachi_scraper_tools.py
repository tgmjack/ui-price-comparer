import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions as s_ex
from selenium.webdriver.support.ui import Select
import pandas as pd
import pyautogui
import keyboard
import selenium.webdriver.chrome.options as Options
import pydirectinput
import datetime
import Levenshtein

def new_metalic_extras_function(driver, our_extra):
    
    option_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[11]/div[1]/input'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,option_xp)))
    option_button  = driver.find_element_by_xpath(option_xp)
    click(option_button)
    
    print("bzr 1     doing spesh inint ")
    time.sleep(1)
    wait_until_done_loading(driver)
    time.sleep(1)
    wait_until_done_loading(driver)
    time.sleep(1)
    wait_until_done_loading(driver)
    time.sleep(1)
    wait_until_done_loading(driver)
    loading_options_menu(driver)

    
    good_elems = []
    removed_allready_set_extra = False
    try:
        print("looking for elems 2 ")
        options_window  = driver.find_elements_by_xpath('/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]')[0]
        rows = options_window.find_elements_by_tag_name("div")
        print("r  ex ")
        for r in rows:
            if not removed_allready_set_extra:
   #             print("r   "+str(r.get_attribute("innerHTML")))
    #            for td in r.find_elements_by_tag_name("div"):
     #               print(str(td.get_attribute("innerHTML")) + "        tds    ")
                try:
                    name = r.get_attribute("innerHTML")
                except:
                    name = "no name "
                if our_extra in name:
            #        print(" it works got extra 1")
                    bef_inp_td = r.find_elements_by_tag_name("div")[0]
                    inp_td = r.find_elements_by_tag_name("div")[2]
                    aft_td = r.find_elements_by_tag_name("div")[2]
                    inp_td.find_elements_by_tag_name("input")[0].click();
                    removed_allready_set_extra = True
                else:
                    pass
      #              print(str(our_extra)+ "     not match      "+ str(name))
    except:
        time.sleep(5)
        loading_options_menu(driver)
        print("looking for elems 2 ")
        options_window  = driver.find_elements_by_xpath('/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]')[0]
        rows = options_window.find_elements_by_tag_name("div")
        print("r  etr ")
        for r in rows:
            if not removed_allready_set_extra:
         #       print("r   "+str(r.get_attribute("innerHTML")))
          #      for td in r.find_elements_by_tag_name("div"):
           #         print(str(td.get_attribute("innerHTML")) + "        tds    ")
                try:
                    name = r.get_attribute("innerHTML")
                except:
                    name = "no name "
                if our_extra in name:
           #         print(" it works got extra 2")
                    bef_inp_td = r.find_elements_by_tag_name("div")[0]
                    inp_td = r.find_elements_by_tag_name("div")[2]
                    aft_td = r.find_elements_by_tag_name("div")[2]
                    removed_allready_set_extra = True
                    inp_td.find_element_by_tag_name("input")[0].click();
                else:
                    pass
        #            print(str(our_extra)+ "     not match      "+ str(name))

#    time.sleep(999)

    loading_options_menu(driver)
    print("ok we got options menu open   ")
    stop_yet  = False
    internal_sorted = False
    external_sorted = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    options_window  = driver.find_elements_by_xpath('/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]')
    
    for web_elem in options_window:
        print("1")
        more_elems = web_elem.find_elements_by_class_name('associate-option-item-name-container')
     #   print(web_elem.get_attribute('innerHTML'))
        print("bzr 4 b ")
        elem_counter = 0
        loading_options_menu(driver)
        for even_more_elem in more_elems:
            print(' ciiiiii   one')

#            print(even_more_elem.get_attribute('innerHTML'))
            this_price = even_more_elem.find_element_by_class_name('associate-option-item-cost').get_attribute('innerHTML')
            this_name = even_more_elem.find_element_by_class_name('associate-option-item-name').get_attribute('innerHTML').lower()
            if "metallic" in this_name and external_sorted == False:
                options = even_more_elem.find_elements_by_tag_name('input')
                for o in options:
                    if 'option_' in o.get_attribute('id'):
                        if o.get_attribute('id')[7].isdigit():
                            check_box = o
                            click(check_box)
                            print("clicked this cb  ext ")
                            external_sorted = True
                loading_options_menu(driver)

            if ("cloth" in this_name or "leather" in this_name) and internal_sorted == False:
                options = even_more_elem.find_elements_by_tag_name('input')
                for o in options:
                    if 'option_' in o.get_attribute('id'):
                        if o.get_attribute('id')[7].isdigit():
                            check_box = o
                            click(check_box)
                            print("clicked this cb int")
                            internal_sorted = True
                loading_options_menu(driver)

    xp = '//*[@id="validateOptions"]'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH, xp)))
    close  = driver.find_element_by_xpath(xp)
    close.click();
    time.sleep(1)
    wait_until_done_loading(driver)
    loading_options_menu(driver)
                            
class a_car():
    def __init__(self,capcode,make, model, deriv, blp):
        self.capcode = capcode
        self.make = make
        self.model = model
        self.deriv = deriv
        self.blp = blp

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



def get_comp():
    thedb = pd.read_csv("hit_comp.csv", dtype = str)
    final = []
    for i in range(thedb.shape[0]):
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


def get_prices_special(driver , theblp , gmon, gmil, gup, ogmaint):
    last_price = 0
    if ogmaint:
        the_maint = 'Associate Regulated CH with maint'
    else:
        the_maint = 'Associate CH no maint - PLG'
    prices = []
    og_gup = gup
    if gup == "1":
        if gmon == "24":
            gup = '24 months 1 in advance followed by 23'
        if gmon == "30":
            gup = '30 months 1 in advance followed by 29'
        if gmon == "36":
            gup = '36 months 1 in advance followed by 35'
        if gmon == "48":
            gup = '48 months 1 in advance followed by 47'
    if gup == "3":
        if gmon == "24":
            gup = '24 months 03 in advance followed by 23'
        if gmon == "30":
            gup = '30 months 03 in advance followed by 29'
        if gmon == "36":
            gup = '36 months 03 in advance followed by 35'
        if gmon == "48":
            gup = '48 months 03 in advance followed by 47'
    if gup == "6":
        if gmon == "24":
            gup = '24 months 06 in advance followed by 23'
        if gmon == "30":
            gup = '30 months 06 in advance followed by 29'
        if gmon == "36":
            gup = '36 months 06 in advance followed by 35'
        if gmon == "48":
            gup = '48 months 06 in advance followed by 47'
    if gup == "9":
        if gmon == "24":
            gup = '24 months 09 in advance followed by 23'
        if gmon == "30":
            gup = '30 months 09 in advance followed by 29'
        if gmon == "36":
            gup = '36 months 09 in advance followed by 35'
        if gmon == "48":
            gup = '48 months 09 in advance followed by 47'
######################################################### mon
    wait_until_done_loading(driver)
    months_sel_id = 'termSelect'
    months = Select(driver.find_element_by_id(months_sel_id))

    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)

    time.sleep(0.5)
    while months.first_selected_option.text != gmon:
        if datetime.datetime.now() > future:
            print(1/0)
        months.select_by_visible_text(gmon)
    wait_until_done_loading(driver)
    time.sleep(0.5)

########################################################## mil
    terms_inp_id = 'milesPerAnum'
    terms = driver.find_element_by_id(terms_inp_id)

    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)


    while str(terms.get_attribute('value')).replace(",","") != gmil:
        if datetime.datetime.now() > future:
            print(1/0)
        delete(terms)
        terms.send_keys(gmil)
        print(terms.get_attribute('value'))
    wait_until_done_loading(driver)
    time.sleep(1)


########################################################## month up
    time.sleep(0.5)
    months_up_sel_id = 'paymentsSelect'
    months_up = Select(driver.find_element_by_id(months_up_sel_id))
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    attempts = 0
    while months_up.first_selected_option.text != gup:
        attempts+= 1
        if attempts % 2 == 0:
            the_months_up=remove_zero_from_months_up(gup)
        if attempts % 5 == 0:
            the_months_up=ogmonsup

        if datetime.datetime.now() > future:
            print(1/0)
        try:
            months_up = Select(driver.find_element_by_id(months_up_sel_id))
            months_up.select_by_visible_text(gup)
        except:
            print("months up fail  "+str(gup))
            months_up_sel_id = 'paymentsSelect'
            months_up = Select(driver.find_element_by_id(months_up_sel_id))

######################################################## maint
    prod_id = 'productSelect'
    product_sel = Select(driver.find_element_by_id(prod_id))
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while product_sel.first_selected_option.text != the_maint:
        if datetime.datetime.now() > future:
            print(1/0)

        product_sel.select_by_visible_text(the_maint)
    wait_until_done_loading(driver)
 #   time.sleep(1)
    dismiss_warning_pop_up(driver)
    calc_id = 'btCalculate'
    calc = driver.find_element_by_id(calc_id)
    click(calc)
    time.sleep(1)
    wait_until_done_loading(driver)
    dismiss_warning_pop_up(driver)



######################################################### price below
    wait_until_done_loading(driver)
 #   time.sleep(1)
    dismiss_warning_pop_up(driver)
    calc_id = 'btCalculate'
    calc = driver.find_element_by_id(calc_id)
    click(calc)
    time.sleep(1)
    wait_until_done_loading(driver)
    dismiss_warning_pop_up(driver)
    monthly_price_id = 'driverQuoteTotalMonthlyCost'
    price = driver.find_element_by_id(monthly_price_id).get_attribute("innerHTML")
    print(str(price)+"           price ")
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 230)
    trynum2 = 0
    while "£0.00" in price:
        trynum2 += 1
        print(str(gmon)+"     =      7 ")
        print(str(gup)+"     =      7 ")
        price = retry_setting_terms(driver, og_gup, gmon, gmil , ogmaint, gup , trynum2)
        if datetime.datetime.now() > future:
            price = "failed to get hitatchi price, if persistent and you can get price, tell jack"
        if  "£0.00" in price:
            default_opts_button_xp = '//*[@id="btDefaultQuote"]'
            if ' value="Default Quote" title="Default Quote" disabled="">' in driver.page_source:
                print("good button ting hhhhh")
            else:
                default_opts_button_xp = '//*[@id="btDefaultQuote"]'
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,default_opts_button_xp)))
                def_button  = driver.find_element_by_xpath(default_opts_button_xp)
                click(def_button)
                time.sleep(1)
                wait_until_done_loading(driver)
                time.sleep(1)
                wait_until_done_loading(driver)
                everything_screwed = False
                if '<input type="button" id="btDefaultQuote" class="tooltip btn-gray-125" value="Default Quote" title="Default Quote" disabled="">' in driver.page_source:
                    pass
                elif '<input type="button" id="btDefaultQuote" class="tooltip btn-red-125" value="Default Quote" title="Default Quote">' in driver.page_source:
                    options_chooser(driver)
                    time.sleep(1)
                    wait_until_done_loading(driver)
                    
                    if '<input type="button" id="btDefaultQuote" class="tooltip btn-gray-125" value="Default Quote" title="Default Quote" disabled="">' in driver.page_source:
                        pass
                    elif '<input type="button" id="btDefaultQuote" class="tooltip btn-red-125" value="Default Quote" title="Default Quote">' in driver.page_source:
                        options_chooser(driver)
                        time.sleep(1)
                        wait_until_done_loading(driver)

    return price;

def retry_setting_terms(driver, monthsup, ogmonths, miles , ogmaint , gup2 , trynum2):
    wait_until_done_loading(driver)
    months_sel_id = 'termSelect'
    months = Select(driver.find_element_by_id(months_sel_id))

    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    print(str(months)+"     =      8 ")
    time.sleep(0.5)
    ogmonthsup = gup2
    if monthsup == "1":
        gup2 = '48 months 1 in advance followed by 47'
    if monthsup == "3":
        gup2 = '48 months 03 in advance followed by 45'
    if monthsup == "6":
        gup2 = '48 months 06 in advance followed by 42'
    if monthsup == "9":
        gup2 = '48 months 09 in advance followed by 39'

    while months.first_selected_option.text != "48":
        if datetime.datetime.now() > future:
            print(1/0)
        months.select_by_visible_text("48")
    wait_until_done_loading(driver)
    time.sleep(0.5)

########################################################## mil
    terms_inp_id = 'milesPerAnum'
    terms = driver.find_element_by_id(terms_inp_id)

    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)


    while str(terms.get_attribute('value')).replace(",","") != "20000":
        if datetime.datetime.now() > future:
            print(1/0)
        delete(terms)
        terms.send_keys("20000")
        print(terms.get_attribute('value'))
    wait_until_done_loading(driver)
    time.sleep(1)


    time.sleep(0.5)
    months_up_sel_id = 'paymentsSelect'
    months_up = Select(driver.find_element_by_id(months_up_sel_id))
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    attempts = 0
    while months_up.first_selected_option.text != gup2:
        attempts+= 1
        if attempts % 2 == 0:
            the_months_up=remove_zero_from_months_up(gup2)
        if attempts % 5 == 0:
            the_months_up=ogmonsup

        if datetime.datetime.now() > future:
            print(1/0)
        try:
            months_up = Select(driver.find_element_by_id(months_up_sel_id))
            months_up.select_by_visible_text(gup2)
        except:
            print("months up fail  "+str(gup2))
            months_up_sel_id = 'paymentsSelect'
            months_up = Select(driver.find_element_by_id(months_up_sel_id))

    if  trynum2 > 2:
        print("try num good ")
        default_opts_button_xp = '//*[@id="btDefaultQuote"]'
        if ' value="Default Quote" title="Default Quote" disabled="">' in driver.page_source:
            print("good button ting hhhhh")
        else:
            print("br crmn 4")
            options_chooser(driver)
            time.sleep(1)
            wait_until_done_loading(driver)
            print("br crmn 5")
            if '<input type="button" id="btDefaultQuote" class="tooltip btn-gray-125" value="Default Quote" title="Default Quote" disabled="">' in driver.page_source:
                pass
            elif '<input type="button" id="btDefaultQuote" class="tooltip btn-red-125" value="Default Quote" title="Default Quote">' in driver.page_source:
                options_chooser(driver)
                time.sleep(1)
                wait_until_done_loading(driver)

    wait_until_done_loading(driver)
    dismiss_warning_pop_up(driver)
    calc_id = 'btCalculate'
    calc = driver.find_element_by_id(calc_id)
    click(calc)
    time.sleep(1)
    wait_until_done_loading(driver)
    dismiss_warning_pop_up(driver)
    wait_until_done_loading(driver)
    dismiss_warning_pop_up(driver)
    calc_id = 'btCalculate'
    calc = driver.find_element_by_id(calc_id)
    click(calc)
    time.sleep(1)
    wait_until_done_loading(driver)
    dismiss_warning_pop_up(driver)


####################################################################
    wait_until_done_loading(driver)
    months_sel_id = 'termSelect'
    months = Select(driver.find_element_by_id(months_sel_id))

    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)

    time.sleep(0.5)
    while months.first_selected_option.text != str(ogmonths):
        if datetime.datetime.now() > future:
            print(1/0)
        print(str(ogmonths)+"     =      9 ")
        months.select_by_visible_text(str(ogmonths))
    wait_until_done_loading(driver)
    time.sleep(0.5)

########################################################## mil
    terms_inp_id = 'milesPerAnum'
    terms = driver.find_element_by_id(terms_inp_id)

    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)


    while str(terms.get_attribute('value')).replace(",","") != str(miles):
        if datetime.datetime.now() > future:
            print(1/0)
        delete(terms)
        terms.send_keys(str(miles))
        print(terms.get_attribute('value'))
    wait_until_done_loading(driver)
    time.sleep(1)

###

    time.sleep(0.5)
    months_up_sel_id = 'paymentsSelect'
    months_up = Select(driver.find_element_by_id(months_up_sel_id))
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    attempts = 0
    while months_up.first_selected_option.text != ogmonthsup:
        attempts+= 1
        if attempts % 2 == 0:
            the_months_up=remove_zero_from_months_up(ogmonthsup)
        if attempts % 5 == 0:
            the_months_up=ogmonsup

        if datetime.datetime.now() > future:
            print(1/0)
        try:
            months_up = Select(driver.find_element_by_id(months_up_sel_id))
            months_up.select_by_visible_text(ogmonthsup)
        except:
            print("months up fail  "+str(ogmonthsup))
            months_up_sel_id = 'paymentsSelect'
            months_up = Select(driver.find_element_by_id(months_up_sel_id))

    ####



    wait_until_done_loading(driver)
    dismiss_warning_pop_up(driver)
    calc_id = 'btCalculate'
    calc = driver.find_element_by_id(calc_id)
    click(calc)
    time.sleep(1)
    wait_until_done_loading(driver)
    dismiss_warning_pop_up(driver)
    wait_until_done_loading(driver)
    dismiss_warning_pop_up(driver)
    calc_id = 'btCalculate'
    calc = driver.find_element_by_id(calc_id)
    click(calc)
    time.sleep(1)
    wait_until_done_loading(driver)
    dismiss_warning_pop_up(driver)
    monthly_price_id = 'driverQuoteTotalMonthlyCost'
    price = driver.find_element_by_id(monthly_price_id).get_attribute("innerHTML")
    print(str(price)+"           price ")
    return price

def loading_options_menu(driver):
    loader_xp = '//*[@id="ajax-loader"]'
    loader  = driver.find_element_by_xpath(loader_xp)
    while not "display: none;" in loader.get_attribute("style"):
        print("loading opts stuff ")

        
def options_chooser_special(driver , our_extra):

    option_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[11]/div[1]/input'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,option_xp)))
    option_button  = driver.find_element_by_xpath(option_xp)
    click(option_button)
    print("bzr 1     doing spesh inint ")
    time.sleep(1)
    wait_until_done_loading(driver)
    time.sleep(1)
    wait_until_done_loading(driver)
    time.sleep(1)
    wait_until_done_loading(driver)
    time.sleep(1)
    wait_until_done_loading(driver)
    loading_options_menu(driver)
    good_elems = []
    removed_allready_set_extra = False
    try:
        print("looking for elems 2 ")
        options_window  = driver.find_elements_by_xpath('/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]')[0]
        rows = options_window.find_elements_by_tag_name("div")
        print("r  ex ")
        for r in rows:
            if not removed_allready_set_extra:
                print("r   "+str(r.get_attribute("innerHTML")))
                for td in r.find_elements_by_tag_name("div"):
                    print(str(td.get_attribute("innerHTML")) + "        tds    ")
                try:
                    name = r.get_attribute("innerHTML")
                except:
                    name = "no name "
                if our_extra in name:
            #        print(" it works got extra 1")
                    bef_inp_td = r.find_elements_by_tag_name("div")[0]
                    inp_td = r.find_elements_by_tag_name("div")[2]
                    aft_td = r.find_elements_by_tag_name("div")[2]
                    inp_td.find_elements_by_tag_name("input")[0].click();
                    removed_allready_set_extra = True
                else:
                    print(str(our_extra)+ "     not match      "+ str(name))
    except:
        time.sleep(5)
        loading_options_menu(driver)
        print("looking for elems 2 ")
        options_window  = driver.find_elements_by_xpath('/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]')[0]
        rows = options_window.find_elements_by_tag_name("div")
        print("r  etr ")
        for r in rows:
            if not removed_allready_set_extra:
                print("r   "+str(r.get_attribute("innerHTML")))
                for td in r.find_elements_by_tag_name("div"):
                    print(str(td.get_attribute("innerHTML")) + "        tds    ")
                try:
                    name = r.get_attribute("innerHTML")
                except:
                    name = "no name "
                if our_extra in name:
           #         print(" it works got extra 2")
                    bef_inp_td = r.find_elements_by_tag_name("div")[0]
                    inp_td = r.find_elements_by_tag_name("div")[2]
                    aft_td = r.find_elements_by_tag_name("div")[2]
                    removed_allready_set_extra = True
                    inp_td.find_element_by_tag_name("input")[0].click();
                else:
                    print(str(our_extra)+ "     not match      "+ str(name))

#    time.sleep(999)
    loading_options_menu(driver)
    stop_yet  = False
    internal_sorted = False
    external_done_yet = False
    internal_done_yet = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    options_window  = driver.find_elements_by_xpath('/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]')
    while not external_done_yet and not internal_done_yet:
        if datetime.datetime.now() > future:
            print(1/0)
        for extras in range(2):
            print("abloody extra signpost "+ str(extras))
            time.sleep(1)
            wait_until_done_loading(driver)
            time.sleep(1)
            wait_until_done_loading(driver)
            print("aqaqa 67     extra =  "+str(extras))
            print(extras)
            this_extra_got = False

            for web_elem in options_window:
                print("1")
                if not this_extra_got:

                    
                    print("bzr 4")
                    more_elems = web_elem.find_elements_by_class_name('associate-option-item-name-container')
                    print("bzr 4 a ")
                    print(web_elem.get_attribute('innerHTML'))
                    print("bzr 4 b ")
                    elem_counter = 0
                    while len(more_elems) < 5:
                        print("no choices ")
                        more_elems = web_elem.find_elements_by_class_name('associate-option-item-name-container')

                    for even_more_elem in more_elems:
                        print(' ciiiiii   one')
                        if this_extra_got:
                            print("but weve allready got this extra 9999 ")
                        #    time.sleep(999)
                        if not this_extra_got:
                #            print(even_more_elem.get_attribute('innerHTML'))
                            this_price = even_more_elem.find_element_by_class_name('associate-option-item-cost').get_attribute('innerHTML')
                            this_name = even_more_elem.find_element_by_class_name('associate-option-item-name').get_attribute('innerHTML').lower()
                           # check_box = [tag name = input and type = checkbox and 'option_' in id]
                            print("   hghyghghghghg ")
                            print(this_name)
                            print("    4777777777777777777777777777777777777        ")
                            options = even_more_elem.find_elements_by_tag_name('input')
                            for o in options:
                       #         print(o.get_attribute('id'))
                                if 'option_' in o.get_attribute('id'):
                                    if o.get_attribute('id')[7].isdigit():
                                        check_box = o


                            if not stop_yet:

                                if even_more_elem.get_attribute('innerHTML') == "Standard":
                        #            print("propper stop     we found stand section")
                                    stop_yet = True

                                elif 'cloth' in this_name and not internal_done_yet and not this_extra_got:
                                    if this_price == '£0.00':
                                        print("bzr  aaaaa")
                                        click(check_box)
                                        selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                        not_clicked = True
                                        click_counter = 0
                                        tstamp = datetime.datetime.now()
                                        future2 = tstamp1 +  datetime.timedelta(seconds = 130)
                                        while not_clicked and not this_extra_got:
                                             if datetime.datetime.now() > future2:
                                                 print(1/0)
                                             print("   not clicked loop for cloth  ")
                                             time.sleep(5)
                                             selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                             been_through_options = False
                                             tstamp1 = datetime.datetime.now()
                                             future3 = tstamp1 +  datetime.timedelta(seconds = 130)
                                             while not been_through_options and not this_extra_got:
                                                 if datetime.datetime.now() > future3:
                                                     print(1/0)
                                                 click(check_box)
                                                 print("bzr 5")
                                                 time.sleep(5)

                                                 selected = driver.find_elements_by_id('selected-options-listing')
                                                 for s in selected:
                                                     print(" br 4 ")
                                                     if 'cloth' in s.get_attribute('innerHTML').lower():
                                              #           print(" br 5      cos we got "+str(s.get_attribute('innerHTML')))
                                                         not_clicked = False
                                                         internal_done_yet = True
                                                         this_extra_got = True
                                                         time.sleep(5)
                                                     else:
                                             #            print(s.get_attribute('innerHTML').lower())
                                                         print("aint cloth")
                                                 been_through_options = True
                                                 if not_clicked:
                                                     click_counter+=1

                                                     if click_counter % 2 == 0:
                                                         time.sleep(1)
                                                         click(check_box)
                                                         time.sleep(1)
                                                         click(check_box)
                                                     else:
                                                         click(check_box)
    #                                             try:
     #                                                for s in selected:
      #                                                   if 'cloth' in s.get_attribute('innerHTML').lower():
       #                                                      not_clicked = False
        #                                                     internal_done_yet = True
         #                                                    this_extra_got = True
          #                                                   time.sleep(5)
           #                                              else:
            #                                                 print(s.get_attribute('innerHTML')+ "  is not cloth ")
             #
              #                                       been_through_options = True
               #                                  except:
                #                                     selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                 #                                    try:
                  #                                       for s in selected:
                   ##                                          print("selected print below ")
                     ##                                        print(s)
                       #                                      print(s.get_attribute('innerHTML'))
                        #                                 #print(selected)
                         #                            except:
    #                     #                                for s in selected:
                           #                              print("wont iterate ")
    #

    #
    #
     #
      #                                           click(check_box)
       #                                          time.sleep(5)


                                    else:
                                        print(this_price)
                                        print(1/0)
                                elif 'leather' in this_name.lower() and not internal_done_yet and not 'steering' in this_name.lower() and not this_extra_got:
                                    if this_price == '£0.00':
                                        click(check_box)
                                        selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                        not_clicked = True
                                        click_counter = 0
                                        tstamp1 = datetime.datetime.now()
                                        future4 = tstamp1 +  datetime.timedelta(seconds = 130)
                                        while not_clicked and not this_extra_got:
                                             if datetime.datetime.now() > future4:
                                                 print(1/0)
                                             print("   not clicked loop for leather ----------- ")
                                             time.sleep(5)
                                             print("y")
                                             selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                             been_through_options = False
                                             print("y2")
                                             tstamp1 = datetime.datetime.now()
                                             future5 = tstamp1 +  datetime.timedelta(seconds = 130)
                                             while not been_through_options and not this_extra_got:
                                                 if datetime.datetime.now() > future5:
                                                     print(1/0)
                                                 print("y3")
                                                 click(check_box)
                                                 time.sleep(5)
                                                 selected = driver.find_elements_by_id('selected-options-listing')
                                                 for s in selected:
                                                     print(" br 4 ------------------------------------")
                                                     if 'leather' in s.get_attribute('innerHTML').lower():
                                                         print(" br 5 ")
                                                         not_clicked = False
                                                         internal_done_yet = True
                                                         this_extra_got = True
                                                         for i in range(10):
                                                             print(" leather is sorted ")
                                                         time.sleep(5)
                                                     else:
                                                         pass
                                                 print("y 444 ")
                                                 been_through_options = True
                                                 if click_counter % 2 == 0:
                                                     time.sleep(1)
                                                     click(check_box)
                                                     time.sleep(1)
                                                     click(check_box)
                                                 else:
                                                     click(check_box)
                                                 print("y yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy y      end  ")

                                elif 'metallic' in this_name.lower() and not external_done_yet and not this_extra_got:
                                    #if this_price == '£0.00':
                                    click(check_box)
                                    selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                    not_clicked = True
                                    click_counter = 0
                                    tstamp1 = datetime.datetime.now()
                                    future6 = tstamp1 +  datetime.timedelta(seconds = 130)
                                    while not_clicked and not this_extra_got:
                                        if datetime.datetime.now() > future6:
                                            print(1/0)
                                        print("   not clicked loop for metalic  ")
                                        time.sleep(5)

                                        if click_counter % 2 == 0:
                                            time.sleep(1)
                                            click(check_box)
                                            time.sleep(1)
                                            click(check_box)
                                        else:
                                            click(check_box)

                                        selected = driver.find_elements_by_id('selected-options-listing')
                                        print(" ssssssssssssssssssssssssssssssssssssssssss ")
                                        for s in selected:
                                            ss = s.get_attribute('innerHTML').lower()
                                            print(ss)
                                        for s in selected:
                                            print(" br 4 676767766 ")
                                            if 'metallic' in s.get_attribute('innerHTML').lower():
                                                print(" br 5 ")
                                                not_clicked = False
                                                external_done_yet = True
                                                this_extra_got = True
                                                time.sleep(5)
                                            else:
                                                print("this aint metalic   " + str(s.get_attribute('innerHTML').lower()))
                                        click_counter+= 1
                                        been_through_options = True
                                        print(" bottom of mettalic whilre loop  ")
                                    print(" end of met while  ")



                                             #######
                          #                   selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                           #                  print(" br 1 ")
                            #                 been_through_options = False
                             #                while not been_through_options and not this_extra_got:
                              #                   print(" br 2 ")
                               #                  click(check_box)
                                #                 time.sleep(5)
                                 #                try:
                                  #                   print(" br 3 ")
                                   #                  print(str(len(selected))+ "    number of options")
                                    #                 for s in selected:
                                     #                    print(" br 4 ")
                                      #                   if 'paint' in s.get_attribute('innerHTML').lower():
                                       #                      print(" br 5 ")
                                        #                     not_clicked = False
                                         #                    external_done_yet = True
                                          #                   this_extra_got = True
                                           #                  time.sleep(5)
                                            #             else:
                                             #                pass
                                              #           print(" br 6 ")
                                               ##      print(" br 7 ")
                                                 #    been_through_options = True
                           #                      except Exception as e:
                            #                         print(e)
                             #                        print(e.messsage)
                              #                       print(" br 8 ")
                               #                      selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                #                     print(str(len(selected))+ "    number of options")
                                 ##                    try:
                                   ##                      for s in selected:
                                     #                        print(s)
                                      #                       print(s.get_attribute('innerHTML'))
                                       #              except:
    #                                   #                  for s in selected:
                                         #                print("wont iterate ")
                                          #           print(driver.page_source)
                                           #          time.sleep(7)
                                            #         print(" br 9 ")
                                             #





                       #         print(driver.page_source)
                        elem_counter+=1
                        print("bottom ere")

        if not external_done_yet and not internal_done_yet:
            options_window  = driver.find_elements_by_xpath('/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]')
    print("done  with special options ")
#    print(6/0)
    ok_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[4]/input[1]'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,ok_xp)))

    ok_button  = driver.find_element_by_xpath(ok_xp)
    click(ok_button)
    print("    arse     ")

    time.sleep(1)
    wait_until_done_loading(driver)
    time.sleep(1)
    wait_until_done_loading(driver)

    try:
        error_xp = '/html/body/div[9]/div[2]/div[2]'
        error  = driver.find_element_by_xpath(error_xp)
        if "display: block;" in error.get_attribute("style"):
            print("missed soomething       doing a second try  ")
            print("ffffffffffuuuuuuuuuuccccccccccckkkkkkkkkkkkkkk")
            options_chooser_special2(driver)
            print(10/0)
            return second_try
        else:
            return True
    except:
        return True
    print(1/0)


def options_chooser_special2(driver):

    option_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[11]/div[1]/input'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,option_xp)))
    option_button  = driver.find_element_by_xpath(option_xp)
    click(option_button)
    print("bzr 1     doing spesh inint ")
    time.sleep(1)
    wait_until_done_loading(driver)
    time.sleep(1)
    wait_until_done_loading(driver)
    good_elems = []
    print("bzr 2")
   # external_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]'
  #  internal_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]/div[15]'
   # standard_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]/div[28]'
 #   options_window_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]'
#                          /html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]
  #  WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,external_xp)))
#    external_window  = driver.find_elements_by_xpath(external_xp)
 #   WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,external_xp)))
 #   external_window  = driver.find_elements_by_xpath(external_xp)

#    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,options_window_xp)))
    print("bzr 3")
    print("looking for elems 2 ")
    options_window  = driver.find_elements_by_xpath('/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]')
    print("looking for elems")
 #   print(options_window.get_attribute('innerHTML'))
    stop_yet  = False
    internal_sorted = False
    external_done_yet = False
    internal_done_yet = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not external_done_yet and not internal_done_yet:
        if datetime.datetime.now() > future:
            print(1/0)
        for extras in range(2):
            time.sleep(1)
            wait_until_done_loading(driver)
            time.sleep(1)
            wait_until_done_loading(driver)
            print("aqaqa 67")
            print(extras)
            this_extra_got = False

            for web_elem in options_window:
                print("1")
                if not this_extra_got:
                    print("bzr 4")
                    more_elems = web_elem.find_elements_by_class_name('associate-option-item-name-container')
                    print("bzr 4 a ")
                    print(web_elem.get_attribute('innerHTML'))
                    print("bzr 4 b ")
                    elem_counter = 0
                    for even_more_elem in more_elems:
                        print(' ciiiiii  two  ')
                        if not this_extra_got:
                #            print(even_more_elem.get_attribute('innerHTML'))
                            this_price = even_more_elem.find_element_by_class_name('associate-option-item-cost').get_attribute('innerHTML')
                            this_name = even_more_elem.find_element_by_class_name('associate-option-item-name').get_attribute('innerHTML')
                           # check_box = [tag name = input and type = checkbox and 'option_' in id]
                            options = even_more_elem.find_elements_by_tag_name('input')
                            for o in options:
                       #         print(o.get_attribute('id'))
                                if 'option_' in o.get_attribute('id'):
                                    if o.get_attribute('id')[7].isdigit():
                                        check_box = o


                            if not stop_yet:
                                if even_more_elem.get_attribute('innerHTML') == "Standard":
                        #            print("propper stop     we found stand section")
                                    stop_yet = True

                                elif 'cloth' in this_name and not internal_done_yet and not this_extra_got:
                                    if this_price == '£0.00':
                                        print("bzr  aaaaa")
                                        click(check_box)
                                        selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                        not_clicked = True
                                        click_counter = 0
                                        tstamp = datetime.datetime.now()
                                        future2 = tstamp1 +  datetime.timedelta(seconds = 130)
                                        while not_clicked and not this_extra_got:
                                             if datetime.datetime.now() > future2:
                                                 print(1/0)
                                             print("   not clicked loop for cloth  ")
                                             time.sleep(5)
                                             selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                             been_through_options = False
                                             tstamp1 = datetime.datetime.now()
                                             future3 = tstamp1 +  datetime.timedelta(seconds = 130)
                                             while not been_through_options and not this_extra_got:
                                                 if datetime.datetime.now() > future3:
                                                     print(1/0)
                                                 click(check_box)
                                                 print("bzr 5")
                                                 time.sleep(5)

                                                 selected = driver.find_elements_by_id('selected-options-listing')
                                                 for s in selected:
                                                     print(" br 4 ")
                                                     if 'cloth' in s.get_attribute('innerHTML').lower():
                                              #           print(" br 5      cos we got "+str(s.get_attribute('innerHTML')))
                                                         not_clicked = False
                                                         internal_done_yet = True
                                                         this_extra_got = True
                                                         time.sleep(5)
                                                     else:
                                             #            print(s.get_attribute('innerHTML').lower())
                                                         print("aint cloth")
                                                 been_through_options = True
                                                 if not_clicked:
                                                     click_counter+=1

                                                     if click_counter % 2 == 0:
                                                         time.sleep(1)
                                                         click(check_box)
                                                         time.sleep(1)
                                                         click(check_box)
                                                     else:
                                                         click(check_box)
    #                                             try:
     #                                                for s in selected:
      #                                                   if 'cloth' in s.get_attribute('innerHTML').lower():
       #                                                      not_clicked = False
        #                                                     internal_done_yet = True
         #                                                    this_extra_got = True
          #                                                   time.sleep(5)
           #                                              else:
            #                                                 print(s.get_attribute('innerHTML')+ "  is not cloth ")
             #
              #                                       been_through_options = True
               #                                  except:
                #                                     selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                 #                                    try:
                  #                                       for s in selected:
                   ##                                          print("selected print below ")
                     ##                                        print(s)
                       #                                      print(s.get_attribute('innerHTML'))
                        #                                 #print(selected)
                         #                            except:
    #                     #                                for s in selected:
                           #                              print("wont iterate ")
    #

    #
    #
     #
      #                                           click(check_box)
       #                                          time.sleep(5)


                                    else:
                                        print(this_price)
                                        print(1/0)
                                elif 'leather' in this_name.lower() and not internal_done_yet and not 'steering' in this_name.lower() and not this_extra_got:
                                    if this_price == '£0.00':
                                        click(check_box)
                                        selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                        not_clicked = True
                                        click_counter = 0
                                        tstamp1 = datetime.datetime.now()
                                        future4 = tstamp1 +  datetime.timedelta(seconds = 130)
                                        while not_clicked and not this_extra_got:
                                             if datetime.datetime.now() > future4:
                                                 print(1/0)
                                             print("   not clicked loop for leather ----------- ")
                                             time.sleep(5)
                                             print("y")
                                             selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                             been_through_options = False
                                             print("y2")
                                             tstamp1 = datetime.datetime.now()
                                             future5 = tstamp1 +  datetime.timedelta(seconds = 130)
                                             while not been_through_options and not this_extra_got:
                                                 if datetime.datetime.now() > future5:
                                                     print(1/0)
                                                 print("y3")
                                                 click(check_box)
                                                 time.sleep(5)
                                                 selected = driver.find_elements_by_id('selected-options-listing')
                                                 for s in selected:
                                                     print(" br 4 ------------------------------------")
                                                     if 'leather' in s.get_attribute('innerHTML').lower():
                                                         print(" br 5 ")
                                                         not_clicked = False
                                                         internal_done_yet = True
                                                         this_extra_got = True
                                                         for i in range(10):
                                                             print(" leather is sorted ")
                                                         time.sleep(5)
                                                     else:
                                                         pass
                                                 print("y 444 ")
                                                 been_through_options = True
                                                 if click_counter % 2 == 0:
                                                     time.sleep(1)
                                                     click(check_box)
                                                     time.sleep(1)
                                                     click(check_box)
                                                 else:
                                                     click(check_box)
                                                 print("y yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy y      end  ")

                                elif 'metallic' in this_name.lower() and not external_done_yet and not this_extra_got:
                                    #if this_price == '£0.00':
                                    click(check_box)
                                    selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                    not_clicked = True
                                    click_counter = 0
                                    tstamp1 = datetime.datetime.now()
                                    future6 = tstamp1 +  datetime.timedelta(seconds = 130)
                                    while not_clicked and not this_extra_got:
                                        if datetime.datetime.now() > future6:
                                            print(1/0)
                                        print("   not clicked loop for metalic  ")
                                        time.sleep(5)

                                        selected = driver.find_elements_by_id('selected-options-listing')
                                        for s in selected:
                                            print(" br 4 676767766 ")
                                            if 'metallic' in s.get_attribute('innerHTML').lower():
                                                print(" br 5 ")
                                                not_clicked = False
                                                external_done_yet = True
                                                this_extra_got = True
                                                time.sleep(5)
                                            else:
                                                print("this aint metalic   " + str(s.get_attribute('innerHTML').lower()))

                                        been_through_options = True
                                        if click_counter % 2 == 0:
                                            time.sleep(1)
                                            click(check_box)
                                            time.sleep(1)
                                            click(check_box)
                                        else:
                                            click(check_box)



                                             #######
                          #                   selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                           #                  print(" br 1 ")
                            #                 been_through_options = False
                             #                while not been_through_options and not this_extra_got:
                              #                   print(" br 2 ")
                               #                  click(check_box)
                                #                 time.sleep(5)
                                 #                try:
                                  #                   print(" br 3 ")
                                   #                  print(str(len(selected))+ "    number of options")
                                    #                 for s in selected:
                                     #                    print(" br 4 ")
                                      #                   if 'paint' in s.get_attribute('innerHTML').lower():
                                       #                      print(" br 5 ")
                                        #                     not_clicked = False
                                         #                    external_done_yet = True
                                          #                   this_extra_got = True
                                           #                  time.sleep(5)
                                            #             else:
                                             #                pass
                                              #           print(" br 6 ")
                                               ##      print(" br 7 ")
                                                 #    been_through_options = True
                           #                      except Exception as e:
                            #                         print(e)
                             #                        print(e.messsage)
                              #                       print(" br 8 ")
                               #                      selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                #                     print(str(len(selected))+ "    number of options")
                                 ##                    try:
                                   ##                      for s in selected:
                                     #                        print(s)
                                      #                       print(s.get_attribute('innerHTML'))
                                       #              except:
    #                                   #                  for s in selected:
                                         #                print("wont iterate ")
                                          #           print(driver.page_source)
                                           #          time.sleep(7)
                                            #         print(" br 9 ")
                                             #





                          #      print(driver.page_source)
                        elem_counter+=1
        if not external_done_yet and not internal_done_yet:
            options_window  = driver.find_elements_by_xpath('/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]')
 #   print("done ")

    ok_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[4]/input[1]'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,ok_xp)))

    ok_button  = driver.find_element_by_xpath(ok_xp)
    click(ok_button)
#    print("    arse     ")

    time.sleep(1)
    wait_until_done_loading(driver)
    time.sleep(1)
    wait_until_done_loading(driver)

    try:
        error_xp = '/html/body/div[9]/div[2]/div[2]'
        error  = driver.find_element_by_xpath(error_xp)
        if "display: block;" in error.get_attribute("style"):
   #         print("missed soomething       doing a second try  ")
  #          print("ffffffffffuuuuuuuuuuccccccccccckkkkkkkkkkkkkkk")
            print(10/0)
            return second_try
        else:
            return True
    except:
        return True
    print(1/0)


def dismiss_warning_pop_up(driver):
    close_xp = '/html/body/div[3]/div[1]/a/span'
    ok_xp = '/html/body/div[3]/div[3]/div/button/span'
    try:
        close = driver.find_element_by_xpath(close_xp)
        click(close)
    except:
        try:
            ok = driver.find_element_by_xpath(ok_xp)
            click(ok)
        except:
            try:
                ok_xp = '/html/body/div[3]/div[3]/div/button'
                ok = driver.find_element_by_xpath(ok_xp)
                click(ok)
            except:
                try:
                    ok_xp = '/html/body/div[3]/div[3]/div'
                    ok = driver.find_element_by_xpath(ok_xp)
                    click(ok)
                except:
                    pass

def enter_date(driver):

#    try:
#        calender_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[10]/div[5]/img'
#        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,calender_xp)))
#    except:
        #          //*[@id="saveForm"]/div[10]/div[5]/img
    calender_xp= '//*[@id="saveForm"]/div[10]/div[5]/img'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,calender_xp)))

    cal = driver.find_element_by_xpath(calender_xp)
    click(cal)
    time.sleep(1.5)
    #ui-datepicker-div > table > tbody > tr:nth-child(6) > td:nth-child(2) > a
    #            /html/body/div[5]/table/tbody/tr[6]/td[2]/a
    table_xp = '//*[@id="ui-datepicker-div"]/table/tbody'
    date_xp_2 = '/html/body/div[5]/table/tbody/tr[6]/td[2]/a'
    date_xp = '/html/body/div[5]/table/tbody/tr[4]/td[7]/a'
    worked = False
    while not worked:
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,table_xp)))
            table = driver.find_element_by_xpath(table_xp)
            worked = True
        except:
            click(cal)
    all_stuff = table.find_elements_by_css_selector("*")
    for obj in all_stuff:
        the_txt = obj.get_attribute("innerHTML")
        print(the_txt)

        outerhtml = obj.get_attribute('outerHTML') # to extract outerHTML
        if outerhtml[0] == "<" and outerhtml[1] == "a":
            if "31" in the_txt:
                print("did 31")
                obj.click();
                time.sleep(1)
                return True
            if "30" in the_txt:
                print("did 30")
                obj.click();
                time.sleep(1)
                return True
            if "29" in the_txt:
                print("did 29")
                obj.click();
                time.sleep(1)
                return True
            if "28" in the_txt:
                print("did 28")
                obj.click();
                time.sleep(1)
                return True

 #   print("apparentkyu no ")
    print(9/0)
#    try:
#        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,date_xp)))
#    except:
#        date_xp = date_xp_2
#        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,date_xp)))
#    date = driver.find_element_by_xpath(date_xp)
#    click(date)

def enter_cap_id(driver, cap_id):
    print("enter cap_id start")
    cap_id_id = 'capCode'
  #  print(driver.page_source)
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, cap_id_id )))
#    except:
#        cap_id_xp = '//*[@id="capCode"]'
#        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, cap_id_xp )))
    cap_id_obj = driver.find_element_by_id(cap_id_id)
    cap_id_obj.send_keys(cap_id)
    current_cap_id = cap_id_obj.get_attribute("value")
    current_cap_id2 = cap_id_obj.get_attribute("innerHTML")
    print(current_cap_id)
    print(current_cap_id2)
    print(cap_id)
    if cap_id == current_cap_id:
        print("yay1")
    if cap_id == current_cap_id2:
        print("yay2")

#
#    error_msg_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[4]/div/div/div'
#    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, error_msg_xp )))
#    error_obj = driver.find_element_by_xp(error_msg_xp)
#    error1 = error_obj.get_attribute("innerHTML")

    search_cap_id_id = "capCodeButtonSearch"
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, search_cap_id_id )))
    search_cap_id_obj = driver.find_element_by_id(search_cap_id_id)
    search_cap_id_obj.click();
    time.sleep(2)
    print("finishing entering cap_id ")
#    error_obj = driver.find_element_by_xp(error_msg_xp)
#    error2 = error_obj.get_attribute("innerHTML")
#    print(error1)
#    print(error2)
#    print("yay")
#

def double_check_car(driver, blp):
    time.sleep(1)
    print("aight lets check ")
    try:
        error_class = 'errorMessage'
        error_obj = driver.find_element_by_class_name(error_class)
        error1 = error_obj.get_attribute("innerHTML")
        print(error1)
        if "No variants with matching CAP codes found. Please try again" in error1:
            print("that error is here ")
            return False
    except:
        print("no e msg ")

    blp_id = 'listPriceSelect'
    WebDriverWait(driver,54).until(EC.presence_of_element_located((By.ID, blp_id)))
    blp_obj = Select(driver.find_element_by_id(blp_id))
    their_blp = blp_obj.first_selected_option.text;
    print(their_blp)
    their_blp_clean = ""
    bracket_found = False
    for char in their_blp:
        if char != "(" and bracket_found == False:
            their_blp_clean += char
            print("char " +str(char))
        else:
            bracket_found = True
    their_blp_clean = their_blp_clean.replace("£","").replace(",","").strip()
    blp = blp.replace("£","").replace(",","").strip()
    print(their_blp_clean)
    print(blp)
    if abs(float(their_blp_clean) - float(blp)) < 1000:
        print("blp match :) ")
        return True
    else:
        print(" blp mismatch ")
        return False

def options_chooser(driver):

    option_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[11]/div[1]/input'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,option_xp)))
    option_button  = driver.find_element_by_xpath(option_xp)
    click(option_button)
    print("bzr 1  base ")
    time.sleep(1)
    wait_until_done_loading(driver)
    time.sleep(1)
    wait_until_done_loading(driver)
    good_elems = []
    print("bzr 2")
   # external_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]'
  #  internal_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]/div[15]'
   # standard_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]/div[28]'
 #   options_window_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]'
#                          /html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]
  #  WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,external_xp)))
#    external_window  = driver.find_elements_by_xpath(external_xp)
 #   WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,external_xp)))
 #   external_window  = driver.find_elements_by_xpath(external_xp)

#    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,options_window_xp)))
    print("bzr 3")
    print("looking for elems 2 ")
    options_window  = driver.find_elements_by_xpath('/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]')
    print("looking for elems")
 #   print(options_window.get_attribute('innerHTML'))
    stop_yet  = False
    internal_sorted = False
    external_done_yet = False
    internal_done_yet = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not external_done_yet and not internal_done_yet:
        if datetime.datetime.now() > future:
            print(1/0)
        for extras in range(2):
            time.sleep(1)
            wait_until_done_loading(driver)
            time.sleep(1)
            wait_until_done_loading(driver)
            print(extras)
            this_extra_got = False

            for web_elem in options_window:
                print("1")
                if not this_extra_got:
                    print("bzr 4")
                    more_elems = web_elem.find_elements_by_class_name('associate-option-item-name-container')
                    print("bzr 4 a ")
                    print(web_elem.get_attribute('innerHTML'))
                    print("bzr 4 b ")
                    elem_counter = 0
                    for even_more_elem in more_elems:
                        print(' ciiiiii  three ')
                        if not this_extra_got:
                #            print(even_more_elem.get_attribute('innerHTML'))
                            this_price = even_more_elem.find_element_by_class_name('associate-option-item-cost').get_attribute('innerHTML')
                            this_name = even_more_elem.find_element_by_class_name('associate-option-item-name').get_attribute('innerHTML')
                           # check_box = [tag name = input and type = checkbox and 'option_' in id]
                            options = even_more_elem.find_elements_by_tag_name('input')
                            for o in options:
                       #         print(o.get_attribute('id'))
                                if 'option_' in o.get_attribute('id'):
                                    if o.get_attribute('id')[7].isdigit():
                                        check_box = o


                            if not stop_yet:
                                if even_more_elem.get_attribute('innerHTML') == "Standard":
                        #            print("propper stop     we found stand section")
                                    stop_yet = True

                                elif 'cloth' in this_name and not internal_done_yet and not this_extra_got:
                                    if this_price == '£0.00':
                                        print("bzr  aaaaa")
                                        click(check_box)
                                        selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                        not_clicked = True
                                        click_counter = 0
                                        tstamp = datetime.datetime.now()
                                        future2 = tstamp1 +  datetime.timedelta(seconds = 130)
                                        while not_clicked and not this_extra_got:
                                             if datetime.datetime.now() > future2:
                                                 print(1/0)
                                             print("   not clicked loop for cloth  ")
                                             time.sleep(5)
                                             selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                             been_through_options = False
                                             tstamp1 = datetime.datetime.now()
                                             future3 = tstamp1 +  datetime.timedelta(seconds = 130)
                                             while not been_through_options and not this_extra_got:
                                                 if datetime.datetime.now() > future3:
                                                     print(1/0)
                                                 click(check_box)
                                                 print("bzr 5")
                                                 time.sleep(5)

                                                 selected = driver.find_elements_by_id('selected-options-listing')
                                                 for s in selected:
                                                     print(" br 4 ")
                                                     if 'cloth' in s.get_attribute('innerHTML').lower():
                                              #           print(" br 5      cos we got "+str(s.get_attribute('innerHTML')))
                                                         not_clicked = False
                                                         internal_done_yet = True
                                                         this_extra_got = True
                                                         time.sleep(5)
                                                     else:
                                             #            print(s.get_attribute('innerHTML').lower())
                                                         print("aint cloth")
                                                 been_through_options = True
                                                 if not_clicked:
                                                     click_counter+=1

                                                     if click_counter % 2 == 0:
                                                         time.sleep(1)
                                                         click(check_box)
                                                         time.sleep(1)
                                                         click(check_box)
                                                     else:
                                                         click(check_box)
    #                                             try:
     #                                                for s in selected:
      #                                                   if 'cloth' in s.get_attribute('innerHTML').lower():
       #                                                      not_clicked = False
        #                                                     internal_done_yet = True
         #                                                    this_extra_got = True
          #                                                   time.sleep(5)
           #                                              else:
            #                                                 print(s.get_attribute('innerHTML')+ "  is not cloth ")
             #
              #                                       been_through_options = True
               #                                  except:
                #                                     selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                 #                                    try:
                  #                                       for s in selected:
                   ##                                          print("selected print below ")
                     ##                                        print(s)
                       #                                      print(s.get_attribute('innerHTML'))
                        #                                 #print(selected)
                         #                            except:
    #                     #                                for s in selected:
                           #                              print("wont iterate ")
    #

    #
    #
     #
      #                                           click(check_box)
       #                                          time.sleep(5)


                                    else:
                                        print(this_price)
                                        print(1/0)
                                elif 'leather' in this_name.lower() and not internal_done_yet and not 'steering' in this_name.lower() and not this_extra_got:
                                    if this_price == '£0.00':
                                        click(check_box)
                                        selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                        not_clicked = True
                                        click_counter = 0
                                        tstamp1 = datetime.datetime.now()
                                        future4 = tstamp1 +  datetime.timedelta(seconds = 130)
                                        while not_clicked and not this_extra_got:
                                             if datetime.datetime.now() > future4:
                                                 print(1/0)
                                             print("   not clicked loop for leather ----------- ")
                                             time.sleep(5)
                                             print("y")
                                             selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                             been_through_options = False
                                             print("y2")
                                             tstamp1 = datetime.datetime.now()
                                             future5 = tstamp1 +  datetime.timedelta(seconds = 130)
                                             while not been_through_options and not this_extra_got:
                                                 if datetime.datetime.now() > future5:
                                                     print(1/0)
                                                 print("y3")
                                                 click(check_box)
                                                 time.sleep(5)
                                                 selected = driver.find_elements_by_id('selected-options-listing')
                                                 for s in selected:
                                                     print(" br 4 ------------------------------------")
                                                     if 'leather' in s.get_attribute('innerHTML').lower():
                                                         print(" br 5 ")
                                                         not_clicked = False
                                                         internal_done_yet = True
                                                         this_extra_got = True
                                                         for i in range(10):
                                                             print(" leather is sorted ")
                                                         time.sleep(5)
                                                     else:
                                                         pass
                                                 print("y 444 ")
                                                 been_through_options = True
                                                 if click_counter % 2 == 0:
                                                     time.sleep(1)
                                                     click(check_box)
                                                     time.sleep(1)
                                                     click(check_box)
                                                 else:
                                                     click(check_box)
                                                 print("y yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy y      end  ")

                                elif 'paint' in this_name.lower() and not external_done_yet and not this_extra_got:
                                    if this_price == '£0.00':
                                        click(check_box)
                                        selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                        not_clicked = True
                                        click_counter = 0
                                        tstamp1 = datetime.datetime.now()
                                        future6 = tstamp1 +  datetime.timedelta(seconds = 130)
                                        while not_clicked and not this_extra_got:
                                            if datetime.datetime.now() > future6:
                                                print(1/0)
                                            print("   not clicked loop for paint  ffffssss ")
                                            time.sleep(5)

                                            selected = driver.find_elements_by_id('selected-options-listing')
                                            for s in selected:
                                                print(" br 4 676767766 ")
                                                if 'paint' in s.get_attribute('innerHTML').lower():
                                                    print(" br 5 ")
                                                    not_clicked = False
                                                    external_done_yet = True
                                                    this_extra_got = True
                                                    time.sleep(5)
                                                else:
                                                    print("this aint paint   " + str(s.get_attribute('innerHTML').lower()))

                                            been_through_options = True
                                            if click_counter % 2 == 0:
                                                time.sleep(1)
                                                click(check_box)
                                                time.sleep(1)
                                                click(check_box)
                                            else:
                                                click(check_box)



                                             #######
                          #                   selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                           #                  print(" br 1 ")
                            #                 been_through_options = False
                             #                while not been_through_options and not this_extra_got:
                              #                   print(" br 2 ")
                               #                  click(check_box)
                                #                 time.sleep(5)
                                 #                try:
                                  #                   print(" br 3 ")
                                   #                  print(str(len(selected))+ "    number of options")
                                    #                 for s in selected:
                                     #                    print(" br 4 ")
                                      #                   if 'paint' in s.get_attribute('innerHTML').lower():
                                       #                      print(" br 5 ")
                                        #                     not_clicked = False
                                         #                    external_done_yet = True
                                          #                   this_extra_got = True
                                           #                  time.sleep(5)
                                            #             else:
                                             #                pass
                                              #           print(" br 6 ")
                                               ##      print(" br 7 ")
                                                 #    been_through_options = True
                           #                      except Exception as e:
                            #                         print(e)
                             #                        print(e.messsage)
                              #                       print(" br 8 ")
                               #                      selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                #                     print(str(len(selected))+ "    number of options")
                                 ##                    try:
                                   ##                      for s in selected:
                                     #                        print(s)
                                      #                       print(s.get_attribute('innerHTML'))
                                       #              except:
    #                                   #                  for s in selected:
                                         #                print("wont iterate ")
                                          #           print(driver.page_source)
                                           #          time.sleep(7)
                                            #         print(" br 9 ")
                                             #





                               # print(driver.page_source)
                        elem_counter+=1
        if not external_done_yet and not internal_done_yet:
            options_window  = driver.find_elements_by_xpath('/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]')
    print("done ")

    ok_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[4]/input[1]'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,ok_xp)))

    ok_button  = driver.find_element_by_xpath(ok_xp)
    click(ok_button)
    print("    arse     ")

    time.sleep(1)
    wait_until_done_loading(driver)
    time.sleep(1)
    wait_until_done_loading(driver)

    try:
        error_xp = '/html/body/div[9]/div[2]/div[2]'
        error  = driver.find_element_by_xpath(error_xp)
        if "display: block;" in error.get_attribute("style"):
            print("missed soomething       doing a second try  ")
            second_try = options_chooser_2(driver)
            return second_try
        else:
            return True
    except:
        return True
    print(1/0)



def get_their_deriv(driver):
    full_desc_id = 'fullDescription';
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID, full_desc_id)))
    return driver.find_element_by_id(full_desc_id).get_attribute("value")






def wait_for_delete():
    car_chosen = False
    while not car_chosen:
        if keyboard.is_pressed('q'):
            car_chosen = True

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

def click(button):
    try:
        time.sleep(1)
        button.click()
        print('clicked   '  + str(button))
    except Exception as e:
        print(str(e))

def defclick(button):
    time.sleep(1)
    button.click()
    print('clicked   '  + str(button))



def initial_setup():
    driver_xpath2 = "chromedriver.exe"

    chrome_options = Options.Options()     ### stop text alerts
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(driver_xpath2 ,chrome_options=chrome_options)
    driver.get("https://www.novunacapitalcontrol.co.uk/cc/bs/login.action")
    return driver

def find_e_by_xp3(driver, xp, ):
    print(str(xp) + " bout to click ")
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,xp)))
    element = driver.find_element_by_xpath(xp)
    return element


def find_e_by_xp(driver, xp):
    print(str(xp) + " bout to click ")
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,xp)))
    element = driver.find_element_by_xpath(xp)
    return element
def find_e_by_xp2(driver, xp):
    print(str(xp) + " bout to click ")
    element = driver.find_element_by_xpath(xp)
    return element
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

def log_in(driver , username , password):
    #//*[@id="username"]

   # print(driver.page_source)
    user_b = find_e_by_xp(driver,'//*[@id="username"]')
    user_b.send_keys(username)
    #//*[@id="password"]
    pass_b = find_e_by_xp(driver,'//*[@id="password"]')
    pass_b.send_keys(password)
    # //*[@id="submit"]
    ok_but = find_e_by_xp(driver,'//*[@id="submit"]')
    click(ok_but)
  #//*[@id="btn-ok"]
    ok_but2 = find_e_by_xp(driver,'//*[@id="btn-ok"]')
    click(ok_but2)

def start_new_quote_1(driver):
    #    //*[@id="portlet-associate-quotes"]/div[1]/a/span
    new_quote = find_e_by_xp(driver,'//*[@id="portlet-associate-quotes"]/div[1]/a/span')
    click(new_quote)

#def check_blp(driver, our_blp):
 #   pass
    #if theres only 1 check if it has exact blp

    #if theres more than 1 find if any of them have correct blp

    #else return false
def try_to_move_into_frame(driver):
    try:
        frame_xpath = '//*[@id="framePopup1"]'#    arval button
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,frame_xpath)))
        frame = driver.find_element_by_xpath(frame_xpath)
        driver.switch_to.frame(frame)
    except:
        pass
    finally:
        pass

# //*[@id="capCode"]





def try_1_car_finder(driver, car, dont_try_this = 0):
    print("1ffffffffffffffffffffff")
    make_b = make_finder(car.capcode, driver)
    click(make_b)
    print("bb1")
    time.sleep(20)
    print("bb1")

    model_b = model_finder2(car.model, driver)
    click(model_b)
    print("bb2")
    time.sleep(20)
    print("bb2")
  #  model_b = find_e_by_xp(driver,'//*[@id="modelSelect"]')
   # var_b = find_e_by_xp(driver,'//*[@id="specificationDivId"]/span[2]/input')
    match = check_blp(driver, car.blp)
    if match:
        return match
    else:
        return match, allready_tried

def find_this_car(driver1, car):
    allready_tried = []
    first_try, incorrect_variant = try_1_car_finder(driver1, car)
#    try:
 #       print(" ftc 1 ")
  #      first_try, incorrect_variant = try_1_car_finder(driver1, car)
   #     allready_tried.append(incorrect_variant)
    #except:
     #   print(" ftc 2 ")
      #  first_try = try_1_car_finder(driver1, car)

#    print(" ftc 3")
 #   if first_try == False:
  ##      worked = False
    #    for i in range(5):
     #       print(" counter ")
      #      if worked == False:
       #         try:
        #            worked,incorrect_variant = try_1_car_finder(dont_try_this = allready_tried)
         #           allready_tried.append(incorrect_variant)
          #      except:
           #         worked = try_1_car_finder(dont_try_this = allready_tried)
    #print(" ftc 4 ")


def choose_make(driver , themake):
    make_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[8]/div[3]/select'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,make_xp)))
    make_sel = Select(driver.find_element_by_xpath(make_xp))
    make_sel.select_by_visible_text(themake)

def choose_model(driver , themodel):
    model_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[8]/div[4]/select'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,model_xp)))
    model_sel = Select(driver.find_element_by_xpath(model_xp))
    model_sel.select_by_visible_text(themodel)

    current_opt = model_sel.first_selected_option.text
    opts = model_sel.options


    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while current_opt != themodel:
        if datetime.datetime.now() > future:
            print(1/0)
        model_sel = Select(driver.find_element_by_xpath(model_xp))
        model_sel.select_by_visible_text(themodel)

        current_opt = model_sel.first_selected_option.text

def final_car_check(driver, thederiv, blp):
    time.sleep(1)
    print("final csar check   999999999999999")
    wait_until_done_loading(driver)

    blp_id = 'listPriceSelect'
    WebDriverWait(driver,54).until(EC.presence_of_element_located((By.ID, blp_id)))
    blp_obj = Select(driver.find_element_by_id(blp_id))
    their_blp = blp_obj.first_selected_option.text;
    print(their_blp)
    their_blp_clean = ""
    bracket_found = False
    for char in their_blp:
        if char != "(" and bracket_found == False:
            their_blp_clean += char
            print("char " +str(char))
        else:
            bracket_found = True
    their_blp_clean = their_blp_clean.replace("£","").replace(",","").strip()
    blp = blp.replace("£","").replace(",","").strip()
    print(their_blp_clean)
    print(blp)
    if abs(float(their_blp_clean) - float(blp)) < 1000:
        print("blp match :) ")
        return True
    else:
        print(" blp mismatch ")
        return False




def choose_deriv(driver , thederiv, our_blp , round_try):
    deriv_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[9]/div[1]/span[2]/input'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,deriv_xp)))
    deriv_sel = driver.find_element_by_xpath(deriv_xp)

    deriv_arrow_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[9]/div[1]/span[2]/a'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,deriv_arrow_xp)))
    deriv_arrow = driver.find_element_by_xpath(deriv_arrow_xp)

    deriv_class = 'ui-helper-hidden-accessible'



    times_tried = 0
    deriv_sorted = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 70)
    while(not deriv_sorted):
        if datetime.datetime.now() > future:
            print(1/0)
        print("that loop")
        times_tried+= 1
        if times_tried > 5:
            print(1/0)
        delete(deriv_sel)
        delete(deriv_sel)
        delete(deriv_sel)
        delete(deriv_sel)
        delete(deriv_sel)
        delete(deriv_sel)
#        click(deriv_arrow)
        time.sleep(1)
        wait_until_done_loading(driver)
      #  deriv_sel.send_keys(Keys.BACK_SPACE)
        print("type")

        deriv_sel.send_keys(thederiv.strip())
        time.sleep(1)
        wait_until_done_loading(driver)
        print("delete")
     #   deriv_sel.send_keys(Keys.ENTER)
        print("  deriv   sel    ")
      #  deriv_sel.send_keys(Keys.ENTER)
        print("  deriv   sel    ")
        time.sleep(1)
        wait_until_done_loading(driver)
        print("aft")
       # print(driver.page_source)
        click(deriv_arrow)
        print("aft")
     #   print(driver.page_source)
        still_looking_for_xp = True
        conseq_miss_bool = False
        conseq_miss = 0
        for i in range(80):
            if conseq_miss > 5:
                for i in range(5):
                    print("conseq miss ")
                conseq_miss_bool = True
            if still_looking_for_xp == True and conseq_miss_bool == False:
                print("opt searcher")
                try:
                    if i == 0:
                        p_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[9]/div[1]/ul/li/a'
                    else:
                        p_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[9]/div[1]/ul/li['+str(i)+']/a'

                    try:
                        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,p_xp)))
                        object1 = driver.find_element_by_xpath(p_xp)
                        tobject1 = object1.get_attribute('innerHTML')
                        print("fin for  "+ str(i))
                    except:
                        print("failed but trying again with " +str(i))
                        click(deriv_arrow)
                        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,p_xp)))
                        object1 = driver.find_element_by_xpath(p_xp)
                        tobject1 = object1.get_attribute('innerHTML')

                    if len(tobject1)< 2:
                        print("   this isnt a deriv   ")



                    tobject1 = tobject1.replace("</strong>","").replace("<strong>","")
                    print(" tobject we go was " +str(tobject1))                    ######### <strip tags
                    #time.sleep(7)
                    char_to_remove = "none"
                    double_zero = False
                    for char in range(len(tobject1)):
                        if tobject1[char] == "(":
                            if tobject1[char+1] == "£":
                                decimal_found = False
                                decimal_extra = 0
                                extra_counter = 0
                                for extra_counter in range(9):
                                    if tobject1[char+extra_counter] == ".":
                                        print("got decimal")
                                        if tobject1[char+extra_counter+1].isdigit():
                                            if tobject1[char+extra_counter+2] == "0":
                                                if tobject1[char+extra_counter+3]==")":
                                                    print("unnecesary 0")
                                                    if tobject1[char+extra_counter+1] == "0":
                                                        double_zero = True
                                                    char_to_remove = char+extra_counter+2
                    print(str(tobject1)+"   this is it after the thing     xxxxx ")
                    tobject5 = ""
                    text = tobject1


                    if not double_zero:
                        print('og_text   ' +str(text))
                        text25 = ""
                        if char_to_remove != "none":
                            for char in range(len(text)):
                                if char!= char_to_remove:
                                    text25 = text25 +text[char]
                            text = text25
                        print('og_text   ' +str(text))
                        tobject1 = text
                    else:
                        tobject1 = tobject1.replace(".00","")






                    print(tobject1 + "  this is it after the thing     xxxxx end ")
                    tobject1 = tobject1.replace(" ","")
                    thederiv = thederiv.replace(" ","")
                    if tobject1 == thederiv.strip():
                        for j in range(20):
                            print(j)
                        still_looking_for_xp = p_xp
                        best_object = object1

                    else:
                        print("dun mat")
                        print(tobject1)
                        print(thederiv.strip())
                        print("dun mat")
                #        else:
                 #           print("^^^^^^^^^^^")
                  #          print(tobject1)
                   #         print(thederiv.strip())
                    #        print("##########")
        #
                except:
                    print("problem xxxxx")
                    conseq_miss+=1
                    print(p_xp)

        else:
            print("done looking ")
        if still_looking_for_xp != True:
            click(best_object)
            print("yaaaaaaaaaaaaaaaaaaaaaaaay click")

   #     deriv_sel.send_keys(Keys.ENTER)
        print("yaaaaaaaaaaaaaaaaaaaaaaaay")
        time.sleep(1)
        wait_until_done_loading(driver)

        deriv_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[9]/div[1]/span[2]/input'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,deriv_xp)))

        the_opt_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[9]/div[1]/ul/li[41]/a'


        text = driver.find_element_by_xpath(deriv_xp).get_attribute("title")
        text2 = driver.find_element_by_xpath(deriv_xp).get_attribute("innerHTML")


        calender_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[10]/div[5]/img'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,calender_xp)))
        cal = driver.find_element_by_xpath(calender_xp)
        click(cal)

        date_xp = '/html/body/div[5]/table/tbody/tr[4]/td[7]/a'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,date_xp)))
        date = driver.find_element_by_xpath(date_xp)
        click(date)
        text2 = driver.find_element_by_xpath(deriv_xp).get_attribute("innerHTML")
        text = driver.find_element_by_xpath(deriv_xp).get_attribute("title")
 #       while len(text.strip()) < 5 and len(text2.strip()) < 5:
  #          print("len loop 1")
   #         text = driver.find_element_by_xpath(deriv_xp).get_attribute("title")
    #        print(text)
     #       print("len loop 2")
      #      text2 = driver.find_element_by_xpath(deriv_xp).get_attribute("innerHTML")
       #     print(text2)

####################################################  remove zeroes from theirs below
        char_to_remove = "none"
        double_zero = False
        for char in range(len(text)):
            if text[char] == "(":
                if text[char+1] == "£":
                    decimal_found = False
                    decimal_extra = 0
                    extra_counter = 0
                    for extra_counter in range(9):
                        print(text[char+extra_counter])
                        if text[char+extra_counter] == ".":
                            print("got decimal")
                            if text[char+extra_counter+1].isdigit():
                                if text[char+extra_counter+2] == "0":
                                    if text[char+extra_counter+3]==")":
                                        print("unnecesary 0")
                                        if text[char+extra_counter+1] == "0":
                                            double_zero = True
                                        char_to_remove = char+extra_counter+2
        print(str(text)+"   this is it after the thing     xxxxx ")
        if double_zero == False:
            print("prf 1")
            text25 = ""
            if char_to_remove != "none":
                print("prf 2")
                for char in range(len(text)):
                    print("prf 3")
                    if char!= char_to_remove:
                        text25 = text25 +text[char]
                text = text25
        else:
            text = text.replace(".00","")
        print('after zeroes dealt with =====================================    ' +str(text))
        text_theirs = text.replace(".00","")



####################################################  remove zeroes from the deriv
        char_to_remove = "none"
        double_zero = False
        our_deriv = thederiv
        for char in range(len(our_deriv)):
            if our_deriv[char] == "(":
                if our_deriv[char+1] == "£":
                    decimal_found = False
                    decimal_extra = 0
                    extra_counter = 0
                    for extra_counter in range(9):
                        if our_deriv[char+extra_counter] == ".":
                            print("got decimal")
                            if our_deriv[char+extra_counter+1].isdigit():
                                if our_deriv[char+extra_counter+2] == "0":
                                    if our_deriv[char+extra_counter+3]==")":
                                        print("unnecesary 0")
                                        if our_deriv[char+extra_counter+1] == "0":
                                            double_zero = True
                                        char_to_remove = char+extra_counter+2
        print(str(our_deriv)+"   this is it after the thing     xxxxx ")
        if double_zero == False:
            print("prf 1")
            text25 = ""
            if char_to_remove != "none":
                print("prf 2")
                for char in range(len(our_deriv)):
                    print("prf 3")
                    if char!= char_to_remove:
                        text25 = text25 +our_deriv[char]
                thederiv = text25
        else:
            thederiv=thederiv.replace(".00","")
        print('after zeroes dealt our deriv with =====================================    ' +str(thederiv))



        text = text_theirs
        text = text.replace(" ","")
        thederiv = thederiv.replace(" ","")
        if text.strip() == thederiv.strip() or text2.strip() == thederiv.strip():
            print("actual match")
            deriv_sorted = True

        else:
            print("nope ddd 1")
            print(text)
            print(text2)
            print(thederiv)
            print("nope ddd 2")

        print("eeeeeeeeeeeeeeeee ")
#        time.sleep(60)

    print("well were bloody gere ")
    time.sleep(10)
    if round_try % 2 == 0:
        print("  options chooser  ")
        worked = options_chooser(driver)
    else:
 #   try:
        def_quote_id = 'btDefaultQuote'
        def_q = driver.find_element_by_id(def_quote_id)
        click(def_q)
        worked = True

  #  except:
#    worked = options_chooser(driver)

    print("well were bloody gere ")
    print("endy end ")
    time.sleep(1)

    wait_until_done_loading(driver)


    if worked == True:

        return final_car_check(driver , thederiv, our_blp)

    else:
        return False


def sort_init_terms(driver , van):
    wait_until_done_loading(driver)
    months_sel_id = 'termSelect'
    months = Select(driver.find_element_by_id(months_sel_id))
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while months.first_selected_option.text != '24':
        months.select_by_visible_text('24')
        if datetime.datetime.now() > future:
            print(1/0)

    terms_inp_id = 'milesPerAnum'
    terms = driver.find_element_by_id(terms_inp_id)
    if van == False:
        tstamp1 = datetime.datetime.now()
        future = tstamp1 +  datetime.timedelta(seconds = 130)
        while terms.get_attribute('value') != '8000' and terms.get_attribute('value') != '8,000':
            if datetime.datetime.now() > future:
                print(1/0)
            delete(terms)
            terms.send_keys('8000')
            print(terms.get_attribute('value'))
    else:
        tstamp1 = datetime.datetime.now()
        future = tstamp1 +  datetime.timedelta(seconds = 130)
        while terms.get_attribute('value') != '10000' and terms.get_attribute('value') != '10,000':
            if datetime.datetime.now() > future:
                print(1/0)
            delete(terms)
            terms.send_keys('10000')
            print(terms.get_attribute('value'))

    print(" init breadcrum    =========================   PPPPPPP ")
    months_up_sel_id = 'paymentsSelect'
    months_up = Select(driver.find_element_by_id(months_up_sel_id))
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)

    while months_up.first_selected_option.text != '24 months 03 in advance followed by 23' and months_up.first_selected_option.text != '24 months 3 in advance followed by 23':
        if datetime.datetime.now() > future:
            print(1/0)
        months_up = Select(driver.find_element_by_id(months_up_sel_id))
        try:
            months_up.select_by_visible_text('24 months 03 in advance followed by 23')
        except:
            months_up.select_by_visible_text('24 months 3 in advance followed by 23')

    wait_until_done_loading(driver)
    time.sleep(1)
    calc_id = 'btCalculate'
    calc = driver.find_element_by_id(calc_id)
    click(calc)
    time.sleep(1)
    wait_until_done_loading(driver)
    months_sel_id = 'termSelect'
    months = Select(driver.find_element_by_id(months_sel_id))
    print(" init breadcrum    =========================   PPPPPPP  2")
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while months.first_selected_option.text != '24':
        months.select_by_visible_text('24')
        if datetime.datetime.now() > future:
            print(1/0)

    terms_inp_id = 'milesPerAnum'
    terms = driver.find_element_by_id(terms_inp_id)
    if van == False:
        tstamp1 = datetime.datetime.now()
        future = tstamp1 +  datetime.timedelta(seconds = 130)
        while terms.get_attribute('value') != '8000' and terms.get_attribute('value') != '8,000':
            if datetime.datetime.now() > future:
                print(1/0)
            delete(terms)
            terms.send_keys('8000')
            print(terms.get_attribute('value'))
    else:
        tstamp1 = datetime.datetime.now()
        future = tstamp1 +  datetime.timedelta(seconds = 130)
        while terms.get_attribute('value') != '10000' and terms.get_attribute('value') != '10,000':
            if datetime.datetime.now() > future:
                print(1/0)
            delete(terms)
            terms.send_keys('10000')
            print(terms.get_attribute('value'))


    print(" init breadcrum    =========================   PPPPPPP 3")
    months_up_sel_id = 'paymentsSelect'
    months_up = Select(driver.find_element_by_id(months_up_sel_id))
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while months_up.first_selected_option.text != '24 months 03 in advance followed by 23' and months_up.first_selected_option.text != '24 months 3 in advance followed by 23':
        if datetime.datetime.now() > future:
            print(1/0)
        months_up = Select(driver.find_element_by_id(months_up_sel_id))
        try:
            months_up.select_by_visible_text('24 months 03 in advance followed by 23')
        except:
            months_up.select_by_visible_text('24 months 3 in advance followed by 23')
    print(" init breadcrum    =========================   PPPPPPP 4")

def wait_until_done_loading(driver):
    loading_id = 'divShadow'
    load1 = driver.find_element_by_id(loading_id).get_attribute("style")
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while 'block' in load1.lower():
        if datetime.datetime.now() > future:
            print(1/0)
        load1 = driver.find_element_by_id(loading_id).get_attribute("style")
        print("loading")
    print(load1)


def remove_zero_from_months_up(the_months_up):

    the_months_up=the_months_up.replace("03" , "3")
    the_months_up=the_months_up.replace("06" , "6")
    the_months_up=the_months_up.replace("09" , "9")
    return the_months_up

def enter_otr(driver , otr):
    wait_until_done_loading(driver)
    otr_inp_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[10]/div[6]/input'
    otr_inp_id = 'associateOTRP'
    try:
        otr_inp = driver.find_element_by_id(otr_inp_id)
        delete(otr_inp)
        otr_inp.send_keys(otr)
    except:
        wait_until_done_loading(driver)
        calc_id = 'btCalculate'
        calc = driver.find_element_by_id(calc_id)
        click(calc)
        time.sleep(1)
        wait_until_done_loading(driver)
        otr_inp = driver.find_element_by_id(otr_inp_id)
        delete(otr_inp)
        otr_inp.send_keys(otr)
    pass

def save_this_quote(driver):



    qnt = ""
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    times_tried = 0
    while len(qnt)<3:
        times_tried +=1
        if times_tried > 4:
            terms_inp_id = 'milesPerAnum'
            terms = driver.find_element_by_id(terms_inp_id)
            delete(terms)
            terms.send_keys("8000")
            calc_id = 'btCalculate'
            calc = driver.find_element_by_id(calc_id)
            click(calc)
            time.sleep(1)
            wait_until_done_loading(driver)
            delete(terms)
            terms.send_keys("10000")
            calc_id = 'btCalculate'
            calc = driver.find_element_by_id(calc_id)
            click(calc)
            time.sleep(1)
            wait_until_done_loading(driver)
            if check_van(driver):
                terms_inp_id = 'milesPerAnum'
                terms = driver.find_element_by_id(terms_inp_id)
                delete(terms)
                terms.send_keys("10000")
                calc_id = 'btCalculate'
                calc = driver.find_element_by_id(calc_id)
                click(calc)
                time.sleep(1)
                wait_until_done_loading(driver)


        if datetime.datetime.now() > future:
            print(1/0)
        save_id = 'btSave'
        save = driver.find_element_by_id(save_id)
        click(save)
        time.sleep(1)
        wait_until_done_loading(driver)
        time.sleep(1)
        qn_id = 'driverQuoteNo'
        qn = driver.find_element_by_id(qn_id)
        qnt = qn.get_attribute("value")
        print(qnt)
        qnth = qn.get_attribute("innerHTML")
        print(qnth)

#    print(1/0)
    return qn.get_attribute("value")

def get_prices(driver , van, theblp):
    last_price = 0
    prices = []
    if not van:
        for maint in range(2):
            for mile in range(7):
                for month in range(3):
                    if not (mile == 6 and month == 2):

                      #  time.sleep(6)
                        dismiss_warning_pop_up(driver)
                        the_months = 'not_set'
                        if month == 0:
                            the_months = "24"
                            the_months_up = '24 months 03 in advance followed by 23'
                        if month == 1:
                            the_months = "36"
                            the_months_up = '36 months 03 in advance followed by 35'
                        if month == 2:
                            the_months = "48"
                            the_months_up = '48 months 03 in advance followed by 47'
                        the_months_up_og = the_months_up

                        the_miles = 'not_set'
                        if mile == 0:
                            the_miles = "5000"
                        if mile == 1:
                            the_miles = "8000"
                        if mile == 2:
                            the_miles = "10000"
                        if mile == 3:
                            the_miles = "15000"
                        if mile == 4:
                            the_miles = "20000"
                        if mile == 5:
                            the_miles = "25000"
                        if mile == 6:
                            the_miles = "30000"

                        if maint == 0:
                            the_maint = 'Associate CH no maint - PLG'
                        if maint == 1:
                            the_maint = 'Associate CH with maint - PLG'


                        wait_until_done_loading(driver)
                        months_sel_id = 'termSelect'
                        months = Select(driver.find_element_by_id(months_sel_id))

                        tstamp1 = datetime.datetime.now()
                        future = tstamp1 +  datetime.timedelta(seconds = 130)

                        time.sleep(0.5)
                        while months.first_selected_option.text != the_months:
                            if datetime.datetime.now() > future:
                                print(1/0)
                            months.select_by_visible_text(the_months)
                        wait_until_done_loading(driver)
                        time.sleep(0.5)

                        months_up_sel_id = 'paymentsSelect'
                        months_up = Select(driver.find_element_by_id(months_up_sel_id))

                        tstamp1 = datetime.datetime.now()
                        future = tstamp1 +  datetime.timedelta(seconds = 130)
                        attempts = 0
                        while months_up.first_selected_option.text != the_months_up:
                            attempts+= 1
                            if attempts % 2 == 0:
                                the_months_up=remove_zero_from_months_up(the_months_up_og)
                            if attempts % 5 == 0:
                                the_months_up=the_months_up_og

                            if datetime.datetime.now() > future:
                                print(1/0)
                            try:
                                months_up = Select(driver.find_element_by_id(months_up_sel_id))
                                months_up.select_by_visible_text(the_months_up)
                            except:
                                print("months up fail  "+str(the_months_up))
                                months_up_sel_id = 'paymentsSelect'
                                months_up = Select(driver.find_element_by_id(months_up_sel_id))

                        terms_inp_id = 'milesPerAnum'
                        terms = driver.find_element_by_id(terms_inp_id)

                        tstamp1 = datetime.datetime.now()
                        future = tstamp1 +  datetime.timedelta(seconds = 130)


                        while str(terms.get_attribute('value')).replace(",","") != the_miles:
                            if datetime.datetime.now() > future:
                                print(1/0)
                            delete(terms)
                            terms.send_keys(the_miles)
                            print(terms.get_attribute('value'))
                        wait_until_done_loading(driver)
                        time.sleep(1)


                        prod_id = 'productSelect'
                        product_sel = Select(driver.find_element_by_id(prod_id))

                        tstamp1 = datetime.datetime.now()
                        future = tstamp1 +  datetime.timedelta(seconds = 130)

                        while product_sel.first_selected_option.text != the_maint:
                            if datetime.datetime.now() > future:
                                print(1/0)
                            product_sel.select_by_visible_text(the_maint)

                        wait_until_done_loading(driver)
                        time.sleep(1)
                        calc_id = 'btCalculate'
                        calc = driver.find_element_by_id(calc_id)
                        click(calc)
                        time.sleep(1)
                        wait_until_done_loading(driver)
                        dismiss_warning_pop_up(driver)
                        wait_until_done_loading(driver)
                        months_sel_id = 'termSelect'
                        months = Select(driver.find_element_by_id(months_sel_id))
                        tstamp1 = datetime.datetime.now()
                        future = tstamp1 +  datetime.timedelta(seconds = 130)
                        while months.first_selected_option.text != the_months:
                            if datetime.datetime.now() > future:
                                print(1/0)
                            months.select_by_visible_text(the_months)
                        wait_until_done_loading(driver)
                #        time.sleep(1)

                        months_up_sel_id = 'paymentsSelect'
                        months_up = Select(driver.find_element_by_id(months_up_sel_id))
                        attempts = 0
                        while months_up.first_selected_option.text != the_months_up:
                            attempts+=1
                            if datetime.datetime.now() > future:
                                print(1/0)
                            if attempts % 2 == 0:
                                the_months_up=remove_zero_from_months_up(the_months_up_og)
                            if attempts % 5 == 0:
                                the_months_up=the_months_up_og
                            try:
                                months_up = Select(driver.find_element_by_id(months_up_sel_id))
                                months_up.select_by_visible_text(the_months_up)
                            except:
                                print("bummmmmmm      no months up selled ")

                        terms_inp_id = 'milesPerAnum'
                        terms = driver.find_element_by_id(terms_inp_id)
                        tstamp1 = datetime.datetime.now()
                        future = tstamp1 +  datetime.timedelta(seconds = 130)
                        while str(terms.get_attribute('value')).replace(",","") != the_miles:
                            if datetime.datetime.now() > future:
                                print(1/0)

                            delete(terms)
                            terms.send_keys(the_miles)
                            print(terms.get_attribute('value'))
                        wait_until_done_loading(driver)
                 #       time.sleep(1)


                        prod_id = 'productSelect'
                        product_sel = Select(driver.find_element_by_id(prod_id))
                        tstamp1 = datetime.datetime.now()
                        future = tstamp1 +  datetime.timedelta(seconds = 130)
                        while product_sel.first_selected_option.text != the_maint:
                            if datetime.datetime.now() > future:
                                print(1/0)

                            product_sel.select_by_visible_text(the_maint)

                        wait_until_done_loading(driver)
                     #   time.sleep(1)
                        dismiss_warning_pop_up(driver)
                        calc_id = 'btCalculate'
                        calc = driver.find_element_by_id(calc_id)
                        click(calc)
                        time.sleep(1)
                        wait_until_done_loading(driver)
                        dismiss_warning_pop_up(driver)
                        monthly_price_id = 'driverQuoteTotalMonthlyCost'
                        price = driver.find_element_by_id(monthly_price_id).get_attribute("innerHTML")
                        print(str(price)+"           price ")

                        if the_miles == "30000" and the_months == "48":
                            price = " nope  cant have over 100k total miles "

                        zeros_count = 0
                        tstamp9 = datetime.datetime.now()
                        future9 = tstamp9 +  datetime.timedelta(seconds = 130)
                        while '£0.00' in price  or ('£100.00' in price and month == 0 and maint == 1 and mile == 0):
                            zeros_count+=1
                            if zeros_count % 2 == 0:
                                wait_until_done_loading(driver)
                                delete(terms)
                                terms.send_keys('25000')
                                wait_until_done_loading(driver)
                                monthly_price_id = 'driverQuoteTotalMonthlyCost'
                                price = driver.find_element_by_id(monthly_price_id).get_attribute("innerHTML")
                                print(str(price)+"           price ")
                                calc = driver.find_element_by_id(calc_id)
                                click(calc)
                                time.sleep(1)
                                wait_until_done_loading(driver)

    ####################
                            if datetime.datetime.now() > future9:
                                    print(1/0)

                            print("00")
                            wait_until_done_loading(driver)
                            months_sel_id = 'termSelect'
                            months = Select(driver.find_element_by_id(months_sel_id))

                            tstamp1 = datetime.datetime.now()
                            future = tstamp1 +  datetime.timedelta(seconds = 130)

                            while months.first_selected_option.text != the_months:
                                if datetime.datetime.now() > future:
                                    print(1/0)
                                try:
                                    months.select_by_visible_text(the_months)
                                except:
                                    print("0  AAAAAAAAAA   0")
                            wait_until_done_loading(driver)
                            time.sleep(1)
                            print("00 a")

                            months_up_sel_id = 'paymentsSelect'
                            months_up = Select(driver.find_element_by_id(months_up_sel_id))

                            tstamp1 = datetime.datetime.now()
                            attempts = 0
                            future = tstamp1 +  datetime.timedelta(seconds = 130)
                            while months_up.first_selected_option.text != the_months_up:
                                attempts += 1
                                if datetime.datetime.now() > future:
                                    print(1/0)
                                if attempts % 2 == 0:
                                    the_months_up=remove_zero_from_months_up(the_months_up_og)
                                if attempts % 5 == 0:
                                    the_months_up=the_months_up_og

                                try:
                                    months_up = Select(driver.find_element_by_id(months_up_sel_id))
                                    months_up.select_by_visible_text(the_months_up)
                                except:
                                    print("months up fail   666  = " +str(the_months_up))
                                    months_up_sel_id = 'paymentsSelect'
                                    months_up = Select(driver.find_element_by_id(months_up_sel_id))
                            print("00 c")
                            terms_inp_id = 'milesPerAnum'
                            terms = driver.find_element_by_id(terms_inp_id)

                            tstamp1 = datetime.datetime.now()
                            future = tstamp1 +  datetime.timedelta(seconds = 130)
                            print("00 d")

                            while str(terms.get_attribute('value')).replace(",","") != the_miles:
                                if datetime.datetime.now() > future:
                                    print(1/0)
                                delete(terms)
                                terms.send_keys(the_miles)
                                print(terms.get_attribute('value'))
                            wait_until_done_loading(driver)
                            time.sleep(1)

                            print("00 e")

                            calc = driver.find_element_by_id(calc_id)
                            click(calc)
                            time.sleep(1)
                            wait_until_done_loading(driver)
                            price = driver.find_element_by_id(monthly_price_id).get_attribute("innerHTML")

                            calc = driver.find_element_by_id(calc_id)
                            click(calc)
                            time.sleep(1)
                            wait_until_done_loading(driver)
                            price = driver.find_element_by_id(monthly_price_id).get_attribute("innerHTML")

                        price = driver.find_element_by_id(monthly_price_id).get_attribute("innerHTML")
                        print("the actual price collected = " +str(price))
                        prices.append(price)
                            ####################








                        print(str(price)+"           price ")
                        if last_price == price:
                            print(1/0)
                        else:
                           last_price = price#

                        worked = False
                        while not worked:
                            worked = final_car_check(driver, 'unnecasary', theblp)

                        if month == 0 and maint == 0 and mile == 0:
                            quote_num = save_this_quote(driver)
                    ##    if month == 0 and maint == 1 and mile == 0:
                     #       time.sleep(999999)

    else:
        for maint in range(2):
            for mile in range(5):
                for month in range(3):
                    the_months = 'not_set'
                    if month == 0:
                        the_months = "24"
                        the_months_up = '24 months 03 in advance followed by 23'
                    if month == 1:
                        the_months = "36"
                        the_months_up = '36 months 03 in advance followed by 35'
                    if month == 2:
                        the_months = "48"
                        the_months_up = '48 months 03 in advance followed by 47'

                    the_miles = 'not_set'
             #       if mile == 0:
              #          the_miles = "5000"
               #     if mile == 1:
                #        the_miles = "8000"
                    if mile == 0:
                        the_miles = "10000"
                    if mile == 1:
                        the_miles = "15000"
                    if mile == 2:
                        the_miles = "20000"
                    if mile == 3:
                        the_miles = "25000"
                    if mile == 4:
                        the_miles = "30000"

                    if maint == 0:
                        the_maint = 'Associate Regulated CH no maint - LCV'
                    if maint == 1:
                        the_maint = 'Associate Regulated CH maint - LCV'


                    wait_until_done_loading(driver)
                    months_sel_id = 'termSelect'
                    months = Select(driver.find_element_by_id(months_sel_id))
                    tstamp1 = datetime.datetime.now()
                    future = tstamp1 +  datetime.timedelta(seconds = 130)
                    while months.first_selected_option.text != the_months:
                        if datetime.datetime.now() > future:
                            print(1/0)
                        months.select_by_visible_text(the_months)
                    wait_until_done_loading(driver)
                    time.sleep(1)

                    months_up_sel_id = 'paymentsSelect'
                    months_up = Select(driver.find_element_by_id(months_up_sel_id))
                    tstamp1 = datetime.datetime.now()
                    attempts = 0
                    future = tstamp1 +  datetime.timedelta(seconds = 130)
                    while months_up.first_selected_option.text != the_months_up:
                        attempts += 1
                        if datetime.datetime.now() > future:
                            print(1/0)
                        if attempts % 2 == 0:
                            the_months_up=remove_zero_from_months_up(the_months_up_og)
                        if attempts % 5 == 0:
                            the_months_up=the_months_up_og
                        try:
                            months_up = Select(driver.find_element_by_id(months_up_sel_id))
                            months_up.select_by_visible_text(the_months_up)
                        except:
                            print("months up fail 777 "+str(the_months_up))
                            months_up_sel_id = 'paymentsSelect'
                            months_up = Select(driver.find_element_by_id(months_up_sel_id))

                    terms_inp_id = 'milesPerAnum'
                    terms = driver.find_element_by_id(terms_inp_id)
                    tstamp1 = datetime.datetime.now()
                    future = tstamp1 +  datetime.timedelta(seconds = 130)
                    while str(terms.get_attribute('value')).replace(",","") != the_miles:
                        if datetime.datetime.now() > future:
                            print(1/0)
                        delete(terms)
                        terms.send_keys(the_miles)
                        print(terms.get_attribute('value'))
                    wait_until_done_loading(driver)
                    time.sleep(1)


                    prod_id = 'productSelect'
                    product_sel = Select(driver.find_element_by_id(prod_id))
                    tstamp1 = datetime.datetime.now()
                    future = tstamp1 +  datetime.timedelta(seconds = 130)
                    while product_sel.first_selected_option.text != the_maint:
                        if datetime.datetime.now() > future:
                            print(1/0)
                        product_sel.select_by_visible_text(the_maint)

                    wait_until_done_loading(driver)
                    time.sleep(1)
                    calc_id = 'btCalculate'
                    calc = driver.find_element_by_id(calc_id)
                    click(calc)
                    time.sleep(1)
                    wait_until_done_loading(driver)

                    wait_until_done_loading(driver)
                    months_sel_id = 'termSelect'
                    months = Select(driver.find_element_by_id(months_sel_id))
                    tstamp1 = datetime.datetime.now()
                    future = tstamp1 +  datetime.timedelta(seconds = 130)
                    while months.first_selected_option.text != the_months:
                        if datetime.datetime.now() > future:
                            print(1/0)
                        months.select_by_visible_text(the_months)
                    wait_until_done_loading(driver)
            #        time.sleep(1)

                    months_up_sel_id = 'paymentsSelect'
                    months_up = Select(driver.find_element_by_id(months_up_sel_id))
                    tstamp1 = datetime.datetime.now()
                    future = tstamp1 +  datetime.timedelta(seconds = 130)
                    attempts = 0
                    while months_up.first_selected_option.text != the_months_up:
                        attempts+=1
                        if datetime.datetime.now() > future:
                            print(1/0)
                        if attempts % 2 == 0:
                            the_months_up=remove_zero_from_months_up(the_months_up_og)
                        if attempts % 5 == 0:
                            the_months_up=the_months_up_og
                        months_up = Select(driver.find_element_by_id(months_up_sel_id))
                        months_up.select_by_visible_text(the_months_up)


                    terms_inp_id = 'milesPerAnum'
                    terms = driver.find_element_by_id(terms_inp_id)
                    tstamp1 = datetime.datetime.now()
                    future = tstamp1 +  datetime.timedelta(seconds = 130)
                    while str(terms.get_attribute('value')).replace(",","") != the_miles:
                        if datetime.datetime.now() > future:
                            print(1/0)
                        delete(terms)
                        terms.send_keys(the_miles)
                        print(terms.get_attribute('value'))
                    wait_until_done_loading(driver)
             #       time.sleep(1)


                    prod_id = 'productSelect'
                    product_sel = Select(driver.find_element_by_id(prod_id))
                    tstamp1 = datetime.datetime.now()
                    future = tstamp1 +  datetime.timedelta(seconds = 130)
                    while product_sel.first_selected_option.text != the_maint:
                        if datetime.datetime.now() > future:
                            print(1/0)
                        product_sel.select_by_visible_text(the_maint)

                    wait_until_done_loading(driver)
                 #   time.sleep(1)
                    calc_id = 'btCalculate'
                    calc = driver.find_element_by_id(calc_id)
                    click(calc)
                    time.sleep(1)
                    wait_until_done_loading(driver)


                    wait_until_done_loading(driver)
                 #   time.sleep(1)
                    calc_id = 'btCalculate'
                    calc = driver.find_element_by_id(calc_id)
                    click(calc)
                    time.sleep(1)
                    wait_until_done_loading(driver)

                    monthly_price_id = 'driverQuoteTotalMonthlyCost'
                    price = driver.find_element_by_id(monthly_price_id).get_attribute("innerHTML")
                    print(str(price)+"           price ")

                    if the_miles == "30000" and the_months == "48":
                        price = " nope  cant have over 100k total miles "



                    zeros_count = 0
                    tstamp9 = datetime.datetime.now()
                    future9 = tstamp9 +  datetime.timedelta(seconds = 130)
                    while '£0.00' in price or '£100.00' in price:
                        zeros_count+=1
                        if zeros_count % 2 == 0:
                            wait_until_done_loading(driver)
                            delete(terms)
                            terms.send_keys('25000')
                            wait_until_done_loading(driver)
                            monthly_price_id = 'driverQuoteTotalMonthlyCost'
                            price = driver.find_element_by_id(monthly_price_id).get_attribute("innerHTML")
                            print(str(price)+"           price ")
                            calc = driver.find_element_by_id(calc_id)
                            click(calc)
                            time.sleep(1)
                            wait_until_done_loading(driver)
                        if datetime.datetime.now() > future9:
                                print(1/0)
                                print("00")
                        wait_until_done_loading(driver)
                        months_sel_id = 'termSelect'
                        months = Select(driver.find_element_by_id(months_sel_id))

                        tstamp1 = datetime.datetime.now()
                        future = tstamp1 +  datetime.timedelta(seconds = 130)

                        while months.first_selected_option.text != the_months:
                            if datetime.datetime.now() > future:
                                print(1/0)
                            months.select_by_visible_text(the_months)
                        wait_until_done_loading(driver)
                        time.sleep(1)
                        print("00 a")

                        months_up_sel_id = 'paymentsSelect'
                        months_up = Select(driver.find_element_by_id(months_up_sel_id))

                        tstamp1 = datetime.datetime.now()
                        future = tstamp1 +  datetime.timedelta(seconds = 130)
                        print("00 b")
                        attempts = 0
                        future = tstamp1 +  datetime.timedelta(seconds = 130)
                        while months_up.first_selected_option.text != the_months_up:
                            attempts += 1
                            if datetime.datetime.now() > future:
                                print(1/0)
                            if attempts % 2 == 0:
                                the_months_up=remove_zero_from_months_up(the_months_up_og)
                            if attempts % 5 == 0:
                                the_months_up=the_months_up_og
                            try:
                                months_up = Select(driver.find_element_by_id(months_up_sel_id))
                                months_up.select_by_visible_text(the_months_up)
                            except:
                                print("months up fail 111     its not "+strthe_months_up())
                                months_up_sel_id = 'paymentsSelect'
                                months_up = Select(driver.find_element_by_id(months_up_sel_id))
                        print("00 c")
                        terms_inp_id = 'milesPerAnum'
                        terms = driver.find_element_by_id(terms_inp_id)

                        tstamp1 = datetime.datetime.now()
                        future = tstamp1 +  datetime.timedelta(seconds = 130)
                        print("00 d")

                        while str(terms.get_attribute('value')).replace(",","") != the_miles:
                            if datetime.datetime.now() > future:
                                print(1/0)
                            delete(terms)
                            terms.send_keys(the_miles)
                            print(terms.get_attribute('value'))

                        wait_until_done_loading(driver)
                        time.sleep(1)

                        print("00 e")

                        calc = driver.find_element_by_id(calc_id)
                        click(calc)
                        time.sleep(1)
                        wait_until_done_loading(driver)
                        price = driver.find_element_by_id(monthly_price_id).get_attribute("innerHTML")

                    monthly_price_id = 'driverQuoteTotalMonthlyCost'
                    price = driver.find_element_by_id(monthly_price_id).get_attribute("innerHTML")
                    print(str(price)+"           price ")
                    prices.append(price)




                    print(str(price)+"           price ")
                    if last_price == price:
                        print(1/0)
                    else:
                       last_price = price#

                    worked = False
                    while not worked:
                        worked = final_car_check(driver, 'unnecasary', theblp)

                    if month == 0 and maint == 0 and mile == 0:
                        quote_num = save_this_quote(driver)



    print("   hhhggghhh   ")
    for p in prices:
        print(p)
   # print(quote_num)
    print("   hhhggghhh  2   ")#
   # time.sleep(9999)
    return prices , quote_num

def options_chooser(driver):

    option_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[11]/div[1]/input'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,option_xp)))
    option_button  = driver.find_element_by_xpath(option_xp)
    click(option_button)
    print("bzr 1")
    time.sleep(1)
    wait_until_done_loading(driver)
    time.sleep(1)
    wait_until_done_loading(driver)
    good_elems = []
    print("bzr 2")
   # external_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]'
  #  internal_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]/div[15]'
   # standard_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]/div[28]'
 #   options_window_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]'
#                          /html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]
  #  WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,external_xp)))
#    external_window  = driver.find_elements_by_xpath(external_xp)
 #   WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,external_xp)))
 #   external_window  = driver.find_elements_by_xpath(external_xp)

#    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,options_window_xp)))
    print("bzr 3")
    print("looking for elems 2 ")
    options_window  = driver.find_elements_by_xpath('/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]')
    print("looking for elems")
 #   print(options_window.get_attribute('innerHTML'))
    stop_yet  = False
    internal_sorted = False
    external_done_yet = False
    internal_done_yet = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not external_done_yet and not internal_done_yet:
        if datetime.datetime.now() > future:
            print(1/0)
        for extras in range(2):
            time.sleep(1)
            wait_until_done_loading(driver)
            time.sleep(1)
            wait_until_done_loading(driver)
            print(extras)
            this_extra_got = False

            for web_elem in options_window:
                print("1")
                if not this_extra_got:
                    print("bzr 4")
                    more_elems = web_elem.find_elements_by_class_name('associate-option-item-name-container')
                    print("bzr 4 a ")
                    print(web_elem.get_attribute('innerHTML'))
                    print("bzr 4 b ")
                    elem_counter = 0
                    for even_more_elem in more_elems:
                        print(' ciiiiii  four  ')
                        if not this_extra_got:
                #            print(even_more_elem.get_attribute('innerHTML'))
                            this_price = even_more_elem.find_element_by_class_name('associate-option-item-cost').get_attribute('innerHTML')
                            this_name = even_more_elem.find_element_by_class_name('associate-option-item-name').get_attribute('innerHTML')
                           # check_box = [tag name = input and type = checkbox and 'option_' in id]
                            options = even_more_elem.find_elements_by_tag_name('input')
                            for o in options:
                     #           print(o.get_attribute('id'))
                                if 'option_' in o.get_attribute('id'):
                                    if o.get_attribute('id')[7].isdigit():
                                        check_box = o


                            if not stop_yet:
                                if even_more_elem.get_attribute('innerHTML') == "Standard":
                                    print("propper stop     we found stand section")
                                    stop_yet = True

                                elif 'cloth' in this_name.lower() and not internal_done_yet and not this_extra_got:
                                    if this_price == '£0.00':
                                        print("bzr  aaaaa")
                                        click(check_box)
                                        selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                        not_clicked = True
                                        click_counter = 0
                                        tstamp1 = datetime.datetime.now()
                                        future2 = tstamp1 +  datetime.timedelta(seconds = 130)
                                        while not_clicked and not this_extra_got:
                                             if datetime.datetime.now() > future2:
                                                 print(1/0)
                                             print("   not clicked loop for cloth  ")
                                             time.sleep(5)
                                             selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                             been_through_options = False
                                             tstamp1 = datetime.datetime.now()
                                             future3 = tstamp1 +  datetime.timedelta(seconds = 130)
                                             while not been_through_options and not this_extra_got:
                                                 if datetime.datetime.now() > future3:
                                                     print(1/0)
                                                 click(check_box)
                                                 print("bzr 5")
                                                 time.sleep(5)

                                                 selected = driver.find_elements_by_id('selected-options-listing')
                                                 for s in selected:
                                                     print(" br 4 ")
                                                     if 'cloth' in s.get_attribute('innerHTML').lower():
                                                         print(" br 5      cos we got "+str(s.get_attribute('innerHTML')))
                                                         not_clicked = False
                                                         external_done_yet = True
                                                         this_extra_got = True
                                                         time.sleep(5)
                                                     else:
                                    #                     print(s.get_attribute('innerHTML').lower())
                                                         print("aint cloth")
                                                 been_through_options = True
                                                 if not_clicked:
                                                     click_counter+=1
                                                     if click_counter % 2 == 0:
                                                         time.sleep(1)
                                                         click(check_box)
                                                         time.sleep(1)
                                                         click(check_box)
                                                     else:
                                                         click(check_box)
    #                                             try:
     #                                                for s in selected:
      #                                                   if 'cloth' in s.get_attribute('innerHTML').lower():
       #                                                      not_clicked = False
        #                                                     internal_done_yet = True
         #                                                    this_extra_got = True
          #                                                   time.sleep(5)
           #                                              else:
            #                                                 print(s.get_attribute('innerHTML')+ "  is not cloth ")
             #
              #                                       been_through_options = True
               #                                  except:
                #                                     selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                 #                                    try:
                  #                                       for s in selected:
                   ##                                          print("selected print below ")
                     ##                                        print(s)
                       #                                      print(s.get_attribute('innerHTML'))
                        #                                 #print(selected)
                         #                            except:
    #                     #                                for s in selected:
                           #                              print("wont iterate ")
    #

    #
    #
     #
      #                                           click(check_box)
       #                                          time.sleep(5)


                                    else:
                                        print(this_price)
                                        pass
                                elif 'leather' in this_name.lower() and not internal_done_yet and not 'steering' in this_name.lower() and not this_extra_got:
                                    if this_price == '£0.00':
                                        click(check_box)
                                        selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                        not_clicked = True
                                        click_counter = 0
                                        tstamp1 = datetime.datetime.now()
                                        future4 = tstamp1 +  datetime.timedelta(seconds = 130)
                                        while not_clicked and not this_extra_got:
                                             if datetime.datetime.now() > future4:
                                                 print(1/0)
                                             print("   not clicked loop for leather  ")
                                             time.sleep(5)
                                             selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                             been_through_options = False
                                             tstamp1 = datetime.datetime.now()
                                             future5 = tstamp1 +  datetime.timedelta(seconds = 130)
                                             while not been_through_options and not this_extra_got:
                                                 if datetime.datetime.now() > future5:
                                                     print(1/0)
                                                 click(check_box)
                                                 time.sleep(5)
                                                 selected = driver.find_elements_by_id('selected-options-listing')
                                                 for s in selected:
                                                     print(" br 4444444444 ------------------------------------------------------------------------------------------------------------- ")
                                                     if 'leather' in s.get_attribute('innerHTML').lower():
                                                         print(" br 5 ")
                                                         not_clicked = False
                                                         internal_done_yet = True
                                                         this_extra_got = True
                                                         time.sleep(5)
                                                     else:
                                                         pass
                                                 been_through_options = True
                                                 if not_clicked:
                                                     click(check_box)


                                elif 'paint' in this_name.lower() and not external_done_yet and not this_extra_got:
                                    if this_price == '£0.00':
                                        click(check_box)
                                        selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                        not_clicked = True
                                        click_counter = 0
                                        tstamp1 = datetime.datetime.now()
                                        future6 = tstamp1 +  datetime.timedelta(seconds = 130)
                                        while not_clicked and not this_extra_got:
                                            if datetime.datetime.now() > future6:
                                                print(1/0)
                                            print("   not clicked loop for paint  ")
                                            time.sleep(5)

                                            selected = driver.find_elements_by_id('selected-options-listing')
                                            for s in selected:
                                                print(" br 4 ")
                                                if 'paint' in s.get_attribute('innerHTML').lower():
                                                    print(" br 5 ")
                                                    not_clicked = False
                                                    external_done_yet = True
                                                    this_extra_got = True
                                                    time.sleep(5)
                                                else:
                                                    print("this aint paint   " + str(s.get_attribute('innerHTML').lower()))
                                            been_through_options = True
                                            if not_clicked:
                                                click(check_box)



                                             #######
                          #                   selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                           #                  print(" br 1 ")
                            #                 been_through_options = False
                             #                while not been_through_options and not this_extra_got:
                              #                   print(" br 2 ")
                               #                  click(check_box)
                                #                 time.sleep(5)
                                 #                try:
                                  #                   print(" br 3 ")
                                   #                  print(str(len(selected))+ "    number of options")
                                    #                 for s in selected:
                                     #                    print(" br 4 ")
                                      #                   if 'paint' in s.get_attribute('innerHTML').lower():
                                       #                      print(" br 5 ")
                                        #                     not_clicked = False
                                         #                    external_done_yet = True
                                          #                   this_extra_got = True
                                           #                  time.sleep(5)
                                            #             else:
                                             #                pass
                                              #           print(" br 6 ")
                                               ##      print(" br 7 ")
                                                 #    been_through_options = True
                           #                      except Exception as e:
                            #                         print(e)
                             #                        print(e.messsage)
                              #                       print(" br 8 ")
                               #                      selected = driver.find_elements_by_class_name('associate-option-selected-item-name')
                                #                     print(str(len(selected))+ "    number of options")
                                 ##                    try:
                                   ##                      for s in selected:
                                     #                        print(s)
                                      #                       print(s.get_attribute('innerHTML'))
                                       #              except:
    #                                   #                  for s in selected:
                                         #                print("wont iterate ")
                                          #           print(driver.page_source)
                                           #          time.sleep(7)
                                            #         print(" br 9 ")
                                             #





                         #       print(driver.page_source)
                        elem_counter+=1
        if not external_done_yet and not internal_done_yet:
            options_window  = driver.find_elements_by_xpath('/html/body/div[9]/div[2]/div[3]/div[1]/div[1]/div[2]')
    print("done ")

    ok_xp = '/html/body/div[9]/div[2]/div[3]/div[1]/div[4]/input[1]'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,ok_xp)))

    ok_button  = driver.find_element_by_xpath(ok_xp)
    click(ok_button)
    print("    arse     ")

    time.sleep(1)
    wait_until_done_loading(driver)
    time.sleep(1)
    wait_until_done_loading(driver)

    try:
        error_xp = '/html/body/div[9]/div[2]/div[2]'
        error  = driver.find_element_by_xpath(error_xp)
        if "display: block;" in error.get_attribute("style"):
            print("missed soomething    ")
            return False
        else:
            return True
    except:
        return True
    print(1/0)

def get_options(driver):
    print("getting opts")
    opts_group_id = 'associateQuote-options-listing'
    selected = driver.find_elements_by_id(opts_group_id)
    theopts = ""
    for s in selected:
        selected2 = s.find_elements_by_tag_name("div")
        for s2 in selected2:
            s3 = s2.find_elements_by_tag_name("span")
            for s4 in s3:

                print(s4.get_attribute("innerHTML"))
                theopts += s4.get_attribute("innerHTML").strip() + "     lll     "
    return theopts

def check_van(driver):
    lcv = False
    txt = 'The miles per annum for commercial vehicles should be no less than 10,000 miles'
    class_name = 'errorMessage'
    prod_id = 'productSelect'

    product_sel = Select(driver.find_element_by_id(prod_id))

    if 'LCV' in product_sel.first_selected_option.text:
        lcv = True
    err = driver.find_elements_by_class_name(class_name)
    if txt in err:
        lcv = True
    return lcv
