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
uname.send_keys('********')

password = driver.find_element(By.NAME, 'password')
password.send_keys('********')

login_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input')
login_button.click()

time.sleep(5)

# Navigate to tournaments section
driver.get("https://admin.staging.go-games.gg/admin/tournaments/tournament/")
time.sleep(5)

# open tournament creation form
driver.get("https://admin.staging.go-games.gg/admin/tournaments/tournament/add/")

# name field
tournament_name = driver.find_element(By.NAME, 'name')
tournament_name.send_keys('Automated tournament_03')

# Application set
application = driver.find_element(By.NAME, 'application')
application.send_keys('ghost')

# country code field
country = driver.find_element(By.NAME, 'country')
country.send_keys('BD')

# Game Set
game = driver.find_element(By.XPATH, '//*[@id="id_game"]')
select = Select(game)
select.select_by_visible_text("Amigos")

# Set Game start and end time
current_datetime = datetime.now() - timedelta(hours=6)
end_datetime = current_datetime + timedelta(hours=24)

# Format dates and times
start_date_str = current_datetime.strftime('%Y-%m-%d')
start_time_str = current_datetime.strftime('%H:%M:%S')
end_date_str = end_datetime.strftime('%Y-%m-%d')
end_time_str = end_datetime.strftime('%H:%M:%S')

# Set start date and time
start_date = driver.find_element(By.XPATH, '//*[@id="id_start_time_0"]')
start_date.clear()
start_date.send_keys(start_date_str)

start_time = driver.find_element(By.XPATH, '//*[@id="id_start_time_1"]')
start_time.clear()
start_time.send_keys(start_time_str)

# Set end date and time
end_date = driver.find_element(By.XPATH, '//*[@id="id_end_time_0"]')
end_date.clear()
end_date.send_keys(end_date_str)

end_time = driver.find_element(By.XPATH, '//*[@id="id_end_time_1"]')
end_time.clear()
end_time.send_keys(end_time_str)



# title field
title = driver.find_element(By.NAME, 'title')
title.send_keys('Test')

subtitle = driver.find_element(By.NAME, 'subtitle')
subtitle.send_keys('Test')

list_subtitle = driver.find_element(By.NAME, 'list_subtitle')
list_subtitle.send_keys('Test')

# Internal title set
internal_title = driver.find_element(By.XPATH, '//*[@id="id_internal_title"]')
select = Select(internal_title)
select.select_by_visible_text("Test")



# check Top tournament
top_tournament = driver.find_element(By.XPATH, '//*[@id="id_is_feature_game"]')
if not top_tournament.is_selected():
    top_tournament.click()

assert top_tournament.is_selected(), "Checkbox is not selected"

# Tournament Type set
# Prize Customization

# Tournament trial configuration
tournament_trial = driver.find_element(By.XPATH, '//*[@id="id_tournament_trial_conf-0-trial"]')
tournament_trial.clear()
tournament_trial.send_keys('3')

# Trial package confs
package_confs = driver.find_element(By.XPATH, '//*[@id="id_tournament_trial_conf_package-0-currency"]')
select = Select(package_confs)
select.select_by_visible_text("Ticket")

currency_value = driver.find_element(By.XPATH, '//*[@id="id_tournament_trial_conf_package-0-currency_value"]')
currency_value.clear()
currency_value.send_keys('3')

trial_value = driver.find_element(By.XPATH, '//*[@id="id_tournament_trial_conf_package-0-trial_value"]')
trial_value.clear()
trial_value.send_keys('3')

# Click the Save button
save_button = driver.find_element(By.XPATH, '//*[@id="tournament_form"]/div/div[9]/input[1]')


save_button.click()

update = driver.find_element(By.XPATH, '//*[@id="myModal"]/div/div[2]/input[2]')
update.click()


time.sleep(10)