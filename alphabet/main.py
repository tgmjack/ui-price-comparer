import time
from config import *
from excel_handler import *
from main_loop import *
import datetime
cars_to_get = get_excel_file_with_model_and_deriv()
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
            diy_my = diy_deriv[lastspace_n_num_pos:]
            diy_deriv = diy_deriv[:lastspace_n_num_pos]
    if diy_match:
        matches.append(c)
cars_to_get = matches

#print(diy_my)
#print(lastspace_n_num_pos)
#time.sleep(9999)

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
for b in b1:
    for og in cars_to_get:
        if b.capcode == og.capcode:
            round_3.append(og)

b3 = alphabet_main(round_3, 3)
round_4 = []
for b in b3:
    for og in cars_to_get:
        if b.capcode == og.capcode:
            round_4.append(og)
for b in b2:
    for og in cars_to_get:
        if b.capcode == og.capcode:
            round_4.append(og)
for b in b1:
    for og in cars_to_get:
        if b.capcode == og.capcode:
            round_4.append(og)

b4 = alphabet_main(round_4, 4)
round_5 = []
for b in b4:
    for og in cars_to_get:
        if b.capcode == og.capcode:
            round_5.append(og)
for b in b3:
    for og in cars_to_get:
        if b.capcode == og.capcode:
            round_5.append(og)
for b in b2:
    for og in cars_to_get:
        if b.capcode == og.capcode:
            round_5.append(og)
for b in b1:
    for og in cars_to_get:
        if b.capcode == og.capcode:
            round_5.append(og)
b5 = alphabet_main(round_5,5)



for i in range(50):
    print("what? propper done?")
