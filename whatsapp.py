from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#System.setProperty("webdriver.chrome.driver", "/home/anshita/Code/selenium");
driver = webdriver.Chrome()
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
 
#customise message
string = "your message goes here"
 
x_arg = '//span[@title="<replace name of contact here>"]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
print ("found")
group_title.click()
print ("found contact")
inp_xpath='//div[@class="_2S1VP copyable-text selectable-text"]'
input_box=wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
print ("found input")
for i in range(20): #here replace 20 with number of messsages to send
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1) #interval of 1 second
