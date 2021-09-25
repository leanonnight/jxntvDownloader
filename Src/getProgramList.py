
# 获取 https://www.inapian.com/ 网的电视剧列表

# https://www.inapian.com/list/s-2-wd--letter--year-0-area--order-addtime-p-1.html
# https://www.inapian.com/list/s-2-wd--letter--year-0-area--order-addtime-p-2.html
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = None
programList = []

def getProgramList():
    with open("program电视剧列表.txt", "a+", encoding="utf-8") as f:
        for i in range(40, 415):
            try:
                driver.get("https://www.inapian.com/list/s-2-wd--letter--year-0-area--order-addtime-p-" + str(i) + ".html")
            except Exception:
                traceback.print_exc()
                driver.execute_script('window.stop()')
            # while True:
            #     try:
            divs = driver.find_elements_by_class_name("mpic")
            print("第" + str(i) + "页:")
            f.write("第" + str(i) + "页:" + "\n")
            for div in divs:
                a = div.find_element_by_tag_name("a")
                title = a.get_attribute("title")
                href = a.get_attribute("href")
                print(title, "-----", href)
                f.write(title + "-----" + href + "\n")



if __name__ == "__main__":
    # get直接返回，不再等待界面加载完成
    # desired_capabilities = DesiredCapabilities.CHROME
    # desired_capabilities["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(10)  # 10秒
    driver.set_script_timeout(10)
    time.sleep(2)
    getProgramList()