import SeleniumOperation


#url = "https://class101.net/search?category=604f1c9756c3676f1ed00304&sort=likedOrder"

driver = SeleniumOperation.getHeadlessDriver()

#SeleniumOperation.scrape(url, driver)

# priceResults = driver.find_elements_by_xpath(
#     "//strong[contains(@class,'SellingPrice-yffb6l-0 cUbeAw')]")


# clicking on individual class
# classAddress = driver.find_elements_by_xpath(
#     "//a[contains(@class, 'ProductCardfragment__HoverStyledLink-sc-1cja13i-0 gfCFNQ')]")

# addressList = []

# for element in classAddress:
#     addressList.append(element.get_attribute('href'))

# print(addressList)
# print(len(addressList))


# driver.get(addressList[0])

# reviews = driver.find_element_by_xpath(
#     "//dd[contains(@class, 'PostReviewSectionViewController__PostReviewInfoDescription-sc-1khhvgt-5 lhQFbC')]").text


# print(reviews)

SeleniumOperation.scrape(
    'https://class101.net/products/hf3H7C5T96VByVsA3ZRz', driver)


def getReviewsSatisfaction(driver):
    '''

    '''
    reviews = driver.find_elements_by_xpath(
        "//dd[contains(@class, 'PostReviewSectionViewController__PostReviewInfoDescription-sc-1khhvgt-5 lhQFbC')]")

    reviewNum = reviews[0].text
    satisfaction = reviews[1].text

    return reviewNum, satisfaction


# class_df = pd.DataFrame(columns=['reviews', 'satisfaction'])

# aRow = {'reviews': reviewNum, 'satisfaction': satisfaction}

# class_df = class_df.append(aRow, ignore_index=True)

# print(class_df)


def findChapterLessons(driver):
    '''
    Given a selenium driver, Returns string containing number of chapters and lectures
    '''
    chapterLecture = driver.find_element_by_xpath(
        "//dd[contains(@class, 'KlassSummarySection__DefinitionDescription-lcwqnj-4 jeiEOD')]")

    return chapterLecture.text


def extractChapterLessons(textExtract):
    '''
    Extracts and returns the number of chapters and lectures from given string
    '''
    # unitindex = [i for i, ltr in enumerate(textExtract) if ltr == '개']
    # commaindex = textExtract.index(",")

    # chapter = textExtract[:unitindex[0]]

    # lectures = textExtract[commaindex+2:myindex[1]]

    chapterIndex = textExtract.index("chapter")
    lessonIndex = textExtract.index("lesson")

    chapter = textExtract[:chapterIndex-1]
    lesson = textExtract[chapterIndex+9:lessonIndex-1]

    return int(chapter), int(lesson)


def getChapterLessons(driver):
    '''


    '''

    textExtract = findChapterLessons(driver)

    chapter, lesson = extractChapterLessons(textExtract)

    return chapter, lesson


def getClassLevel(driver):
    '''

    '''

    classLevel = driver.find_element_by_xpath(
        "//span[contains(@class, 'ChargeSectionTitle__HightLight-sc-1s0lydo-0 dJoEdj')]")

    return classLevel.text


def getLikes(driver):
    '''

    '''
    likes = driver.find_elements_by_xpath(
        "//button[contains(@class, 'sc-hKgILt eFWsxw sc-bqyKva glLlrc SalesProductInfoTable__WishlistButton-sc-1cslumm-2 bUSrQo')]/span[contains(@class, 'sc-eCssSg hmocIu')]")

    return int(likes[1].text)


def findFeedback(driver):
    '''

    '''

    feedbacks = driver.find_elements_by_xpath(
        "//div[contains(@class, 'LiveFeedbackSectionViewController__LiveFeedbackStatusItem-sc-1ahetk9-4 cUJPkM')]")

    return feedbacks


def extractFeedback(feedbacks):
    '''
    '''

    feedback_pct = None
    feedback_time = None

    feedbackString = ""

    for feedback in feedbacks:
        feedbackString = feedbackString + feedback.text

    if "%" in feedbackString:
        percent_index = feedbackString.index("%")
        feedback_pct = feedbackString[7:percent_index]

    if "응답" in feedbackString:
        feedback_time = feedbackString[percent_index+1:]

    return feedback_pct, feedback_time


def getFeedback(driver):
    '''
    '''

    feedbacks = findFeedback(driver)
    feedback_pct, feedback_time = extractFeedback(feedbacks)

    return feedback_pct, feedback_time


def hasSubtitles(driver):
    '''
    '''

    hasSubtitles = driver.find_elements_by_xpath(
        "//dd[contains(@class, 'KlassSummarySection__DefinitionDescription-lcwqnj-4 jeiEOD')]")

    subtitles = hasSubtitles[2].text.upper()

    if subtitles == "YES":
        return True

    else:
        return False
