from arval.scraper_tools2 import *
from arval.excel_handler import *
from arval.config import *
##### get the href and pull out the num from the a tag.
##### then check if that id has correct style

def ensure_metallic(driver , extras):
    amend_options_xp = '//*[@id="buttonAmendOptions"]/tbody/tr/td[2]/a'
    WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,amend_options_xp)))
    ammend = driver.find_element_by_xpath(amend_options_xp)

    ammend.click()
    time.sleep(1)
    wait_for_loading(driver)
    time.sleep(1)
    extras_list_id = '//*[@id="divMain"]/table[1]/tbody/tr[6]/td/table'
    q_opts = driver.find_element_by_xpath(extras_list_id)
    every_tr = q_opts.find_elements_by_tag_name("tr")

    for e in extras:
        print(e)

########## find metallic 
    categoryies_id = 'tbloptions'
    xp = '//*[@id="divMain"]/table[1]/tbody/tr[6]/td/table/tbody/tr[8]/td[1]/a'
    extras_categories_xp = '//*[@id="divMain"]/table[1]/tbody/tr[6]/td/table/tbody'
    table = driver.find_element_by_xpath(extras_categories_xp)
    categories = table.find_elements_by_tag_name("tr")
    metallic_found =False
    metallic_category = ""
    metallic_category_name = ""
    a_tag_href = ""
    for i in categories:
        if metallic_found == False:
            try:
                A = i.find_elements_by_tag_name("td")[0]
                B = A.find_elements_by_tag_name("a")[0]
                if 'metallic' in B.get_attribute("innerHTML").lower():
              #      if ">0.00" in i.get_attribute("innerHTML"):
                    metallic_found =True
                    metallic_category = i
                    A = i.find_elements_by_tag_name("td")[0]
                    print("yay1 ")
                    B = A.find_elements_by_tag_name("a")[0]
                    metallic_a_tag = B
                    a_tag_href = metallic_a_tag.get_attribute("href")
                    metallic_category_name = B.get_attribute("innerHTML").lower()
                    print("yoooooooooooo hooooooooooo "+str(i.get_attribute("innerHTML").lower()))
            except:
                pass
    print("a_tag_href bef  = "+str(a_tag_href))
    a_tag_href = a_tag_href.replace("javascript:toggleoptions('","").replace("');","")
    print("free_category_name = "+str(metallic_category_name))
    print("a_tag_href = "+str(a_tag_href))


#########   remov extras 
    extras_categories_xp = '//*[@id="divMain"]/table[1]/tbody/tr[6]/td/table/tbody'
    table = driver.find_element_by_xpath(extras_categories_xp)
    categories = table.find_elements_by_tag_name("tr")
    for e in extras:
        for i in categories:
            found = False
            try:
                A = i.find_elements_by_tag_name("table")[0]
                print("yay1 ")
                B = A.find_elements_by_tag_name("tbody")[0]
                print("yay2 ")
                found = True
            except:
                pass
            if found:
                print(B.get_attribute("innerHTML"))
                C = B.find_elements_by_tag_name("tr")[0]
                print("yay3 ")
                name = C.find_elements_by_tag_name("td")[1].get_attribute("innerHTML")
                if e in name:
                    print("yay4 ")
                    A = i.find_elements_by_tag_name("table")[0]
                    B = A.find_elements_by_tag_name("tbody")[0]
                    print("yay5 ")
                    C = B.find_elements_by_tag_name("tr")[0]
                    D = C.find_elements_by_tag_name("td")[0].click()
                    time.sleep(1)
                    wait_for_loading(driver)
                    time.sleep(1)



####### now click a metallic 
    id_ting = "tblOptions"+a_tag_href
    D = driver.find_element_by_id(id_ting)
    print(D.get_attribute("innerHTML"))
    print(D.get_attribute("style"))
    while "display: none;" in D.get_attribute("style"):
        time.sleep(5)
        metallic_a_tag.click()
        print("its in")

    # D > table / body >>>>> rows 
    E = D.find_elements_by_tag_name("table")[0]
    F = E.find_elements_by_tag_name("tbody")[0]
    rows = F.find_elements_by_tag_name("tr")
    metallic_paint_chosen = False
    the_metallic_paint_chosen = "none"
    best_price = 9999999999
    best_extra = 'not_set'
    for tr in rows:
        tds = tr.find_elements_by_tag_name("td")
        extra_price = float(str(tds[2].get_attribute("innerHTML")).replace("&nbsp;","").strip())
        if extra_price < best_price:
            best_price = extra_price
            the_tr = tr
        

    if not metallic_paint_chosen:
        tds = the_tr.find_elements_by_tag_name("td")
        tds[0].click()
        metallic_paint_chosen = True            
        the_metallic_paint_chosen = tds[1].get_attribute("innerHTML")

    return metallic_paint_chosen , the_metallic_paint_chosen







def remove_these_extras(driver , extras):
    amend_options_xp = '//*[@id="buttonAmendOptions"]/tbody/tr/td[2]/a'
    WebDriverWait(driver,25).until(EC.presence_of_element_located((By.XPATH,amend_options_xp)))
    ammend = driver.find_element_by_xpath(amend_options_xp)

    ammend.click()
    time.sleep(1)
    wait_for_loading(driver)
    time.sleep(1)
    extras_list_id = '//*[@id="divMain"]/table[1]/tbody/tr[6]/td/table'
    q_opts = driver.find_element_by_xpath(extras_list_id)
    every_tr = q_opts.find_elements_by_tag_name("tr")

    for e in extras:
        print(e)





#####   check for free # n save it category name 

    categoryies_id = 'tbloptions'
    xp = '//*[@id="divMain"]/table[1]/tbody/tr[6]/td/table/tbody/tr[8]/td[1]/a'
    extras_categories_xp = '//*[@id="divMain"]/table[1]/tbody/tr[6]/td/table/tbody'
    table = driver.find_element_by_xpath(extras_categories_xp)
    categories = table.find_elements_by_tag_name("tr")
    free_found =False
    free_category = ""
    free_category_name = ""
    a_tag_href = ""
    for i in categories:
        if free_found == False:
            try:
                A = i.find_elements_by_tag_name("td")[0]
                B = A.find_elements_by_tag_name("a")[0]
                if 'paint' in B.get_attribute("innerHTML").lower():
                    if ">0.00" in i.get_attribute("innerHTML"):
                        free_found =True
                        free_category = i
                        A = i.find_elements_by_tag_name("td")[0]
                        print("yay1 ")
                        B = A.find_elements_by_tag_name("a")[0]
                        free_a_tag = B
                        a_tag_href = free_a_tag.get_attribute("href")
                        free_category_name = B.get_attribute("innerHTML").lower()
                        print("yoooooooooooo hooooooooooo "+str(i.get_attribute("innerHTML").lower()))
            except:
                pass
    print("a_tag_href bef  = "+str(a_tag_href))
    a_tag_href = a_tag_href.replace("javascript:toggleoptions('","").replace("');","")
    print("free_category_name = "+str(free_category_name))
    print("a_tag_href = "+str(a_tag_href))
#    time.sleep(9999999999)


        
    ## remove selected stuff
    
    extras_categories_xp = '//*[@id="divMain"]/table[1]/tbody/tr[6]/td/table/tbody'
    table = driver.find_element_by_xpath(extras_categories_xp)
    categories = table.find_elements_by_tag_name("tr")
    for e in extras:
        for i in categories:
            found = False
            try:
                A = i.find_elements_by_tag_name("table")[0]
                print("yay1 ")
                B = A.find_elements_by_tag_name("tbody")[0]
                print("yay2 ")
                found = True
            except:
                pass
            if found:
                print(B.get_attribute("innerHTML"))
                C = B.find_elements_by_tag_name("tr")[0]
                print("yay3 ")
                name = C.find_elements_by_tag_name("td")[1].get_attribute("innerHTML")
                if e in name:
                    print("yay4 ")
                    A = i.find_elements_by_tag_name("table")[0]
                    B = A.find_elements_by_tag_name("tbody")[0]
                    print("yay5 ")
                    C = B.find_elements_by_tag_name("tr")[0]
                    D = C.find_elements_by_tag_name("td")[0].click()
                    time.sleep(1)
                    wait_for_loading(driver)
                    time.sleep(1)

 #   time.sleep(999999)
    

    #### click free solid      #### change to the free one 
    extras_categories_xp = '//*[@id="divMain"]/table[1]/tbody/tr[6]/td/table/tbody'
    table = driver.find_element_by_xpath(extras_categories_xp)
    categories = table.find_elements_by_tag_name("tr")
    free_paint_chosen =False


#    try:
 #       print("yo 2sdasasa")
  #      paints = free_category.find_elements_by_tag_name("tr")
   #     for sp in paints:
    #        print("yo 1aaa")
     #       tds = sp.find_elements_by_tag_name("td")
      #      if '0.00' in tds[2].get_attribute("innerHTML") and free_paint_chosen == False:
       #         tds[0].find_elements_by_tag_name("input")[0].click()
        #        free_paint_chosen = True
         #   else:
#          #      print(tds[2].get_attribute("innerHTML") + str("APPARENTLY NOT "))
 #       if not free_paint_chosen:
  #          print("yo eta fffff  "+str(free_category.find_elements_by_tag_name("a").get_attribute("innerHTML")))
   #         print(1/0)
#    except:




    ### ensure free category is open 
    id_ting = "tblOptions"+a_tag_href
    D = driver.find_element_by_id(id_ting)
    print(D.get_attribute("innerHTML"))
    print(D.get_attribute("style"))
    while "display: none;" in D.get_attribute("style"):
        time.sleep(5)
        free_a_tag.click()
        print("its in")



    # D > table / body >>>>> rows 
    E = D.find_elements_by_tag_name("table")[0]
    F = E.find_elements_by_tag_name("tbody")[0]
    rows = F.find_elements_by_tag_name("tr")
    free_paint_chosen = False
    the_free_paint_chosen = "none"
    for tr in rows:
        print(tr.get_attribute("innerHTML"))
        if not free_paint_chosen:
            tds = tr.find_elements_by_tag_name("td")
            for t in tds:
                print("a td yo ")
                print(t.get_attribute("innerHTML"))
            if ("0.00" in tds[2].get_attribute("innerHTML")):
                tds[0].click()
                free_paint_chosen = True            
                the_free_paint_chosen = tds[1].get_attribute("innerHTML")
   

    return free_paint_chosen , the_free_paint_chosen

def remove_extras(driver , our_metallic):
    print("br 0a")
    # detect if paint is free or has more than 1
    time.sleep(0.5)
    wait_for_loading(driver)
    time.sleep(0.5)
 #   try_to_move_into_frame(driver)
    print("br1")
    extras_list_id = 'tblExtrasFactory'; # //*[@id="tblExtrasFactory"]/tbody/tr/td[1]
    try:
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,extras_list_id)))
    except:
        driver.switch_to.default_content()
        time.sleep(0.5)
        try_to_move_into_frame(driver)
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,extras_list_id)))
    print("br 2")
    q_opts = driver.find_element_by_id(extras_list_id)
    the_opts = q_opts.find_elements_by_tag_name("tr")
    actual_opts = []
    for o in the_opts:
        list1 = o.find_elements_by_tag_name("td")
        for l in list1:
            txt = l.get_attribute("innerHTML")
            actual_opts.append(txt)

    print("brr")
    for l in actual_opts:
        for o in l:
            print(o)


    
    print(str(len(the_opts))+"        the_opts  ")
    if len(the_opts) > 0:
        if our_metallic == False:
            removed , free_paint = remove_these_extras(driver , actual_opts)
        else:
            removed , free_paint =ensure_metallic(driver , actual_opts)

        
    if removed:
        time.sleep(1)
        wait_for_loading(driver)
        time.sleep(0.5)
        return_xp = '//*[@id="divMain"]/table[2]/tbody/tr/td[3]/table/tbody/tr/td[2]/a'
        driver.find_element_by_xpath(return_xp).click()
        time.sleep(0.5)
        wait_for_loading(driver)
        time.sleep(0.5)
        return True
    else:
        print(9/0)



def arval_single_loop(our_capcode, our_make, our_model, our_deriv , our_months, our_miles, our_months_up, our_otr,our_blp, our_maint , our_arval_login, our_arval_password, shared_dict, proc_num , pause  , our_metallic):
    print("arval set up ")
    driver1 = setup()
    print("arval has set up ")
    print(our_months_up)
    loginandquote(driver1,our_arval_login,our_arval_password, "WP Contract Hire New")
    try:
        capcode_entered = enter_this_capcode(our_capcode, driver1, our_months_up ,  "WP Contract Hire New" )
    except Exception as e:   
        if "Cap code not found or is invalid for this MLA" in str(e):
            shared_dict[proc_num] = ["arval" , "no capcode match"]
            return;
        else:
            print(e)
            print(e.message)
            print(e.Message)
            while 1 == 1:
                print("fix this 1111111 ")
            print(9/0)
    
    print(" bart ")
    if pause:
        print("arval pause ready")
        shared_dict[proc_num] = ["arval" , " now ready "  ]
        return;
    enter_otr(driver1, our_otr )
    print("entered otr   99999999999999999999999999999999999999999")
    remove_breakdown_ass(driver1)
    print("remove brek 9999999999999999999999999999")
    try_dismiss_wltp(driver1)
    remove_extras(driver1 , our_metallic)
    print("dis wltp 9999999999999999999999999999999999999999")

    prices = []
    for ma in our_maint:
        for mi in our_miles:
            for mo in our_months:
                price = get_this_price(driver1 , mo, mi, ma)
                prices.append(price)
            
    print("got price 999999999999999999    "+str(prices))
    if type(shared_dict) == str:
        print("returning")
        return prices
    print("returning    via dict ")

    if type(shared_dict) == str:
        print("finishing non multiproccesed arval")
        return;
    else:
        print("finishing multiproccesed arval")
        shared_dict[proc_num] = ["arval" , prices  ]
        return;

    
