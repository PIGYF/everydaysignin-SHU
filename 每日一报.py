from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# ChromeDriver 镜像: http://npm.taobao.org/mirrors/chromedriver
# chromeDriver 下载以及放到scripts

# 不显示浏览器窗口
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)

url = 'https://selfreport.shu.edu.cn/XueSFX/HalfdayReport.aspx?t=1'
# url = 'https://selfreport.shu.edu.cn/XueSFX/HalfdayReport.aspx?t=2'
# browser = webdriver.Chrome()        # 打开chrome浏览器
browser.get(url)

# 信息
username = '19720732'
password = 'Zyf024532'
temperature = '36.0'

browser.find_element_by_id('username').send_keys(username)
browser.find_element_by_id('password').send_keys(password)
browser.find_element_by_id('submit').click()
print('登录成功')

browser.find_element_by_id('p1_ChengNuo-inputEl-icon').click()
browser.find_element_by_id('p1_TiWen-inputEl').clear()
browser.find_element_by_id('p1_TiWen-inputEl').send_keys(temperature)
browser.find_element_by_id('fineui_11-inputEl-icon').click()
browser.find_element_by_id('fineui_13-inputEl-icon').click()
browser.find_element_by_id('fineui_17-inputEl-icon').click()
browser.find_element_by_id('fineui_19-inputEl-icon').click()

browser.find_element_by_id('p1_ctl00_btnSubmit').click()     # 提交
browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/a[1]').click()
time.sleep(1)

browser.quit()

print('每日一报完成')


