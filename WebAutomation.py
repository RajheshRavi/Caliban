from selenium import webdriver


def openFacebook(mail, password):
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')
    driver.find_element_by_id('email').send_keys(mail)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_id('loginbutton').click()

def openYoutube(search):                                        # Check
    driver = webdriver.Chrome()
    driver.get('https://youtube.com')
    #driver.find_element_by_id('search').send_keys(search)
    #driver.find_element_by_id('search-icon-legacy').click()
    driver.find_element_by_xpath('//*[@id="search"]').send_keys(search)
    driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()


openYoutube('Kali linux')
#openFacebook()