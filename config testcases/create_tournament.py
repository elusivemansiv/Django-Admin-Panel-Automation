from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.get("https://admin.staging.go-games.gg/admin/login/?next=/admin/")

time.sleep(5)

# login django admin panel
uname = driver.find_element(By.NAME, 'username')
uname.send_keys('gg-mansib')

password = driver.find_element(By.NAME, 'password')
password.send_keys('goama12345')

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
tournament_name.send_keys('Automated tournament_02')

# Application set
application = driver.find_element(By.NAME, 'application')
application.send_keys('gotest')

# country code field
country = driver.find_element(By.NAME, 'country')
country.send_keys('BD')

# Game Set
game = driver.find_element(By.XPATH, '//*[@id="id_game"]')
select = Select(game)
select.select_by_visible_text("Boat Rush")

# Set Game start and end time
start_date = driver.find_element(By.XPATH, '//*[@id="id_start_time_0"]')
start_date.send_keys("2024-06-09")

start_time = driver.find_element(By.XPATH, '//*[@id="id_start_time_1"]')
start_time.send_keys('14:53:37')

end_date = driver.find_element(By.XPATH, '//*[@id="id_end_time_0"]')
end_date.send_keys("2024-06-25")

end_time = driver.find_element(By.XPATH, '//*[@id="id_end_time_1"]')
end_time.send_keys('14:53:37')

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



save_button = driver.find_element(By.XPATH, '//*[@id="tournament_form"]/div/div[9]/input[1]')

# Click the Save button
save_button.click()

update = driver.find_element(By.XPATH, '//*[@id="myModal"]/div/div[2]/input[2]')
update.click()


time.sleep(10)