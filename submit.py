<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
username = 'xxx'     #你的用户名
password = 'xxx'     #你的密码
url = 'https://jkxxcj.zjhu.edu.cn/login.html'
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('window-size=1920x3000')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--headless')
driver=webdriver.Chrome(r'/root/chromedriver',options=chrome_options)   #改成你自己的chromedriver在服务器中的路径
driver.get(url)
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/ul/li[1]/div[2]/input').send_keys(username)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/ul/li[2]/div[2]/input').send_keys(password)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/ul/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/ul/li[2]/a').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/button').click()
time.sleep(3)
if driver.find_element_by_xpath('/html/body/div[4]/div[3]/a'):
    driver.find_element_by_xpath('/html/body/div[4]/div[3]/a').click()
    print("success")
driver.close()
=======
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
username = 'xxx'     #你的用户名
password = 'xxx'     #你的密码
url = 'https://jkxxcj.zjhu.edu.cn/login.html'
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('window-size=1920x3000')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--headless')
driver=webdriver.Chrome(r'/root/chromedriver',options=chrome_options)   #改成你自己的chromedriver在服务器中的路径
driver.get(url)
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/ul/li[1]/div[2]/input').send_keys(username)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/ul/li[2]/div[2]/input').send_keys(password)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/ul/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/ul/li[2]/a').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/button').click()
time.sleep(3)
if driver.find_element_by_xpath('/html/body/div[4]/div[3]/a'):
    driver.find_element_by_xpath('/html/body/div[4]/div[3]/a').click()
    print("success")
driver.close()
>>>>>>> 4564c5c (first add)
