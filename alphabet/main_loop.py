import time
from config import *
from excel_handler import *
from scrapper_tools import *
import datetime

def reset_for_next_go(driver1, round_number):
    print("faaaaaaaaaaaaaaaaacking reseting ")


   # try:
    #    driver1.close()
    #except:
     #   pass
    new_one_opened = False
    while not new_one_opened:
        print("new1 loop")
        try:
            driver1.quit()
            print("driver quited")
        except:
            print("driver not quit")
            pass
        try:
            driver1 = open_alphabet()
            wait_until_front_page(driver1)
            click_calc2(driver1)
            new_one_opened = True
            return driver1
        except:
        #    try:
         #    driver1.close()
          #  except:
           #     pass
            try:
                print("no dice opening new driver")
                driver1.quit()
            except:
                pass
    print("propper fuck")

def alphabet_main(cars_to_get, round_number):
    new_deals=[]
    everything_screwed = False
    bad_capcodes = []
    row_counter = 1
    diy_file = get_diy_file()
 #   driver1 = open_alphabet()
  #  wait_until_front_page(driver1)
    position_check_counter = 0
    model_tries_attempted = 0
    for i in cars_to_get:
        print(str(i)+ "   ======     i ")
#        try:
        everything_screwed = False
        model_found = False
        error_loc = "none"
        deriv_found = False
        everything_screwed = False
        model_found = False
        print("main2")
        tstamp1 = datetime.datetime.now()
        future1 = tstamp1 +  datetime.timedelta(seconds = 1300)


        diy_match = False
        for kl in range(diy_file.shape[0]) :
            if diy_file['capcode'].iloc[kl].strip() == i.capcode.strip():
                print("match_start")
                diy_match = True
                diy_man = diy_file['make'].iloc[kl]
                diy_model = diy_file['model'].iloc[kl]
                diy_deriv = diy_file['deriv'].iloc[kl]
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
                diy_blp = i.blp
                print("match ")


        if diy_match == False:
            everything_screwed = True

        print(" QQQ ")
        if not everything_screwed:
            try:
                driver1 = open_alphabet()
                wait_until_front_page(driver1)
                new_driver_sorted = True
            except:
                everything_screwed = True
                error_loc = " init driver set up  "


            print(" QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQqaq ")
            time.sleep(5)
            print(" cf1 ")
            try:
                click_calc2(driver1)
            except:
                print(" init calc click ")
                error_loc = " init calc click "
                everything_screwed = True
            time.sleep(5)
            print(" cf2 ")
            if not everything_screwed:
                try:
                    switch_to_iframe_1(driver1)
                    time.sleep(5)
                except:
                    print(" init frame switch  ")
                    error_loc = " init frame switch  "
                    everything_screwed = True
 #           print("ok now jut chilling")
  #          time.sleep(99)
            print(" cf3 ")
            if not everything_screwed:
                if round_number % 2 == 0:
                    try:
                        click_lcv6(driver1)
                        print(" click ")
                    except:
                        print(" lcv click ")
                        error_loc = " lcv click "
                        everything_screwed = True


            if not everything_screwed:
                try:
                    diy_man = find_this_make_2(i.capcode )
                    choose_man_1(driver1, diy_man)
                except:
                    print("f3")
                    everything_screwed = True
                    error_loc = " choosing man "

            print(" cf4 ")

            time.sleep(1)
            if not everything_screwed:
                try:
                    choose_model_1(driver1, diy_model)
                except:
                    print("f4 ")
                    everything_screwed = True
                    error_loc = " choosing mod "

            print(" cf5 ")
            time.sleep(0.5)
            if not everything_screwed:
                try:
                    choose_deriv_1(driver1, diy_deriv , diy_man, diy_model)
                except:
                    print("f5")
                    everything_screwed = True
                    error_loc = " choosing deriv "


            print(" cf6 ")
            time.sleep(0.5)
            if not everything_screwed:
                try:
                    choose_my_1(driver1 , diy_my)
                    print("goodness me ")
                except:
                    print("f6")
                    everything_screwed = True
                    error_loc = " choosing my "



            if everything_screwed == False:
                try:
                    deriv_found = blp_check_1(driver1, diy_blp)
                    if not deriv_found:
                        everything_screwed =True
                        error_loc = "blp check"
                except:
                    everything_screwed =True
                    error_loc = "blp check"

            if deriv_found ==True and everything_screwed == False:
                try:
                    enter_otr(driver1, i.otr)
                except:
                    everything_screwed =True
                    error_loc = "entering otr"
                time.sleep(1)

                try:
                    set_months_up(driver1, 3);
                except:
                    everything_screwed =True
                    error_loc = " months up setter ";
                try:
                    final_check_and_set_init_terms(driver1, diy_blp, i.otr)
                except:
                    everything_screwed =True
                    error_loc = "final check"


            if deriv_found ==True and not everything_screwed:
                try:
                    p = get_prices(driver1)
                except:
                    everything_screwed = True
                    error_loc = "prices"
            if deriv_found ==True and not everything_screwed:
                months_up_txt = get_months_up(driver1)
            months_counter = 0
            miles_counter = 1
            if not everything_screwed:
                for j in range(21):
                    print(str(j)+ "      jjjjjjjjjj     stuff ")
                    cm = p[j]
                    fm = p[j+21]
                    print("cm     " + str(cm))
                    print("fm     " + str(fm))
                    months_counter +=1
                    months = 0

                    if miles_counter == 1:
                        miles = 5000
                    if miles_counter == 2:
                        miles = 8000
                    if miles_counter == 3:
                        miles = 10000
                    if miles_counter == 4:
                        miles = 15000
                    if miles_counter == 5:
                        miles = 20000
                    if miles_counter == 6:
                        miles = 25000
                    if miles_counter == 7:
                        miles = 30000




                    if months_counter == 1:
                        months = 24
                    if months_counter == 2:
                        months = 36
                    if months_counter == 3:
                        months = 48

                    print(" just finished car  9 9 9 9 9 9 9 9 9 9 9 9 ")
                  #  print(str(i.capcode)+"     " + str(i.deriv))
                    print("cm = " +str(cm) + "      fm = "+str(fm) + "miles_counter = " + str(miles_counter) + "   gives >" + str(miles))
                    new_deals.append(deal_pair_final(i.capcode, months, miles, cm, fm,i.make,i.model,i.deriv, i.otr, i.blp , months_up_txt))
                                                #self,capcode,months,miles,cm, fm, make, model, deriv,otr,blp):
                    if months_counter == 3:
                        months_counter = 0
                        miles_counter+=1
     #   except:
      #          everything_screwed = True
       #         error_loc = " big error  "



        if everything_screwed:
            bad_capcodes.append(deal_pair_final(i.capcode, error_loc, "bad", "bad", "bad",i.make,i.model,i.deriv, i.otr, i.blp , " bad "))
        try:
            save_what_we_got444("alphabet_prices_"+str(round_number),new_deals)
        except:
            save_what_we_got444("alphabet_prices_close_the_other_"+str(round_number),new_deals)
        try:
            save_what_we_got444("alphabet_badcapcodes_"+str(round_number),bad_capcodes)
        except:
            save_what_we_got444("alphabet_badcapcodes_close_the_other_"+str(round_number),bad_capcodes)

        new_driver_sorted = False
        new_driver_sorted_counter = 0
  #      while not new_driver_sorted:
   #         new_driver_sorted_counter+=1
        print("times tried to sort out driver "+str(new_driver_sorted_counter))
        try:
            driver1.close()
        except:
            pass
        try:
            driver1.quit()
        except:
            pass
     #       try:
    #            driver1 = open_alphabet()
   #             wait_until_front_page(driver1)
  #              new_driver_sorted = True
 #           except:
#                pass

    print("end of this round")
    try:
        driver1.close()
    except:
        pass
    try:
        driver1.quit()
    except:
        pass
    return bad_capcodes
