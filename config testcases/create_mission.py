from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.get("https://admin.staging.go-games.gg/admin/login/?next=/admin/")

time.sleep(5)

# login django admin panel
uname = driver.find_element(By.NAME, 'username')
uname.send_keys('*******')

password = driver.find_element(By.NAME, 'password')
password.send_keys('*******')

login_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input')
login_button.click()

time.sleep(5)

# Automated Mission Creation
# Navigate to mission offer section
driver.get("https://admin.staging.go-games.gg/admin/tournaments/missionoffer/")
time.sleep(5)

# open mission creation form
driver.get("https://admin.staging.go-games.gg/admin/tournaments/missionoffer/add/")

# Application set
application = driver.find_element(By.NAME, 'application')
application.send_keys('ghost')

# country Set
country = driver.find_element(By.XPATH, '//*[@id="id_countries"]')
select = Select(country)
select.select_by_visible_text("Bangladesh")

# mission number
mission = driver.find_element(By.NAME, 'mission')
mission.send_keys('1')

# variables(score) set
variables = driver.find_element(By.NAME, 'variables')
variables.send_keys('1')

# reward set
reward = driver.find_element(By.NAME, 'reeward')
reward.send_keys('1')

# reward type set
reward_type = driver.find_element(By.XPATH, '//*[@id="id_reward_type"]')
select = Select(reward_type)
select.select_by_visible_text("Goama Token")

# Set start and end time
start_date = driver.find_element(By.XPATH, '//*[@id="id_start_date_0"]')
start_date.send_keys("2024-06-10")

start_time = driver.find_element(By.XPATH, '//*[@id="id_start_date_1"]')
start_time.send_keys('13:20:30')

end_date = driver.find_element(By.XPATH, '//*[@id="id_end_date_0"]')
end_date.send_keys("2024-06-25")

end_time = driver.find_element(By.XPATH, '//*[@id="id_end_date_1"]')
end_time.send_keys('13:20:30')

# Click the Save button
save_button = driver.find_element(By.NAME, '_save')
save_button.click()
time.sleep(10)
