'''
Created on Sep 10, 2018

@author: minsookim
'''

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import re


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


driver= webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options = options)

url = "http://www.jisho.org"
driver.get(url)


#inputBox = browser.find_element_by_name('keyword')
#element = driver.find_element_by_name('q')
#element.send_keys('hey')
word_input = input("What word are you searching for? ")

element = driver.find_element_by_name('keyword')
element.send_keys(word_input + "\n")

#driver.find_element_by_id("btnTranslate").click();

#inputBox.send_keys('ashi\n')
#button.click()
print("Definition of: " + word_input)


if(re.search('[a-zA-Z]', word_input) == None):
    print(driver.find_element_by_xpath('//*[@id="primary"]/div[1]/div/div[2]/div/div[2]/div/span[2]').text)
else: (print(driver.find_element_by_xpath('//*[@id="primary"]/div[1]/div[1]/div[1]/div[1]/div/span[2]/span').text))


if __name__ == "__main__":
    print()


