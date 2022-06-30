import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import pyautogui
import difflib
import keyboard
#import jellyfish
import datetime
import selenium.webdriver.chrome.options as Options
from Levenshtein import distance as lev

def read_txt_file():
    with open('config.txt' , encoding='utf-8') as f:
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
                    print("   £    found ")
                    pound_counter+=1
                if pound_counter == 3 and char == '"':
                    pound_counter = 100

    return username, password, customer
def click_lcv6(driver):

    confirm_xp = '/html/body/div[2]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/asset-lookup-search-engine/div/asset-lookup-modal/div/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[2]/button'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,confirm_xp)))
    confirm_button = driver.find_element_by_xpath(confirm_xp)
    click(confirm_button)
    time.sleep(5)

def blp_check_1(driver, diy_blp):
    confirm_xp = '//*[@id="asset-lookup-confirm"]'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,confirm_xp)))
    confirm_button = driver.find_element_by_xpath(confirm_xp)
    click(confirm_button)
    time.sleep(5)
    cost_br_xp = '//*[@id="quote-page-wrap"]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/div[4]/sr-price-breakdown-tile-button/button'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,cost_br_xp)))
    cost_break_down = driver.find_element_by_xpath(cost_br_xp)
    click(cost_break_down)
    time.sleep(5)
    blp_xp = '//*[@id="price-breakdown-modal"]/div/div/div[2]/form/sr-price-breakdown-row[1]/fieldset/div[4]/div/div[1]/div/input'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,blp_xp)))
    blp = str(driver.find_element_by_xpath(blp_xp).get_attribute("value")).replace(",","")
    print(blp)
    if abs(float(blp)-float(diy_blp)) < 2:
        print("less than 2")
        return True
    else:
        print(abs(float(blp)-float(diy_blp)))
        print("bad blp not less than 2")
        return False

def switch_to_iframe_1(driver):
    frame_1_xp = "/html/body/app-root/ng-component/div/div/div/proposal-page/div/div/quick-quote-page/legacy-php-view/iframe";     # '//*[@id="system-page-container"]/proposal-page/div/div/quick-quote/legacy-php-view/iframe'
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,frame_1_xp)))
    iframe1 = driver.find_element_by_xpath(frame_1_xp)
    driver.switch_to.frame(iframe1)

def choose_man_1(driver, diy_man):
    print("best_make     1a")
    man_sel_xp = '//*[@id="Manufacturer-input-element"]'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,man_sel_xp)))
    man_sel = Select(driver.find_element_by_xpath(man_sel_xp))
    man_selected_bool = False
    man_selected = "none"
    opts = man_sel.options;
 #   print("best_make     1b")
    for o in opts:
        o=o.text
        print(o)
  #  print("best_make    2")
    try:
        man_sel.select_by_visible_text(diy_man)
        man_selected = diy_man
        man_selected_bool = True
   #     print("best_make  propper selled ere ")
    except:
        diy_man2 = ""
        counter = 0
        for char in diy_man:
            if counter == 0:
                diy_man2 += diy_man[counter]
            else:
                diy_man2 += diy_man[counter].lower()
            counter += 1
#        print("best_make     3")
        try:
            man_sel.select_by_visible_text(diy_man2)
            man_selected = diy_man
            man_selected_bool = True
        except:
            pass
   # print("best_make     4")
    if man_selected_bool:
        if man_sel.first_selected_option.text.lower() == man_selected.lower():
            return True
        else:
            print(man_sel.first_selected_option.text)
            print(man_selected)
  #  print("best_make     5")
    best_score = 99999
    best_make = ""
    for o in opts:
        score = lev(o.text , diy_man)
        print(str(score) + "    " + str(o))
        if score < best_score:
            best_score = score
            best_make = o.text
    man_sel.select_by_visible_text(best_make)
    print("best_make     6")
    return True


def choose_model_1(driver, diy_model):
    print(diy_model)
    model_sel_xp = '//*[@id="Model-input-element"]'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,model_sel_xp)))
    model_sel = Select(driver.find_element_by_xpath(model_sel_xp))
    try:
        model_sel.select_by_visible_text(diy_model)
    #    print("model match        hooray ")
        return True
    except:
        try:
            model_sel.select_by_visible_text(diy_model.strip())
   #         print("model match        hooray     22 ")
            return True
        except:
            try:
                model_sel.select_by_visible_text(diy_model+ " van")
  #              print("model match        hooray     22 ")
                return True
            except:
                best_match = 99
                best_name = "not set"
                at_least_one_good_one = False
                time.sleep(2)
 #               print("mi bread crum ")
                model_sel = Select(driver.find_element_by_xpath(model_sel_xp))
                for o in model_sel.options:
                    print(o.text)

                    this_match = lev(o.text,diy_model)
                    print(this_match)
                    if this_match < 4:
                        if this_match< best_match:
                            at_least_one_good_one = True
                            best_match = this_match
                            best_name = o.text
                if at_least_one_good_one:
                    model_sel.select_by_visible_text(best_name)
#                    print("model match        hooray     33 ")
                    return True

    print("no model match uh oh ")
    return False;


def check_if_we_can_still_close_blp_stuff(driver):
    time.sleep(1)
    xp = '//*[@id="price-breakdown-modal"]/div/div/div[3]/button'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH, xp)))
    v = driver.find_element_by_xpath(xp)
    v.click()
    time.sleep(1)

def add_metallic_paint(driver):
    check_if_we_can_still_close_blp_stuff(driver)
    vo_xp = '//*[@id="quote-page-wrap"]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/div[2]/sr-vehicle-options-tile-button/button'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH, vo_xp)))
    v_opts = driver.find_element_by_xpath(vo_xp)
    v_opts.click();
    #
    time.sleep(1)
    #



#    xp2 = '//*[@id="vehicle-options-modal"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/fieldset/a[2]'
#    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH, xp2)))
#    opt = driver.find_element_by_xpath(xp2)
#    if ("metallic" in opt.get_attribute("innerHTML").lower()):
#        opt.click()
#        print(9999/0)
##    else:
#        print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
#        print(opt.get_attribute("outerHTML"))
#        print(opt.get_attribute("innerHTML"))
#        print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
#    print("  8888888888888888      8888888888888888888888 8           8888888888888888      88888888888888888888888888888888888  88888888888888888888888888888888888    8888888888888888888888888888888 ")

    xp = '//*[@id="vehicle-options-modal"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/fieldset/a['
    for j in range(6):
        try:
            the_xp = xp+str(j)+']'
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH, the_xp)))
            opt = driver.find_element_by_xpath(the_xp)
            if ("metallic" in opt.get_attribute("innerHTML").lower()):
                opt.click()
                print("metal chosen ")

            else:
                print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
                print(opt.get_attribute("outerHTML"))
                print(opt.get_attribute("innerHTML"))
                print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")

        except:
            print("nope "+str(the_xp))
# solid unclick below = not neccesary
#          //*[@id="vehicle-options-modal"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/fieldset/a[1]
#    xp = '//*[@id="vehicle-options-modal"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[1]/fieldset/a['
#    for j in range(20):
#        try:
#            the_xp = xp+str(j)+']'
#            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH, the_xp)))
###            opt = driver.find_element_by_xpath(the_xp)
    #        if ("solid" in opt.get_attribute("innerHTML").lower()):
    #            opt.click()
    #            print("solid unclick ")
    #    #        print(9/0)
    #        else:
    #            print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    #            print(opt.get_attribute("outerHTML"))
    #            print(opt.get_attribute("innerHTML"))
    #            print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
#
#        except:
#            print("nope "+str(the_xp))
#    print(95/0)
    close_xp = '//*[@id="vehicle-options-modal"]/div/div/div[3]/button'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,close_xp)))
    close = driver.find_element_by_xpath(close_xp)
    close.click()


def choose_deriv_1(driver, diy_deriv, make, model):#
    time.sleep(1)
 #   print(diy_deriv)
    deriv_sel_xp = '//*[@id="Derivative-input-element"]'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,deriv_sel_xp)))
    deriv_sel = Select(driver.find_element_by_xpath(deriv_sel_xp))
    try:
        deriv_sel.select_by_visible_text(diy_deriv)
        return True
    except:
        opts = deriv_sel.options
        make_bits = make.split(" ");
        model_bits = model.split(" ");
        for ma in make_bits:
  #          print(str(ma)+"     ma ")
            if ma in diy_deriv:
   #             print(" ma is in deriv "+str(diy_deriv))
                diy_deriv = diy_deriv.replace(ma, "")
    #            print(" ma is in deriv "+str(diy_deriv))
        for mo in model_bits:
     #       print(str(mo)+"   mo  ")
            if mo in diy_deriv:
                diy_deriv = diy_deriv.replace(mo , "")
      #  print(str(diy_deriv)+"       new deriv")
        try:
            deriv_sel.select_by_visible_text(diy_deriv)
            return True
        except:
       #     print("  aaaaaa   ")
            opts_bits = []
            for o in opts:
                opts_bits.append(o.text.split(" "))
        #        print(o.text)

            current_deriv_bits = diy_deriv.split(" ")
            best_match = "none"
            best_match_count = 0
            derivs_index_counter = 0
            for o in opts_bits:
 #               print(str(o)+"   these are the options bits im looking ")
                bit_count = len(o)
                match_count = 0
                for bit in o:
  #                  print("their bit = "+str(bit))
                    for our_bit in current_deriv_bits:
   #                     print("our bit = "+str(our_bit))
                        if bit == our_bit:
    #                        print(str(our_bit) + " = match = "+str(bit))
                            match_count +=1;#
                            if best_match_count < match_count:
                                best_match = o
                                best_match_index = derivs_index_counter
                                best_match_count = match_count
     #                           print("fugger me nig")
                if bit_count == match_count:
                    correct_chosen_deriv = 0;
      #              print(str(correct_chosen_deriv)+ "      correct_chosen_deriv ")
                derivs_index_counter+=1
       #     print(str(best_match) + "    was bet match inint")


    try:
        print("final_chance")
        for o in opts:
            print(o.text)
            if o.text == opts[best_match_index].text:
                print(opts[best_match_index].text)
                deriv_sel.select_by_visible_text(opts[best_match_index].text)
                return True
    except:
        pass
    return False


def choose_my_1(driver, diy_my):
    try:
        my_sel_xp = '//*[@id="ModelYear-input-element"]'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,my_sel_xp)))
        my_sel = Select(driver.find_element_by_xpath(my_sel_xp))
        my_sel.select_by_visible_text(diy_my)
    except:
        time.sleep(1)
        my_sel_xp = '//*[@id="ModelYear-input-element"]'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,my_sel_xp)))
        my_sel = Select(driver.find_element_by_xpath(my_sel_xp))
        my_sel.select_by_visible_text(diy_my)
    return True


def try_switch_to_frame_1(driver):
    try:              #//*[@id="system-page-container"]/proposal-page/div/div/quick-quote/legacy-php-view/iframe
        frame_1_xp  = '//*[@id="system-page-container"]/proposal-page/div/div/quick-quote/legacy-php-view/iframe'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,frame_1_xp)))
        iframe1 = driver.find_element_by_xpath(frame_1_xp)
        driver.switch_to.frame(iframe1)
    except:
        print("couldnt switch to frame 1")

def initialize_quote(driver, round_tried):
    print("top of init")
    ## if its round 2 or 4 try vans
                   #    /html/body/app-root/ng-component/div/cw-side-nav/div/div/ul/div[2]/li[1]/div/a
    new_quote_calc_xp='/html/body/app-root/ng-component/div/cw-side-nav/div/div/ul/div[2]/li[1]/div/a'
    new_car_box_xp = '//*[@id="asset-lookup-modal"]/div/div'
    general_box = False
    car_button_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[1]/button'
    car_selected=False
    lcv_button_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[2]/button'
    button_class_when_chosen = 'btn btn-block btn-asset-type active' # for car or lcv
    chosen_alfa = False
    make_xp = '//*[@id="Manufacturer-input-element"]'


    del_xp ='//*[@id="price-breakdown-modal"]/div/div/div[2]/form/sr-price-breakdown-row[6]/fieldset/div[1]/label'

    ready_to_start = False
    fail_counter = 0
    lcv_selected=False
    chosen_vw = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not ready_to_start:
        if future < datetime.datetime.now():
            print(1/0)
     #   print("ready start")
   ##     #print(driver.page_source)
        try:
            print("rs1")
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,new_car_box_xp)))
            print("rs2")
            new_car_box = driver.find_element_by_xpath(new_car_box_xp)
            print("rs3")
            general_box=True
            print("init ready")
        except:
            print("exception in ready for new quote")
            ##print(driver.page_source)
        print("init sp0")
#        time.sleep(15)
#        try:
        try:
            print("init sp0.1")
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,car_button_xp)))
            car_button = driver.find_element_by_xpath(car_button_xp)
        except:
            print("cant find car but ")
        print("init sp0.15")
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,lcv_button_xp)))
            lcv_button = driver.find_element_by_xpath(lcv_button_xp)
        except:
            print("cant find lcv but ")
        print("init sp0.2")
        try:
            if round_tried == 1 or round_tried ==3:
                if button_class_when_chosen in car_button.get_attribute("class"):
                    car_selected = True
                else:
                    print(button_class_when_chosen)
                if button_class_when_chosen in lcv_button.get_attribute("class"):
                    car_selected = False
                    print("init sp0.3")
                    click(car_button)
                    print("just chosen car")
                    time.sleep(0.5)
            if round_tried == 2 or round_tried ==4:
                print("init lcv")
                if button_class_when_chosen in lcv_button.get_attribute("class"):
                    lcv_selected = True
                if button_class_when_chosen in car_button.get_attribute("class"):
                    lcv_selected = False
                    click(lcv_button)
                    print("just chosen car")
                    time.sleep(0.5)
        except:
            print("choosing car/lcv exception ")
#        except:
#            print("car/lcv exception")
#        print("init sp1")
        try:
            if round_tried == 1 or round_tried ==3:
                print("init alfa")
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,make_xp)))
                make = Select(driver.find_element_by_xpath(make_xp))
                current_make = make.first_selected_option.text
                if current_make == 'Alfa Romeo':
                    chosen_alfa=True
                else:
                    print(current_make)
                    make.select_by_visible_text('Alfa Romeo')
                    print("just chosen alfa")
                    time.sleep(0.5)

            if round_tried == 2 or round_tried ==4:
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,make_xp)))
                make = Select(driver.find_element_by_xpath(make_xp))
                current_make = make.first_selected_option.text
                if current_make == 'Volkswagen':
                    chosen_vw=True
                else:
                    print(current_make)
                    make.select_by_visible_text('Volkswagen')
                    print("just chosen vw")
                    time.sleep(0.5)
        except:
            print("make proof exception")
        print("AAAAA")
        if fail_counter%7 == 0:
            print("fail 7")
            try:
                driver.switch_to.default_content
            except:
                print("no switch def 1")
            try:
                driver.switch_to.default_content()
            except:
                print("no switch def 2")



        if fail_counter%5==0:
            print("AbbbbA")
            try:
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,new_quote_calc_xp)))
                calc = driver.find_element_by_xpath(new_quote_calc_xp)
                click(calc)
                time.sleep(0.5)
            except:
                try:
                    new_quote_calc_class = 'd-flex align-items-center pl-0 w-100'
                    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS,new_quote_calc_class)))
                    calc_but = driver.find_element_by_class(new_quote_calc_class)
                    click(calc)
                    time.sleep(0.5)
                except:
                    print("failed to click calc")
            try:
                print("AbbbbA 1 ")
                try_switch_to_frame_1(driver)
                print("AbbbbA 2 ")
            except:
                print("failed switch frame")
        print("1aaa")
        if not car_selected or not chosen_alfa:
            fail_counter+=1
            time.sleep(0.5)
            if fail_counter > 300:
                print(1/0)
        print("1bbb")
        if round_tried == 1 or round_tried ==3:
            if car_selected  and chosen_alfa:
                print("rdy to strt 1 or 3 ")
                ready_to_start=True
        if round_tried == 2 or round_tried ==4:
            if lcv_selected  and chosen_vw:
                print("rdy to strt 2 or 4")
                ready_to_start=True
        print("777777777777")
        if car_selected:
            print("car_selected :) ")
        if chosen_alfa:
            print("alfa :) ")
        print(str(round_tried) + " 77777777777777777777777 ")
    print("ppppppppppppppppppppppppppppppppppppppppppoi")
def click(button):
    try:
        time.sleep(1)
        button.click()
        print('clicked   '  + str(button))
    except Exception as e:
        print(str(e))


def try_dismiss_wltp(driver):
    try:
        driver.switch_to.alert.dismiss();
    except:
        pass
    finally:
        pass

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


def open_alphabet(user, passw):
    print("leeeeeel")
   # try:
    driver_xpath2 = "chromedriver.exe"
    print("leeeeeel 0.1")
    chrome_options = Options.Options()
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(driver_xpath2 ,chrome_options=chrome_options)
    driver.get("https://identity.codeweavers.net/platform/alphabet/uk-car-line/app/showroom/login")
    username = user
    password = passw
    username_xpath = '//*[@id="username"]';
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,username_xpath)))
    username_box = driver.find_element_by_xpath(username_xpath)
    username_box.send_keys(username)
  #  #print(driver.page_source)
    print("1767676767611")

    password_xpath = '//*[@id="password"]';
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,password_xpath)))
    password_box = driver.find_element_by_xpath(password_xpath)
    for i in range(10):
        print(password)
    password_box.send_keys(password)
 #   #print(driver.page_source)
    print("1ikk11")

    login_button_xpath = '//*[@id="dps-login"]';
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,login_button_xpath)))
    login_button = driver.find_element_by_xpath(login_button_xpath)
    click(login_button) ### now we open the arval website
 #   \ver.page_source)
    print("111777777777777777777777777777")
    try:
        continue_xpath = '//*[@id="submit"]';
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,continue_xpath)))
        continue_button = driver.find_element_by_xpath(continue_xpath)
        click(continue_button)

    except:
        pass
    print("lel   were done ")
    return(driver)

def wait_until_front_page(driver):
    welcome_xp = '//*[@id="system-page-container"]/ng-component/cw-dashboard-jumbotron/div/div/cw-dashboard-header-details/div/div/h2'
    welcome_html = 'Welcome back'
    new_quote_calc_xp = '/html/body/app-root/ng-component/div/cw-legacy-side-nav/div/div/ul/div[2]/li[1]/div/a'
    new_quote_calc_xp = '/html/body/app-root/ng-component/div/cw-legacy-side-nav/div/div/ul/div[2]/li[1]/div/a'
 #                       /html/body/app-root/ng-component/div/cw-legacy-side-nav/div/div/ul/div[2]/li[1]/div/a
# /html/body/app-root/ng-component/div/cw-legacy-side-nav/div/div/ul/div[2]/li[1]/div/a
    new_quote_calc_class = 'd-flex align-items-center pl-0 w-100'

    front_page_ready = False
    welcome = False
    calc = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
        #if datetime.datetime.now() > future:
            #print(1/0)
    while not front_page_ready:
        print("top of front page loop")
        try:
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,welcome_xp)))
            welcome_elem = driver.find_element_by_xpath(welcome_xp)
            if welcome_html in welcome_elem.get_attribute("innerHTML"):
                print("welcome sorted")
                welcome = True
            else:
                print("no match welcome elem in front page loop")
        except:
            print("exception looking foor welcome elem in front page loop")
        print("fp sp 1")
        try:
            new_quote_calc_class = 'd-flex align-items-center pl-0 w-100'
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,new_quote_calc_xp)))
            calc_but = driver.find_element_by_xpath(new_quote_calc_xp)
            calc = True
            print("calc4")
        except:
            try:
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS,new_quote_calc_class)))
                calc_but = driver.find_element_by_class(new_quote_calc_class)
                calc = True
                print("calc4444")
            except:
                print("calc not found in loop ")
        print("fp sp 2")
        if calc and welcome:
            front_page_ready= True
            print("looks like fp sorted")
        print("fp sp 3")
        if datetime.datetime.now() > future:
            print(1/0)
        print("fp sp 4")


def find_correct_frame(driver):
 #   #print(driver.page_source)
    print("finding correct frame start ")
 #   try_to_move_into_frame(driver)

    correct_frame = True
    try:
        man_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/div/form/div[1]/label';
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,man_xp)))
        man_label = driver.find_element_by_xpath(man_xp)
    except:
        correct_frame = False
 #   #print(driver.page_source)
    print("finding correct frame 2 ")
    tries = 0
    while not correct_frame:
        tries+=1
        if tries > 3:
            reset_car_finder(driver)
            click_calculator(driver)
            tries = 0
        try:
        #    #print(driver.page_source)
            print("finding correct frame 3 ")
            man_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/div/form/div[1]/label';
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,man_xp)))
            man_label = driver.find_element_by_xpath(man_xp)
            correct_frame = True
        except:
                                # //*[@id="system-page-container"]/quick-quote/legacy-php-view/iframe
            try:#//*[@id="asset-lookup-mo //*[@id="system-page-container"]/quick-quote/legacy-php-view/iframe
                choose_car_frame_xpath = '//*[@id="system-page-container"]/quick-quote/legacy-php-view/iframe'
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , choose_car_frame_xpath)))
                choose_car_frame = driver.find_element_by_xpath(choose_car_frame_xpath)
                driver.switch_to.frame(choose_car_frame);
                man_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/div/form/div[1]/label';
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,man_xp)))
                man_label = driver.find_element_by_xpath(man_xp)
                correct_frame = True
            except:
                print("probably not first row 2 ")
                try:
         #           #print(driver.page_source)
                    print("finding correct frame 4 ")
                    choose_car_frame_xpath = '//*[@id="asset-lookup-modal"]'
                    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , choose_car_frame_xpath)))
                    choose_car_frame = driver.find_element_by_xpath(choose_car_frame_xpath)
                    driver.switch_to.frame(choose_car_frame);
                    man_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/div/form/div[1]/label';
                    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,man_xp)))
                    man_label = driver.find_element_by_xpath(man_xp)
                    correct_frame = True
                except:
                    print("lololololololoologggggggggggggggggggggggggggggggggggggggggggggggggggg     2 ")
                    try:
          #              #print(driver.page_source)
                        print("finding correct frame 5 ")
                        choose_car_frame_xpath = '//*[@id="quote-page-wrap"]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/asset-lookup-search-engine/div/asset-lookup-modal'
                        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , choose_car_frame_xpath)))
                        choose_car_frame = driver.find_element_by_xpath(choose_car_frame_xpath)
                        driver.switch_to.frame(choose_car_frame);
                        man_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/div/form/div[1]/label';
                        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,man_xp)))
                        man_label = driver.find_element_by_xpath(man_xp)
                        correct_frame = True
                    except:
           #             #print(driver.page_source)
                        try_to_move_into_frame(driver)
                        pass


def check_lcv_clicked(driver):
    car_selected = True
    print(" aaaaaaaaaaaaaaaa ")
    lcv_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[2]/button';
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH , lcv_xp)))
    lcv_button1 = driver.find_element_by_xpath(lcv_xp)

    car_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[1]/button';
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH , car_xp)))
    car_button1 = driver.find_element_by_xpath(car_xp)
    print(" aaaaaaaaaaaaaaaa 2222222222222 ")


    if lcv_button1.get_attribute("class") == "btn btn-block btn-asset-type" or car_button1.get_attribute("class") == "btn btn-block btn-asset-type active":
        car_selected = True
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)

    while car_selected:
   #     #print(driver.page_source)
        lcv_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[2]/button';
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH , lcv_xp)))
        lcv_button1 = driver.find_element_by_xpath(lcv_xp)
        click(lcv_button1)

        lcv_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[2]';
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH , lcv_xp)))
        lcv_buttona = driver.find_element_by_xpath(lcv_xp)
        click(lcv_buttona)

        lcv_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[2]/button/span[1]'
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH , lcv_xp)))
        lcv_button = driver.find_element_by_xpath(lcv_xp)
        click(lcv_button)

    #-------------------------------------------------------------------------------------------------------------------------------------#

        lcv_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[2]/button/span[1]/i'
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH , lcv_xp)))
        lcv_button = driver.find_element_by_xpath(lcv_xp)
        click(lcv_button)

        lcv_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[2]/button';
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH , lcv_xp)))
        lcv_button1 = driver.find_element_by_xpath(lcv_xp)

        car_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[1]/button';
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH , car_xp)))
        car_button1 = driver.find_element_by_xpath(car_xp)

        if lcv_button1.get_attribute("class") == "btn btn-block btn-asset-type" or car_button1.get_attribute("class") == "btn btn-block btn-asset-type active":
            car_selected = True
            print(" aaaajhg ")
        else:
            car_selected = False
        print(" 88 ")


def click_calc2(driver):


    try:
        A_xp = '/html/body/app-root/ng-component/div/cw-legacy-side-nav/div/div/ul/div[2]/li[1]';
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,A_xp)))
        calc_button = driver.find_element_by_xpath(A_xp)
        click(calc_button)
        print(" ccccccccc ")
    except:
        try:
            A_xp = '/html/body/app-root/system-root/div/cw-side-nav/div/div/ul/div[2]/li[1]/div/a';
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,A_xp)))
            calc_button = driver.find_element_by_xpath(A_xp)
            click(calc_button)
            print(" ccccccccc ")
        except:
            try:
                new_quote_calc_class = 'd-flex align-items-center pl-0 w-100'
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS,new_quote_calc_class)))
                calc_but = driver.find_element_by_class(new_quote_calc_class)
                click(calc)
                print(" ccccccccc aa ")
            except:
                try:
                #    driver.get('https://showroom.codeweavers.net/alphabet/uk-car-line/proposals-options?action=quoting')
                    print(" ccccccccc bb ")
                except:
                    print("no calc 2 click")

def click_calculator(driver):
    try:
        A_xp = '/html/body/app-root/system-root/div/cw-side-nav/div/div/ul/div[2]/li[1]/div';
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,A_xp)))
        calc_button = driver.find_element_by_xpath(A_xp)
        click(calc_button)
    except:
        pass
    try:
        A_xp = '/html/body/app-root/system-root/div/cw-side-nav/div/div/ul/div[2]/li[1]/div/a';
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,A_xp)))
        calc_button = driver.find_element_by_xpath(A_xp)
        click(calc_button)
    except:
        new_quote_calc_class = 'd-flex align-items-center pl-0 w-100'
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS,new_quote_calc_class)))
        calc_but = driver.find_element_by_class(new_quote_calc_class)
        click(calc)
    try:
        A_xp = '/html/body/app-root/system-root/div/cw-side-nav/div/div/ul/div[2]/li[1]/div/a/cw-icon';
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,A_xp)))
        calc_button = driver.find_element_by_xpath(A_xp)
        click(calc_button)
    except:
        pass

    time.sleep(5)




    find_correct_frame(driver)

 #   #print(driver.page_source)
    #driver.switch_to.frame(choose_car_frame);
  #  #print(driver.page_source)
    try:
        man_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/div/form/div[1]/label';
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,man_xp)))
        man_label = driver.find_element_by_xpath(man_xp)
    except:
        pass

    while not man_label.is_displayed():

        try:
            man_xp = '//*[@id="Manufacturer-input-element"]';
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,man_xp)))
            man_box = driver.find_element_by_xpath(man_xp)
        except:
            pass

        try:
            A_xp = '/html/body/app-root/system-root/div/cw-side-nav/div/div/ul/div[2]/li[1]/div';
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,A_xp)))
            calc_button = driver.find_element_by_xpath(A_xp)
            click(calc_button)
        except:
            pass

        try:
            A_xp = '/html/body/app-root/system-root/div/cw-side-nav/div/div/ul/div[2]/li[1]/div/a';
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,A_xp)))
            calc_button = driver.find_element_by_xpath(A_xp)
            click(calc_button)
        except:
            pass

        try:
            A_xp = '/html/body/app-root/system-root/div/cw-side-nav/div/div/ul/div[2]/li[1]/div/a/cw-icon';
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,A_xp)))
            calc_button = driver.find_element_by_xpath(A_xp)
            click(calc_button)
        except:
            pass


def click_lcv(driver):
    lcv_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[2]/button';
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH , lcv_xp)))
    lcv_button1 = driver.find_element_by_xpath(lcv_xp)
    click(lcv_button1)

    lcv_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[2]';
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH , lcv_xp)))
    lcv_buttona = driver.find_element_by_xpath(lcv_xp)
    click(lcv_buttona)

    lcv_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[2]/button/span[1]'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH , lcv_xp)))
    lcv_button = driver.find_element_by_xpath(lcv_xp)
    click(lcv_button)

    lcv_xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[2]/button/span[1]/i'
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH , lcv_xp)))
    lcv_button = driver.find_element_by_xpath(lcv_xp)
    click(lcv_button)

    print("aaa")
    check_lcv_clicked(driver)

def ready_to_choose_make(driver):

    xp = '/html/body/div[3]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/asset-lookup-search-engine/div/asset-lookup-modal/div/div/div/div[2]/asset-lookup-selection/div/div/form/div[1]/label'
    xp2 = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/div/form/div[1]/label'
    xp3 = '/html/body/div[3]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/asset-lookup-search-engine/div/asset-lookup-modal/div/div/div/div[2]/asset-lookup-selection/div/div/form/div[1]/div/select/option[3]'

    try:
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xp)))
        found_make = driver.find_element_by_xpath(xp)
        print("4")
    except:
        pass

    try:
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xp2)))
        found_make = driver.find_element_by_xpath(xp2)
        print("4 222 ")
    except:
        pass

    try:
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xp3)))
        found_make = driver.find_element_by_xpath(xp3)
        print(" 888")
    except:
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


def enter_this_make(driver, make1):
    click(make1)

def find_this_model(driver , model, model_tries_attempted, models_tried):
    print("top  of the models too ya (in an irish accentt)")
    try:
        close_price_details(driver)
        car_chooser_xp = '//*[@id="quote-page-wrap"]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/asset-lookup-search-engine/div/div/div/a'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH ,car_chooser_xp)))
        chooser = driver.find_element_by_xpath(car_chooser_xp)
        click(chooser)
    except:
        pass
    models = []
          # //*[@id="Model-input-element"]
    m_xp = '//*[@id="Model-input-element"]'
    models = []
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while len(models)<2:
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , m_xp)))
        sel_model = Select(driver.find_element_by_xpath(m_xp))
        models = sel_model.options
        print("mody hgygukjhgkyhglugkhg")
        for fuck_off in models:
            print(fuck_off.text)
        if datetime.datetime.now() > future:
            print(1/0)
    print(str(len(models))+ "              ffffffffffuckin what?")
#    models_to_remove = []
 #   for i in models_tried:
  #      print(str(i) + " a model allready tried" )
   #     num_of_times = models_tried.count(i)
    #    if num_of_times > 3:
     #       for j in models:
      #          if i == j.get_attribute("innerHTML"):
       ##             print("allready there")
         #       else:
          #          models_to_remove.append(i)

#    print(" modi to removi ")
 #   for p in models_to_remove:
  #      print(p)

#    print(" remov 999 model")
 #   for i in models_to_remove:
  #      print("allready tried  model  "+ str(i))
   #     for j in models:
    #        if i == j.get_attribute("innerHTML"):
     #           models.remove(j)
      #          print("removed model  777 " + str(j))
    #print(" remov 999 model end")
    models_str = []
    for i in models:
        ii = i.text
        models_str.append(ii)

    equivs = equivelants(model)
    for zz in range(len(equivs)):
        print("replacing")
        model = model.replace(equivs[zz]["list_of_sames"][0], equivs[zz]["list_of_sames"][1], 1)
        print(equivs[zz]["list_of_sames"][0])
        print(equivs[zz]["list_of_sames"][1])

    print("  njnj    ")
    best_model = parts_of_strings_comparer(models, model, "model", False)
    click(best_model)
    return best_model

#    elif model_tries_attempted == 4:
 #       best_model = levenshtein_comparer()
  #      return best_model
   # else:
    #    print("need more ways to check for model ")

def confirm_deriv_interaction(driver):
    der_xp = '//*[@id="Derivative-input-element"]'
    able_to_interact=False
    able_to_interact_a=False
    able_to_interact_b=False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 15)
    while not able_to_interact:
        print("deriv interact proof loop ")
        if datetime.datetime.now() > future:
            print(1/0)
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , der_xp)))
            sel_der = Select(driver.find_element_by_xpath(der_xp))
            current_opt = sel_der.first_selected_option.text
            opts = sel_der.options
            print("finding options")
        except:
            print("exception in finding elements for proving interaction with deriv")
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , der_xp)))
            sel_der = Select(driver.find_element_by_xpath(der_xp))
            sel_der.select_by_visible_text(opts[1].get_attribute("innerHTML"))
            time.sleep(1)
            if sel_der.first_selected_option.text == opts[1].get_attribute("innerHTML"):
                print("interact a")
                able_to_interact_a = True
                time.sleep(0.5)
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , der_xp)))
                sel_der = Select(driver.find_element_by_xpath(der_xp))
                sel_der.select_by_visible_text(opts[2].get_attribute("innerHTML"))
                time.sleep(1)
                if sel_der.first_selected_option.text == opts[2].get_attribute("innerHTML"):
                    print("interact b")
                    able_to_interact_b = True
                    time.sleep(0.5)
                else:
                    print(sel_der.first_selected_option.text)
                    print(opts[2].get_attribute("innerHTML"))
                    print("the above 2 do not match so were stuck")
            else:
                print(sel_der.first_selected_option.text)
                print(opts[1].get_attribute("innerHTML"))
                print("the above 2 do not match so were stuck")
        except:
            print("exception interacting with der sel")
        if able_to_interact_a and able_to_interact_b:
            able_to_interact=True

def prove_my_chosen_and_confirm_clicked(driver):
    product_xp = '//*[@id="ProductKey"]'
    interact_with_product = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not interact_with_product:
        if datetime.datetime.now() > future:
            print(1/0)
        print("ineract with product loop")
        time.sleep(0.5)
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , product_xp)))
            sel_der = Select(driver.find_element_by_xpath(product_xp))
        except:
            print("exception finding product box ")
        ch = 'Contract Hire'
        cp = 'Contract Purchase'
        try:
            sel_der.select_by_visible_text(cp)
            time.sleep(0.5)
            if sel_der.first_selected_option.text == cp:
                time.sleep(0.5)
                sel_der.select_by_visible_text(ch)
                time.sleep(0.5)
                if sel_der.first_selected_option.text == ch:
                    interact_with_product = True
        except:
            print("exception working with product thing")
        try:
            confirm_xp = '//*[@id="asset-lookup-confirm"]'
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , confirm_xp)))
            confirm = driver.find_element_by_xpath(confirm_xp)
            click(confirm)
        except:
            print("not clicking confirm in prove loop")
def click_more_detail_button(driver):
#                      //*[@id="quote-page-wrap"]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/div[4]/sr-price-breakdown-tile-button/button
    more_detail_xp = '//*[@id="quote-page-wrap"]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/div[4]/sr-price-breakdown-tile-button/button'
    car_blp_xp = '//*[@id="price-breakdown-modal"]/div/div/div[2]/form/sr-price-breakdown-row[1]/fieldset/div[4]/div/div[1]/div/input'
              #//*[@id="price-breakdown-modal"]/div/div/div[2]/form/sr-price-breakdown-row[1]/fieldset/div[4]/div/div[1]/div/input
    delivery_xp = '//*[@id="price-breakdown-modal"]/div/div/div[2]/form/sr-price-breakdown-row[6]/fieldset/div[2]/div/div[1]/div/input'
#                   //*[@id="price-breakdown-modal"]/div/div/div[2]/form/sr-price-breakdown-row[6]/fieldset/div[2]/div/div[1]/div/input
    rfl_xp = '//*[@id="price-breakdown-modal"]/div/div/div[2]/form/sr-price-breakdown-row[5]/fieldset/div[1]/select'
    exc_counter = 0
    details_open = False
    blp_found = False
    delivery_removed = False
    og_delivery_found = False
    og_delivery_finished=False
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , more_detail_xp)))
    more_detail = driver.find_element_by_xpath(more_detail_xp)
    click(more_detail)
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not details_open:
        if datetime.datetime.now() > future:
            print(1/0)
        time.sleep(2)
        if blp_found:
            details_open = True
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , car_blp_xp)))
            car_blp = driver.find_element_by_xpath(car_blp_xp).get_attribute("value")
            if len(str(car_blp))>5:
                blp_found=True
        except:
            print("exceptioon finding blp in proving detail ")

    #    if og_delivery_finished:
    #        if driver.find_element_by_xpath(delivery_xp).get_attribute("value") == og_delivery:
    #            if blp_found:
    #                details_open = True
    #        else:
    #            print("no og delivery match")
    #    try:
    #        print("sp1")
    #        if not og_delivery_found:
    #            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , delivery_xp)))
    #            og_delivery = driver.find_element_by_xpath(delivery_xp).get_attribute("value")
    #            print("og delivery " +str(og_delivery))
    #            og_delivery_found=True
    #        elif og_delivery_found and not og_delivery_finished:
    ##            print("sp2")
    #            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , delivery_xp)))
    #            delivery_box = driver.find_element_by_xpath(delivery_xp)
    #            delete(delivery_box)
    #            delivery_box.send_keys("0")
    #            time.sleep(4)
    #            print("sp3")
    #            new_delivery = driver.find_element_by_xpath(delivery_xp).get_attribute("value")
    #            print(new_delivery)
    #            if '0.00' == str(new_delivery) or '' == str(new_delivery):
    #                print("sp4")
    #                delete(delivery_box)
    #                delivery_box.send_keys(str(og_delivery))
    #                og_delivery_finished= True
    #                print("sp5")
    #            else:
    #                print("delivery not 0  its " + str(new_delivery))
    #    except:
    #        print("exceptioon interacting with delivery in proving detail ")
    #        exc_counter+=1
    #        if exc_counter > 10:
    #            delivery_xp = '//*[@id="price-breakdown-modal"]/div/div/div[2]/form/sr-price-breakdown-row[5]/fieldset/div[2]/div/div[1]/div/input'
                              #//*[@id="price-breakdown-modal"]/div/div/div[2]/form/sr-price-breakdown-row[5]/fieldset/div[2]/div/div[1]/div/input
                            ##//*[@id="price-breakdown-modal"]/div/div/div[2]/form/sr-price-breakdown-row[6]/fieldset/div[2]/div/div[1]/div/input
    print("click_more_detail_button sorted")
        #time.sleep(99999)

def try_all_derivs(driver, our_blp, mak1, mod1):
    ##### might need to build a checker that makes sure make n model doont change n put them back if they do
    der_xp = '//*[@id="Derivative-input-element"]'
    my_xp = '//*[@id="ModelYear-input-element"]'
    confirm_xp = '//*[@id="asset-lookup-confirm"]'
    total_deposit = ""


    derivatives_ready = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not derivatives_ready:
        if datetime.datetime.now() > future:
            print(1/0)
        print("top deriv loop")
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , der_xp)))
            sel_der = Select(driver.find_element_by_xpath(der_xp))
            opts = sel_der.options
            if (len(opts)>2):
                derivatives_ready = True
        except:
            print("cant find deriv sel")


    opts_text = []
    for kk in opts:
        opts_text.append(kk.text)

    var_found = False
    for i in opts_text:
        if i != "Please Select":
            print(str(i)+  "  jusst trying this deriv     669900")
            if not var_found:
                confirm_deriv_interaction(driver)

                print(i)
                this_der_chosen = False
                tstamp1 = datetime.datetime.now()
                future = tstamp1 +  datetime.timedelta(seconds = 130)
                while not this_der_chosen:
                    if datetime.datetime.now() > future:
                        print(1/0)
                    print("propper chose deriv loop")
                    sel_der.select_by_visible_text(i)
                    if sel_der.first_selected_option.text == i:
                        this_der_chosen = True

                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , my_xp)))
                my_sel = Select(driver.find_element_by_xpath(my_xp))
                my_opts = my_sel.options
                tstamp1 = datetime.datetime.now()
                future = tstamp1 +  datetime.timedelta(seconds = 130)
                while(len(my_opts)<2):
                    if datetime.datetime.now() > future:
                        print(1/0)
                    print("wait for my loop")
                    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , my_xp)))
                    my_sel = Select(driver.find_element_by_xpath(my_xp))
                    my_opts = my_sel.options
                my_opts_t = []
                print("here are the opts for my")
                for jj  in my_opts:
                    my_opts_t.append(jj.text)

                for j in my_opts_t:
                    if not var_found:
                        print(str(j)+  "  jusst trying this my     669900")
                        if j != "Please Select":
                            try:
                                my_sel.select_by_visible_text(j)
                                selected = my_sel.first_selected_option.text
                                my_selled = False
                                while not my_selled:
                                    print("my_sell loop")
                                    if selected == j:
                                        my_selled = True
                                    my_sel.select_by_visible_text(j)
                                    selected = my_sel.first_selected_option.text



                                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , confirm_xp)))
                                confirm = driver.find_element_by_xpath(confirm_xp)
                                confirm_status = confirm.get_attribute("disabled")
                                tstamp1 = datetime.datetime.now()
                                future = tstamp1 +  datetime.timedelta(seconds = 20)
                                while confirm_status == "disabled" or confirm_status == True or confirm_status == "true":
                                    if datetime.datetime.now() > future:
                                        print(1/0)
                                    print(str(confirm_status)+"      confirm stat")
                                    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , confirm_xp)))
                                    confirm = driver.find_element_by_xpath(confirm_xp)
                                    confirm_status = confirm.get_attribute("disabled")
                                click(confirm)

                                prove_my_chosen_and_confirm_clicked(driver)

                                click_more_detail_button(driver)

                                var_found = check_blp(driver, our_blp)
                                if var_found:
                                    for i in range(666):
                                        print("blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp blp ")
                                if not var_found:
                                    close_price_details(driver)
                                    car_chooser_xp = '//*[@id="quote-page-wrap"]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/asset-lookup-search-engine/div/div/div/a'
                                    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , car_chooser_xp)))
                                    car_chooser = driver.find_element_by_xpath(car_chooser_xp)
                                    click(car_chooser)
                                    time.sleep(4)
                                    if j == my_opts_t[-1]:
                                        print("well ere we bloody gu then")
                            except:
                                print("skipping  this my  "+str(j))
                                try:
                                    close_price_details(driver)
                                    car_chooser_xp = '//*[@id="quote-page-wrap"]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/asset-lookup-search-engine/div/div/div/a'
                                    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , car_chooser_xp)))
                                    car_chooser = driver.find_element_by_xpath(car_chooser_xp)
                                    click(car_chooser)
                                    time.sleep(4)
                                except:
                                    print(1/0)
                    else:
                        print("allready got car so skipping rest of my")
    print("finished looking for deriv")
    if var_found:
        print("and we got var")
    return var_found



def equivelants(our_deriv):
    print(" start of equivs ")
    list_of_sames = [ ["Tekna+" , "Tekna Plus"], ["[Tech Pack]", "Tech Pack"],["[EZ]","EZ"] , ["4dr", "4 Door"],  ["5dr", "5 Door"], ["3dr", "3 Door"] , ["EAT8","Auto"] , ["[5 seat]","5Seat"], ["[7 seat]","7Seat"]]
    for i in list_of_sames:
        for j in i:
            pass
    possible_matches = []
    for i in list_of_sames:
        match = True
        char_pos = []
        print(i[0])
        print(our_deriv)
        start = our_deriv.find(i[0])
        print(start)
        thisdict = {  "list_of_sames": i,"pos": start}
        possible_matches.append(thisdict)

    probable_matches = []
    for i in possible_matches:
        if i["pos"]!= -1:
            print(i)
            print(" kkk ")
            probable_matches.append(i)

    return probable_matches

def find_this_make_2(this_capcode ):
    print("new go at finding that bastard make ")
    og_capcode = this_capcode
    if og_capcode[0] == 'L' and og_capcode[1] == 'R':
        make = "land rover"
    if og_capcode[0] == 'D' and og_capcode[1] == 'S':
        make = "DS Automobiles"
    if og_capcode[0] == 'C' and og_capcode[1] == 'I':
        make = "Citroen"
    if og_capcode[0] == 'A' and og_capcode[1] == 'U':
        make = "Audi"
    if og_capcode[0] == 'S' and og_capcode[1] == 'E':
        make = "Seat"
    if og_capcode[0] == 'A' and og_capcode[1] == 'B':
        make = "Abarth"
    if og_capcode[0] == 'A' and og_capcode[1] == 'L':
        make = "ALFA ROMEO"
    if og_capcode[0] == 'B' and og_capcode[1] == 'M':
        make = "BMW"
    if og_capcode[0] == 'D' and og_capcode[1] == 'A':
        make = "DACIA"
    if og_capcode[0] == 'F' and og_capcode[1] == 'I':
        make = "FIAT"
    if og_capcode[0] == 'F' and og_capcode[1] == 'O':
        make = "FORD"
    if og_capcode[0] == 'H' and og_capcode[1] == 'O':
        make = "HONDA"
    if og_capcode[0] == 'H' and og_capcode[1] == 'Y':
        make = "HYUNDAI"
    if og_capcode[0] == 'I' and og_capcode[1] == 'S':
        make = "ISUZU"
    if og_capcode[0] == 'I' and og_capcode[1] == 'T':
        make = "ISUZU TRUCKS"
    if og_capcode[0] == 'I' and og_capcode[1] == 'V':
        make = "IVECO"
    if og_capcode[0] == 'J' and og_capcode[1] == 'A':
        make = "JAGUAR"
    if og_capcode[0] == 'J' and og_capcode[1] == 'E':
        make = "JEEP"
    if og_capcode[0] == 'K' and og_capcode[1] == 'I':
        make = "KIA"
    if og_capcode[0] == 'L' and og_capcode[1] == 'E':
        make = "LEXUS"
    if og_capcode[0] == 'L' and og_capcode[1] == 'S':
        make = "LOTUS"
    if og_capcode[0] == 'M' and og_capcode[1] == '3':
        make = "MAN"
    if og_capcode[0] == 'M' and og_capcode[1] == 'S':
        make = "MASERATI"
    if og_capcode[0] == 'M' and og_capcode[1] == 'X':
        make = "MAXUS"
    if og_capcode[0] == 'M' and og_capcode[1] == 'A':
        make = "MAZDA"
    if og_capcode[0] == 'M' and og_capcode[1] == 'E':
        make = "MERCEDES-BENZ"
    if og_capcode[0] == 'N' and og_capcode[1] == 'M':
        make = "MG MOTOR UK"
    if og_capcode[0] == 'M' and og_capcode[1] == 'N':
        make = "MINI"
    if og_capcode[0] == 'M' and og_capcode[1] == 'I':
        make = "MITSUBISHI"
    if og_capcode[0] == 'N' and og_capcode[1] == 'I':
        make = "NISSAN"
    if og_capcode[0] == 'N' and og_capcode[1] == 'M':
        make = "MGMOTORUK"
    if og_capcode[0] == 'P' and og_capcode[1] == 'S':
        make = "POLESTAR"
    if og_capcode[0] == 'P' and og_capcode[1] == 'O':
        make = "PORSCHE"
    if og_capcode[0] == 'R' and og_capcode[1] == '1':
        make = "RENAULT"
    if og_capcode[0] == 'P' and og_capcode[1] == 'E':
        make = "PEUGEOT"
    if og_capcode[0] == 'S' and og_capcode[1] == 'E':
        make = "SEAT"
    if og_capcode[0] == 'S' and og_capcode[1] == 'K':
        make = "SKODA"
    if og_capcode[0] == 'S' and og_capcode[1] == 'S':
        make = "SSANGYONG"
    if og_capcode[0] == 'S' and og_capcode[1] == 'U':
        make = "SUBARU"
    if og_capcode[0] == 'S' and og_capcode[1] == 'I':
        make = "SUZUKI"
    if og_capcode[0] == 'T' and og_capcode[1] == 'E':
        make = "TESLA"
    if og_capcode[0] == 'T' and og_capcode[1] == 'O':
        make = "TOYOTA"
    if og_capcode[0] == 'V' and og_capcode[1] == 'A':
        make = "VAUXHALL"
    if og_capcode[0] == 'V' and og_capcode[1] == 'W':
        make = "VOLKSWAGEN"
                #Volkswagen
    if og_capcode[0] == 'V' and og_capcode[1] == 'O':
        make = "VOLVO"
    if og_capcode[0] == 'C' and og_capcode[1] == 'U':
        make = "CUPRA"


    our_make = make
    return our_make


def find_this_make(driver, this_capcode ):
    print("new go at finding that bastard make ")
    og_capcode = this_capcode
    if og_capcode[0] == 'L' and og_capcode[1] == 'R':
        make = "land rover"
    if og_capcode[0] == 'D' and og_capcode[1] == 'S':
        make = "DS Automobiles"
    if og_capcode[0] == 'C' and og_capcode[1] == 'I':
        make = "Citroen"
    if og_capcode[0] == 'A' and og_capcode[1] == 'U':
        make = "Audi"
    if og_capcode[0] == 'S' and og_capcode[1] == 'E':
        make = "Seat"
    if og_capcode[0] == 'A' and og_capcode[1] == 'B':
        make = "Abarth"
    if og_capcode[0] == 'A' and og_capcode[1] == 'L':
        make = "ALFA ROMEO"
    if og_capcode[0] == 'B' and og_capcode[1] == 'M':
        make = "BMW"
    if og_capcode[0] == 'D' and og_capcode[1] == 'A':
        make = "DACIA"
    if og_capcode[0] == 'F' and og_capcode[1] == 'I':
        make = "FIAT"
    if og_capcode[0] == 'F' and og_capcode[1] == 'O':
        make = "FORD"
    if og_capcode[0] == 'H' and og_capcode[1] == 'O':
        make = "HONDA"
    if og_capcode[0] == 'H' and og_capcode[1] == 'Y':
        make = "HYUNDAI"
    if og_capcode[0] == 'I' and og_capcode[1] == 'S':
        make = "ISUZU"
    if og_capcode[0] == 'I' and og_capcode[1] == 'T':
        make = "ISUZU TRUCKS"
    if og_capcode[0] == 'I' and og_capcode[1] == 'V':
        make = "IVECO"
    if og_capcode[0] == 'J' and og_capcode[1] == 'A':
        make = "JAGUAR"
    if og_capcode[0] == 'J' and og_capcode[1] == 'E':
        make = "JEEP"
    if og_capcode[0] == 'K' and og_capcode[1] == 'I':
        make = "KIA"
    if og_capcode[0] == 'L' and og_capcode[1] == 'E':
        make = "LEXUS"
    if og_capcode[0] == 'L' and og_capcode[1] == 'S':
        make = "LOTUS"
    if og_capcode[0] == 'M' and og_capcode[1] == '3':
        make = "MAN"
    if og_capcode[0] == 'M' and og_capcode[1] == 'S':
        make = "MASERATI"
    if og_capcode[0] == 'M' and og_capcode[1] == 'X':
        make = "MAXUS"
    if og_capcode[0] == 'M' and og_capcode[1] == 'A':
        make = "MAZDA"
    if og_capcode[0] == 'M' and og_capcode[1] == 'E':
        make = "MERCEDES-BENZ"
    if og_capcode[0] == 'N' and og_capcode[1] == 'M':
        make = "MG MOTOR UK"
    if og_capcode[0] == 'M' and og_capcode[1] == 'N':
        make = "MINI"
    if og_capcode[0] == 'M' and og_capcode[1] == 'I':
        make = "MITSUBISHI"
    if og_capcode[0] == 'N' and og_capcode[1] == 'I':
        make = "NISSAN"
    if og_capcode[0] == 'N' and og_capcode[1] == 'M':
        make = "MGMOTORUK"
    if og_capcode[0] == 'P' and og_capcode[1] == 'S':
        make = "POLESTAR"
    if og_capcode[0] == 'P' and og_capcode[1] == 'O':
        make = "PORSCHE"
    if og_capcode[0] == 'R' and og_capcode[1] == '1':
        make = "RENAULT"
    if og_capcode[0] == 'P' and og_capcode[1] == 'E':
        make = "PEUGEOT"
    if og_capcode[0] == 'S' and og_capcode[1] == 'E':
        make = "SEAT"
    if og_capcode[0] == 'S' and og_capcode[1] == 'K':
        make = "SKODA"
    if og_capcode[0] == 'S' and og_capcode[1] == 'S':
        make = "SSANGYONG"
    if og_capcode[0] == 'S' and og_capcode[1] == 'U':
        make = "SUBARU"
    if og_capcode[0] == 'S' and og_capcode[1] == 'I':
        make = "SUZUKI"
    if og_capcode[0] == 'T' and og_capcode[1] == 'E':
        make = "TESLA"
    if og_capcode[0] == 'T' and og_capcode[1] == 'O':
        make = "TOYOTA"
    if og_capcode[0] == 'V' and og_capcode[1] == 'A':
        make = "VAUXHALL"
    if og_capcode[0] == 'V' and og_capcode[1] == 'W':
        make = "VOLKSWAGEN"
                #Volkswagen
    if og_capcode[0] == 'V' and og_capcode[1] == 'O':
        make = "VOLVO"
    our_make = make

    make_box_sorted = False
    mk_find_counter = 0
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not make_box_sorted:
        if datetime.datetime.now() > future:
            print(1/0)
        print("looking for make box")
        mk_find_counter+=1
        try:
            make_box = Select(driver.find_element_by_id("Manufacturer-input-element"))
            make_box_sorted = True
        except:
            print("no make bocx in make select")

        if mk_find_counter % 20:
            try_switch_to_frame_1(driver)


    make_box = Select(driver.find_element_by_id("Manufacturer-input-element"))
    make_options = make_box.options
    enough_makes = False
    while not enough_makes:
        print("enough makes loop")
        if len(make_options)< 4:
            print(str(len(make_options))+"   number of  makes  ")
            make_box = Select(driver.find_element_by_id("Manufacturer-input-element"))
            make_options = make_box.options
        else:
            enough_makes = True

    found_matching_make = False
    for j in make_options:
        print(str(j.get_attribute('innerHTML')) + "      make _ option   " )
        if j.get_attribute('innerHTML').lower().strip() == make.lower().strip():
            correct_make = j.get_attribute('innerHTML')
            found_matching_make = True
        else:
            print(j.get_attribute('innerHTML').lower())
            print(make.lower())
    if found_matching_make:
        print(str(correct_make) + "   make were gunna have ")
    else:
        for bugger in range(1000):
            print(str(make) + "   we cant find a bloody make ")
    make_box.select_by_visible_text(correct_make)
    propper_make_selected = False
    print("1")
    while not propper_make_selected:
        print("looking for make")
        if make_box.first_selected_option.text.lower() == correct_make.lower():
            propper_make_selected = True
        else:
            make_box.select_by_visible_text(correct_make)
            print("trying to select make again")

    print("mmiimmii end ")
    return correct_make


def lcv_check(capcode):
    s_capcode = capcode.strip()
    if s_capcode[len(s_capcode)-1].lower() == "l":
        return True
    elif s_capcode[0].lower() == 'n':
        if s_capcode[1].lower() == 'i':
            if s_capcode[2].lower() == 'n':
                if s_capcode[3].lower() == 'v':
                    if s_capcode[4].lower() == '0':
                        if s_capcode[5].lower() == '0':
                            print("  -===>- bbb -<===- ")
                            return True
    else:
        return False

def ps_remover(input_string):
    found_a_ps = False
    for i in range(len(input_string)-4):
            if found_a_ps == False:
                if input_string[i].isdigit():
                    if input_string[i+1].isdigit():
                        if input_string[i+2] == "p":
                            if input_string[i+3] == "s":
                                input_string = input_string[:i+2] + input_string[i+4:]
                                found_a_ps = True
                                print("dealt with a ps")
    return input_string



def enter_model(driver, model):
    click(model)



def find_deriv(driver , deriv, capcode, allready_tried):
    print("trying a deriv func ")
    derivs_buttons = []
    num_of_derivs = 60
    try:
        a1 = '//*[@id="Derivative-input-element"]/option[19]'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , a1)))
    except:
        num_of_derivs =19
    try:
        a1 = '//*[@id="Derivative-input-element"]/option[8]'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , a1)))
    except:
        num_of_derivs =8
    a1 = '//*[@id="Derivative-input-element"]/option['
    for i in range(num_of_derivs):
        try:
            xp = a1 + str(i)+"]"
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xp)))
            deriv_button = driver.find_element_by_xpath(xp)
            derivs_buttons.append(deriv_button)
            print(deriv_button)
        except:
            print(a1 + str(i)+"]      < aint a deriv we can find ")

  #  models_to_remove = []
   # for i in models_tried:
    #    num_of_times = models_tried.count(i)
     #   if num_of_times > 3:
      #      for j in models_to_remove:
       ##         if j == i:
         #           print("allready there")
          #      else:
           ##         models_to_remove.append(i)


    print("allready got")
    for j in allready_tried:
        print(j)
    print(" remov 999 deriv ")
    for i in derivs_buttons:
        print(i.get_attribute('innerHTML'))
        for j in allready_tried:
            if j == i.get_attribute('innerHTML'):
                #print(j.get_attribute('innerHTML'))
                derivs_buttons.remove(i)
                print("got rid of this deriv  "+str(i))
    print(" remov 999 deriv end ")

    equivs = equivelants(deriv)
    for zz in range(len(equivs)):
        print("replacing")
        deriv = deriv.replace(equivs[zz]["list_of_sames"][0], equivs[zz]["list_of_sames"][1], 1)
        print(equivs[zz]["list_of_sames"][0])
        print(equivs[zz]["list_of_sames"][1])

    is_van = lcv_check(capcode)
    deriv_chosen = parts_of_strings_comparer(derivs_buttons, deriv, "deriv", is_van)
    for bbb in range(20):
        print(" finally actually chosen     ==== " + str(deriv_chosen.get_attribute("innerHTML")))

    return deriv_chosen
    while(1<2):
        print(" HALLEIGHUO YA ")
        try:
            print(deriv_chosen.get_attribute("innerHTML"))
        except:
            for b in deriv_chosen:
                print(b.get_attribute("innerHTML"))

def enter_deriv(driver1 , deriv):
    click(deriv)

def parts_of_strings_comparer(list_of_objects_with_strings, our_string, model_or_deriv, van = False):
   # for i in range(1111):
    #    print(" ------------------------------------- ")
    our_string = ps_remover(our_string)
    for i in list_of_objects_with_strings:
        if i.text == "Please Select":
            list_of_objects_with_strings.remove(i)

    list_fs = []
    print("dddddddddd")
    this_string = "";
    our_strings_bits = []
    bit = "";
    while len(our_strings_bits) < 1:
        for index , char in enumerate(our_string):
            print(str(char) + "    char ")
            if (char == " "):
                our_strings_bits.append(this_string)
                this_string = "";
            elif (index == len(our_string)-1):
                this_string+=our_string[len(our_string)-1]
                our_strings_bits.append(this_string)
                this_string = "";
            else:
                this_string+=char

    print("are bits")
    for i in our_strings_bits:
        print(i)

    print("!!!!!!!!!!!!!!!!!!!!!")
    for o in list_of_objects_with_strings:
        o = o.text
        print(o)
        list_fs.append(o)



    print(" string workkkkkkkkkkkkkkkkkkkkk")
    for i in list_fs:
        print(i)
        i = ps_remover(i)
        print(i)
        if van:
            i = deal_with_van_h1(i)

    list_ps = []
    for string in list_fs:
        string+=(string[len(string)-1])
        this_string = "";
        these_bits = []
        for index, char in enumerate(string):
            print(index)
            print(len(string))
            if char == " " or index == len(string)-1:
                these_bits.append(this_string)
                this_string = "";
            else:
                this_string+=char
        list_ps.append(these_bits)

    number_of_bits = len(our_strings_bits)
    most_matched = -99
    joint_top_list= []
    our_bits_matched = [];
    for i in range(len(our_strings_bits)):
        our_bits_matched.append(0)

    for b in range(50):
        print(" ,,........ ")

    for  num, car  in enumerate(list_ps):
        print("lps")
        bits_matched = 0
        for i in range(len(our_strings_bits)):
            our_bits_matched[i]=0
        print("############################################")
        print("############################################")
        print("############################################")
        print("theirs   OPIOIO  " + str(car))
        print("ours   OPIOIO  " + str(our_string))
        print("############################################")
        print("############################################")
        print("############################################");

        for bit in car:

            print(str(bit) + "   this bit is from their string")
            this_bit_has_a_match = False
            print(our_bits_matched)
            print("reset wether this has a match")
            for our_index , our_bit in enumerate(our_strings_bits):
                print(str(our_bit) + "   this bit is from our string yesooooooooooooooo")
                if str(our_bit).lower() == str(bit).lower():
                    if our_bits_matched[our_index] == 0:
                        bits_matched +=1
                        print("????????????????????????????????????????????????????????????????? PLus 1 " + str(bit))
                        this_bit_has_a_match = True
                        our_bits_matched[our_index] = 1;
                    else:
                        print("this has allready been matched " + str(our_index))
             #           pass
                else:
            #        pass
                    print("these arent the same " + str(our_bit)+ "     " + str(bit))
            if this_bit_has_a_match == False:
                print("dint mach init under me")
                print(bit)
                print("our_bits, that didnt match with it  are below ")
                for our_index , our_bit in enumerate(our_strings_bits):
                    print(our_bit)


                for bit1 in car:
                    print(bit1)
                print("?????????????????????????????????????????????????????????????????    minus 1 " + str(bit))
                if model_or_deriv == "deriv":
                    bits_matched += -1

            else:
                print(" only went n got a bloody match " + str(car))

        print(str(bits_matched) + "              pooooooooooooooooooooooooooooooool  ")

        if bits_matched == most_matched:
            print(str(car) + " is the current best match for our " + str(bits_matched))
            joint_top_list.append(num)
        if bits_matched > most_matched:
            joint_top_list = []
            print(str(car) + " is the current best match for our " + str(bits_matched))
            joint_top_list.append(num)
            most_matched = bits_matched
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    for j in joint_top_list:
        print(j)
        print(list_ps[j])
    print(our_string)

    print("0000000   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    for i in joint_top_list:
        print(i)
        print(list_of_objects_with_strings[joint_top_list[0]].text)
        print(list_of_objects_with_strings[i].get_attribute('innerHTML'))
    print("11111111 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    if len(joint_top_list) == 1:
        print(list_of_objects_with_strings[joint_top_list[0]].text)
        print("reting ")
        return list_of_objects_with_strings[joint_top_list[0]]
    else:
        print("deal with even stevens ")
        ### do string comparison and return min diff
        print(len(list_of_objects_with_strings))
        print(len(joint_top_list))

        for e in joint_top_list:
            print(e)
        for e in list_of_objects_with_strings:
            print(e)

        return list_of_objects_with_strings[joint_top_list[0]]



def deal_with_van_h1(string):
    print(" van h1 start")
    found_stuff = []
    for i in range(len(string)-1):
        if string[i] == " ":
            if string[i+1] == "h" or string[i+1] == "L":
                if string[i+2].isdigit():
                    if string[i+3] == " ":
                        this_stuff = [string[i+1], string[i+2]]
                        found_stuff.append(this_stuff)

    if len(found_stuff)>1:
        new_string = ""
        for f in found_stuff:
            string.remove(f)
            new_string += f
        if len(new_string)>2:
            while (1<2):
                print(new_string)
        string = string + " " + new_string
    print(" van h1 finish ")
    return string
    #find h1 a1 etc...
    #remove
    # reattatch as 1 thing
    # return string


def choose_model_year(driver):
    #   //*[@id="ModelYear-input-element"]/option[3]
    #   //*[@id="ModelYear-input-element"]/option[2]
    for i in range(5):
        print("           my            ")
    model_years = []
    my_num = 15
    try:
        xp = '//*[@id="ModelYear-input-element"]/option[7]';
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xp)))
        my = driver.find_element_by_xpath(xp)
        model_years.append(my)
    except:
        my_num = 7;
    for i in range(my_num):
        try:
            xp = '//*[@id="ModelYear-input-element"]/option['+str(i)+']';
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xp)))
            my = driver.find_element_by_xpath(xp)
            model_years.append(my)
        except:
            print("not a my ")
            print(i)


    biggest_my = "";
    years = []



    for i in model_years:
        txt = i.get_attribute('innerHTML')
        if txt[0] == "2":
            if txt[1] == "1":
                try:
                    if txt[2] == "B":
                        return (i)
                except:
                    pass
    for i in model_years:
        txt = i.get_attribute('innerHTML')
        if txt[0] == "2":
            if txt[1] == "1":
                try:
                    if txt[2] == "A":
                        return (i)
                except:
                    pass
    for i in model_years:
        txt = i.get_attribute('innerHTML')
        if txt[0] == "2":
            if txt[1] == "1":
                if len(txt) == 2:
                    return (i)




    for i in model_years:
        txt = i.get_attribute('innerHTML')
        if txt[0] == "2":
            if txt[1] == "0":
                try:
                    if txt[2] == "B":
                        return (i)
                except:
                    pass
    for i in model_years:
        txt = i.get_attribute('innerHTML')
        if txt[0] == "2":
            if txt[1] == "0":
                try:
                    if txt[2] == "A":
                        return (i)
                except:
                    pass
    for i in model_years:
        txt = i.get_attribute('innerHTML')
        if txt[0] == "2":
            if txt[1] == "0":
                if len(txt) == 2:
                    return (i)


    for i in model_years:
        txt = i.get_attribute('innerHTML')
        if txt[0] == "1":
            if txt[1] == "9":
                try:
                    if txt[2] == "B":
                        return (i)
                except:
                    pass

    for i in model_years:
        txt = i.get_attribute('innerHTML')
        if txt[0] == "1":
            if txt[1] == "9":
                try:
                    if txt[2] == "A":
                        return (i)
                except:
                    pass

    for i in model_years:
        txt = i.get_attribute('innerHTML')
        if txt[0] == "1":
            if txt[1] == "9":
                if len(txt) == 2:
                    return (i)

    for i in model_years:
        txt = i.get_attribute('innerHTML')
        if txt[0] == "1":
            if txt[1] == "8":
                try:
                    if txt[2] == "B":
                        return (i)
                except:
                    pass

    for i in model_years:
        txt = i.get_attribute('innerHTML')
        if txt[0] == "1":
            if txt[1] == "8":
                try:
                    if txt[2] == "A":
                        return (i)
                except:
                    pass

    for i in model_years:
        txt = i.get_attribute('innerHTML')
        if txt[0] == "1":
            if txt[1] == "8":
                if len(txt) == 2:
                    return (i)

    for i in range(50):
        print("my didnt work")
    return False



def confirm_car(driver):
    xp = '//*[@id="asset-lookup-confirm"]'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xp)))
    but = driver.find_element_by_xpath(xp)
    click(but)


def check_blp(driver, our_blp):
    print("start of check blp")
    blp_xpath = '//*[@id="price-breakdown-modal"]/div/div/div[2]/form/sr-price-breakdown-row[1]/fieldset/div[4]/div/div[1]/div/input'

    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH , blp_xpath)))
    blp = driver.find_element_by_xpath(blp_xpath)
    try:
        the_blp = blp.get_attribute('value').replace(',','')
        print("blps1")
    except:
        pass
    try:
        our_blp = our_blp.replace(',','')
        print("blps2")
    except:
        pass
    print(str(our_blp) + "ours ininininni")
    print(str(the_blp) + "theirs ininininni")
    print("200  a ")

    print("end of check blp")
    if float(the_blp) == float(our_blp):
        print("blp is good")
        return True
    else:
        print(" blp did not match         ours = " + str(our_blp) + "     theirs = " + str(blp.get_attribute('value').replace(',','')))
        return False

def enter_otr(driver, our_otr):

    print(" otr satrt ")
    try:
        xp2 = '//*[@id="quote-page-wrap"]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/div[4]/sr-price-breakdown-tile-button/button'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xp2)))
        extras = driver.find_element_by_xpath(xp2)
        extras.click();
    except:
        pass
    middle_xp = '//*[@id="price-breakdown-modal"]/div/div/div[2]/form/div/div/div'
    otr_box_xp = '//*[@id="price-breakdown-modal"]/div/div/div[2]/form/sr-price-breakdown-row[8]/fieldset/div[2]/div/div[1]/div/input'
    close_xp = '//*[@id="price-breakdown-modal"]/div/div/div[3]/button'
                #//*[@id="price-breakdown-modal"]/div/div/div[3]/button
         #       //*[@id="price-breakdown-modal"]/div/div/div[3]/button
    removed_extras = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    #if datetime.datetime.now() > future:
        #print(1/0)
    while not removed_extras:
        print("top of removing extras loop")
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , middle_xp)))
            mid_button = driver.find_element_by_xpath(middle_xp)
            og_html = mid_button.get_attribute("innerHTML")
            click(mid_button)
            time.sleep(3)
            new_html= mid_button.get_attribute("innerHTML")
            print(og_html)
            print(new_html)
            if "Alphabet discounts have been removed." in new_html:
                removed_extras = True
        except:

            print("exception removing extras")



        if datetime.datetime.now() > future:
            print(1/0)


    otr_entered = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    #if datetime.datetime.now() > future:
        #print(1/0)
    while not otr_entered:
        print("top of entering otr loop")
    #    try:
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , otr_box_xp)))
        except:
            try:
                otr_box_xp='/html/body/div[2]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/div[4]/sr-price-breakdown/div/div/div/div[2]/form/sr-price-breakdown-row[8]/fieldset/div[2]/div/div[1]/div/input';
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , otr_box_xp)))
            except:
                #            /html/body/div[2]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/div[4]/sr-price-breakdown/div/div/div/div[2]/form/sr-price-breakdown-row[7]/fieldset/div[2]/div/div[1]/div/input
                otr_box_xp='/html/body/div[2]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/div[4]/sr-price-breakdown/div/div/div/div[2]/form/sr-price-breakdown-row[7]/fieldset/div[2]/div/div[1]/div/input';
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , otr_box_xp)))


        otr_button = driver.find_element_by_xpath(otr_box_xp)
        delete(otr_button)
        otr_button.send_keys(str(our_otr))
        otr_button.send_keys(Keys.ENTER)
        time.sleep(5)
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , otr_box_xp)))
        current_otr = driver.find_element_by_xpath(otr_box_xp).get_attribute("value")
        if float(current_otr.replace(',','')) - float(our_otr) < 1:
            print("otr sorted")
            otr_entered = True
        else:
            print(float(current_otr.replace(',','')))
#        except Exception as e:
#            print(e)
#            print(e.msg)
        #    print(e.message)
#            print("exception entering otr")
        if datetime.datetime.now() > future:
            print(1/0)
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , close_xp)))
    close_button = driver.find_element_by_xpath(close_xp)
    print(" otr end ")
    click(close_button)
#    close_xp2 = '//*[@id="price-breakdown-modal"]/div/div/div[1]/button/span[1]'
#    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , close_xp2)))
#    close_button = driver.find_element_by_xpath(close_xp2)
#    print(" otr end 2")
#    click(close_button)

def close_price_details(driver):
    close_xp = '//*[@id="price-breakdown-modal"]/div/div/div[3]/button'
    close_xp2 = '//*[@id="price-breakdown-modal"]/div/div/div[1]/button/span[1]'
    try:
        print("trying close button 1")
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , close_xp)))
        close_button = driver.find_element_by_xpath(close_xp)
        click(close_button)
    except:
        print("exception with close button 1")
    try:
        print("trying close button 2")
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , close_xp2)))
        close_button = driver.find_element_by_xpath(close_xp2)
        click(close_button)
    except:
        print("exception with close button 2")

def set_months_up(driver, months_up_to_choose):
    months_up_xp = '//*[@id="AdvancePayments"]'
    try:
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , months_up_xp)))
        months = Select(driver.find_element_by_xpath(months_up_xp))
        months.select_by_visible_text(str(months_up_to_choose))
    except:
        time.sleep(1)
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , months_up_xp)))
        months = Select(driver.find_element_by_xpath(months_up_xp))
        months.select_by_visible_text(str(months_up_to_choose))
def get_months_up(driver):
    months_up_xp = '//*[@id="AdvancePayments"]'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , months_up_xp)))
    months = Select(driver.find_element_by_xpath(months_up_xp))
    return months.first_selected_option.text;


def final_check_and_set_init_terms(driver, our_blp, our_otr):
    otr_box_xp_2='/html/body/div[2]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/div[4]/sr-price-breakdown/div/div/div/div[2]/form/sr-price-breakdown-row[8]/fieldset/div[2]/div/div[1]/div/input'
    otr_box_xp = '//*[@id="price-breakdown-modal"]/div/div/div[2]/form/sr-price-breakdown-row[8]/fieldset/div[2]/div/div[1]/div/input'
    close_xp = '//*[@id="price-breakdown-modal"]/div/div/div[3]/button'
    car_blp_xp = '//*[@id="price-breakdown-modal"]/div/div/div[2]/form/sr-price-breakdown-row[1]/fieldset/div[4]/div/div[1]/div/input'
    close_xp = '//*[@id="price-breakdown-modal"]/div/div/div[3]/button'
    close_xp2 = '//*[@id="price-breakdown-modal"]/div/div/div[1]/button/span[1]'

    blp_n_otr_good = False
    otr_good = False
    blp_good = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    #if datetime.datetime.now() > future:
        #print(1/0)
    while not blp_n_otr_good:
        print("blp n otr loop")
        try:
            try:
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , otr_box_xp)))
                cotr = driver.find_element_by_xpath(otr_box_xp).get_attribute("value")
            except:
                try:
                    otr_box_xp = otr_box_xp_2
                    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , otr_box_xp_2)))
                    cotr = driver.find_element_by_xpath(otr_box_xp_2).get_attribute("value")
                except:
                    otr_box_xp='/html/body/div[2]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/div[4]/sr-price-breakdown/div/div/div/div[2]/form/sr-price-breakdown-row[7]/fieldset/div[2]/div/div[1]/div/input';
                    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , otr_box_xp_2)))
                    cotr = driver.find_element_by_xpath(otr_box_xp_2).get_attribute("value")
            cotr = cotr.replace(',','')
            our_otr = str(our_otr).replace(',','')
            if abs(float(cotr) - float(our_otr))<1:
                otr_good = True
            else:
                print("otr diff   = " + str(abs(float(cotr) - float(our_otr))))

        except Exception as e:
            print(e)
            print(e.msg)
            print("exception looking for otr in final check loop")
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , car_blp_xp)))
            cblp = driver.find_element_by_xpath(car_blp_xp).get_attribute("value")
            cblp = cblp.replace(',','')
            our_blp=str(our_blp).replace(',','')
            if abs(float(cblp) - float(our_blp))<1:
                blp_good = True
            else:
                print("blp diff    = " + str(abs(float(cblp) - float(our_blp))))

        except Exception as e:
            print(e)
            print(e.msg)
            print(e.message)
            print("exception looking for blp in final check loop")
        if datetime.datetime.now() > future:
            print(1/0)
        if blp_good and otr_good:
            blp_n_otr_good=True

    for goes in range(2):
        close_price_details(driver)


        product_xp = '//*[@id="ProductKey"]'
        maint_xp = '//*[@id="MaintenanceProvider"]'
        months_up_xp = '//*[@id="AdvancePayments"]'
        months_xp = '//*[@id="Term"]'
        miles_xp = '//*[@id="AnnualMileage"]'
        calc_xp = '//*[@id="btn-calc-to-regularpayment"]'

        time.sleep(0.5)
        product_chosen = False
        tstamp1 = datetime.datetime.now()
        future = tstamp1 +  datetime.timedelta(seconds = 130)
        while not product_chosen:
            print("product chosen loop")
            try:
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , product_xp)))
                product = Select(driver.find_element_by_xpath(product_xp))
                product.select_by_visible_text(product_type_config)
                if product.first_selected_option.text == product_type_config:
                    product_chosen=True
                else:
                    print(str(product.first_selected_option.text)  +  "    these dunt match      "  +str(product_type_config))
            except:
                print("exception in productyt chosen loop")
            if datetime.datetime.now() > future:
                print(1/0)
        # set_contract options
        time.sleep(0.5)
        maint_chosen = False
        tstamp1 = datetime.datetime.now()
        future = tstamp1 +  datetime.timedelta(seconds = 130)
        while not maint_chosen:
            print("maint chosen loop")
            try:
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , maint_xp)))
                maint = Select(driver.find_element_by_xpath(maint_xp))
                maint.select_by_visible_text("Customer Maintained with RFL")
                if maint.first_selected_option.text == "Customer Maintained with RFL":
                    maint_chosen=True
                else:
                    print(str(maint.first_selected_option.text)  +  "    these dunt match     Customer Maintained with RFL")
            except:
                print("exception in maint chosen loop")
            if datetime.datetime.now() > future:
                print(1/0)
        time.sleep(0.5)
        months_up_chosen = False
        tstamp1 = datetime.datetime.now()
        future = tstamp1 +  datetime.timedelta(seconds = 130)
        while not months_up_chosen:
            print("months up  chosen loop")
            try:
                months_up_xp = '//*[@id="AdvancePayments"]'
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , months_up_xp)))
                months = Select(driver.find_element_by_xpath(months_up_xp))
                months.select_by_visible_text(str(months_up_config))
                if str(months.first_selected_option.text) == str(months_up_config):
                    months_up_chosen=True
                else:
                    print(str(months.first_selected_option.text)  +  "    these dunt match    " +str(months_up_config))
            except:
                print("exception in months up loop")
            if datetime.datetime.now() > future:
                print(1/0)
        time.sleep(0.5)
        init_months_chosen = False
        tstamp1 = datetime.datetime.now()
        future = tstamp1 +  datetime.timedelta(seconds = 130)
        while not init_months_chosen:
            print("months init chosen loop")
            try:
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , months_xp)))
                months = Select(driver.find_element_by_xpath(months_xp))
                months.select_by_visible_text("24")
                if str(months.first_selected_option.text) == "24":
                    init_months_chosen=True
                else:
                    print(str(months.first_selected_option.text)  +  "    these dunt match    24")
            except:
                print("exception in months init loop")
            if datetime.datetime.now() > future:
                print(1/0)
        time.sleep(0.5)
        init_miles_chosen = False
        tstamp1 = datetime.datetime.now()
        future = tstamp1 +  datetime.timedelta(seconds = 130)
        while not init_miles_chosen:
            print("miles init chosen loop")
            try:
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , miles_xp)))
                miles = Select(driver.find_element_by_xpath(miles_xp))
                miles.select_by_visible_text("6000")
                if str(miles.first_selected_option.text).strip() == "6000":
                    init_miles_chosen=True
                else:
                    print(str(miles.first_selected_option.text.strip())  +  "    these dunt match    6000")
            except:
                print("exception in miles init loop")
            if datetime.datetime.now() > future:
                print(1/0)

        time.sleep(0.5)
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH , calc_xp)))
        calc = driver.find_element_by_xpath(calc_xp)
        click(calc)
        time.sleep(2)



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

def get_this_prices(driver, our_months, our_miles, our_months_up , maint):
    time.sleep(1)
    months_xp = '//*[@id="Term"]'
    miles_xp = '//*[@id="AnnualMileage"]';
    maint_xp = '//*[@id="MaintenanceProvider"]/option[1]'
    no_maint_xp = '//*[@id="MaintenanceProvider"]/option[2]'
    if maint == False:
        maint_txt = "Customer Maintained with RFL"
    if maint == True:
        maint_txt =  "Alphabet with recovery"
    maint_sel_xp = '//*[@id="MaintenanceProvider"]'
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , maint_sel_xp)))
    maint = Select(driver.find_element_by_xpath(maint_sel_xp))
    maint.select_by_visible_text(maint_txt)
    if maint.first_selected_option.text == maint_txt:
        maint_sorted = True

        #########      miles enter
    miles_sorted = False
    time.sleep(1)
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , miles_xp)))
    miles = Select(driver.find_element_by_xpath(miles_xp))
    for o in miles.options:
        print(o.text)
        print("oi")
        if o.text.strip() == str(our_miles).strip():
            miles.select_by_visible_text(o.text)
            print("ye")
            if miles.first_selected_option.text == our_miles:
                miles_sorted = True
        else:
            print(print("no   |"+str(o.text.strip())+"|   |"+str(our_miles).strip()+"|"))
    if miles_sorted == False:
        time.sleep(1)
        miles = Select(driver.find_element_by_xpath(miles_xp))
        print(len(miles.options))
        for o in miles.options:
            print(o.text)
            print("oi")
            if str(o.text.strip()) == str(our_miles).strip():
                miles.select_by_visible_text(o.text)
                print("ye")
                if str(miles.first_selected_option.text) == str(our_miles):
                    miles_sorted = True
            else:
                print(print("no   |"+str(o.text.strip())+"|   |"+str(our_miles).strip()+"|"))
    if miles_sorted == False:
        print(9/0)



    ##############       months
    time.sleep(1)
    months_sorted = False
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , months_xp)))
    months = Select(driver.find_element_by_xpath(months_xp))
    months.select_by_visible_text(str(our_months))
    time.sleep(0.5)
    print(str(months.first_selected_option.text)+ "    selled ")
    if months.first_selected_option.text == str(our_months):
        months_sorted = True

    if months_sorted == False:
        time.sleep(1)
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , months_xp)))
        months = Select(driver.find_element_by_xpath(months_xp))
        print("months sel")
        months.select_by_visible_text(str(our_months))
        time.sleep(0.5)
        print(str(months.first_selected_option.text)+ "    selled ")
        if months.first_selected_option.text == str(our_months):
            months_sorted = True

    if months_sorted == False:
        print(len(months.options))
        print(str(months.first_selected_option.text)+ "   this still isnt what we want     "+str(our_months))
        print(5/0)


    time.sleep(1)
    set_months_up(driver, 3)
    time.sleep(0.5)
    set_months_up(driver, 3)
    calc_click_1 = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not calc_click_1:
        print("cc1 loop")
        calc_xp = '//*[@id="btn-calc-to-regularpayment"]'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , calc_xp)))
        calc = driver.find_element_by_xpath(calc_xp)
        click(calc)
        time.sleep(0.5)
        calc_click_1=True
        if datetime.datetime.now() > future:
            print(1/0)
    ############
    time.sleep(1)
    rental_got = False
    tstamp1 = datetime.datetime.now()
    future = tstamp1 +  datetime.timedelta(seconds = 130)
    while not rental_got:
        print(" not rental loop w 1")
        print(" not rental loop w t 1")
        rental_xp = '//*[@id="TotalRegularPayment"]'     # monthly rental
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , rental_xp)))
        print(" not rental loop w t 2")
        rental = driver.find_element_by_xpath(rental_xp).get_attribute('value')
        rental_got = True
    return rental

def get_prices(driver):
    last_price = 0
    prices=[]
    months_xp = '//*[@id="Term"]'
    #   //*[@id="Term"]/option[1]
    miles_xp = '//*[@id="AnnualMileage"]';
    maint_xp = '//*[@id="MaintenanceProvider"]/option[1]'
    no_maint_xp = '//*[@id="MaintenanceProvider"]/option[2]'
    month_options = []
    print("woah")

    for maint in range(2):

        if maint == 0:
            maint_txt = "Customer Maintained with RFL"
        if maint == 1:
            maint_txt =  "Alphabet with recovery"
        maint_sorted = False
        tstamp1 = datetime.datetime.now()
        future = tstamp1 +  datetime.timedelta(seconds = 130)
        while not maint_sorted:
            print("maint sorting loop")
            try:
                maint_sel_xp = '//*[@id="MaintenanceProvider"]'
                WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , maint_sel_xp)))
                maint = Select(driver.find_element_by_xpath(maint_sel_xp))
                maint.select_by_visible_text(maint_txt)
                if maint.first_selected_option.text == maint_txt:
                    maint_sorted = True
            except:
                print("exception in getting prices,    specifically maint")
            if datetime.datetime.now() > future:
                print(1/0)

        for miles in range(7):
            if miles == 0:
                our_miless = '6000'
            elif miles == 1:
                our_miless = '8000'
            elif miles == 2:
                our_miless = '10000'
            elif miles == 3:
                our_miless = '15000'
            elif miles == 4:
                our_miless = '20000'
            elif miles == 5:
                our_miless = '25000'
            elif miles == 6:
                our_miless = '30000'
            miles_sorted = False
            tstamp1 = datetime.datetime.now()
            future = tstamp1 +  datetime.timedelta(seconds = 130)
            while not miles_sorted:
                print("miles sorting loop")
                try:
                    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , miles_xp)))
                    miles = Select(driver.find_element_by_xpath(miles_xp))
                    miles.select_by_visible_text(our_miless)
                    if miles.first_selected_option.text == our_miless:
                        miles_sorted = True
                except:
                    print("exception in getting prices,    specifically miles")
                if datetime.datetime.now() > future:
                    print(1/0)


            for months in range(3):
                if months == 0:
                    our_months = "24";
                if months == 1:
                    our_months = "36";
                if months == 2:
                    our_months = "48";
                set_months_up(driver, 3);
                months_sorted = False
                tstamp1 = datetime.datetime.now()
                future = tstamp1 +  datetime.timedelta(seconds = 130)
                while not months_sorted:
                    print("months sorting loop")
                    try:
                        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , months_xp)))
                        months = Select(driver.find_element_by_xpath(months_xp))
                        months.select_by_visible_text(our_months)
                        if months.first_selected_option.text == our_months:
                            months_sorted = True
                    except:
                        print("exception in getting prices,    specifically months")
                    if datetime.datetime.now() > future:
                        print(1/0)
       #         for opt in month_options:
        #            print(our_months)
         #           print(opt.get_attribute('value'))
          #          if our_months == opt.get_attribute('value'):
           #             click(opt)
            #            print("clicking on " + str(opt.get_attribute('value')))

                set_months_up(driver, 3)

                calc_click_1 = False
                tstamp1 = datetime.datetime.now()
                future = tstamp1 +  datetime.timedelta(seconds = 130)
                while not calc_click_1:
                    print("cc1 loop")
                    try:
                        calc_xp = '//*[@id="btn-calc-to-regularpayment"]'
                        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , calc_xp)))
                        calc = driver.find_element_by_xpath(calc_xp)
                        click(calc)
                        time.sleep(0.5)
                        calc_click_1=True
                    except:
                        print("exception in getting prices,    specifically click 1")
                    if datetime.datetime.now() > future:
                        print(1/0)

                time.sleep(10)
                rental_got = False
                tstamp1 = datetime.datetime.now()
                future = tstamp1 +  datetime.timedelta(seconds = 130)
                while not rental_got:
                    print(" not rental loop w 1")
                    try:
                        print(" not rental loop w t 1")
                        rental_xp = '//*[@id="TotalRegularPayment"]'     # monthly rental
                        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , rental_xp)))
                        print(" not rental loop w t 2")
                        rental = driver.find_element_by_xpath(rental_xp).get_attribute('value')
                        print(" not rental loop w t 3")
                        if len(str(rental))>4:
                            print("       final   rental   below           ")
                            print(rental)
                            if last_price == rental:
                                print(1/0)
                            else:
                                last_price = rental
                            prices.append(rental)
                            rental_got = True
                    except:
                        print("exception in getting prices,    specifically prices")
                        #print(driver.page_source)
                        close_xp = '/html/body/div[2]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/div[4]/sr-price-breakdown/div/div/div/div[3]/button'
                        close_xp2 = '/html/body/div[3]/div[1]/quick-quote-proposal-mode/div/div/div[2]/quick-quote-proposal-actions/div[4]/sr-price-breakdown/div/div/div/div[3]/button'
                        try:
                            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , close_xp)))
                            close1 = driver.find_element_by_xpath(close_xp)
                        except:
                            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , close_xp2)))
                            close1 = driver.find_element_by_xpath(close_xp2)

                        click(close1)
                    if datetime.datetime.now() > future:
                        print(1/0)

    return prices


def double_check(driver,our_month, our_mile, maint,month_options,mile_options):

    print("making sure it got right mm , m n m")
    print(our_month)
    print(our_mile)
    print(maint)
    print("===========================================================")
    months_xp = '//*[@id="Term"]'
    miles_xp = '//*[@id="AnnualMileage"]';
    maint_xp = '//*[@id="MaintenanceProvider"]'

    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , months_xp)))
    current_m = driver.find_element_by_xpath( months_xp).get_attribute('value')
 #   print("checking months")
  #  print(our_month)
   # print(current_m)

    while current_m != our_month:
        for opt in month_options:
    #        print(our_month)
     #       print(opt.get_attribute('value'))
            if our_month == opt.get_attribute('value'):
                click(opt)
        current_m = driver.find_element_by_xpath( months_xp).get_attribute('value')


    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , miles_xp)))
    current_mil = driver.find_element_by_xpath(miles_xp).get_attribute('value')
#    print("checking months")
 #   print(our_mile)
  #  print(current_mil)
    while current_mil != our_mile:
        for opt in mile_options:

      #      print(our_month)
   #         print(" double checking mile ")
    #        print(our_mile)
     #       print(opt.get_attribute('value'))
            if our_mile == opt.get_attribute('value'):
                click(opt)
        current_mil = driver.find_element_by_xpath( miles_xp).get_attribute('value')


    maint_xp = '//*[@id="MaintenanceProvider"]';
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , maint_xp)))
    current_maint = driver.find_element_by_xpath(maint_xp).get_attribute('value')

    print("checking maint ")
    print(maint)
    print(current_maint)

    if maint == 1:
        while current_maint != "Customer Maintained with RFL":
            print(" bad maint ")
            no_maint_xp = '//*[@id="MaintenanceProvider"]/option[2]'
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , no_maint_xp)))
            no_maint_but = driver.find_element_by_xpath(no_maint_xp)
            click(no_maint_but)
            current_maint = driver.find_element_by_xpath(maint_xp).get_attribute('value')


    else:
        print(" maint is 0 ")
        print(current_maint)

    print("its got m m m nar ")
    print(current_m)
    print(current_mil)
    print(current_maint)



def reset_car_finder(driver):
    print(" abababababaababaabaaabbabaa uhhh mao mao mao, ba ba , ooo mao mao mao.")
    driver.get("https://identity.codeweavers.net/platform/alphabet/uk-car-line/app/showroom/login")

def reset_deriv_finder(driver, our_make, model, isvan):
    print("just getting a fresh deriv, keeping old make n model")
    reset_car_finder(driver)
    click_calculator(driver)
    if isvan:
        click_lcv(driver)
    reenter_this_make(driver , our_make)
    reenter_this_model(driver, model)



def reenter_this_model(driver, model):
    print(" re enter model      =" + str(model))
    xp1 = '//*[@id="Model-input-element"]/option['
    model_options = []
    top_num = 43
    try:
        xp1a = '//*[@id="Model-input-element"]/option[21]'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xp1a)))
        found_model = driver.find_element_by_xpath(xp1a)
    except:
        top_num = 21
    try:
        xp1a = '//*[@id="Model-input-element"]/option[6]'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xp1a)))
        found_model = driver.find_element_by_xpath(xp1a)
    except:
        top_num = 6

    for i in range(top_num):
        xpath_opt = xp1+str(i)+']'
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xpath_opt)))
            found_model = driver.find_element_by_xpath(xpath_opt)
            model_options.append(found_model)
        except:
            print("arse aaa ")
            print(xpath_opt)
            pass

    for j in model_options:
        print(j.get_attribute('innerHTML'))
        if j.get_attribute('innerHTML').lower() == model.lower():
            correct_make = j

    click(correct_make)






def reenter_this_make(driver, make1):
    print(" re enter this make  " + str(make1))
    xp1 = '//*[@id="Manufacturer-input-element"]/option['
    make_options = []
    top_num = 43
    try:
        xp1a = '//*[@id="Manufacturer-input-element"]/option[21]'
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xp1a)))
        found_make = driver.find_element_by_xpath(xp1a)
    except:
        top_num = 21

    for i in range(top_num):
        xpath_opt = xp1+str(i)+']'
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xpath_opt)))
            found_make = driver.find_element_by_xpath(xpath_opt)
            make_options.append(found_make)
        except:
            print("arse aaa ")
            print(xpath_opt)
            pass


    for j in make_options:
        print(j.get_attribute('innerHTML'))
        if j.get_attribute('innerHTML').lower() == make1.lower():
            correct_make = j

    click(correct_make)



def models_helper(model_a, deriv=""):
    if model_a == "E-NIRO":
        print(" fuck ")
        return "Niro"
    print("replacing   quelchy ")

    equivs = equivelants(deriv)
    if len(equivs)>0:
        for zz in range(len(equivs)):
            print("replacing")
            deriv = deriv.replace(equivs[zz]["list_of_sames"][0], equivs[zz]["list_of_sames"][1], 1)
            print(equivs[zz]["list_of_sames"][0])
            print(equivs[zz]["list_of_sames"][1])
        print(model_a + " " + deriv)
        print("replacing   quelchy meh  ")
    #    time.sleep(999)
        return(model_a + " " + deriv)

    else:
        print("replacing   quelchy    lasty ")
        raise Exception("no good comparison ")
