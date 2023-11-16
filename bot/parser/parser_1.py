from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import pandas.io.formats.style
from unicodedata import normalize
import time


class Potok_parser:
    def __init__(self, formob: str, kurs: str, srok, caf, download_mode):
        global browser
        browser = webdriver.Chrome()

        if formob.lower() == "дневная":
            self.formob = "Д"
        if kurs.lower() == "курс 1":
            self.kurs = 1
        self.srok = str(srok).capitalize()
        self.caf = str(caf).upper()
        self.download_mode = download_mode

    def parse(self):

        browser.get("https://raspis.rggu.ru")

        self.main_button_click("Расписание по потоку")

        self.select_by_value("formob", self.formob)
        self.select_by_value("kyrs", self.kurs)
        self.select_by_text("srok", self.srok)
        browser.find_element(By.NAME, "potokbut").click()
        time.sleep(5)

        self.group_checker("fprep", self.caf, "caf")
        browser.find_element(By.NAME, "potokbut2").click()
        time.sleep(5)

        return self.table_drawer()

    def main_button_click(self, name):
        return browser.find_element(By.XPATH, f"//*[text() = '{name}']").click()

    def select_by_value(self, selectID, value):
        select = Select(browser.find_element(By.ID, selectID))
        select.select_by_value(str(value))

    def select_by_text(self, selectID, value):
        select = Select(browser.find_element(By.ID, selectID))
        select.select_by_visible_text(value)

    def group_checker(self, input_el, key,
                      selectID):  # input study group, check equals with select and return table-name result for check
        elem = browser.find_element(By.NAME, input_el)
        elem.send_keys(key)
        time.sleep(5)
        select = Select(browser.find_element(By.ID, selectID))
        return select.first_selected_option.text

    def table_drawer(self):

        pd.set_option("display.max_columns", None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', 1000)
        pd.set_option('max_colwidth', 400)
        pd.set_option("display.colheader_justify", "right")

        def auto_truncate(val):
            return val[:25] + '.'

        df_list = pd.read_html(browser.page_source, header=0, match="Пара", converters={'Предмет': auto_truncate})
        df = df_list[0]

        if self.download_mode:
            df.to_excel(r"/Users/alexded/Desktop/rg_sch_par/bot/files/schedule.xlsx", index=False)
        else:
            df['Дата'] = df['Дата'].str[:5]
            res = df.rename(columns={"Группа": "Гр."}).drop('Тип', axis=1).to_string(index=False, justify='center',
                                                                                     col_space=10)
            return res


# Potok_parser("дневная", "курс 1", "на неделю", "ПИГС", download_mode = False).parse()


"""main_button_click('Расписание по потоку')

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
"""
