from bs4 import BeautifulSoup as bs
import pandas as pd

import time
import requests
import random
import re
from unicodedata import numeric


def qb_gathering(self):
    year1 = "201"
    year2 = "202"
    final_list = []
    for x in range(5, 10):
        actualYear = year1 + str(x)
        website = "https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=" + actualYear
        page = requests.get(website)
        soup = bs(page.content, "html.parser")
        soup.find_all(class_="player-name")
        quotes = [i.text for i in soup.find_all(class_="player-name")]
        for y in range(0, 12):
            final_list.append(quotes[y])

        # randomSleep = random.randint(1,10)
        # time.sleep(randomSleep)

    for x in range(0, 2):
        actualYear = year2 + str(x)
        website = "https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=" + actualYear
        page = requests.get(website)
        soup = bs(page.content, "html.parser")
        soup.find_all(class_="player-name")
        quotes = [i.text for i in soup.find_all(class_="player-name")]
        for y in range(0, 12):
            final_list.append(quotes[y])

    return final_list

def wr_combine_stats():
    website = "https://ras.football/denzel-mims-ras/"
    #can just put the name into the ras website, may have to account for duplciates
    page = requests.get(website)
    soup = bs(page.content, "html.parser")
    ras_text = soup.get_text(strip=True)
    ras_list = ras_text.split()

    weight_counter = 0
    height_counter = 0
    dash_counter = 0
    speed_counter = 0
    cone_counter = 0
    broad_counter = 0
    vert_counter = 0
    arm_counter = 0
    hand_counter = 0

    text_counterw = 0
    text_counterh = 0
    text_counterd = 0
    text_counterc = 0
    text_counterb = 0
    text_counterv = 0
    text_counters = 0
    text_countera = 0
    text_counterha = 0

    weight = 0
    height = 0
    arm = 0
    dash = 0
    vert = 0
    broad = 0
    hand = 0
    cone = 0


    for x in range(0, len(ras_list)):
        if ras_list[x] == "weight":
            weight_counter = ras_list[x + 2]
            if weight_counter != 0 and text_counterw == 0:
                text_counterw = 1
                weight = weight_counter
        if ras_list[x] == "height":
            height_counter = ras_list[x + 2]
            if height_counter != 0 and text_counterh == 0:
                text_counterh = 1
                height = height_counter
        if ras_list[x] == "dash":
            dash_counter = ras_list[x + 2]
            text_counterd += 1
            if dash_counter != 0 and text_counterd == 2:
                text_counterd = 3
                dash = dash_counter
        if ras_list[x] == "cone":
            cone_counter = ras_list[x + 4]
            if cone_counter != 0 and text_counterc == 0:
                text_counterc = 1
                cone = cone_counter

        if ras_list[x] == "broad":
            broad_counter = ras_list[x + 3]
            if broad_counter != 0 and text_counterb == 0:
                text_counterb = 1
                broad = broad_counter

                inches = broad[:-2]
                feet =  broad[0:-2]
                broad = int(feet)*12 + int(inches)

        if ras_list[x] == "vertical":
            vert_counter = ras_list[x + 3]
            if vert_counter != 0 and text_counterv == 0:
                text_counterv = 1
                vert = vert_counter

    total_combine_stats = [dash, cone, broad, vert]
    website = "https://www.mockdraftable.com/player/denzel-mims"
    # can just put the name into the ras website, may have to account for duplciates
    page = requests.get(website)
    soup = bs(page.content, "lxml")
    stats = soup.find_all('td')

    ah_list = []
    for x in range (0, len(stats)):
        current = stats[x]
        current = current.get_text(strip=True)
        if (current == "Arm Length"):
            temp = stats[x+1].get_text(strip=True)
            temp = temp.replace('"' , '')
            temp1 = temp[:-1]
            temp2 = temp[-1]
            fraction = numeric(temp2)
            total = int(temp1) + float (fraction)
            ah_list.append(total)
        if (current == "Hand Size"):
            temp = stats[x + 1].get_text(strip=True)
            temp = temp.replace('"', '')
            temp1 = temp[:-1]
            temp2 = temp[-1]
            fraction = numeric(temp2)
            total = int(temp1) + float(fraction)
            ah_list.append(total)

    total_combine_stats.append(ah_list[0])
    total_combine_stats.append(ah_list[1])
    height_int = int(height[0])*12 + int(height[1:2]) + int(height[3:4])/8
    weight = int(weight)
    bmi = weight/float(height_int)/float(height_int)*703
    bmi = "%.1f" % bmi
    total_combine_stats.append(bmi)

    print(total_combine_stats)
    return total_combine_stats

def wr_combine_grouping(stats):
    dash_score = 0
    cone_score = 0
    launch_score = 0
    hand_score = 0
    arm_score = 0
    bmi_score = 0

    count = 0

    # [dash, cone, broad, vert], arm, hand, bmi
    for x in range(0, len(stats)):
        temp = float(stats[x])
        if x == 0:
            if temp < 4.36:
                dash_score = 1.71
            elif temp < 4.49:
                dash_score = 1.08
            elif temp < 4.58:
                dash_score = 1.00
            elif temp < 4.73:
                dash_score = .95
            else:
                dash_score = .72
        if x == 1:
            if temp < 6.83:
                cone_score = 1.16
            else:
                cone_score = 1
        # if x == 2:
        #     if stats[x] < 4.36:
        #         dash_score = 1.71
        #     elif stats[x] < 4.49:
        #         dash_score = 1.08
        #     elif stats[x] < 4.58:
        #         dash_score = 1.00
        #     elif stats[x] < 4.73:
        #         dash_score = .95
        #     else:
        #         dash_score = .72
        #
        # if x == 3:
        #     if stats[x] < 4.36:
        #         dash_score = 1.71
        #     elif stats[x] < 4.49:
        #         dash_score = 1.08
        #     elif stats[x] < 4.58:
        #         dash_score = 1.00
        #     elif stats[x] < 4.73:
        #         dash_score = .95
        #     else:
        #         dash_score = .72

        if x == 5:
            if temp > 9.74:
                hand_score = 1.36
            elif temp > 9.49:
                hand_score = 1.10
            else:
                hand_score = 1.00

        if x == 4:
            if temp > 33.7:
                arm_score = 1.68
            elif temp > 30:
                arm_score = 1.29
            else:
                arm_score = 1.00

        if x == 6:
            if temp > 27.5:
                bmi_score = 1.20
            elif temp > 26.2:
                bmi_score = 1.10
            else:
                bmi_score = 1.00
    launch_score = 1.31
    total_groupings = [dash_score, cone_score, launch_score, arm_score, hand_score, bmi_score]
    return total_groupings
def wr_combine_score(score_list):
    total_score =  .16*score_list[0] + .19 * score_list[1] + .05 * score_list [2] + .23 * score_list[3] + .15 * score_list[4] + .22 * score_list[5]
    print(total_score)

if __name__ == '__main__':
    wr_combine = wr_combine_stats()
    score_list = wr_combine_grouping(wr_combine)
    wr_combine_score(score_list)
