# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

def test_driver():
    driver = webdriver.Chrome()
    driver.get('https://www.pff.com/news/draft-2023-nfl-draft-board-big-board')
    players = driver.find_elements(By.XPATH, '//strong')
    print(players[0])
    players_list = []
    for p in range(len(players)):
        players_list.append(players[p].text)
    print(players_list)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_driver()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
