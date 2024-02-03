# Import requests
from datetime import datetime 
import time
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 
from flask import Flask, request, render_template
import vidaudio
import sys


app = Flask(__name__)

userUrl = ""

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    if request.method == "POST":
       # getting input with freq = set_freq in HTML form
       userUrl = request.form.get("userUrl") # <--- do whatever you want with that value
       return userUrl
    return render_template("upload.html")
  
if __name__=='__main__':
   app.run()

URL = userUrl
 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 

driver.implicitly_wait(3)

driver.get(URL) 
time.sleep(3)

allText = driver.find_elements(By.CSS_SELECTOR, "p")

length = len(allText)

while len(allText) > 0:
    vidaudio.script_to_subclips(allText[length-len(allText)])


