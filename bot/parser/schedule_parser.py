from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time


class ParserUni:
    def __init__(self, srok, input_data, download_mode, parse_mode, formob="", kurs=""):
        global browser
        browser = webdriver.Chrome()
        inverse_graduate = {"дневная": "Д", "вечерняя": "В", "заочная": "З", "второе высшее": "2",
                            "магистратура": "М", "аспирантура": "А", "дистанционное": "У"}
        inverse_kurs = {"курс 1": "1", "курс 2": "2", "курс 3": "3", "курс 4": "4",
                        "курс 5": "5", "курс 6": "6"}

        self.formob = inverse_graduate.get(formob)
        self.kurs = inverse_kurs.get(kurs)
        self.srok = str(srok).capitalize()
        self.input_data = str(input_data).upper()
        self.download_mode = download_mode
        self.parse_mode = parse_mode

    def parse_teacher(self):
        browser.get("https://raspis.rggu.ru")

        self.main_button_click("Расписание по преподавателю")

        self.group_checker("fprep1", self.input_data, "prep")
        time.sleep(1)
        self.select_by_text("srokprep", self.srok)
        browser.find_element(By.NAME, "prepbut").click()
        time.sleep(3)

        return self.table_drawer()

    def parse_group(self):
        browser.get("https://raspis.rggu.ru")

        self.main_button_click("Расписание по потоку")

        self.select_by_value("formob", self.formob)
        self.select_by_value("kyrs", self.kurs)
        self.select_by_text("srok", self.srok)
        browser.find_element(By.NAME, "potokbut").click()
        time.sleep(3)

        self.group_checker("fprep", self.input_data, "caf")
        browser.find_element(By.NAME, "potokbut2").click()
        time.sleep(3)
        return self.table_drawer()

    @staticmethod
    def main_button_click(name):
        return browser.find_element(By.XPATH, f"//*[text() = '{name}']").click()

    @staticmethod
    def select_by_value(select_id, value):
        select = Select(browser.find_element(By.ID, select_id))
        select.select_by_value(str(value))

    @staticmethod
    def select_by_text(select_id, value):
        select = Select(browser.find_element(By.ID, select_id))
        select.select_by_visible_text(value)

    @staticmethod
    def group_checker(input_el, key,
                      select_id):  # input, check equals with select and return table-name result for check
        elem = browser.find_element(By.NAME, input_el)
        elem.send_keys(key)
        time.sleep(5)
        select = Select(browser.find_element(By.ID, select_id))
        return select.first_selected_option.text

    def table_drawer(self):

        pd.set_option("display.max_columns", None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.width', 1000)
        pd.set_option('max_colwidth', 400)
        pd.set_option("display.colheader_justify", "right")

        def auto_truncate(val):
            return val[:25] + '.'

        try:
            df_list = pd.read_html(browser.page_source, header=0, match="Пара", converters={'Предмет': auto_truncate})
            df = df_list[0]
        except ValueError:
            return 0

        if self.download_mode:
            df.to_excel(r"/Users/alexded/Desktop/rg_sch_par/bot/files/schedule.xlsx", index=False)
        elif self.parse_mode == "group":
            df['Дата'] = df['Дата'].str[:5]
            res = (df.rename(columns={"Группа": "Гр."}).drop('Тип', axis=1)
                   .to_string(index=False, justify='center', col_space=10))
            return res
        elif self.parse_mode == "teach":
            res = (df.rename(columns={"Группа": "Гр."}).drop('Тип', axis=1)
                   .to_string(index=False, justify='center', col_space=10))
            return res

# print(ParserUni(srok="дневная", input_data = "Пигс", download_mode = False, formob="дневная", kurs ="курс 2").parse_group())
# print(ParserUni(srok="дневная", input_data="Алексеев", download_mode=False, parse_mode="teach").parse_teacher())
