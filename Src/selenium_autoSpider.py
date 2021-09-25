from selenium import webdriver

import time
import Util.CommonUtil as util


# 获取节目列表，包含节目名称和节目网址


dushixianchangList = []
def getDushixianchang():
    driver = webdriver.Chrome()
    driver.get('http://v.jxntv.cn/?ch=91&ca=92')
    time.sleep(2)

    startTime = time.time()
    btn_nextpage = driver.find_element_by_class_name("btn-nextpage")
    for i in range(0, 20):
        try:
            btn_nextpage.click()
            while True:
                time.sleep(0.1)
                btn_style = btn_nextpage.get_attribute("style")
                if not "display: none;" == btn_style:
                    break
        except Exception:
            pass

    # time.sleep(1000)
    # b.quit()

    endTime = time.time()
    print("点击更新共耗时:" + util.time_to_str(endTime - startTime))

    news_items = driver.find_elements_by_class_name("news-item")

    startTime = time.time()
    for news_item in news_items:
        a = news_item.find_element_by_class_name("title").find_element_by_tag_name("a")
        dushixianchangList.append('title=%s,href=%s' % (a.text, a.get_attribute("href")))

    endTime = time.time()

    print("获取新闻项耗时:" + util.time_to_str(endTime - startTime))
    for dushixianchang in dushixianchangList:
        print(dushixianchang)

    with open("都市现场.txt", "w", encoding="utf-8") as f:
        body = ""
        for dushixianchang in dushixianchangList:
            body = body + dushixianchang + "\n"
        f.write(body)


def getDushixianchangwujianban():
    driver = webdriver.Chrome()
    driver.get('http://v.jxntv.cn/?ch=91&ca=107')
    time.sleep(2)

    startTime = time.time()
    btn_nextpage = driver.find_element_by_class_name("btn-nextpage")
    for i in range(0, 20):
        try:
            btn_nextpage.click()
            while True:
                time.sleep(0.1)
                btn_style = btn_nextpage.get_attribute("style")
                if not "display: none;" == btn_style:
                    break
        except Exception:
            pass

    # time.sleep(1000)
    # b.quit()

    endTime = time.time()
    print("点击更新共耗时:" + util.time_to_str(endTime - startTime))

    news_items = driver.find_elements_by_class_name("news-item")

    startTime = time.time()
    for news_item in news_items:
        a = news_item.find_element_by_class_name("title").find_element_by_tag_name("a")
        dushixianchangList.append('title=%s,href=%s' % (a.text, a.get_attribute("href")))

    endTime = time.time()

    print("获取新闻项耗时:" + util.time_to_str(endTime - startTime))
    for dushixianchang in dushixianchangList:
        print(dushixianchang)

    with open("都市现场午间版.txt", "w", encoding="utf-8") as f:
        body = ""
        for dushixianchang in dushixianchangList:
            body = body + dushixianchang + "\n"
        f.write(body)

def getDibaodangjia():
    driver = webdriver.Chrome()
    driver.get('http://v.jxntv.cn/?ch=91&ca=108')
    time.sleep(2)

    startTime = time.time()
    btn_nextpage = driver.find_element_by_class_name("btn-nextpage")
    for i in range(0, 10):
        try:
            btn_nextpage.click()
            while True:
                time.sleep(0.1)
                btn_style = btn_nextpage.get_attribute("style")
                if not "display: none;" == btn_style:
                    break
        except Exception:
            pass

    # time.sleep(1000)
    # b.quit()

    endTime = time.time()
    print("点击更新共耗时:" + util.time_to_str(endTime - startTime))

    news_items = driver.find_elements_by_class_name("news-item")

    startTime = time.time()
    for news_item in news_items:
        a = news_item.find_element_by_class_name("title").find_element_by_tag_name("a")
        dushixianchangList.append('title=%s,href=%s' % (a.text, a.get_attribute("href")))

    endTime = time.time()

    print("获取新闻项耗时:" + util.time_to_str(endTime - startTime))
    for dushixianchang in dushixianchangList:
        print(dushixianchang)

    with open("地宝当家.txt", "w", encoding="utf-8") as f:
        body = ""
        for dushixianchang in dushixianchangList:
            body = body + dushixianchang + "\n"
        f.write(body)

def getDushiqingyuan():
    driver = webdriver.Chrome()
    driver.get('http://v.jxntv.cn/?ch=91&ca=109')
    time.sleep(2)

    startTime = time.time()
    btn_nextpage = driver.find_element_by_class_name("btn-nextpage")
    for i in range(0, 10):
        try:
            btn_nextpage.click()
            while True:
                time.sleep(0.1)
                btn_style = btn_nextpage.get_attribute("style")
                if not "display: none;" == btn_style:
                    break
        except Exception:
            pass

    # time.sleep(1000)
    # b.quit()

    endTime = time.time()
    print("点击更新共耗时:" + util.time_to_str(endTime - startTime))

    news_items = driver.find_elements_by_class_name("news-item")

    startTime = time.time()
    for news_item in news_items:
        a = news_item.find_element_by_class_name("title").find_element_by_tag_name("a")
        dushixianchangList.append('title=%s,href=%s' % (a.text, a.get_attribute("href")))

    endTime = time.time()

    print("获取新闻项耗时:" + util.time_to_str(endTime - startTime))
    for dushixianchang in dushixianchangList:
        print(dushixianchang)

    with open("都市情缘.txt", "w", encoding="utf-8") as f:
        body = ""
        for dushixianchang in dushixianchangList:
            body = body + dushixianchang + "\n"
        f.write(body)



if __name__ == '__main__':
    getDushiqingyuan()