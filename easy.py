import webbrowser
import time
import datetime
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:/Python38/chromedriver.exe')
b=time.strftime("%H:%M")
print (b)
c=("11:59")

d=datetime.date.today().strftime("%A")    
print("Day of week: ",d)

e=("Saturday")
if d==e:
    while(b!=c):
        b=time.strftime("%H:%M")
        if b==c:        
            driver.get('https://ilasalle.adobeconnect.com/_a824687455/rm5w629t92kj/?OWASP_CSRFTOKEN=c660577bc42d7ca2e8f73733486e48bc36671ce3a40622c78d80b1d2afd1c74b&proto=true')
            id_box = driver.find_element_by_name('guestName')
            id_box = driver.find_element_by_id('guestName')
            id_box.send_keys('rhondi bryan')
            login_button = driver.find_element_by_name('feature=1477')
            login_button.click()
            time.sleep(5)
            big_login = driver.find_element_by_id('tabletBetaLabelID')
            driver.execute_script("arguments[0].click();", big_login)
else:
    print ("Think Hard")

