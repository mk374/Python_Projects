'''
Created on Sep 10, 2018

@author: minsookim
'''

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import re


class JishoDictionaryAccess():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver= webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options = options)
        
    def search_Word_and_Print(self, driver, word_input):
    
        #driver.get("http://www.jisho.org")
        element = driver.find_element_by_name('keyword')
        #word_input = input("What word are you searching for? ")
        element.send_keys(word_input + "\n")
        print("Jisho Definition of: " + word_input)
        
        
        if(re.search('[a-zA-Z]', word_input) == None): #if the search is not English
            print(driver.find_element_by_xpath('//*[@id="primary"]/div[1]/div/div[2]/div/div[2]/div/span[2]').text)
        else: (print(driver.find_element_by_xpath('//*[@id="primary"]/div[1]/div[1]/div[1]/div[1]/div/span[2]/span').text))
    

    


