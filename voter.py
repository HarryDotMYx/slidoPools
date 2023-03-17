# Created By HarryX
import time
import sys
import argparse
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.options import Options

class SlidoBot:
    def __init__(self, hash=None, xpath=None, driver=None):
        if not all([hash, xpath, driver]):
            raise ValueError("Invalid argument")
        self.hash = hash
        self.xpath = xpath
        self.driver = driver.lower()
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        if "chrome" in self.driver:
            self.driver = Chrome(options=chrome_options)
        elif "firefox" in self.driver:
            self.driver = Firefox(executable_path=self.driver)
        else:
            raise ValueError("Invalid driver")
    
    def close_browser(self):
        self.driver.quit()

    def vote(self):
        self.driver.get(f"https://app.sli.do/event/{self.hash}/embed/polls/5566a1a3-cdf3-4d21-8350-f6b7ec7e3907")
        time.sleep(1)
        click_elem = self.driver.find_element_by_xpath(f"//span[text()='{self.xpath}']")
        click_elem.click()
        btn_elem = self.driver.find_element_by_xpath("//button")
        btn_elem.click()

def main():
    parser = argparse.ArgumentParser(description="Slido voting bot")
    parser.add_argument("-hash", help="Event hash", required=True)
    parser.add_argument("-xpath", help="Option to vote for", required=True)
    parser.add_argument("-driver", help="Browser driver", required=True)
    parser.add_argument("-votes", help="Number of votes to cast", required=True, type=int)
    args = parser.parse_args()

    for i in range(1, args.votes + 1):
        bot = SlidoBot(args.hash, args.xpath, args.driver)
        bot.vote()
        bot.close_browser()
        print(f"Votes: {i}")

if __name__ == "__main__":
    print("Voting...")
    main()
