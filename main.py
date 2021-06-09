import class101
import SeleniumOperation
from datetime import datetime


urlCollection = {'실공예': 'https://class101.net/search?category=604f1c9756c3676f1ed00318&page=1&sort=likedOrder',
                 '코바늘뜨개': 'https://class101.net/search?category=604f1c9756c3676f1ed00326&page=1&sort=likedOrder',
                 '패브릭공예': 'https://class101.net/search?category=604f1c9756c3676f1ed0032c&page=1&sort=likedOrder',
                 '종이공예': 'https://class101.net/search?category=604f1c9756c3676f1ed00337&page=1&sort=likedOrder',
                 '나무공예': 'https://class101.net/search?category=604f1c9756c3676f1ed0033b&page=1&sort=likedOrder',
                 '가죽공예': 'https://class101.net/search?category=604f1c9756c3676f1ed0033c&page=1&sort=likedOrder',
                 '라탄공예': 'https://class101.net/search?category=604f1c9756c3676f1ed0033d&page=1&sort=likedOrder',
                 '레진공예': 'https://class101.net/search?category=604f1c9756c3676f1ed0033e&page=1&sort=likedOrder',
                 '금속공예': 'https://class101.net/search?category=604f1c9756c3676f1ed0033f&page=1&sort=likedOrder',
                 '포장공예': 'https://class101.net/search?category=604f1c9756c3676f1ed00340&page=1&sort=likedOrder',
                 '도예': 'https://class101.net/search?category=604f1c9756c3676f1ed00341&page=1&sort=likedOrder',
                 '향': 'https://class101.net/search?category=604f1c9756c3676f1ed00342&page=1&sort=likedOrder',
                 '플라워': 'https://class101.net/search?category=604f1c9756c3676f1ed00346&page=1&sort=likedOrder',
                 '펠트아트': 'https://class101.net/search?category=604f1c9756c3676f1ed0034b&page=1&sort=likedOrder',
                 '클레이아트': 'https://class101.net/search?category=604f1c9756c3676f1ed0034c&page=1&sort=likedOrder',
                 '미니어처': 'https://class101.net/search?category=604f1c9756c3676f1ed0034d&page=1&sort=likedOrder',
                 '더새로운공예': 'https://class101.net/search?category=604f1c9756c3676f1ed0034e&page=1&sort=likedOrder'}

driver = SeleniumOperation.getHeadlessDriver()
driver.implicitly_wait(5)

for classtopic, url in urlCollection.items():

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    class101.scrapeAllPages(
        driver, url, classtopic, "/Users/CheHoon/Desktop/class101Data")

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)


driver.quit()
