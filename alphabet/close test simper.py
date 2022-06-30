from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.chrome.options as Options
from selenium import webdriver
import time
from tkinter import *
from multiprocessing import Process

def dothing(): # open one chromedriver in detatched mode (because i specifically want it to stay open when finished)
    print("yo   ")


def open_2_things():
    processes = []
    for i in range(2):
        p1 = Process( target = dothing , args = ())
        processes.append(p1)
    for proc in processes:
        proc.start()    
    for proc in processes:
        proc.join()
    print("done    ")

window=Tk()     
B = Button(window, text ="go", command = open_2_things)  # when i click this button it opens 2 googles
B.place(x=10, y=10);

if __name__ == '__main__':
    window.mainloop();



