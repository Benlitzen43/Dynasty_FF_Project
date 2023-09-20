# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup as bs
import pandas as pd

import time
import requests
import random

def data_gathering():

    pd.set_option('display.max_colwidth', 500)
    page = requests.get("https://www.playerprofiler.com/nfl/treylon-burks/")
    soup = bs(page.content, "html.parser")
    soup.find_all(class_ = 'leading-none')
    quotes = [i.text for i in soup.find_all(class_ = 'leading-none')]
    importantList = []
    count = 0
    noCount = False
    for x in quotes:
        if(noCount == True):
            importantList.append(x)
            count += 1
            if (count == 11):
                noCount = False
        if(x == 'College Dominator'):
            importantList.append(x)
            noCount = True



def wr_gathering():
    year1 = "201"
    year2 = "202"

    for x in range (2, 3):
        actualYear = year1 + str(x)
        website = "https://www.fantasypros.com/nfl/reports/leaders/ppr-wr.php?year=" + actualYear
        page = requests.get(website)
        soup = bs(page.content, "html.parser")
        soup.find_all('tr')
        quotes = [i.text for i in soup.find_all('tr')]
        # <tr><td class="center">1</td><td class="player-label player-9857"><a class="player-name" href="/nfl/players/aj-green.php">
        # A.J. Green</a></td><td class="center">
        # <a href="/nfl/teams/cincinnati-bengals.php">CIN</a></td><td class="center">299.8</td><td class="center">16</td><td class="center">18.7</td></tr>
        print(quotes)
    for x in range(0, 2):
        print("meow")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    wr_gathering()
    data_gathering()


