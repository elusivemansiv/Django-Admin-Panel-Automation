from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime, timedelta

driver = webdriver.Chrome()
driver.get("https://admin.staging.go-games.gg/admin/login/?next=/admin/")

time.sleep(5)

# login django admin panel
uname = driver.find_element(By.NAME, 'username')
uname.send_keys('*****')

password = driver.find_element(By.NAME, 'password')
password.send_keys('*****')

login_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input')
login_button.click()

time.sleep(5)

# Automated Daily login Creation
# Navigate to campaign Daily login section
driver.get("https://admin.staging.go-games.gg/admin/campaign/dailyreturndriverconf/")
time.sleep(5)

# open mission creation form
driver.get("https://admin.staging.go-games.gg/admin/campaign/dailyreturndriverconf/add/")

# Application set
application = driver.find_element(By.NAME, 'application')
application.send_keys('gotest')

# country Set
country = driver.find_element(By.XPATH, '//*[@id="id_country"]')
select = Select(country)
select.select_by_visible_text("Bangladesh")

# banner title
b_title = driver.find_element(By.NAME, 'banner_title')
b_title.send_keys('Daily Login Rewards')

# cta text
cta_txt = driver.find_element(By.NAME, 'cta_text')
cta_txt.send_keys('Claim Now')


# Set start and end time
# Get the current date and time
current_datetime = datetime.now()

# Adjust for time zone difference (you are 6 hours ahead)
end_datetime = current_datetime + timedelta(hours=72)

# Format dates and times
start_date_str = current_datetime.strftime('%Y-%m-%d')
end_date_str = end_datetime.strftime('%Y-%m-%d')

# Set start date
start_date = driver.find_element(By.XPATH, '//*[@id="id_start_date"]')
start_date.clear()
start_date.send_keys(start_date_str)

# Set end date
end_date = driver.find_element(By.XPATH, '//*[@id="id_end_date"]')
end_date.clear()
end_date.send_keys(end_date_str)

# DAILY RETURN DRIVER PROGRAMS
# Serial title
sl_title = driver.find_element(By.NAME, 'return_progress-0-serial_title')
sl_title.send_keys('Day 1')

sl_number = driver.find_element(By.NAME, 'return_progress-0-serial')
sl_number.send_keys('1')

reward = driver.find_element(By.NAME, 'return_progress-0-reward')
reward.send_keys('5')

reward_type = driver.find_element(By.XPATH, '//*[@id="id_return_progress-0-reward_type"]')
select = Select(reward_type)
select.select_by_visible_text("ticket")


# Click the Save button
save_button = driver.find_element(By.NAME, '_save')
save_button.click()
time.sleep(10)
