import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

from database_sqlalchemy.connect_sqlite import ConnectSqlite


class DownloadElement(object):
    def __init__(self):
        edge_options = Options()
        edge_options.add_argument('--headless')
        self.web_driver = webdriver.Edge(
            options=edge_options,
            service=Service(r'web_driver/msedgedriver.exe')
        )
        self.url = "https://ptable.com/?lang=zh-hans#%E6%80%A7%E8%B4%A8/%E7%B3%BB%E5%88%97"

        self.connect_sqlite = ConnectSqlite()

        # self.database_conn = sqlite3.connect(
        #     'database_sqlalchemy/identifier.sqlite')
        # self.cursor = self.database_conn.cursor()

    @staticmethod
    def save_json(path, data):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def main(self):
        self.web_driver.get(self.url)
        element_list = self.web_driver.find_element(By.ID,
                                                    'Ptable').find_elements(
            By.TAG_NAME, 'li')

        element_data = []

        for element in element_list:
            if element.text:
                element.click()
                time.sleep(0.5)

                basic_info = element.text.split('\n')
                # 原子序数
                atomic_num = int(basic_info[0])
                # 化学符号
                element_symbol = basic_info[1]
                # 名称
                name = basic_info[2]
                # 原子量
                atomic_mass = basic_info[3].replace('(', '').replace(')', '')

                # 类型
                element_type = self.web_driver.find_element(By.XPATH, '//*[@id="Property"]/li[1]/output').text
                # 状态
                element_status = self.web_driver.find_element(By.XPATH, '//*[@id="Property"]/li[3]/output').text
                # 维基百科
                wikipedia_url = self.web_driver.find_element(By.XPATH, '//*[@id="AsideWriteup"]/a').get_attribute('href')
                # 能级
                energy_level = self.web_driver.find_element(By.XPATH, '//*[@id="Property"]/li[5]/output').text
                # 电负性
                electronegativity = self.web_driver.find_element(By.XPATH, '//*[@id="Property"]/li[6]/output').text
                # 熔点
                fusing_point = self.web_driver.find_element(By.XPATH, '//*[@id="Property"]/li[7]/output').text.replace(',', '')
                # 沸点
                boiling_point = self.web_driver.find_element(By.XPATH, '//*[@id="Property"]/li[8]/output').text.replace(',', '')
                # 电子亲和能
                electronic_affinity = self.web_driver.find_element(By.XPATH, '//*[@id="Property"]/li[9]/output').text
                # 发现年份
                year_of_discovery = self.web_driver.find_element(By.XPATH, '//*[@id="Property"]/li[18]/output').text

                electron_shells_list = self.web_driver.find_elements(By.XPATH, '//*[@id="CloseUp"]/small/span')
                electron_shells = []
                for electron_shell in electron_shells_list:
                    electron_shells.append(electron_shell.text)

                element_info = {
                    'element_type': element_type,
                    'atomic_num': atomic_num,
                    'element_symbol': element_symbol,
                    'element_status': element_status,
                    'name': name,
                    'atomic_mass': float(atomic_mass),
                    'electron_shells': str(electron_shells),
                    'fusing_point': float(fusing_point) if fusing_point and fusing_point != 'N/A' else None,
                    'boiling_point': float(boiling_point) if boiling_point and boiling_point != 'N/A' else None,
                    'energy_level': int(energy_level),
                    'electronegativity': float(electronegativity) if electronegativity and electronegativity != 'N/A' else None,
                    'electronic_affinity': float(electronic_affinity) if electronic_affinity and electronic_affinity != 'N/A' else None,
                    'encyclopedia_entry': str(wikipedia_url),
                    'year_of_discovery': year_of_discovery
                }
                print(element_info)
                # element_data.append(element_info)
                # self.insert_data('chemical_element', element_info)
                print(f'原子序数：{atomic_num}, 化学符号：{element_symbol}, 元素名：{name}, 原子量：{atomic_mass}')
                print(f'电子层：{electron_shells}, 元素状态：{element_status}')
                print(f'熔点：{fusing_point}, 沸点：{boiling_point}')
                print(f'元素类型：{element_type}, 能级：{energy_level}, 电负性：{electronegativity}, 电子亲和能：{electronic_affinity}')
                print(f'维基百科：{wikipedia_url}')
                print(f'发现年份: {year_of_discovery}')
                print('----')
                element_data.append(element_info)
        self.web_driver.quit()
        self.connect_sqlite.add_all_element_data(element_data)
        self.save_json('static/element_data.json', element_data)


if __name__ == '__main__':
    download_element = DownloadElement()
    download_element.main()
