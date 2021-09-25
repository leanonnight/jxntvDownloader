import re
import time
import traceback
from Src.download import downloader

from selenium import webdriver
from Util.RequestUtil import RequestUtil as request
from bs4 import BeautifulSoup

driver = None

def getProgramUrlList(fileName):
    programUrlList = []
    reProgramUrl = re.compile(r'title=(.*),href=(.*)$')
    with open(fileName, "r", encoding="utf-8") as f:
        try:
            while f.readable():
                programUrlLine = f.readline()
                programName = reProgramUrl.match(programUrlLine).group(1)
                programUrl = reProgramUrl.match(programUrlLine).group(2)
                programUrlList.append({"name": programName, "url": programUrl})
        except Exception:
            print("***************************")

        return programUrlList

def getMP4Url(url):
    driver.get(url)
    while True:
        try:
            iframe = driver.find_element_by_tag_name("iframe")
            src = iframe.get_attribute("src")

            driver.get(src)
            while True:
                try:
                    video = driver.find_element_by_tag_name("video")
                    src = video.get_attribute("src")
                    return src
                except Exception:
                    # traceback.print_exc()
                    pass
                time.sleep(0.1)

            break
        except Exception:
            # traceback.print_exc()
            pass
        time.sleep(0.1)


def downloadMP4(programUrlList):
    for programUrlLine in programUrlList:
        programName = programUrlLine["name"]
        programUrl = programUrlLine["url"]

        url = getMP4Url(programUrl)
        print("开始下载" + programName + " 网址: " + url)

        try:
            downloader(url, 64, programName).start()
        except Exception:
            traceback.print_exc()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    downloadMP4(getProgramUrlList("都市现场午间版.txt"))

