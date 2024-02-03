# Import requests
from datetime import datetime 
import time
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 
import vidaudio


# app = Flask(__name__)

userUrl = "https://www.cs.cmu.edu/~15150/resources/lectures/02/lecture02.html"

URL = userUrl
 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 

driver.implicitly_wait(3)

driver.get(URL) 
time.sleep(3)

allText = driver.find_elements(By.CSS_SELECTOR, "p")

length = len(allText)

while len(allText) > 0:
    print(allText[0])
    vidaudio.script_to_subclips("hello.webm", allText[length-len(allText)], 7)


