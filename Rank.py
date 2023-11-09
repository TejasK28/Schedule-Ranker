from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# constant links
CSP_LOGIN_PAGE = 'https://sims.rutgers.edu/csp/'

# Provide the correct path to your chromedriver executable
service = Service('Users\\Tejas\\Downloads\\chromedriver.exe')  # Replace with the actual path

# Initialize the webdriver with the service
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")

# Rest of your code...
