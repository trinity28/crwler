from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.wait import WebDriverWait
import time

n=input("how many numbers would you like to search for\n")
 
# below 8 lines to set proxy setting for internet connection
#leave them commented if you use no proxy

#profile = webdriver.FirefoxProfile() 
#profile.set_preference("network.proxy.type", 1)
#profile.set_preference("network.proxy.http", "192.168.1.107")
#profile.set_preference("network.proxy.http_port", 3128)
#profile.set_preference("network.proxy.ssl", "192.168.1.107");
#profile.set_preference("network.proxy.ssl_port", 3128);
#profile.update_preferences() # proxy setting :-update them accordng to your connection
#driver = webdriver.Firefox(firefox_profile=profile)

driver = webdriver.Firefox()


driver.set_page_load_timeout(50)
for i in range(n):
	number=input("enter the number to search:- ")
	driver.get('https://www.truecaller.com/')
	search=driver.find_element_by_xpath("//input[@class='searchbar-query']")
	search.send_keys(number)# sending the number to search input field
	search.send_keys(Keys.ENTER)

	time.sleep(1)
	if (i==0):
   
		box=driver.find_element_by_tag_name('img')

		box.click()
		time.sleep(2)
		#logging using gmail account


		email_phone = driver.find_element_by_xpath("//input[@id='identifierId']")
		email_phone.send_keys("your email id")
		driver.find_element_by_id("identifierNext").click()
		time.sleep(1)
		password = driver.find_element_by_xpath("//input[@name='password']")
		password.send_keys("password")


		driver.find_element_by_id("passwordNext").click()
		wait = WebDriverWait(driver,20)
		time.sleep(1)
		driver.find_element_by_id("submit_approve_access").click() #comment this line if using email account that has already gave truecaller permission
		

		time.sleep(1)


		wait = WebDriverWait(driver, 20)


	time.sleep(3)# wait till javascript is completely loaded, to fetch email and name


	print "NAME_-",driver.find_element_by_xpath("//*[@id='app']/div[3]/div[1]/div[2]/div[1]/span").text
	print "EMAIL:-",driver.find_element_by_xpath("//*[@id='app']/div[3]/ul/li[3]/div/div[1]").text
