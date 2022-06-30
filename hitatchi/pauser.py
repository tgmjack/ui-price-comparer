from excel_handler import *
from hitachi_scraper_tools import *




def hitatchi_main_loop(cars, comps , round_attempt):
    last_prices = 0
    deals = []
    bad_capcodes = []
    last_qn = "first"
    qn = "first"
    for car in cars:
        print(car.capcode)
    car_num = 0
    for car in cars:
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(" start of car num  = "+str(car_num)+"         round attempt "+str(round_attempt))
        
        car_num +=1
        car_chosen = False
        everything_screwed =False
        error_reason = "not_found"
        comp_found = False
        print("find comp")

        try:
            for comp in comps:
                if not comp_found:
                    if comp.capcode.strip() == car.capcode.strip():
                        comp_found = True
                        print("found comp")
                        diy_blp = comp.blp
                        diy_make = comp.make
                        diy_model = comp.model
                        diy_deriv = comp.deriv
                        diy_my = comp.my
                        diy_deriv = diy_deriv + " (£" + str(diy_blp.replace(".00",""))  + ") ("+ str(diy_my) + ")"


            if comp_found:

                driver1 = initial_setup()
                log_in(driver1)
                start_new_quote_1(driver1)

                
         #       try:
                print("inputing "+str(diy_make))
                choose_make(driver1, diy_make)
                print("inputing "+str(diy_model))
                choose_model(driver1, diy_model)
                print("inputing "+str(diy_deriv))
                car_chosen = choose_deriv(driver1, diy_deriv ,diy_blp  , round_attempt)
          #      except:
           #         everything_screwed = True
            #        error_reason = " finding car "
             #       print("everythingh screwed choosing model")
            else:
                everything_screwed = True
                error_reason = " no comparison "
                print("everythingh screwed   98989898  ")

            if car_chosen and not everything_screwed:
                if not everything_screwed:
                    try:
                        van = check_van(driver1)
                        time.sleep(999)
                    except:
                        everything_screwed = True
                        error_reason = " van "
                        print("everythingh screwed van ")

             #           print("aft van check ")
           #         try:
                    time.sleep(0.5)
                    sort_init_terms(driver1, van)
              #          print("aft init check ")
            #        except:
             #           print("everythingh screwed ")
              #          everything_screwed = True
               #         error_reason = " init terms "

                    if not everything_screwed:
                        
                        try:
                            print("bef enter otr check ")
                               
                            enter_otr(driver1, car.otr)
               #             print("aft enter otr check ")
                        except:
                            everything_screwed = True
                            error_reason = " otr "
                            print("everythingh screwed  otr  ")

                if not everything_screwed:
                    try:
                        time.sleep(1)
                        wait_until_done_loading(driver1)
                    except:
                        everything_screwed = True
                        error_reason = " little wait  "
                        print("everythingh screwed  little wait ")


                prices , qn = get_prices(driver1, van , diy_blp)
                prices2 = []
                for p1 in prices:
                    clean_price = ""
                    for char in p1:
                        if char.isdigit() or char == ".":
                            clean_price+=char
                    prices2.append(clean_price)
                prices = prices2
                                    
                #        count = 0
                 #       print("prices got = below xxaass")
                  #      for p in prices:
                   #         print(count)
                    #        print(p)
            #    count+=1
                  #  except:
                   #     everything_screwed = True
                    #    error_reason = " getting prices  "
                     #   print("everythingh screwed  geting price ")

                if not everything_screwed:
                    if prices == last_prices:
                        everything_screwed = True
                        error_reason = " big prices copy  "
                        print("everythingh screwed  copy")
                        
                    else:
                        print("prices aint last prices ")
                        price_copy_counter = 0
                        try:
                            for p_counter in prices-1:
                                if prices[p_counter] == last_prices[p_counter]:
                                    price_copy_counter += 1 
                                    print(" 1 price copy ")
                        except:
                            print(" cant check each price")

                        if price_copy_counter > 10:
                            print("copies 666666 ")
                            print(1/0)
                        last_prices = prices

                if not everything_screwed:
                    try:
                        their_deriv = get_their_deriv(driver1)
                    except:
                        everything_screwed = True
                        error_reason = " getting their deriv  "
                        print("everythingh screwed 66 ")

                if not everything_screwed:
                    try:
                        opts = get_options(driver1)
                    except:
                        everything_screwed = True
                        error_reason = " getting opts  "
                        print("everythingh screwed 66 ")
            
                    print(str(opts)+ " these are the bloody opts")
                half_num_of_prices = 20
                if not everything_screwed:
                    if last_qn == qn:
                        everything_screwed = True
                        error_reason = " qn copy  "
                        print("everythingh screwed qn ")
                    

                    if not van:
                        mile_n_months = [['24', '5000'],['36', '5000'],['48', '5000'],['24', '8000'],['36', '8000'],['48', '8000'],['24', '10000'],['36', '10000'],['48', '10000'],['24', '15000'],['36', '15000'],['48', '15000'],['24', '20000'],['36', '20000'],['48', '20000'],['24', '25000'],['36', '25000'],['48', '25000'],['24', '30000'],['36', '30000']]
                        half_num_of_prices = 20
                        print("not a van")
                        van_txt = 'not a van'

                    if van:
                        mile_n_months = [['24', '10000'],['36', '10000'],['48', '10000'],['24', '15000'],['36', '15000'],['48', '15000'],['24', '20000'],['36', '20000'],['48', '20000'],['24', '25000'],['36', '25000'],['48', '25000'],['24', '30000'],['36', '30000']]
                        half_num_of_prices = 15
                        print(" a van")
                        van_txt = 'a van'
                    if not everything_screwed:

                        months = 0
                        miles = 0 


                        for dd in range(len(mile_n_months)):
                            try:
                                print(str(dd)+"     counter for price ")
                                print(prices[dd+half_num_of_prices])                        
                                just_skipped = False
                                themonths = mile_n_months[dd][0]
                                themiles = mile_n_months[dd][1]
                                deals.append(deal_pair_qn(car.capcode,themonths,themiles , prices[dd+half_num_of_prices].replace("Â£",""),prices[dd].replace("Â£",""), str(opts)+ " these are the bloody opts" , qn, their_deriv, car.otr , van_txt ))
                            except:
                                print(str(dd)+"                bad counter  ")                    

        except:
            everything_screwed = True
            error_reason = " big error   "
            print("everythingh screwed ")
        if not everything_screwed:
            if last_qn == qn:
                everything_screwed = True
                error_reason = " qn copy  "
                print("everythingh screwed qn ")
        last_qn = qn
            
        
        if everything_screwed:
            print("  saving this bad capcode      888888888      ")
            bad_capcodes.append(deal_pair_qn(car.capcode,'months','miles','maintprice', 'nomaintprice',' options ', error_reason , 'not got ' , car.otr  , van_txt))
        try:
            save_what_we_got_qn(' hitatchi prices round = '+str(round_attempt),deals)
        except:
            save_what_we_got_qn(' hitatchi   spare close other   prices round = '+str(round_attempt),deals)
        try:
            save_what_we_got_qn(' badcapcode prices round = '+str(round_attempt),bad_capcodes)
        except:
            save_what_we_got_qn(' badcapcode   spare close other    prices round = '+str(round_attempt),bad_capcodes)
        try:
            driver1.quit()
        except:
            pass
        try:
            driver1.close()
        except:
            pass

        


    try:
        driver1.quit()
    except:
        pass
    try:
        driver1.close()
    except:
        pass
    return bad_capcodes;

        
print("very start")
cars1 = get_cars()
print(" getting comps")
comps = get_comp()
print(" got comps ")



matches = []
notmatches = []
for car in cars1:
    match_got = False
    for comp in comps:
        if not match_got:
            if comp.capcode.strip() == car.capcode.strip():
                match_got = True
                
    if not match_got:
        notmatches.append(car)
    else:
        matches.append(car)
print("to get 1 ")
for i in matches:
    print(str(i)+ "    match 1  ")

cars1 = matches
bad1 = hitatchi_main_loop(cars1, comps, 1)

print("aight we done round 1 ")
for ba1 in bad1:
    print(ba1.capcode)
    
for ca1 in cars1:
    print(ca1.capcode)


matches2 = []
notmatches2 = []
for car in matches:
    match_got = False
    for comp in bad1:
        if not match_got:
            if comp.capcode.strip() == car.capcode.strip():
                match_got = True
                
    if not match_got:
        notmatches2.append(car)
    else:
        matches2.append(car)
print("to get 2 ")
for i in matches:
    print(str(i.capcode)+ "    match 2  ")        
cars2 = matches2      
bad2 = hitatchi_main_loop(cars2, comps, 2)

print("aight we done round 2 ")
for ba2 in bad2:
    print(ba2.capcode)

matches3 = []
notmatches3 = []
for car in matches2:
    match_got = False
    for comp in bad2:
        if not match_got:
            if comp.capcode.strip() == car.capcode.strip():
                match_got = True
                
    if not match_got:
        notmatches3.append(car)
    else:
        matches3.append(car)
        
print("to get 3 ")
for i in matches:
    print(str(i.capcode)+ "    match 3  ")
cars3 = matches
bad3 = hitatchi_main_loop(cars3, comps, 3)

matches4 = []
notmatches4 = []
for car in matches3:
    match_got = False
    for comp in bad3:
        if not match_got:
            if comp.capcode.strip() == car.capcode.strip():
                match_got = True
                
    if not match_got:
        notmatches4.append(car)
    else:
        matches4.append(car)
        
print("to get 4 ")
for i in matches:
    print(str(i)+ "    match 4  ")
        
cars4 = matches4      
bad4 = hitatchi_main_loop(cars4, comps, 4)


join_all()


