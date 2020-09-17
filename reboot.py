

from selenium import webdriver
import time
import  subprocess



waiting_timer = 2

restart_timer = 30
# BUGGY CONNECTION TEST CODE


def connection_test():
    
    try:
        subprocess.check_output(['ping','google.com']).decode("utf-8")
        return False
    except subprocess.CalledProcessError:
      return  True



def  login():

    browser.maximize_window()
    
    browser.get('http://192.168.8.1/')

    time.sleep(waiting_timer)
    
    settings  =  browser.find_element_by_id('menu_settings')
    
    settings.click()

    time.sleep(waiting_timer)

    username_input_box =  browser.find_element_by_id('username')

    login_password_input_box = browser.find_element_by_id('password')

    login_button = browser.find_element_by_id('pop_login')

    username_input_box.send_keys('admin')

    login_password_input_box.send_keys('admin')

    login_button.click()

    


def reboot():
    
    time.sleep(waiting_timer)
    system_link = browser.find_element_by_id('system')

    reboot_link  =  browser.find_element_by_id('reboot')

    system_link.click()
    time.sleep(waiting_timer)
    reboot_link.click()
    time.sleep(waiting_timer)
    reboot_button =  browser.find_element_by_id('reboot_apply_button')

    reboot_button.click()
    time.sleep(waiting_timer)
    confirm_reboot_button = browser.find_element_by_id('pop_confirm')
    time.sleep(waiting_timer)
    
    confirm_reboot_button.click()

    time.sleep(30)

    browser.quit()


def  automate_reboot():

    login()

    reboot()




while True:
    

    time.sleep(waiting_timer)

    try:
        browser = webdriver.Chrome('chromedriver.exe')
        ping_data = connection_test()
        print(ping_data)
        if ping_data :

            automate_reboot()

            time.sleep(restart_timer)
        else:
            break

    except Exception:
        browser.quit()              

