#我的做法是先在Outlook里把要验证的几百个邮箱输入收件人，形成一个草稿然后复制那个草稿div的ID 再selenium启动浏览器返回人名等信息。


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time,random

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument('--headless')

#这里写webdriver路径
driver = webdriver.Chrome("webdriver路径",options=chrome_options)
driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1622598101&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f0%2f%3fstate%3d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC9pbmJveC9pZC9BUVFrQURBd0FUTTNabVlBWlMweFpUQTBMV1ZsQVdNdE1EQUNMVEF3Q2dBUUFOaXowNXY3UlRKRXBISnVERkJaQ2ZNPS8%26RpsCsrfState%3de8e92110-8ef0-d8d9-6d40-940f5cca2285&id=292841&aadredir=1&whr=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')

username = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//input[@id='i0116']")))
username.clear()
username.send_keys("邮箱"+"\n")#这里输入Outlook邮箱
time.sleep(2)

driver.execute_script("document.getElementById('i0118').setAttribute('class', 'form-control')")
password = WebDriverWait(driver, 50).until(
EC.presence_of_element_located((By.XPATH, "//input[@id='i0118']")))
password.clear()
password.send_keys("邮箱密码")#这里输入Outlook密码
driver.execute_script("document.getElementById('idSIButton9').disabled=false")
signinButton = driver.find_element_by_id('idSIButton9')
signinButton.send_keys(u"登录")
signinButton.click()

# 点击草稿
wait = ui.WebDriverWait(driver,50)
wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'草稿')]"))).click()
# 点击对应草稿
time.sleep(1)
wait2 = ui.WebDriverWait(driver,50)
wait2.until(EC.presence_of_element_located((By.XPATH, "//div[@id='ID']"))).click()#ID这里输入那个草稿的div id

#等待邮箱出现后点击邮箱
wait3 = ui.WebDriverWait(driver,50) 
wait3.until(lambda driver: driver.find_elements_by_xpath('//div[contains(@class,"personaInfoWrapper")]'))
emails=driver.find_elements_by_xpath('//div[contains(@class,"personaInfoWrapper")]')
length=len(emails)

for email in range(length):
    time.sleep(random.uniform(1.5,4.5))
    element=driver.find_elements_by_xpath('//div[contains(@class,"personaInfoWrapper")]')[email+1]
    driver.execute_script("return arguments[0].scrollIntoView(true);", element)
    time.sleep(random.uniform(3,7.5))
    driver.find_elements_by_xpath('//div[contains(@class,"personaInfoWrapper")]')[email].click()
    time.sleep(random.uniform(2,3.5))
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        try:
            email=driver.find_element_by_xpath('//span[contains(@class,"contentLine-")]').text
        except:
            email="Error"          

        #3秒等待linkedin出现后点击
        wait = ui.WebDriverWait(driver,50)
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"customScrollBar centeredOverlayContainer")]')))
        time.sleep(random.uniform(3.5,5.5))
        click_linkedin=driver.find_element_by_name("领英")
        ActionChains(driver).click(click_linkedin).perform()
        time.sleep(random.uniform(1,2.5))
        try:
            name=driver.find_element_by_xpath('//span[contains(@class,"displayName-")]').text
        except:name="no name"
        try:
            job=driver.find_element_by_xpath('//div[contains(@class,"title-")]').get_attribute('title')
        except:
            job="jobless"
        try:
            location=driver.find_element_by_xpath('//span[contains(text(),"联系人")]').text
        except:
            location="homeless"
        data=[email,name,job,location]
        print(data)
        #3秒后关闭窗口
        time.sleep(random.uniform(2.5,4.5))
        click_linkedin=driver.find_element_by_xpath('//button[contains(@class,"ms-Button--action ms-Button--command button")]')
        ActionChains(driver).click(click_linkedin).perform()
        time.sleep(random.uniform(1,2.5))
        driver.switch_to.window(handle)
        

        
            





        
        
    
        
    





    














