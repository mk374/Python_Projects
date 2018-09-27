'''
Created on Sep 17, 2018

@author: minsookim
'''
from JishoDictionaryAccess import JishoDictionaryAccess
from PapagoDictionaryAccess import PapagoDictionaryAccess
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

from tkinter import *

import re

"""
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
JishoDriver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options = options)
PapagoDriver= webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options = options)
"""
JishoDriver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
PapagoDriver= webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

JishoDriver.get("http://www.jisho.org")
PapagoDriver.get("https://papago.naver.com/?sk=en&tk=ja")

#the definitions that we want
def fetch(entry):
    JishoDictionaryAccess().search_Word_and_Print(JishoDriver, entry.get())
    PapagoDictionaryAccess().search_Word_and_Print(PapagoDriver, entry.get())


fields = 'Input'
#format of the interface
def makeform(root, field):
    
    row = Frame(root)
    lab = Label(row, width=15, text=field, anchor='w')
    ent = Entry(row)
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    lab.pack(side=LEFT)
    ent.pack(side=RIGHT, expand=YES, fill=X)
    #entry = [field, ent]
    print(ent.get())
    return ent
    

if __name__ == '__main__':
    root = Tk()
    ent = makeform(root, fields)
    root.bind('<Return>', (lambda e=ent: fetch(e)))   
    b1 = Button(root, text='Show',
          command = (lambda e=ent: fetch(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Quit', command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()

