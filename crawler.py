from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# chrome option 세팅
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)      # 프로세스가 종료된 후 Selenium Browser가 자동으로 종료되지 않도록
# chrome_options.add_argument('window-size=1920x1080')
# chrome_options.add_argument('lang=ko_KR')
# chrome_options.add_argument("disable-gpu")
# chrome_options.add_argument('--disable-infobars')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--remote-debugging-port=9222')
# chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument('headless')

# OS에 설치된 Chrome Driver 버전에 맞게 Install
chrome_driver = ChromeDriverManager().install()
print("드라이버 설치 완료 : ", chrome_driver)

# driver 생성
driver = webdriver.Chrome(service=ChromeService(chrome_driver), options=chrome_options)

# 접속하고자 하는 페이지 uri
driver.get("https://www.naver.com")