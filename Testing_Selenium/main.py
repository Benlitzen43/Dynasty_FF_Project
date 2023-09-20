# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

def test_driver():
    driver = webdriver.Chrome()
    driver.get('https://www.pff.com/news/draft-2024-nfl-draft-board-big-board')
    players = driver.find_elements(By.XPATH, '//strong')
    players_list = []
    for p in range(len(players)):
        players_list.append(players[p].text)

    #filter_list_string = ["QB", "RB", "WR", "TE", "T", "G", "C", "EDGE", "CB", "DT", "DL", "LB", "S"]
    filter_list_comma = ","
    new_players_list = []

    for player in players_list:
        if filter_list_comma in player:
            new_players_list.append(player)

    ranking_list  = []
    position_list = []
    name_list     = []
    college_list  = []
    name = ""

    for strings in new_players_list:

        # Building the lists

        comma_split = strings.split(',')

        current_string_prior = comma_split[0]
        current_string = current_string_prior.split()

        ranking_list.append(current_string[0])
        position_list.append(current_string[1])
        college_list.append(comma_split[1])

        # all other values need to be removed so we can have the name as the remaining thing
        current_string.pop(0)
        current_string.pop(0)
        # Now we make the name
        current_string.pop(0)
        for x in range (0, len(current_string)):
            if (x == len(current_string) - 1):
                name += current_string[x]
            else:
                name += current_string[x] + " "
        name_list.append(name)
        name = ""

        # Cats are good


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_driver()
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
