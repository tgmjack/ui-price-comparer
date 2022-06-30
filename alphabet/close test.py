from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.chrome.options as Options
from selenium import webdriver
import time
from tkinter import *
from multiprocessing import Process, Manager

def open_a_page(): # open one chromedriver in detatched mode (because i specifically want it to stay open when finished)
    driver_xpath2 = "chromedriver.exe"
    chrome_options = Options.Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(driver_xpath2 ,options=chrome_options )
    driver.get("https://www.google.com")
    print("yo   ")
    time.sleep(2)

def open_2_pages():
    processes = []
    manager = Manager()
    d = manager.dict()
    for i in range(2):
        p1 = Process( target = open_a_page , args = ())
        processes.append(p1)
    for proc in processes:
        proc.start()    
    for proc in processes:
        proc.join()
    print("done    ")

window=Tk()     
B = Button(window, text ="go", command = open_2_pages)  # when i click this button it opens 2 googles
B.place(x=10, y=10);

if __name__ == '__main__':
    window.mainloop();



