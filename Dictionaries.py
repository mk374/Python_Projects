'''
Created on Sep 10, 2018

@author: minsookim
'''
from splinter import Browser
browser = Browser('chrome',executable_path='/usr/local/bin/chromedriver')


# Visit URL
url = "http://www.jisho.org"
browser.visit(url)

browser.fill('keyword','あし\n')

if browser.is_text_present('foot'):
    print("Yes, the official website was found!")
else:
    print("No, it wasn't found... We need to improve our SEO techniques")
browser.quit()
