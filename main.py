from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_TH(url, key_world):
    n=3
    title = []
    href = []
    browser = webdriver.Edge()
    browser.get(url)
    browser.find_element(By.ID, 'keyword').send_keys(key_world)
    browser.find_element(By.CLASS_NAME, 'search_submit').click()
    time.sleep(1)
    for link in browser.find_elements(By.XPATH, "//h3[@class=\"item_title\"]//a[@href]"):
        if n>0:
            title.append(link.text)
            href.append(link.get_attribute('href'))
            n-=1
        else:
            break
    browser.quit()
    return title, href


results = []
url = 'https://www.jxau.edu.cn/_web/search/doSearch.do?locale=zh_CN&request_locale=zh_CN&_p=YXM9MiZ0PTI3NDAmZD02NzQzJnA9MSZtPVNOJg__'
key_word = ['农学院', '计信院', '软件院']

for i in range(3):
    title, href = get_TH(url, key_word[i])
    for j in range(3):
        print(title[j], href[j])
        results.append(title[j])
        results.append(href[j])

with open('result.txt', 'w') as f:
    for x in results:
        f.write(str(x)+'\n')
    f.close()