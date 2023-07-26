import requests
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By


class Department(scrapy.Spider):
    name = 'department'
    start_urls = ['https://djursbo.dk/umbraco/api/DepartmentSelector/GetDepartments']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def parse(self, response)->dict:
        data = requests.get(self.start_urls[0])
        if data.status_code == 200:
            content_data = data.json()
            for item in content_data['Data']['Departments']:
                dict_adres = (item['Addresses'][0])
                Description = item['Description']
                PresentationUrl = response.urljoin(item.get('PresentationUrl'))
                self.driver.get(PresentationUrl)
                self.driver.implicitly_wait(15)
                # time.sleep(2)
                prise = self.driver.find_element(By.CLASS_NAME, 'larger').text
                yield {
                    'Description': Description,
                    'dict_adres': dict_adres if dict_adres else 'None',
                    'PresentationUrl': response.urljoin(PresentationUrl) if PresentationUrl else 'None',
                    'Prise': prise if prise else 'None'
                }
        else:
            print(data.status_code)
            pass
