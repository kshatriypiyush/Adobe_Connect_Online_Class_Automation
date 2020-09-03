#Please write the name of your teacher, your name , time and links as given in the code and then try to run the code:
import time
import datetime
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('location of chrome.exe taken from the repository here please.')
b=time.strftime("%H:%M")
print (b)
c=("time of class-1 here")
f=("time of class-2 here")
g=("time of class-3 here")
h=("time of class-4 here")
i=("time of class-5 here")
j=("time of class-6 here")

(Name of Teacher-1)='Link-1 here please'
(Name of Teacher-2)='Link-2 here please'
(Name of Teacher-3)='Link-3 here please'
(Name of Teacher-4)='Link-4 here please'
(Name of Teacher-5)='Link-5 here please'

d=datetime.date.today().strftime("%A")    
print("Day of week: ",d)

e=("Monday") #Here we place the days for the class 
Tue=("Tuesday")
Wed=("Wednesday")
Thur=("Thursday")
Fri=("Friday")


#####Monday Lecture
if d==e:
    while(b!=c):              # c= 08:00 am
        b=time.strftime("%H:%M")
        if b==c:        
            driver.get((Name of Teacher-1))
            id_box = driver.find_element_by_name('guestName')
            id_box = driver.find_element_by_id('guestName')
            id_box.send_keys('Your Name here')
            login_button = driver.find_element_by_name('feature=1477')
            login_button.click()
            time.sleep(2)
            big_login = driver.find_element_by_id('tabletBetaLabelID')
            driver.execute_script("arguments[0].click();", big_login)
        
    while(b!=f):
        b=time.strftime("%H:%M")
        if b==f:        #f = 13:00pm
            driver.get((Name of Teacher-2))
            big_login = driver.find_element_by_id('tabletBetaLabelID')
            driver.execute_script("arguments[0].click();", big_login)        
else:
    print ("Think Hard")

###Tuesday Lecture
if d==Tue:
    while(b!=c):             #c= 08:00 am
        b=time.strftime("%H:%M")
        if b==c:        
            driver.get((Name of Teacher-2))
            id_box = driver.find_element_by_name('guestName')
            id_box = driver.find_element_by_id('guestName')
            id_box.send_keys('Your Name here')
            login_button = driver.find_element_by_name('feature=1477')
            login_button.click()
            time.sleep(2)
            big_login = driver.find_element_by_id('tabletBetaLabelID')
            driver.execute_script("arguments[0].click();", big_login)
        
    while(b!=g):               #g= 12:00 pm
        b=time.strftime("%H:%M")
        if b==g:        
            driver.get((Name of Teacher-5))
            big_login = driver.find_element_by_id('tabletBetaLabelID')
            driver.execute_script("arguments[0].click();", big_login)

    while(b!=h):                #h= 15:00 pm
        b=time.strftime("%H:%M")
        if b==h:        
            driver.get((Name of Teacher-4))
            big_login = driver.find_element_by_id('tabletBetaLabelID')
            driver.execute_script("arguments[0].click();", big_login)
else:
    print ("Think Hard")


###Wednesday Lecture
if d==Wed:
    while(b!=i):                    #i= 14:00 pm
        b=time.strftime("%H:%M")
        if b==i:        
            driver.get((Name of Teacher-3))
            id_box = driver.find_element_by_name('guestName')
            id_box = driver.find_element_by_id('guestName')
            id_box.send_keys('Your Name here')
            login_button = driver.find_element_by_name('feature=1477')
            login_button.click()
            time.sleep(2)
            big_login = driver.find_element_by_id('tabletBetaLabelID')
            driver.execute_script("arguments[0].click();", big_login)

else:
    print ("Think Hard")


#####Thursday Lecture
if d==Thur:
    while(b!=c):                      #c= 08:00 am
        b=time.strftime("%H:%M")
        if b==c:        
            driver.get((Name of Teacher-5))
            id_box = driver.find_element_by_name('guestName')
            id_box = driver.find_element_by_id('guestName')
            id_box.send_keys('Your Name here')
            login_button = driver.find_element_by_name('feature=1477')
            login_button.click()
            time.sleep(2)
            big_login = driver.find_element_by_id('tabletBetaLabelID')
            driver.execute_script("arguments[0].click();", big_login)
        
    while(b!=i):                   #i= 14:00 pm
        b=time.strftime("%H:%M")
        if b==i:        
            driver.get((Name of Teacher-1))
            big_login = driver.find_element_by_id('tabletBetaLabelID')
            driver.execute_script("arguments[0].click();", big_login)        
else:
    print ("Think Hard")

#####Friday Lecture
if d==Fri:
    while(b!=j):                       #j= 09:00 am
        b=time.strftime("%H:%M")
        if b==j:        
            driver.get((Name of Teacher-4))
            id_box = driver.find_element_by_name('guestName')
            id_box = driver.find_element_by_id('guestName')
            id_box.send_keys('Your Name here')
            login_button = driver.find_element_by_name('feature=1477')
            login_button.click()
            time.sleep(2)
            big_login = driver.find_element_by_id('tabletBetaLabelID')
            driver.execute_script("arguments[0].click();", big_login)
        
    while(b!=f):
        b=time.strftime("%H:%M")
        if b==f:        #f = 13:00pm
            driver.get((Name of Teacher-3))
            big_login = driver.find_element_by_id('tabletBetaLabelID')
            driver.execute_script("arguments[0].click();", big_login)      
else:
    print ("Think Hard")
    
