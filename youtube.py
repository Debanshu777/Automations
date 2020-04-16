from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.youtube.com")



search=driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/div/div[1]/input')
search.send_keys("make you mine")
url=driver.current_url
button=driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/button')
button.click()
time.sleep(3)
song_time=driver.find_element_by_class_name("style-scope ytd-thumbnail-overlay-time-status-renderer").text
minute=int(song_time[0])*60+int(song_time[2:3])*10+int(song_time[3])
print(minute)
click2=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]')
click2.click()

while True:
    time.sleep(minute)
    driver.refresh()
