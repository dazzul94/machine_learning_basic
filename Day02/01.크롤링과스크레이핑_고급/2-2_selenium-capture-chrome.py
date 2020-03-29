from selenium import webdriver

path = "C:/Users/dazzul/Documents/GitHub/machine_learning_basic/chromeDriver/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("headless") # 랜더링이 되지만 헤더리스이기 때문에 안보인다.
driver = webdriver.Chrome(path, chrome_options=options)

driver.get('http://naver.com')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('naver_main.png')
driver.quit()
