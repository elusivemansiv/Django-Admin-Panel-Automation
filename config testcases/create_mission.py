from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime, timedelta

driver = webdriver.Chrome()
driver.get("https://admin.dev.go-games.gg/admin/login/?next=/admin/")

time.sleep(5)

# login django admin panel
uname = driver.find_element(By.NAME, 'username')
uname.send_keys('********')

password = driver.find_element(By.NAME, 'password')
password.send_keys('********')

login_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input')
login_button.click()

time.sleep(5)

# Automated Mission Creation

# open mission creation form
driver.get("https://admin.dev.go-games.gg/admin/tournaments/missionoffer/add/")

# Application set
application = driver.find_element(By.NAME, 'application')
application.send_keys('testa-app')

# country Set
country = driver.find_element(By.XPATH, '//*[@id="id_countries"]')
select = Select(country)
select.select_by_visible_text("Bangladesh")

# mission number
mission = driver.find_element(By.NAME, 'mission')
mission.send_keys('18')

# variables(score) set
variables = driver.find_element(By.NAME, 'variables')
variables.clear()
variables.send_keys('1')

# reward set
reward = driver.find_element(By.NAME, 'reeward')
reward.clear()
reward.send_keys('10')

# reward type set
reward_type = driver.find_element(By.XPATH, '//*[@id="id_reward_type"]')
select = Select(reward_type)
select.select_by_visible_text("Goama Token")

# Set start and end time
# Get the current date and time
current_datetime = datetime.now()

# Adjust for time zone difference (you are 6 hours ahead)
current_datetime = datetime.now() - timedelta(hours=6)
end_datetime = current_datetime + timedelta(hours=24)

# Format dates and times
start_date_str = current_datetime.strftime('%Y-%m-%d')
start_time_str = current_datetime.strftime('%H:%M:%S')
end_date_str = end_datetime.strftime('%Y-%m-%d')
end_time_str = end_datetime.strftime('%H:%M:%S')

# Set start date and time
start_date = driver.find_element(By.XPATH, '//*[@id="id_start_date_0"]')
start_date.clear()
start_date.send_keys(start_date_str)

start_time = driver.find_element(By.XPATH, '//*[@id="id_start_date_1"]')
start_time.clear()
start_time.send_keys(start_time_str)

# Set end date and time
end_date = driver.find_element(By.XPATH, '//*[@id="id_end_date_0"]')
end_date.clear()
end_date.send_keys(end_date_str)

end_time = driver.find_element(By.XPATH, '//*[@id="id_end_date_1"]')
end_time.clear()
end_time.send_keys(end_time_str)

# Click the Save button
save_button = driver.find_element(By.NAME, '_save')
save_button.click()
time.sleep(10)
