from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller

class DjursboSpider:
    def __init__(self):
        chromedriver_autoinstaller.install(cwd=True)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def parse(self, url):
        self.driver.get(url)

        # Збільшуємо затримку на 10 секунд
        time.sleep(10)

        department_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.col-xs-12.col-md-5')

        for department_elem in department_elements:
            # department_name = department_elem.find_element(By.CSS_SELECTOR, 'h3.ng-binding').text
            # department_number = department_elem.find_element(By.CSS_SELECTOR, 'span.dep-number.ng-binding').text
            # address = department_elem.find_element(By.CSS_SELECTOR, 'span.ng-binding.ng-scope').text
            # min_rent = department_elem.find_element(By.CSS_SELECTOR, 'span.ng-binding').text
            # min_sqm = department_elem.find_element(By.CSS_SELECTOR, 'span.pull-right span.ng-binding').text
            # max_sqm = department_elem.find_element(By.CSS_SELECTOR, 'span.pull-right span.ng-binding:last-child').text
            # min_rooms = department_elem.find_element(By.CSS_SELECTOR, 'p:nth-child(3) span.pull-right span.ng-binding:first-child').text
            # max_rooms = department_elem.find_element(By.CSS_SELECTOR, 'p:nth-child(3) span.pull-right span.ng-binding:last-child').text
            # department_description = department_elem.find_element(By.CSS_SELECTOR, 'div.department-description span.ng-binding').text
            afdelingssiden_link = department_elem.find_element(By.CSS_SELECTOR, 'a.link-icon').get_attribute('href')

            yield {
                # 'department_name': department_name,
                # 'department_number': department_number,
                # 'address': address,
                # 'min_rent': min_rent,
                # 'min_sqm': min_sqm,
                # 'max_sqm': max_sqm,
                # 'min_rooms': min_rooms,
                # 'max_rooms': max_rooms,
                # 'department_description': department_description,
                'afd_link': afdelingssiden_link,
            }

        self.driver.quit()

if __name__ == "__main__":
    spider = DjursboSpider()
    url = 'https://djursbo.dk/for-boligsoegende/boligsoegning/#ar=1%252C10%252C11%252C12%252C13%252C14%252C15%252C2%252C3%252C4%252C5%252C6%252C7%252C8%252C9&tt=&at=&pr=&wa=&ro=1%253B5&re=null%253B9000&si=0%253B140&av=false&pe=false&cNo=&dNo=&p=0'
    data = spider.parse(url)
    for item in data:
        print(item)
