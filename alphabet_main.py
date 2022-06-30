import time
from alphabet.scrapper_tools import *
import datetime

# our_capcode, our_make, our_model, our_deriv , our_months, our_miles, our_months_up, our_otr,our_blp, our_maint , our_arval_login, our_arval_password , d , proc_num
def alphabet_single_loop(our_capcode, our_make, our_model, our_deriv , our_months, our_miles, our_months_up, our_otr,our_blp, our_maint , login, password , shared_dict , proc_num , pause  , our_metallic):
 #   try:
    print("in alphabet")
    t5k_index = "notset"
    for o in range(len(our_miles)-1):
        print(our_miles[o])
        if str(our_miles[o]) == "5000":
            t5k_index = o
            print("this index ")
    if t5k_index != "notset":
        print("this index fixed")
        our_miles[t5k_index] = "6000"
    if str(our_miles[0]) == "5000":
        our_miles[0] = "6000"
        
    print(our_miles[0]+"   =      "+str(type(our_miles[0])))
    
    diy_file = pd.read_csv("diy_alphabet.csv")
    diy_match = False
    our_blp = our_blp.replace(",","")
    for kl in range(diy_file.shape[0]) :
        if diy_file['capcode'].iloc[kl].strip().lower() == our_capcode.strip().lower():
            print("match_start")
            diy_match = True
            diy_man = diy_file['make'].iloc[kl]
            diy_model = diy_file['model'].iloc[kl]
            diy_deriv = diy_file['deriv'].iloc[kl]
            diy_car_or_van = diy_file['car or van'].iloc[kl]
            lastspace_n_num_pos = 0
            pos = 0
            for char in diy_deriv:
                try:
                    if diy_deriv[pos] == " ":
                        if diy_deriv[pos+1].isdigit():
                            lastspace_n_num_pos= pos
                except:
                    pass
                pos += 1
            diy_my = diy_deriv[lastspace_n_num_pos:].strip()
            diy_deriv = diy_deriv[:lastspace_n_num_pos]
            diy_blp = our_blp
            print("match ")

    if diy_match == False:
        shared_dict[proc_num] = ["alphabet" , "no match"]
        return;

    print("al1")
    driver1 = open_alphabet(login, password)
    print("al2")
    wait_until_front_page(driver1)
    print("al3")
    new_driver_sorted = True
    print("al4")
    click_calc2(driver1)
    print("al5")
    switch_to_iframe_1(driver1)
    print("al6")
    time.sleep(5)
#                        click_lcv6(driver1)

    
    if type(diy_car_or_van) == float:
        xp = '//*[@id="asset-lookup-modal"]/div/div/div[2]/asset-lookup-selection/div/asset-lookup-type/div/div[2]/button'
        WebDriverWait(driver1,10).until(EC.presence_of_element_located((By.XPATH , xp)))
        lcv_button1 = driver1.find_element_by_xpath(xp)
        lcv_button1.click()
        time.sleep(3)

 #   try:
    diy_man = find_this_make_2(our_capcode )
   # except:
    #    shared_dict[proc_num] = ["alphabet" , " doesnt know make  "]
     #   return;
    try:
        choose_man_1(driver1, diy_man)
    except:
        shared_dict[proc_num] = ["alphabet" , " failed finding make  " ]
        return;
    try:
        choose_model_1(driver1, diy_model)
    except:
        shared_dict[proc_num] = ["alphabet" , " failed to find the model  " ]
        return;
    try:
        choose_deriv_1(driver1, diy_deriv , diy_man, diy_model)
    except:
        shared_dict[proc_num] = ["alphabet" , " failed to find the deriv  " ]
        return;

    try:
        choose_my_1(driver1 , diy_my)
 #       print("al7")
        deriv_found = blp_check_1(driver1, diy_blp)
    except:
        shared_dict[proc_num] = ["alphabet" , " failed to find my "  ]
        return;

    if pause:
        shared_dict[proc_num] = ["alphabet" , " now paused "  ]
        return;

    if our_metallic:
        add_metallic_paint(driver1)

  #  print("al8")
    try:
        enter_otr(driver1, our_otr)
    except:
        shared_dict[proc_num] = ["alphabet" , " failed entering otr "  ]
        return;
 #   print("al9")    
    set_months_up(driver1, 3);
  #  print("al10")
    prices = []
    
    for ma in our_maint:
        for mi in our_miles:
            for mo in our_months:
                price = get_this_prices(driver1, mo, mi, our_months_up , ma)
                prices.append(price)
 #   print("al11")
    if type(shared_dict) == str:
        print("finishing non multiproccesed alpha")
        return prices;
    else:
        print("finishing multiproccesed alpha")
        shared_dict[proc_num] = ["alphabet" , prices ]
        return;
    shared_dict[proc_num] = ["alphabet" , "final weird error" ]
    return;
#    except Exception as e:
 #       shared_dict[proc_num] = ["alphabet" , "big error   "+str(e) ]
  #      return;
