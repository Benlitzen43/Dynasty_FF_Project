# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup as bs
import pandas as pd

import time
import requests
import random

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import webbrowser

class yearly_rankings:
    def wr_gathering(self):
        year1 = "201"
        year2 = "202"
        final_list = []
        for x in range(5, 10):
            actualYear = year1 + str(x)
            website = "https://www.fantasypros.com/nfl/reports/leaders/ppr-wr.php?year=" + actualYear
            page = requests.get(website)
            soup = bs(page.content, "html.parser")
            soup.find_all(class_="player-name")
            quotes = [i.text for i in soup.find_all(class_="player-name")]
            for y in range (0, 24):
                final_list.append(quotes[y])

            #randomSleep = random.randint(1,10)
            #time.sleep(randomSleep)

        for x in range(0, 2):
            actualYear = year2 + str(x)
            website = "https://www.fantasypros.com/nfl/reports/leaders/ppr-wr.php?year=" + actualYear
            page = requests.get(website)
            soup = bs(page.content, "html.parser")
            soup.find_all(class_="player-name")
            quotes = [i.text for i in soup.find_all(class_="player-name")]
            for y in range(0, 24):
                final_list.append(quotes[y])

        return final_list

    def rb_gathering(self):
        year1 = "201"
        year2 = "202"
        final_list = []
        for x in range(5, 10):
            actualYear = year1 + str(x)
            website = "https://www.fantasypros.com/nfl/reports/leaders/ppr-rb.php?year=" + actualYear
            page = requests.get(website)
            soup = bs(page.content, "html.parser")
            soup.find_all(class_="player-name")
            quotes = [i.text for i in soup.find_all(class_="player-name")]
            if (x < 3):
                for y in range (0, 12):
                    final_list.append(quotes[y])
            else:
                for y in range (0, 24):
                    final_list.append(quotes[y])

            #randomSleep = random.randint(1,10)
            #time.sleep(randomSleep)

        for x in range(0, 2):
            actualYear = year2 + str(x)
            website = "https://www.fantasypros.com/nfl/reports/leaders/ppr-rb.php?year=" + actualYear
            page = requests.get(website)
            soup = bs(page.content, "html.parser")
            soup.find_all(class_="player-name")
            quotes = [i.text for i in soup.find_all(class_="player-name")]
            for y in range(0, 24):
                final_list.append(quotes[y])

        return final_list

    def te_gathering(self):
        year1 = "201"
        year2 = "202"
        final_list = []
        for x in range(5, 10):
            actualYear = year1 + str(x)
            website = "https://www.fantasypros.com/nfl/reports/leaders/ppr-te.php?year=" + actualYear
            page = requests.get(website)
            soup = bs(page.content, "html.parser")
            soup.find_all(class_="player-name")
            quotes = [i.text for i in soup.find_all(class_="player-name")]
            for y in range (0, 12):
                final_list.append(quotes[y])

            #randomSleep = random.randint(1,10)
            #time.sleep(randomSleep)

        for x in range(0, 2):
            actualYear = year2 + str(x)
            website = "https://www.fantasypros.com/nfl/reports/leaders/ppr-te.php?year=" + actualYear
            page = requests.get(website)
            soup = bs(page.content, "html.parser")
            soup.find_all(class_="player-name")
            quotes = [i.text for i in soup.find_all(class_="player-name")]
            for y in range(0, 12):
                final_list.append(quotes[y])

        return final_list


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
            for y in range (0, 12):
                final_list.append(quotes[y])

            #randomSleep = random.randint(1,10)
            #time.sleep(randomSleep)

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

class data_formatting():
    def __init__(self, wrList):
        #, rbList, teList, qbList):
        self.wrs = wrList
        #self.rbs = rbList
        #self.tes = teList
        #self.qbs = qbList
        self.length = len(self.wrs)
        self.smallLength = self.length/2

    def wrInformation(self):
        infoList = []
        #count = 0
        #value = "WR1"
        dictWR = {}
        for x in range (0, self.length):
            #count +=1
            currentPlayer = self.wrs[x]
            if currentPlayer not in dictWR:
                dictWR[currentPlayer] = 1
            else:
                currentValue = dictWR[currentPlayer]
                currentValue += 1
                dictWR[currentPlayer] = currentValue
            # if (count == 12):
            #     value = "WR2"
            # if (count == 24):
            #     count = 0
            #     value = "WR1"
        dictList = sorted(dictWR.items(), key=lambda y: y[1], reverse=True)
        finalDictWR = {}
        for x in range(0, len(dictList) - 1):
            finalDictWR[dictList[x][0]] = dictList[x][1]
        nameList, valueList = self.dict_unpacking(finalDictWR)
        return nameList, valueList

    def rbInformation(self):
        infoList = []
        #count = 0
        #value = "RB1"
        dictRB = {}
        for x in range (0, self.length):
            #count +=1
            currentPlayer = self.rbs[x]
            if currentPlayer not in dictRB:
                dictRB[currentPlayer] = 1
            else:
                currentValue = dictRB[currentPlayer]
                currentValue += 1
                dictRB[currentPlayer] = currentValue
            # if (count == 12):
            #     value = "RB2"
            # if (count == 24):
            #     count = 0
            #     value = "RB1"
        dictList = sorted(dictRB.items(), key=lambda y: y[1], reverse=True)
        finalDictRB = {}
        for x in range(0, len(dictList) - 1):
            finalDictRB[dictList[x][0]] = dictList[x][1]
        nameList, valueList = self.dict_unpacking(finalDictRB)
        return nameList, valueList

    def teInformation(self):
        infoList = []
        #count = 0
        #value = "TE1"
        dictTE = {}
        for x in range (0, int(self.smallLength)):
            #count +=1
            currentPlayer = self.tes[x]
            if currentPlayer not in dictTE:
                dictTE[currentPlayer] = 1
            else:
                currentValue = dictTE[currentPlayer]
                currentValue += 1
                dictTE[currentPlayer] = currentValue
            # if (count == 12):
            #     value = "TE2"
            # if (count == 24):
            #     count = 0
            #     value = "TE1"
        dictList = sorted(dictTE.items(), key=lambda y: y[1], reverse=True)
        finalDictTE = {}
        for x in range(0, len(dictList) - 1):
            finalDictTE[dictList[x][0]] = dictList[x][1]
        nameList, valueList = self.dict_unpacking(finalDictTE)
        return nameList, valueList

    def qbInformation(self):
        infoList = []
        #count = 0
        #value = "QB1"
        dictQB = {}
        for x in range (0, int(self.smallLength)):
            #count +=1
            currentPlayer = self.qbs[x]
            if currentPlayer not in dictQB:
                dictQB[currentPlayer] = 1
            else:
                currentValue = dictQB[currentPlayer]
                currentValue += 1
                dictQB[currentPlayer] = currentValue
            # if (count == 12):
            #     value = "QB2"
            # if (count == 24):
            #     count = 0
            #     value = "QB1"
        dictList = sorted(dictQB.items(), key=lambda y: y[1], reverse=True)
        finalDictQB = {}
        for x in range (0, len(dictList) - 1):
            finalDictQB[dictList[x][0]] = dictList[x][1]
        nameList, valueList = self.dict_unpacking(finalDictQB)
        return nameList, valueList

    def dict_unpacking(self, dictPos):
        keyList = []
        valueList = []
        for key, value in dictPos.items():
            keyList.append(key)
            valueList.append(value)
        return keyList, valueList

def fix_names(nameList):
    length = len(nameList)
    fixedNames = []

    for x in range (0, length):
        currentName = nameList[x]
        splitName = currentName.split(' ')
        fixedName = "-".join(splitName)
        fixedNames.append(fixedName)
    return fixedNames

class football_db():
    def __init__(self):
        self.row0 = "row0 right row_playerstats row_college"
        self.row1 = "row1 right row_playerstats row_college"
        self.finalStats = []
        self.years = []
        self.ypaList = []

    def web_gathering_prospects(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        website = "https://www.footballdb.com/college-football/teams/fbs/arkansas/roster"
        page = requests.get(website, headers=headers)
        soup = bs(page.content, "html.parser")
        test = "Burks, Treylon"
        soupCat = soup.find_all("a")
        for x in range(0, len(soupCat)):
            meow = str(soupCat[x].get_text(strip=True))
            if test == meow:
                soupList = soupCat[x]
        #soupCat = soup.get_text(strip=True)
        cat = str(soupList)
        cats = cat.split(" ")
        beep = cats[1].replace('"',"")
        beep = beep.replace('href=', "")
        print(beep)
    def web_gathering_nfl(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        website = "https://www.footballdb.com/players/davante-adams-adamsda04?src=search"
        page = requests.get(website, headers = headers)
        soup = bs(page.content, "html.parser")


        count0 = 0
        count1 = 0
        self.collegeStats = soup.find(class_="divToggle_C_reg")
        self.quotes0 = self.collegeStats.find_all('tr', attrs={'class': self.row0})
        self.quotes1 = self.collegeStats.find_all('tr', attrs={'class': self.row1})
        self.fullStats = self.collegeStats.find(class_="header right row_playerstats row_college")

        row_college = self.fullStats.find_all('td')

        self.startYear = self.quotes0[0].find(class_="center")
        self.startYear = str(self.startYear).replace('<td class="center">',"")
        self.startYear = self.startYear.replace('</td>',"")
        self.startYear = int(self.startYear)

        self.college = self.quotes0[0].find('a')
        self.collegeTemp = str(self.college).split(' ')
        self.college = self.collegeTemp[1]
        self.college = self.college.replace('href="',"")
        self.college = self.college.replace('"',"")
        self.collegeList = self.college.split('/')


        while True:
            try:
                if count0 == count1:
                    incorrect = self.filter_out_incorrect_entries(count0)
                    if (len(incorrect ) < 2):
                        break
                    row0_stats = self.quotes0[count0].find_all('td')
                    self.player_data_formation(row0_stats)
                    self.years.append(self.startYear + count0 + count1)
                    count0 += 1
                else:
                    row1_stats = self.quotes1[count1].find_all('td')
                    self.player_data_formation(row1_stats)
                    self.years.append(self.startYear + count0 + count1)
                    count1 += 1
                self.finalStats.append(self.stats_formatted)
            except IndexError:
                break

        self.player_data_formation(row_college)
        self.finalStats.append(self.stats_formatted)

    def filter_out_incorrect_entries(self, count0):
        find_incorrect = self.quotes0[count0].find(class_="center")
        tempString = str(find_incorrect).replace('<td class="center">', "")
        tempString = tempString.replace("</td>", "")
        return tempString

    def player_data_formation(self, stats):
        self.stats = stats
        for x in range(0, 5):
            self.stats.pop(0)
        del self.stats[6:]
        self.stats.pop(4)
        self.stats_formatted = []
        count = 0
        for x in range(0, len(self.stats)):
            tempString = str(self.stats[x]).replace("<td>","")
            tempString = tempString.replace("</td>", "")
            tempString = tempString.replace(",", "")
            if(count < 2 or count == 4):
                tempString = int(tempString)
            else:
                tempString = float(tempString)
            self.stats_formatted.append(tempString)
            count += 1

    def team_pass_attempts_driver(self):
        tempString = ""
        for x in range(1, len(self.collegeList)-1):
            tempString += "/" + self.collegeList[x]
        for x in self.years:
            finalString = "https://www.footballdb.com" + tempString + "/" + str(x)
            self.team_pass_attempts(finalString)


    def team_pass_attempts(self, website):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

        page = requests.get(website, headers=headers)
        soup = bs(page.content, "html.parser")
        self.offense = soup.find(class_="divToggle_offense")
        refined_offense = self.offense.find_all(class_="header right")
        self.ypa = refined_offense[1].find_all('td')
        tempString = self.ypa[5]
        tempString = str(tempString).replace("<td>","")
        tempString = tempString.replace("</td>", "")
        self.ypa = tempString
        self.ypaList.append(self.ypa)

def data_gathering(playerList):
    totalList = []
    for x in range(0, len(playerList)):
        pd.set_option('display.max_colwidth', 500)
        requestPage = "https://www.playerprofiler.com/nfl/" + playerList[x] + "/"
        page = requests.get(requestPage)
        soup = bs(page.content, "html.parser")
        soup.find_all(class_='leading-none')
        quotes = [i.text for i in soup.find_all(class_='leading-none')]
        importantList = []
        count = 0
        noCount = False
        for x in quotes:
            if (noCount == True):
                importantList.append(x)
                count += 1
                if (count == 11):
                    noCount = False
            if (x == 'College Dominator'):
                importantList.append(x)
                noCount = True
        totalList.append(importantList)
    return totalList

def draft_class_gathering_driver_code():
    years = []
    finishedWRs= []
    finishedCollege = []
    finishedLinks = []
    finishedDraftCapital = []

    finalWRsByYear = []
    finalLinksByYear = []
    finalCollegeByYear = []
    finalDraftCapitalByYear = []

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    for x in range (2012, 2022):
        years.append(x)

    for x in range(0, len(years)):
        finalWRs = []
        finalLinks = []
        finalCollege = []
        finalDraftCapital = []
        for y in range(1, 8):
            pd.set_option('display.max_colwidth', 500)
            requestPage = "https://www.footballdb.com/draft/draft.html?lg=NFL&yr=" + str(years[x]) + "&rnd=" + str(y)
            page = requests.get(requestPage, headers=headers)
            soup = bs(page.content, "html.parser")
            WRs, draftCapital, links, college = draft_class_gathering(soup)
            finalWRs.append(WRs)
            finalDraftCapital.append(draftCapital)
            finalLinks.append(links)
            finalCollege.append(college)
        finalWRsByYear = []
        finalDraftCapitalByYear = []
        finalLinksByYear = []
        finalCollegeByYear = []
        for x in range(0, len(finalWRs)):
            for y in range(0, len(finalWRs[x])):
                finalWRsByYear.append(finalWRs[x][y])
                finalDraftCapitalByYear.append(finalDraftCapital[x][y])
                finalLinksByYear.append(finalLinks[x][y])
                finalCollegeByYear.append(finalCollege[x][y])
        finishedWRs.append(finalWRsByYear)
        finishedDraftCapital.append(finalDraftCapitalByYear)
        finishedLinks.append(finalLinksByYear)
        finishedCollege.append(finalCollegeByYear)


    return finishedWRs, finishedDraftCapital, finishedLinks, finishedCollege

def draft_class_gathering(soup):
    allPicks = soup.find_all(class_="tr")
    WRs = []
    draftCapital = []
    links = []
    college = []
    filter = []
    for x in range(0, len(allPicks)-1):
        filter = allPicks[x].find(class_="td w10 td-clear hidden-xs")
        if x > 6:
            position = str(filter.get_text(strip=True))
            if position == "WR":
                names = allPicks[x].find(class_="td w20 td-clear hidden-xs")
                name = names.find("a").get_text(strip=True)
                WRs.append(name)

                link = str(names.find("a"))
                temp = link.replace('<a href="','')
                temp = temp.replace(name, "")
                temp = temp.replace('"></a>',"")
                links.append(temp)

                colleges = allPicks[x].find(class_="td w25 hidden-xs")
                collegeName = colleges.find("a").get_text(strip=True)
                tempList = collegeName.split(" ")
                tempString = "-".join(tempList)
                college.append(tempString)

                pick = allPicks[x].find(class_="td w10 m15").get_text(strip = True)
                draftCapital.append(pick)

    return WRs, draftCapital, links, college


if __name__ == '__main__':


    WRs, draftCapital, links, college = draft_class_gathering_driver_code()


    dataManager = yearly_rankings()
    wrList = dataManager.wr_gathering()
    # rbList = dataManager.rb_gathering()
    # teList = dataManager.te_gathering()
    # qbList = dataManager.qb_gathering()
    # #data_gathering()
    dataFormatter = data_formatting(wrList)
                                    #, rbList, teList, qbList)
    nameListWR, valueListWR = dataFormatter.wrInformation()
    # nameListRB, valueListRB = dataFormatter.rbInformation()
    # nameListTE, valueListTE = dataFormatter.teInformation()
    # nameListQB, valueListQB = dataFormatter.qbInformation()
    #
    dashedNameListWR = fix_names(nameListWR)
    # dashedNameListRB = fix_names(nameListRB)
    # dashedNameListTE = fix_names(nameListTE)
    # dashedNameListQB = fix_names(nameListQB)
    #now we want to take these lists and output them to the csvs
    #after this we will need to the csvs
    playerProfilerWRdata =  data_gathering(dashedNameListWR)
    print(playerProfilerWRdata)
    footballDatabase = football_db()
    footballDatabase.web_gathering_nfl()
    footballDatabase.team_pass_attempts_driver()
    footballDatabase.web_gathering_prospects()



    #things needed to do

    #edit the draft class one to grab from football database instead

    #will need to know what year they were drafted in, then go back one year to the that team's college page (roster and name of college)
    #will then need to be able to recognize the player name and go onto to the page, once this is done we can gather all of the info
    #once we have all of this data we SHOULD be able to output it to a csv and then analyze it, the end is near :)))))))


