from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from .log_files import info_log,add_to_notchecked_list,error_log

# Importing modules
import undetected_chromedriver as uc
from stem import Signal
from stem.control import Controller
import re
import random
import os


from ..pypasser import reCaptchaV2
from ..hcaptcha_ai.hcaptcha_solver import hcaptchaAI
from selenium.common.exceptions import NoSuchElementException

    
#=================================================================================================================================================
#  USER AGENTS

with open(r'E:\projects_new\Major_Project\useragents_pro.txt') as f:
    content = f.readlines()
    user_agent_list = [x.strip() for x in content]
    user_agent = random.choice(user_agent_list)
#===========================================================================================================================================

                               #>>>>>>>>>>>>>>>>> SETTING PROXY AND DRIVER <<<<<<<<<<<<<<<<<#

#==========================================================================================================================================
# function for switching IP
# def switchIP():
    
#     with Controller.from_port(port=9151) as controller:
        
#         controller.authenticate()
#         controller.signal(Signal.NEWNYM)
      
        
#setting up the tor proxy
# PROXY = "socks5://127.0.0.1:9150"


def driver_function():
    """
    Initializes the driver
    
    Parameters 
    ----------
    None
    
    Returns
    -------
    driver
    
    """
    
    options = uc.ChromeOptions()
    # options.add_argument(r"--load-extension=C:\Users\rajva\Downloads\adblock_ultimate")
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-notifications')
    #options.add_argument('--disable-cookies')
    options.add_argument('--incognito')
    options.add_argument("--disable-infobars")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-application-cache")
    options.add_argument("--ignore-certificate-errors")
    #options.add_argument("--headless")
    #options.add_argument('--proxy-server=%s' % PROXY)
    #uc.TARGET_VERSION = 108
    driver = uc.Chrome(use_subprocess=True,options=options) 
    #driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":user_agent})  
    return driver

# #global driver
driver = driver_function()



#=========================================================================================================================================

                                      #>>>>>>>>>>>>>  XPATH FUNCTIONS <<<<<<<<<<<<<<<<<<<<<#

#==========================================================================================================================================

def click_element_XPATH(path):
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,path)))
    return WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,path))).click() 
    
   
def scroll_element_XPATH(path):
    flag=driver.find_element(By.XPATH,path)
    return driver.execute_script("arguments[0].scrollIntoView();",flag)
    
def click_element_LINK_TEXT(path):
    return driver.find_element(By.LINK_TEXT,path).click() 
    
    
def fill_element_XPATH(path,keys):
    return WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,path))).send_keys(keys)
   
    
def text_element_XPATH(path='none'):
    return driver.find_element(By.XPATH,path).text.lower()


#=========================================================================================================================================

                             #>>>>>>>>>>>>>>>> BROWSER CLEANING FUNCTIONS <<<<<<<<<<<<<<<<<<<<<#

#==========================================================================================================================================
# function to clean browser
def clean_browser():
    """
    cleans the browser cookies and history
    
    Parameters 
    ----------
    None
    
    Returns 
    -------
    None
    
    """
    
    
    driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
    if driver_len > 1: # Will execute if more than 1 tabs found.
        for i in range(driver_len - 1, 0, -1):
            driver.switch_to.window(driver.window_handles[i]) #will close the last tab first.
            driver.close()
            print("Closed Tab No. ", i)
        driver.switch_to.window(driver.window_handles[0]) # Switching the driver focus to First tab.
    else:
        print("Found only Single tab.")
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get('chrome://settings/clearBrowserData') 
    time.sleep(2)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
    actions.perform()
    time.sleep(2)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
    actions.perform()
    time.sleep(5) # wait some time to finish
    driver.close() # close this tab
    driver.switch_to.window(driver.window_handles[0]) # switch back
    
    
    
#function for clean browser settings     
def clean_browser_settings():
    """
    decides wether to delete cookies or not
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    
    """
    with open(r"E:\projects_new\Major_Project\clean_browser_settings.txt","r")as file:
        lines = file.readlines() # read line inside the file
        for line in lines:
            if line == 'yes': # if line is yes clean the browser else don't
                driver.delete_all_cookies() 
                print('browser cleaned')
                #clean_browser()  # commented because using the above line for cleaning cookies, instead of old method.
                break
            else:
                pass    
     
    
   
#======================================================================================================================================

                                    #>>>>>>>>>>>>>> FUNCTION TO OPEN WEBSITE <<<<<<<<<<<<<#

#=======================================================================================================================================
  
def open_website(url,website_name,item_type,item_value,driver_failed,ow_tries=1):
    """
    opens the website
    
    Parameters
    ----------
    1. url - url of the website
    2. website_name - name of the website
    3. item_type - tells wether the input is email or phone no
    4. item_value - gives the actual email address or phone no
    5. driver_failed - tells wether the driver has failed or not
    6. ow_tries - tells the number of tries left to reopen the website
    
    Returns
    -------
    either True or False
    
    """
    
    global driver
    
    if driver_failed is False:
        pass     
           
    elif driver_failed is True:
        driver = driver_function()
          
    
    clean_browser_settings()  # call the setting function to check if clean brower is enabled and perfom cleaning
    #switchIP()
    driver.get(url)  # open the url
    driver.maximize_window()
    time.sleep(15)
    title = 'Just a moment...'
    if title == driver.title:  # check if the driver title matches above
        if ow_tries<=3:
            info_log('WARNING',website_name,'website not opening','trying again',item_value) # add to info log stating website opening failed trying again
            open_status =  open_website(url,website_name,item_type,item_value,driver_failed=driver_failed,ow_tries=ow_tries+1)
            return open_status # return if website is opened or not
                    
        else:
             
            return False
            
    else:
        info_log('INFO',website_name,'website opened','sucessfuly for',item_value) # add to info log stating website opened sucessfully for particular email or mobile
        return True  
    
    
 
            
  
#=========================================================================================================================================
    
                                   #>>>>>>>>>>>FUCNTION TO CHECK TEXT ON PAGE<<<<<<<<<<<<<<<<<<<<#
                                   
#==========================================================================================================================================
def check_text_on_page(message_list,disappear=False):
    """
    checks if text is present on the page
    
    Parameters
    ----------
    1. message_list - list containing the messages
    2. disappear - used for messages that disappear quickly
    
    Returns
    -------
    either True or False
    
    """
    
    if disappear is False:
        text = driver.find_element(By.TAG_NAME,'body').text.lower().strip() # find all text in the html body and convert it to lower case and remove white spaces
        text = re.sub('[.!+?&]','',text)  # remove special characters in the text
        search_status='nothing'           # intializig search status
        for message in message_list:      # loop the message list to find , if message is present in text
            if re.search(message,text):
                search_status = 'sucess'  # if messsage is present in text search_status will be sucess
                break                     # if search_status is succes exit from the for loop
            else:
                pass                      # else continue to loop till we find our message in text
            
        if search_status == 'sucess':     # if seearch status is sucess our chec_text_on_page will return True else False
            return True
        
        else:
            return False
        
        
       
    elif disappear is True:
        text = driver.page_source.lower()
        text = re.sub('[.!+?&]','',text)        # remove special characters in the text
        search_status='nothing'  
        for message in message_list:            # loop the message list to find , if message is present in text
            if re.search(message,text):   
                search_status = 'sucess'        # if messsage is present in page source search_status will be sucess
                break                           # if search_status is succes exit from the for loop
            else:
                pass                            # else continue to loop till we find our message in page source
            
        if search_status == 'sucess':           # if seearch status is sucess our chec_text_on_page will return True else False
            return True
        
        else:
            return False
        

#=======================================================================================================================================

                                        #>>>>>>>>>> CAPTCHA SOLVING FUNCTIONS <<<<<<<<<<<<<<<<#   
  
#========================================================================================================================================

 
 # v2 captcha
def v2_captcha():
    """
    solves google recaptcha v2 both visible and invisible
    
    Parameters 
    ----------
    None
    
    Returns
    -------
    wether captcha is 'solved' or 'notsolved'
    
    """
    
    try:
        
        driver.switch_to.frame(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[name^=a]'))))
        driver.find_element(By.XPATH, '//div[@class="recaptcha-checkbox-border"]')
        driver.switch_to.default_content()
        v2_visible = 'yes'
      
      
    except:
        
        driver.switch_to.default_content()
        
        try:
            if driver.find_element(By.XPATH,'(//iframe[@title="recaptcha challenge expires in two minutes"])[1]').is_displayed() is True:
                v2_visible = 'yes'
            else:
                v2_visible = 'no'
        
        
        except NoSuchElementException:
            try:
                if driver.find_element(By.XPATH,'(//iframe[@title="recaptcha challenge expires in two minutes"])[2]').is_displayed() is True:
                    v2_visible = 'yes'
                else:
                    v2_visible = 'no'
                
            except NoSuchElementException:
                try:
                    if driver.find_element(By.XPATH,'(//iframe[@title="recaptcha challenge expires in two minutes"])[3]').is_displayed() is True:
                        v2_visible = 'yes'
                    else:
                        v2_visible = 'no'
                
                except NoSuchElementException:
                    try:
                        if driver.find_element(By.XPATH,'(//iframe[@title="recaptcha challenge expires in two minutes"])[4]').is_displayed() is True:
                            v2_visible = 'yes'
                        else:
                            v2_visible = 'no'
                    except:
                        v2_visible = 'no' 
            
        
        
    print(v2_visible)
        
    if v2_visible == 'yes':    
        problem = reCaptchaV2(driver=driver, play=False) # call v2 captcha solving function
        if problem == False: # if problem is false , then  solution is notsolved
            sol = 'notsolved'
            return sol
   
    
        else: # check if problem is True, i.e captcha is solved
            driver.switch_to.frame(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[name^=a]')))) # switch the frame to captcha frame
            try:
                driver.find_element(By.CSS_SELECTOR, '.recaptcha-checkbox-checked') # verify if checkbox is cheked
                driver.switch_to.default_content() # switch to default frame
                sol = 'solved'
                return sol
            
            except:  # if chekbox is not cheked return not solved
                sol = 'notsoved'
                return sol
            
            
    elif v2_visible == 'no':
        sol = 'solved'
        return sol
        
#=========================================================================================================================================   

# hcaptcha
def h_captcha():
    """
    solves hcaptcha both visible and invisible
    
    Parameters 
    ----------
    None
    
    Returns
    -------
    wether captcha is 'solved' or 'notsolved'
    
    """
    
    hcaptchaAI(driver=driver)
    try:
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        driver.find_element(By.XPATH,'//div[@aria-checked="true"]')
        driver.switch_to.default_content()
        return 'solved'
    
    except NoSuchElementException:
        driver.switch_to.default_content()
        return 'notsolved'
    
#========================================================================================================================================   
    
    
# check captcha on page and return the type of captcha
def check_captcha():
    """
    checks the type of captcha on the page
    
    Parameters
    ----------
    None
    
    Returns
    ------
    either 0,1 or 3 based on the captcha type
    
    """
    
    try:
        
        if driver.find_element(By.XPATH,'//iframe[@title="reCAPTCHA"]'): # check if captcha is of type recaptcha
            captcha_type = 0
            return captcha_type
    
    
    
    except NoSuchElementException: # catch if above try fails
        try: #  check if captcha is of type hcaptcha
            if driver.find_element(By.XPATH,'//iframe[@title="Widget containing checkbox for hCaptcha security challenge"]'): 
                captcha_type = 1
                return captcha_type
        
        except NoSuchElementException: # if above try fails that means there is no captcha on page
            return 3
     
    
#=======================================================================================================================================
       
# solve captcha
def solve_captcha():
    """
    calls the check_captcha function and based on its output calls the v2_captcha or h_captcha function
    
    Parameters
    ----------
    None
    
    Returns
    -------
    either 'solved' or 'notsolved' or 'nocaptcha'
    
    """
    
    captcha_type=check_captcha() #check the captcha type 
    match captcha_type:
        case 0 :
            answer = v2_captcha() 
            return answer
   
        case 1:
            answer = h_captcha() 
            return answer
        
        case 3:
            answer = 'nocaptcha'
            return answer
        
        
   
#========================================================================================================================================