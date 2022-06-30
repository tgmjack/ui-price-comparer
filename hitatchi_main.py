from hitatchi.hitachi_scraper_tools import *




def hitatchi_single_loop(our_capcode, our_make, our_model, our_deriv , our_months, our_miles, our_months_up, our_otr,our_blp, our_maint , login, password, shared_dict , proc_num , pause  , our_metallic):
    comp_found = False
    print(" hit loop start ")
    comps = get_comp()
    for comp in comps:
        if not comp_found:
            if comp.capcode.strip() == our_capcode.strip():
                comp_found = True
                print("found comp")
                diy_blp = comp.blp
                diy_make = comp.make
                diy_model = comp.model
                diy_deriv = comp.deriv
                diy_my = comp.my
                diy_deriv = diy_deriv + " (£" + str(diy_blp.replace(".00",""))  + ") ("+ str(diy_my) + ")"
                cap_id = comp.cap_id

    if comp_found:
        print("got comp")
        driver1 = initial_setup()
        try:
            log_in(driver1, login , password)
            start_new_quote_1(driver1)
        except:
            shared_dict[proc_num] = ["hitatchi" ,"failed while logging in" ]
            return;
        try:
            enter_cap_id(driver1, cap_id)
        except:
            shared_dict[proc_num] = ["hitatchi" ,"failed while entering id"  ]
            return;
        try:
            enter_date(driver1)
        except:
            shared_dict[proc_num] = ["hitatchi" ,"failed while entering date"  ]
            return;
        try:
            car_chosen = double_check_car(driver1, diy_blp)
            if car_chosen == False:
                shared_dict[proc_num] = ["hitatchi" ," something went wrong probably blp miss match in comp file" ]
                return;
        except:
            shared_dict[proc_num] = ["hitatchi" ,"failed while double checking car" ]
            return;


        if car_chosen:
            print("br2")
#            car_chosen = options_chooser3(driver1)
            try:
                time.sleep(1)
                wait_until_done_loading(driver1)
                default_opts_button_xp = '//*[@id="btDefaultQuote"]'
                WebDriverWait(driver1,1).until(EC.presence_of_element_located((By.XPATH,default_opts_button_xp)))
                def_button  = driver1.find_element_by_xpath(default_opts_button_xp)
                click(def_button)
                time.sleep(1)
                wait_until_done_loading(driver1)
                time.sleep(1)
                wait_until_done_loading(driver1)
                everything_screwed = False
            except:
                shared_dict[proc_num] = ["hitatchi" ,"failed after finding car but before prices" ]
                return;

      #      else:
       #         car_chosen = options_chooser_special(driver1)
        #    print("br3")
            if car_chosen == False:
                everything_screwed = True
                error_reason = " options chooser "
                print("everythingh screwed  opts  98989898  ")
                shared_dict[proc_num] = ["hitatchi" ,"options chooser fail"  ]
                return;
        else:
            everything_screwed = True
            error_reason = " entering cap_id "
            print("everythingh screwed  id 98989898  ")
            shared_dict[proc_num] = ["hitatchi" ,"no comparison" ]
            return;
    else:
        everything_screwed = True
        print("everythingh screwed   because no comp file  8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888  ")
        shared_dict[proc_num] = ["hitatchi" ,"no comparison" ]
        return;
    if car_chosen and not everything_screwed:
        if pause:
            shared_dict[proc_num] = ["hitatchi" ," now paused " ]
            return;
        if not everything_screwed:
            van_txt = "not set"
            try:
                van = check_van(driver1)
                if van:
                    for j in range(10):
                        print(str(j)+ "             j ")
                  #  time.sleep(9999)
            except:
                everything_screwed = True
                error_reason = " van "
                print("everythingh screwed van ")

                shared_dict[proc_num] = ["hitatchi" ,"failed van" ]
                return;

            if our_metallic == True:
                try:
                    our_extras_xp = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/form/div[11]/div[5]' 
                    WebDriverWait(driver1,1).until(EC.presence_of_element_located((By.XPATH,our_extras_xp)))
                    extras  = driver1.find_elements_by_xpath(our_extras_xp)[0]
                    opt1 = extras.find_elements_by_tag_name("div")[0]
                    name = extras.find_elements_by_tag_name("span")[0].get_attribute("innerHTML")
                    
                    new_metalic_extras_function(driver1 ,  name)
                    print("spesh ops  done ")
              #      time.sleep(999)
                except:
                    print(" failed choosing metallic ")
                    shared_dict[proc_num] = ["hitatchi" ,"failed choosing metallic " ]
                    return;

            if our_metallic == False:
                if '<input type="button" id="btDefaultQuote" class="tooltip btn-gray-125" value="Default Quote" title="Default Quote" disabled="">' in driver1.page_source:
                    print("good button ting hhhhh")
                elif '<input type="button" id="btDefaultQuote" class="tooltip btn-red-125" value="Default Quote" title="Default Quote">' in driver1.page_source:
                    default_opts_button_xp = '//*[@id="btDefaultQuote"]'
                    WebDriverWait(driver1,1).until(EC.presence_of_element_located((By.XPATH,default_opts_button_xp)))
                    def_button  = driver1.find_element_by_xpath(default_opts_button_xp)
                    click(def_button)
                    time.sleep(1)
                    wait_until_done_loading(driver1)
                    time.sleep(1)
                    wait_until_done_loading(driver1)
                    everything_screwed = False
                    if '<input type="button" id="btDefaultQuote" class="tooltip btn-gray-125" value="Default Quote" title="Default Quote" disabled="">' in driver1.page_source:
                        pass
                    elif '<input type="button" id="btDefaultQuote" class="tooltip btn-red-125" value="Default Quote" title="Default Quote">' in driver1.page_source:
                        options_chooser(driver1)
                        time.sleep(1)
                        wait_until_done_loading(driver1)

                        if '<input type="button" id="btDefaultQuote" class="tooltip btn-gray-125" value="Default Quote" title="Default Quote" disabled="">' in driver1.page_source:
                            pass
                        elif '<input type="button" id="btDefaultQuote" class="tooltip btn-red-125" value="Default Quote" title="Default Quote">' in driver1.page_source:
                            options_chooser(driver1)
                            time.sleep(1)
                            wait_until_done_loading(driver1)
            #else:
#                options_chooser_special(driver1)


            time.sleep(0.5)
            try:
                print("   init terms  ")
                dismiss_warning_pop_up(driver1)
                sort_init_terms(driver1, van)
            except:
                shared_dict[proc_num] = ["hitatchi" ,"failed init terms" ]
                return;
            
            if not everything_screwed:

                try:
                    print("bef enter otr check ")
                    enter_otr(driver1, our_otr)
                except:
                    everything_screwed = True
                    error_reason = " otr "
                    print("everythingh screwed  otr  ")
                    shared_dict[proc_num] = ["hitatchi" ,"otr enter error"  ]
                    return;
        print("big br 1")
        if not everything_screwed:
            try:
                time.sleep(1)
                wait_until_done_loading(driver1)
            except:
                everything_screwed = True
                error_reason = " little wait  "
                print("everythingh screwed  little wait ")
                shared_dict[proc_num] = ["hitatchi" ,"otr enter error" ]
                return;
        print("big br 2")
        if not everything_screwed:
            try:
                prices = []
                for ma in our_maint:
                    for mi in our_miles:
                        for mo in our_months:
                            price = get_prices_special(driver1 , our_blp , mo, mi, our_months_up, ma)
                            prices.append(price)
                print("---------------------------------  hhhhhhhh")
                for p in prices:
                    print(str(p)+"---------------------------------  hhhhhhhh")
                print("---------------------------------   hhhhhhhgyfgfgf ")

                print("   hit ")
            except:
                print("failed getting prices")
                shared_dict[proc_num] = ["hitatchi" ,"failed getting prices" ]
                return;
        print("big br 3")
        if type(shared_dict) == str:
            print("finishing non multiproccesed hit")
            return;
        else:
            print("finishing multiproccesed hit")
            try:
                shared_dict[proc_num] = ["hitatchi" , prices ]
            except:
                shared_dict[proc_num] = ["hitatchi" , " failed returning prices " ]
            return;
        print("big br 3")
    if type(shared_dict) == str:
        print("finishing non multiproccesed hit")
        return;
    else:
        print("finishing multiproccesed hit")
        shared_dict[proc_num] = ["hitatchi" , prices ]
        return;
