import time
from hitachi_scraper_tools import *
from selenium.webdriver.support.ui import Select

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

def big_single_bits ():
    list_of_big_bits = ["S Tronic"]
#equivelants("A1 SPORTBACK 25 TFSI S Line 5dr")

##
def find_e_by_xp(driver, xp):
    print(xp)
    print(driver.page_source)
    WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,xp)))
    element = driver.find_element_by_xpath(xp)
    return element
    
def click(button):
    try:
        time.sleep(1)
        button.click()
        print('clicked   '  + str(button))
    except Exception as e:
        print(str(e))
            

    
def equivelants(our_deriv):
    print(" start of equivs ")
#    list_of_equiv = [[ours1, theirs1],[ours2, theirs2],[ours3, theirs3]...
    list_of_sames = [["[Tech Pack]", "Tech Pack"],["[EZ]","EZ"] , ["5dr", "5 Door"], ["3dr", "3 Door"] , ["EAT8","Auto"] , ["[5 seat]","5Seat"], ["[7 seat]","7Seat"]]
#  Please Select
    for i in list_of_sames:
        for j in i:
            pass
   #         print(j)
#    print("88888")
    possible_matches = []
    for i in list_of_sames:
        match = True
        char_pos = []
        print(i[0])
        print(our_deriv)
       
        start = our_deriv.find(i[0])
        print(start)
#        time.sleep(12)
  #      print(start)
   #     print("aft")

        thisdict = {  "list_of_sames": i,"pos": start}
        possible_matches.append(thisdict)
      
    # if match == True:
     #    print("fan this")
      #   print(our_deriv)
    probable_matches = []
    for i in possible_matches:
        if i["pos"]!= -1:
            print(i)
            probable_matches.append(i)
  #  print(our_deriv)

    #### find numbers followed by ps to replace without ps

    
    return probable_matches

    
#better  = equivelants("A1 SPORTBACK 25 TFSI S Line 5dr [Tech Pack]")
#print(better)      
def make_finder(og_capcode, driver):

    print("mmiimmii")
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
    if og_capcode[0] == 'V' and og_capcode[1] == 'O':
        make = "VOLVO"
    print(" zzzzz  ")
    our_make = make
#   <option label="Alfa Romeo" value="Alfa Romeo">Alfa Romeo</option>    
    try_to_move_into_frame(driver)
# //*[@id="makeSelect"]
             #    '//*[@id="makeSelect"]/option[29]'
    makes_xp_1 = '//*[@id="makeSelect"]/option[';
    makes = []
    print(driver.page_source)
    print(" aaa   33     88    33 ") 
#####################################
  #  xx11 = '//*[@id="makeSelect"]'
   # b1 = find_e_by_xp(driver, xx11)
       #  find_e_by_xp(
    #click(b1)
# //*[@id="makeSelect"]
#    xx22 = '//*[@id="makeSelect"]/option[29]'
 #   b1 = find_e_by_xp(driver, xx22)
  #  click(b1)
# //*[@id="makeSelect"]/option[29]


    print(" bbb 33     88    33 ") 
#####################################
    
    for i in range(60):
        makes_xp = makes_xp_1 + str(i)+ "]";
        try:
            thismake = find_e_by_xp(driver,makes_xp)
            makes.append(thismake)
            print("                   fan this bluddy make                  ")
        except:
            print(makes_xp_1 + str(i)+ "]")

    print(" ccc 33     88    33 ")            
    for j in makes:
        print(j)
 #       print(j.get_attribute('innerHTML'))
        if j.get_attribute('innerHTML').lower() == our_make.lower():
            correct_make = j
        else:
            print(j.get_attribute('innerHTML').lower())
            print(make.lower())
    print(" 33    33 ")
#    time.sleep(99999)
    print(our_make)
    print("mmiimmii end ")
    return correct_make

###########################################################
    ###############################################

def deriv_finder2(our_deriv,driver, allready_tried):
    derivs = []    
    equiv = equivelants(our_deriv)

    for zz in range(len(equiv)-1):        
        our_deriv = our_deriv.replace(equiv[zz]["list_of_sames"][0], equiv[zz]["list_of_sames"][1], 1)
        print(equiv[zz]["list_of_sames"][0])
        print(equiv[zz]["list_of_sames"][1])       
    derivs_options= []
    xp1 = '//*[@id="Derivative-input-element"]/option['
    counter = 0

    for i in range(42):
        xpath_opt = xp1+str(i)+']'
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xpath_opt)))
            found_deriv = driver.find_element_by_xpath(xpath_opt)
            derivs_options.append(found_deriv)
        except:
      #      print(xpath_opt)
            pass
    for i in derivs_options:
        if i.get_attribute('innerHTML') == "Please Select":
            derivs_options.remove(i)
    for u in allready_tried:
        for f in derivs_options:
            if u == f.get_attribute('innerHTML'):
      #          print("8 8 8 8 8 8 8 8 8 8 8      ")
       #         print(u);
        #        print(f);
                derivs_options.remove(f)
    
    correct_deriv = parts_of_strings_comparer(derivs_options, our_deriv, "deriv")
    return correct_deriv

    #####################################################
################################################################
#================================================================    #####################################################
################################################################
#================================================================
def model_equivelants(our_model):
    ### 
    print(" start of model equivs ")
    list_of_sames = [["E-NIRO","Niro"],["5dr", "5 Door"],["3dr", "3 Door"]]

    

    
    possible_matches = []
    for i in list_of_sames:
        print("   los   ")
        matched = False
        try:
            print(i[0])
            start = our_model.find(i[0])
            print(start)
            thisdict = {  "list_of_sames": i,"pos": start}
            possible_matches.append(thisdict)
        except:
            pass
            
 
    probable_matches = []
    for i in possible_matches:
        print("£")
        if i["pos"]!= -1:
            print(i)
            probable_matches.append(i)
  #  print(our_deriv)

    #### find numbers followed by ps to replace without ps
    for i in range(100):
        print(" 6666666666666666666666666666666666666666666666 ")
    time.sleep(10)

    for p in probable_matches:
        print(p)
        print(p.get_attribute('innerHTML'))

    
    return probable_matches
    #####################################################
################################################################
#================================================================
    #####################################################
################################################################
#================================================================

def model_finder2(our_model, driver):
#    //*[@id="modelSelect"]
    print("model finder 2")
    time.sleep(5)
    for i in range(999):
        print("4585 4585 4585")
    print("model ffffffffffffffffffffffffffffffffffffff")
    xp1 = '//*[@id="modelSelect"]/option[';
    models = []
    model_options = []
    counter = 0;
    
    for i in range(20):
        xpath_opt = xp1+str(i)+']'
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xpath_opt)))
            found_model = driver.find_element_by_xpath(xpath_opt)
            model_options.append(found_model)
        except:
            pass

#    try:
 #       model_replacements = model_equivelants(our_model)
  #      for zz in range(len(model_replacements)-1):        
   #         our_model = our_model.replace(model_replacements[zz]["list_of_sames"][0],model_replacements[zz]["list_of_sames"][1], 1)
#    except:
 #       pass
#    for i in range(len(our_model)-1):
 #       if our_model[i].isdigit():
  #          if our_model[i+1].isdigit():
   #             if our_model[i+2] == "p":
    #                if our_model[i+3] == "s":
     #                   our_model = our_model.remove(our_model[i+2])
      #                  our_model = our_model.remove(our_model[i+3])
    correct_option = 99999
    min_amount = 99999
    for x in model_options:
        amount = Levenshtein.distance(x.get_attribute('innerHTML'), our_model)
        if amount < min_amount:
            min_amount = amount
            correct_option = x
            
    print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm98 mmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
   # correct_model = parts_of_strings_comparer(model_options, our_model , "model")
    print(correct_option.get_attribute('innerHTML'))
    print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
    return correct_model


################################################################
    ####################################################
    


def model_worker(model_options, our_model):
    ## break into sections
    ## find most matches
    pass
  

def deriv_finder(our_deriv, driver):
    print("start of deriv finder 1")
    derivs = []

    try:
        equiv = equivelants(our_deriv)
        for zz in range(len(equiv)-1):        
            our_deriv = our_deriv.replace(equiv[zz]["list_of_sames"][0], equiv[zz]["list_of_sames"][1],1)
    except:
        pass
       
 #   print("done equivs")
    derivs_options= []
    xp1 = '//*[@id="Derivative-input-element"]/option['
    counter = 0
    for i in range(42):
        xpath_opt = xp1+str(i)+']'
        try:
            WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH , xpath_opt)))
            found_deriv = driver.find_element_by_xpath(xpath_opt)
            derivs_options.append(found_deriv)
        except:
            pass
  #          print(xpath_opt)
   # print("cd below   uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
    for i in derivs_options:
        if i.get_attribute('innerHTML') == "Please Select":
            derivs_options.remove(i)

    correct_deriv = parts_of_strings_comparer(derivs_options, our_deriv, "deriv")
    print("cd below")
    print(correct_deriv.get_attribute('innerHTML'))
    return correct_deriv



def newest_year_checker(my1, my2):
    num_my1 = ""
    chars_my1 = 0;
    print(my1)
    print(my2)
    for i in my1:
        print(i)
        if i.isdigit():
            num_my1.append(i)
        if i == "a":
            chars_my1+=1;
        if i == "b":
            chars_my1+=2;
        if i == "c":
            chars_my1+=3;
    print(num_my1)
    try:
        my1t = int(num_my1)+chars_my1
    except:
        pass
    
    num_my2 = ""
    chars_my2 = 0;
    for i in my2:
        if i.isdigit():
            num_my2.append(i)
        if i == "a":
            chars_my2+=1;
        if i == "b":
            chars_my2+=2;
        if i == "c":
            chars_my2+=3;
    try:
        my2t = int(num_my2)+chars_my2
    except:
        pass


    if (my1t<my2t):
        return my1
    elif (my1t>my2t):
        return my2
    else:
        print(" mys are same ")

def choose_model_year(driver):
    #   //*[@id="ModelYear-input-element"]/option[3]
    #   //*[@id="ModelYear-input-element"]/option[2]
    for i in range(25):
        print("           my            ")
    model_years = []
    for i in range(15):
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


    for i in range(50):
        print("my didnt work")
    return False

def van_bus_check(driver, model, deriv):
    print(" bb cc 1")
    
    this_string = "";
    our_models_bits = []
    bit = "";
    our_string = model
    for index , char in enumerate(model):
        print(index)
        if (char == " "):
            our_models_bits.append(this_string)
            this_string = "";
        elif (index == len(our_string)-1):
            this_string+=our_string[len(our_string)-1]
            our_models_bits.append(this_string)
            this_string = "";
        else:
            this_string+=char


    our_string = deriv
    this_string = "";
    our_derivs_bits = []
    bit = "";
    for index , char in enumerate(deriv):
        print(index)
        if (char == " "):
            our_derivs_bits.append(this_string)
            this_string = "";
        elif (index == len(our_string)-1):
            this_string+=our_string[len(our_string)-1]
            our_derivs_bits.append(this_string)
            this_string = "";
        else:
            this_string+=char
       
    print("are bits")
    for i in our_models_bits:
        print(i)

    for i in our_derivs_bits:
        print(i)

    lcv_stuff = ["van", "minibus" , "Tourneo Custom" , "Dropside" , "Chassis" , "Cab" , "COMBI"]

    for m in our_models_bits:
        for o in lcv_stuff:
            if m.lower() == o.lower():
                print("bus match")
                return True
            for om in our_models_bits:
                if m.lower()+ " " +om.lower() == o.lower():
                    print("bus match")
                    return True

    for d in our_derivs_bits:
        for o in lcv_stuff:
            if d.lower() == o.lower():
                print("bus match")
                return True

    print(" bb cc 2")
    return False
        
    



def parts_of_strings_comparer(list_of_objects_with_strings, our_string, model_or_deriv):

    for i in list_of_objects_with_strings:
        if i.get_attribute('innerHTML') == "Please Select":
            list_of_objects_with_strings.remove(i)


   # try:
  #      list_of_objects_with_strings.remove("please select")
 #   except:
#        pass
    
    list_fs = []
    print("dddddddddd")
    this_string = "";
    our_strings_bits = []
    bit = "";
    for index , char in enumerate(our_string):
        print(index)
        print(len(our_string))
        
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


    
    for o in list_of_objects_with_strings:
        o = o.get_attribute('innerHTML')
        print(o)
        list_fs.append(o)
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

    for i in list_ps:
        for num, j in enumerate(i):
            if i[num].isdigit():
                if i[num+1].isdigit():
                    if i[num+2] == "p":
                        if i[num+3] == "s":
                            i = i.remove("ps")
    #print("!!!!!!!!!!")
    #for k in list_ps:
   #     print(k)
  #      for j in k:
 #           print(j)
#    print("!!!!!!!!!!")

    


    number_of_bits = len(our_strings_bits)
    most_matched = -99
    joint_top_list= []
    our_bits_matched = [];
    for i in range(len(our_strings_bits)):
        our_bits_matched.append(0)
#    print("start helper ")
    for  num, car  in enumerate(list_ps):
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
                print(str(our_bit) + "   this bit is from our string")
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
        print(list_of_objects_with_strings[joint_top_list[0]].get_attribute('innerHTML'))
        print(list_of_objects_with_strings[i].get_attribute('innerHTML'))
    print("11111111 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    if len(joint_top_list) == 1:
        print(list_of_objects_with_strings[joint_top_list[0]].get_attribute('innerHTML'))
        print("reting ")
        return list_of_objects_with_strings[joint_top_list[0]]
    else:
        print("deal with even stevens ")
        print(len(list_of_objects_with_strings))
        print(len(joint_top_list))

        for e in joint_top_list:
            print(e)
        for e in list_of_objects_with_strings:
            print(e)
        
        return list_of_objects_with_strings[joint_top_list[0]]



    

def string_comparer(list_of_objects_with_strings, string):
    list4 = []
    print("dddddddddd")
    print(string)

    for o in list_of_objects_with_strings:
        o = o.get_attribute('innerHTML')
        print(o)
        list4.append(o)

    sim_vals = []
    for l in list4:
      #  lev = jellyfish.levenshtein_distance(l, string)
       # print(lev)
        jaro = jellyfish.jaro_distance(l.lower(), string.lower())
        print(jaro)
      #  dame =  jellyfish.damerau_levenshtein_distance(l, string)
       # print(dame)
        av_sim = jaro
        print(l)
        print("had similarity value of ")
        print(av_sim)
        sim_vals.append(av_sim)
        
    min1 = 0
    min_index = 0
    for v in range(len(sim_vals)):        
        if float(sim_vals[v])> float(min1):
            min1 = sim_vals[v]
            min_index = v
    print(min1)
    print(min_index)
    print(" tttthhhhhiiiiiissssss     " + str(list_of_objects_with_strings[min_index]))
   # while(1<2):
    #    print(list_of_objects_with_strings[v].get_attribute('innerHTML'))
    return(list_of_objects_with_strings[min_index])


