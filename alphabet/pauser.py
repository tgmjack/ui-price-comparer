import time
from config import *
from excel_handler import *
from scrapper_tools import *
import datetime

cars_to_get = get_excel_file_with_model_and_deriv()

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
    driver1 = open_alphabet()
    new_deals=[]
    
    everything_screwed = False
    bad_capcodes = []
    row_counter = 1
    wait_until_front_page(driver1)
    position_check_counter = 0
    model_tries_attempted = 0
    for i in cars_to_get:
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
                diy_match = True
                diy_man = diy_file['make'].iloc[kl]
                diy_model = diy_file['model'].iloc[kl]
                diy_deriv = diy_file['deriv'].iloc[kl]
                diy_my = diy_file['my'].iloc[kl]
                diy_blp = diy_file['blp'].iloc[kl]
        if diy_match == False:
            everything_screwed = True
        print(" QQQ ")
        if not everything_screwed:
            print(" QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQqaq ")
            time.sleep(599999)
            click_calc2(driver1)
            time.sleep(5)
            switch_to_iframe_1(driver1)
            time.sleep(5)
            choose_man_1(driver1, diy_man)
            time.sleep(5)
            choose_model_1(driver1, diy_model)
            time.sleep(5)
            choose_deriv_1(driver1, diy_deriv)
            time.sleep(5)
            choose_my_1(driver1, diy_my)
            time.sleep(5)

        
        if everything_screwed:
             error_loc = "getting car"

        deriv_found = blp_check_1(driver1, diy_blp)

        if deriv_found ==True and everything_screwed == False:
            try:
                enter_otr(driver1, i.otr)
            except:
                everything_screwed =True
                error_loc = "entering otr"
            time.sleep(1)
            try:
                final_check_and_set_init_terms(driver1, diy_blp, i.otr)
            except:
                everything_screwed =True
                error_loc = "final check"


        if not everything_screwed:
            try:
                p = get_prices(driver1)
            except:
                everything_screwed = False
                error_loc = "prices"

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
                new_deals.append(deal_pair_final(i.capcode, months, miles, cm, fm,i.make,i.model,i.deriv, i.otr, i.blp))
                                            #self,capcode,months,miles,cm, fm, make, model, deriv,otr,blp):
                if months_counter == 3:
                    months_counter = 0
                    miles_counter+=1
        else:
            bad_capcodes.append(deal_pair_final(i.capcode, error_loc, "bad", "bad", "bad",i.make,i.model,i.deriv, i.otr, i.blp))
        try:
            save_what_we_got444("alphabet_prices_"+str(round_number),new_deals)
        except:
            save_what_we_got444("alphabet_prices_close_the_other_"+str(round_number),new_deals)
        try:
            save_what_we_got444("alphabet_badcapcodes_"+str(round_number),bad_capcodes)
        except:
            save_what_we_got444("alphabet_badcapcodes_close_the_other_"+str(round_number),bad_capcodes)

        driver1 = reset_for_next_go(driver1,round_number)


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

matches = []
diy_file = get_diy_file()
for c in cars_to_get:
    diy_match = False
    for kl in range(diy_file.shape[0]) :
        
        if diy_file['capcode'].iloc[kl].strip() == c.capcode.strip():
            diy_match = True
            diy_man = diy_file['make'].iloc[kl]
            diy_model = diy_file['model'].iloc[kl]
            diy_deriv = diy_file['deriv'].iloc[kl]
            diy_my = diy_file['my'].iloc[kl]
    if diy_match:
        matches.append(c)
cars_to_get = matches

for m in matches:
    print("match")


b1 = alphabet_main(cars_to_get, 1)
round_2 = []
for b in b1:
    for og in cars_to_get:
        if b.capcode == og.capcode:
            round_2.append(og)


b2 = alphabet_main(round_2, 2)
round_3 = []
for b in b2:
    for og in cars_to_get:
        if b.capcode == og.capcode:
            round_3.append(og)

b3 = alphabet_main(round_3, 3)
round_4 = []
for b in b3:
    for og in cars_to_get:
        if b.capcode == og.capcode:
            round_4.append(og)
b4 = alphabet_main(round_4, 4)
round_5 = []
for b in b4:
    for og in cars_to_get:
        if b.capcode == og.capcode:
            round_5.append(og)
b5 = alphabet_main(round_5,5)



for i in range(50):
    print("what? propper done?")
