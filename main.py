import class101
import SeleniumOperation
from datetime import datetime


urlCollection = {'oriental': "https://class101.net/search?category=604f1c9756c3676f1ed0030c&page=1&sort=likedOrder",
                 'digitalDrawing': "https://class101.net/search?category=604f1c9756c3676f1ed0030e&page=1&sort=likedOrder",
                 'calligraphy': 'https://class101.net/search?category=604f1c9756c3676f1ed00312&page=1&sort=likedOrder',
                 'miscDrawing': "https://class101.net/search?category=604f1c9756c3676f1ed0030d&page=1&sort=likedOrder"}

driver = SeleniumOperation.getHeadlessDriver()
driver.implicitly_wait(5)

for classtopic, url in urlCollection.items():

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    class101.scrapeAllPages(
        driver, url, classtopic, "/Users/CheHoon/Desktop/experimentData")

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)


driver.quit()
