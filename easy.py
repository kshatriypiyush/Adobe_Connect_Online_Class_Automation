import webbrowser
import time
import datetime
import selenium
from selenium import webdriver

driver = webdriver.Chrome('Enter the path of chromeDriver')#Enter the Path where You download and placed the ChromeDriver Executable File
b=time.strftime("%H:%M")
print (b)
c=("Enter Your Class-1 Time")#Enter Your Class Time
# If You have More than one class in one day let me Know!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
d=datetime.date.today().strftime("%A")    
print("Day of week: ",d)

e=("Enter the Day of your class")#Enter The Day
if d==e:
    while(b!=c):
        b=time.strftime("%H:%M")
        if b==c:        
            driver.get('Enter the URL for your adobeConnect class')
            # Don't Touch Below Part Please, except the 'Enter your name' part
            id_box = driver.find_element_by_name('guestName')
            id_box = driver.find_element_by_id('guestName')
            id_box.send_keys('Enter Your Name for the Online Class')
            login_button = driver.find_element_by_name('feature=1477')
            login_button.click()
            time.sleep(5)
            big_login = driver.find_element_by_id('tabletBetaLabelID')
            driver.execute_script("arguments[0].click();", big_login)
else:
    print ("Think Hard")

