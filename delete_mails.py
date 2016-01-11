from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get('https://mail.yahoo.com')
driver.find_element_by_id('login-username').click()
driver.find_element_by_id('login-username').clear()
driver.find_element_by_id('login-username').send_keys("your_yahoo_mail_id")#eg: yohan_saby@yahoo.co.in
driver.find_element_by_id('login-passwd').click()
driver.find_element_by_id('login-passwd').clear()
driver.find_element_by_id('login-passwd').send_keys("your_password")
driver.find_element_by_id('login-signin').click()


while(True):
    print 'deleting'
    
    # I had superslow internet and hence i gave implicit wait 30. You can ofcourse reduce it 
    # but it actually won't matter since its implicit wait.
    driver.implicitly_wait(30)
    checkbox = driver.find_element_by_css_selector('input[data-action="selectAll-message"]')
    i = 0
    ''' 
    There are arbitarily 10 attempts made to select the checkbox. 
    The reason it is put in while loop is because sometimes for unknown reasons the checkbox is not selected in one go.
    Also, if there are no more mails to be deleted then the loop might go infinte. Hence, I arbitarily chose 10 attempts
    '''
    while not checkbox.is_selected():
        if i == 9:
            break
        else:
            checkbox.click()
            i +=9

    print 'is checkbox selected',checkbox.is_selected()
    if checkbox.is_selected():
        wait = WebDriverWait(driver, 30)#arbitary wait time
        delete_button = wait.until(EC.element_to_be_clickable((By.ID,'btn-delete')))
        delete_button.click()

        confirm_button = wait.until(EC.element_to_be_clickable((By.ID,'okModalOverlay')))
        confirm_button.click()
        
        time.sleep(10)#sleeping as yahoo mail takes some time if there are lot of messages to be deleted.
        print 'deleted'
    else:
        print 'Looks like there are no more mails to delete'
        break
