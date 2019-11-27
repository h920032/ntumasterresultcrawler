from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

chromedriver = "/Users/hugoshih/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get('http://gra108.aca.ntu.edu.tw/regchk/stu_query.asp')

s1 = Select(driver.find_element_by_name('DEP'))

s1.select_by_index(200)  #更改這個可以對應到不同的研究所
driver.find_element_by_name('qry').click()

soup = BeautifulSoup(driver.page_source, "html.parser")

a_tags = soup.select('td')
table = soup.find('table', {'class': 'w15'})
columns = [th.text.replace('\n', '') for th in table.find('tr').find_all('td')]
trs = table.find_all('tr')[1:]
rows = list()
for tr in trs:
    rows.append([td.text.replace('\n', '').replace('\xa0', '').replace('\t', '') for td in tr.find_all('td')])
df = pd.DataFrame(data=rows, columns=columns)
count = 0
for i in df.values:
    if int(i[0]) < 58:
        if i[4] == '已放棄':
            count = count+1
count2 = 0
for i in df.values:
    if int(i[0]) < 58:
        if i[4] == '未報到':
            count2 = count2+1
count3 = 0
for i in df.values:
    if int(i[0]) < 58:
        if i[4] != '未報到' and i[4] != '已放棄':
            count3 = count3+1
print("電信所\n已放棄："+str(count)+"\n未報到："+str(count2)+"\n已報到："+str(count3))


driver.get('http://gra108.aca.ntu.edu.tw/regchk/stu_query.asp')

s1 = Select(driver.find_element_by_name('DEP'))  # 例項化Select


s1.select_by_index(179)
driver.find_element_by_name('qry').click()

soup2 = BeautifulSoup(driver.page_source, "html.parser")
a_tags = soup2.select('td')
table = soup2.find('table', {'class': 'w15'})
columns = [th.text.replace('\n', '') for th in table.find('tr').find_all('td')]
trs2 = table.find_all('tr')[1:]
rows = list()
for tr in trs2:
    rows.append([td.text.replace('\n', '').replace('\xa0', '').replace('\t', '') for td in tr.find_all('td')])
df = pd.DataFrame(data=rows, columns=columns)
count = 0
for i in df.values:
    if int(i[0]) < 58:
        if i[4] == '已放棄':
            count = count+1
count2 = 0
for i in df.values:
    if int(i[0]) < 58:
        if i[4] == '未報到':
            count2 = count2+1
count3 = 0
for i in df.values:
    if int(i[0]) < 58:
        if i[4] != '未報到' and i[4] != '已放棄':
            count3 = count3+1
print("\n資管所\n已放棄："+str(count)+"\n未報到："+str(count2)+"\n已報到："+str(count3))

driver.quit()
