import class101
import SeleniumOperation
from datetime import datetime


urlCollection = {}

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


'''
COLLECTION OF MAIN URLS OF CATEGORIES

    '양식': 'https://class101.net/search?category=604f1c9756c3676f1ed00351&page=1&sort=likedOrder',
    '중식': 'https://class101.net/search?category=604f1c9756c3676f1ed00352&page=1&sort=likedOrder',
    '일식': 'https://class101.net/search?category=604f1c9756c3676f1ed00353&page=1&sort=likedOrder',
    '건강식': 'https://class101.net/search?category=604f1c9756c3676f1ed00356&page=1&sort=likedOrder',
    '음료술': 'https://class101.net/search?category=604f1c9756c3676f1ed0035a&page=1&sort=likedOrder',
    '더새로운요리': 'https://class101.net/search?category=604f1c9756c3676f1ed00355&page=1&sort=likedOrder',
    '베이킹디저트': 'https://class101.net/search?category=604f1c9756c3676f1ed0035e&page=1&sort=likedOrder',
    '악기': 'https://class101.net/search?category=604f1c9756c3676f1ed00366&page=1&sort=likedOrder',
    '보컬랩': 'https://class101.net/search?category=604f1c9756c3676f1ed00371&page=1&sort=likedOrder',
    '작곡프로듀싱': 'https://class101.net/search?category=604f1c9756c3676f1ed00372&page=1&sort=likedOrder',
    '운동': 'https://class101.net/search?category=604f1c9756c3676f1ed00373&page=1&sort=likedOrder',
    '뷰티': 'https://class101.net/search?category=604f1c9756c3676f1ed0037f&page=1&sort=likedOrder',
    '명상': 'https://class101.net/search?category=604f1c9756c3676f1ed00380&page=1&sort=likedOrder',
    '심리': 'https://class101.net/search?category=604f1c9756c3676f1ed00381&page=1&sort=likedOrder',
    '타로사주운세': 'https://class101.net/search?category=604f1c9756c3676f1ed00382&page=1&sort=likedOrder',
    '게임스포츠': 'https://class101.net/search?category=604f1c9756c3676f1ed00383&page=1&sort=likedOrder',
    '라이프해킹': 'https://class101.net/search?category=604f1c9756c3676f1ed00384&page=1&sort=likedOrder',
    '댄스무용': 'https://class101.net/search?category=604f1c9756c3676f1ed00385&page=1&sort=likedOrder',
    '반려동물': 'https://class101.net/search?category=604f1c9756c3676f1ed00386&page=1&sort=likedOrder',
    '인문학': 'https://class101.net/search?category=604f1c9756c3676f1ed00387&page=1&sort=likedOrder',
    '더새로운라이프': 'https://class101.net/search?category=604f1c9756c3676f1ed00388&page=1&sort=likedOrder',
    '사진': 'https://class101.net/search?category=604f1c9756c3676f1ed0038a&page=1&sort=likedOrder',
    '영상': 'https://class101.net/search?category=604f1c9756c3676f1ed0038b&page=1&sort=likedOrder',
    '디자인': 'https://class101.net/search?category=604f1c9756c3676f1ed0038e&page=1&sort=likedOrder',
    '개발': 'https://class101.net/search?category=604f1c9756c3676f1ed00397&page=1&sort=likedOrder',
    '직무교육': 'https://class101.net/search?category=604f1c9756c3676f1ed003a2&page=1&sort=likedOrder',
    '재태크': 'https://class101.net/search?category=604f1c9756c3676f1ed003b3&page=1&sort=likedOrder',
    '창업부업': 'https://class101.net/search?category=604f1c9756c3676f1ed003b7&page=1&sort=likedOrder',
    '마인드': 'https://class101.net/search?category=604f1c9756c3676f1ed003c3&page=1&sort=likedOrder',
    '글쓰기': 'https://class101.net/search?category=604f1c9756c3676f1ed003c4&page=1&sort=likedOrder',
    '언어': 'https://class101.net/search?category=604f1c9756c3676f1ed003cd&page=1&sort=likedOrder',
    '아동교육': 'https://class101.net/search?category=604f1c9756c3676f1ed003d6&page=1&sort=likedOrder',
    'DIY미술키트': 'https://class101.net/search?category=5f9fbe8a5512a2230f099364&page=1&sort=likedOrder',
    'DIY밀키트': 'https://class101.net/search?category=5f9fbe8a5512a2230f099365&page=1&sort=likedOrder',
    'DIY키즈키트': 'https://class101.net/search?category=5f9fbe8a5512a2230f099366&page=1&sort=likedOrder',
    'DIY굿즈': 'https://class101.net/search?category=5f9fbe8a5512a2230f099367&page=1&sort=likedOrder',
    'DIY재료도구': 'https://class101.net/search?category=5f9fbe8a5512a2230f099368&page=1&sort=likedOrder',
    'DIY악기': 'https://class101.net/search?category=5f9fbe8a5512a2230f099369&page=1&sort=likedOrder',
    'DIY라이프및기타': 'https://class101.net/search?category=5f9fbe8a5512a2230f09936a&page=1&sort=likedOrder',
    'DIY공예키트': 'https://class101.net/search?category=5f9fbe8a5512a2230f099363&page=1&sort=likedOrder'
'''
