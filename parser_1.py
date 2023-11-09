from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
from unicodedata import normalize
import time 


#weddriver add
browser = webdriver.Chrome()
browser.get("https://raspis.rggu.ru")

def main_button_click(name):
    return browser.find_element(By.XPATH, f"//*[text() = '{name}']").click()

def select_by_value(selectID, value):
    select = Select(browser.find_element(By.ID, selectID))
    select.select_by_value(str(value))

def select_by_text(selectID, value):
    select = Select(browser.find_element(By.ID, selectID))
    select.select_by_visible_text(value)

def group_checker(input_el, key, selectID): #input study group, check equals with select and return table-name result for check
    elem  =  browser.find_element(By.NAME,  input_el)
    elem.send_keys(key)
    time.sleep(10)
    select = Select(browser.find_element(By.ID, selectID))
    return select.first_selected_option.text

def table_drawer():
    return pd.read_html(browser.page_source, match="Пара", flavor='lxml')



main_button_click('Расписание по потоку')

select_by_value("formob", "Д") #форма обучения
select_by_value("kyrs", 2) #курс
select_by_text("srok", "На неделю") #курс
time.sleep(5)

group_checker("fprep", "ПИГС", "caf")
browser.find_element(By.NAME, "potokbut2").click()
time.sleep(5)

print(table_drawer())


time.sleep(10)
browser.close()
# class = btn-top col-12 col-md-3  id = potokb  "//*[text() = 'Расписание по потоку']"