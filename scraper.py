# Import requests
from datetime import datetime 
import time
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 


# Create a dictionary to hold all the data
variables = ['NAME', 'RANGE', 'ROUND-TRIP LIGHT TIME', 'NAME', 'AZIMUTH', 'ELEVATION', 'WIND SPEED', 'MODE', 'SOURCE', 'FREQUENCY BAND', 'DATA RATE', 'POWER RECEIVED']
res = dict.fromkeys(variables, 0)

