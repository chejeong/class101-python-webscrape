import SeleniumOperation
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
from datetime import datetime


def extractText(webElements):

    text = ""

    for element in webElements:

        text = text + element.text

    return text


def getReviewsSatisfaction(driver):
    '''
    Returns the number of reviews submitted and the satisfaction percentage of the class.
    '''

    reviews = None

    try:
        reviews = driver.find_elements_by_xpath(
            "//dd[contains(@class, 'PostReviewSectionViewController__PostReviewInfoDescription-sc-1khhvgt-5 lhQFbC')]")
    except NoSuchElementException:
        pass

    # if class does not have any reviews
    if not reviews:
        return None, None

    else:
        reviewNum = reviews[0].text
        satisfaction = reviews[1].text

        return reviewNum, satisfaction


def findChapterLessons(driver):
    '''
    Given a selenium driver, Returns string containing number of chapters and lectures
    '''
    chapterLecture = None

    try:
        chapterLecture = driver.find_element_by_xpath(
            "//dd[contains(@class, 'KlassSummarySection__DefinitionDescription-lcwqnj-4 jeiEOD')]")
    except NoSuchElementException:
        pass

    if not chapterLecture:
        return None

    else:
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

    return chapter, lesson


def getChapterLessons(driver):
    '''
    Returns the number of chapters and lessons in a class

    '''

    textExtract = findChapterLessons(driver)

    if not textExtract:
        return None, None

    else:
        chapter, lesson = extractChapterLessons(textExtract)
        return chapter, lesson


def getClassLevel(driver):
    '''
    Returns the class level (difficulty of class)
    '''
    classLevel = None

    try:
        classLevel = driver.find_element_by_xpath(
            "//span[contains(@class, 'ChargeSectionTitle__HightLight-sc-1s0lydo-0 dJoEdj')]")
    except NoSuchElementException:
        pass

    if not classLevel:
        return None

    else:
        return classLevel.text


def getLikes(driver):
    '''
    Returns the number of likes a class received.
    '''
    likes = None

    # sc-hKgILt eFWsxw sc-bqyKva glLlrc SalesProductInfoTable__WishlistButton-sc-1cslumm-2 bUSrQo

    try:
        likes = driver.find_elements_by_xpath(
            "//button[contains(@class, 'sc-hKgILt eFYPau sc-bqyKva glLlrc SalesProductInfoTable__WishlistButton-sc-1cslumm-2 bUSrQo')]/span[contains(@class, 'sc-eCssSg hmocIu')]")
    except NoSuchElementException:
        pass

    if not likes:
        return None

    else:
        return likes[1].text


def findFeedback(driver):
    '''
    Returns the feedback webElement.
    '''

    feedbacks = None

    try:
        feedbacks = driver.find_elements_by_xpath(
            "//div[contains(@class, 'LiveFeedbackSectionViewController__LiveFeedbackStatusItem-sc-1ahetk9-4 cUJPkM')]")
    except NoSuchElementException:
        pass

    return feedbacks


def extractFeedback(feedbacks):
    '''
    Extracts and returns the percentage of feedbacks instructor gives, 
    and the average time it takes for instructor to leave feedback.
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


def getFeedbackStats(driver):
    '''
    Returns the percentage of feedbacks instructor gives, 
    and the average time it takes for instructor to leave feedback.
    '''

    feedbacks = findFeedback(driver)

    if not feedbacks:
        return None, None

    else:
        feedback_pct, feedback_time = extractFeedback(feedbacks)
        return feedback_pct, feedback_time


def hasSubtitles(driver):
    '''
    Returns boolean value of whether class has subtitles.
    '''
    hasSubtitles = None

    try:
        hasSubtitles = driver.find_elements_by_xpath(
            "//dd[contains(@class, 'KlassSummarySection__DefinitionDescription-lcwqnj-4 jeiEOD')]")
    except NoSuchElementException:
        pass

    if not hasSubtitles:
        return None

    else:
        subtitles = hasSubtitles[2].text.upper()

        if subtitles == "YES":
            return True
        else:
            return False


def getCreator(driver):
    '''
    Extracts and returns the text name of the creator/instructor
    '''
    creatorName = None

    try:
        creatorName = driver.find_element_by_xpath(
            "//div[contains(@class, 'CreatorIntroSection__Title-sc-1omckp4-0 exZRo')]//strong")
    except NoSuchElementException:
        pass

    if not creatorName:
        return None

    else:
        return creatorName.text


def getCreatorSocialMediaLinks(driver):
    '''
    Given a webdriver, extracts and returns the social media links of class creator(instructor)
    '''
    socialmedia = None

    try:
        socialmedia = driver.find_elements_by_xpath(
            "//div[contains(@class,'ChannelButtonGroup__Container-dcuo70-0 jKQAqu')]//a[contains(@class, 'LinkComponent__Anchor-gmbdn6-0 johiBf sc-dlfnbm sc-gKsewC bcaJjD BzhTL')]")
    except NoSuchElementException:
        pass

    #sns_links = []
    sns_links = ""

    # check if creator does not have social media
    if not socialmedia:
        return None

    else:
        for _ in socialmedia:
            # sns_links.append(_.get_attribute('href'))

            if sns_links == "":
                sns_links = sns_links + _.get_attribute('href')

            else:
                sns_links = sns_links + ', ' + _.get_attribute('href')

        return sns_links


def getCommunityPosts(driver):
    '''
    Extracts and returns the number of post in community 
    '''

    communityPost = None

    # handling case when there is no communitypoast element
    try:
        communityPost = driver.find_element_by_xpath(
            "//div[contains(@class,'ContentSectionStyle__SectionTitleColumn-sc-10cmaiq-0 CommunitySection__SectionWithTitleColumn-sc-1cvskyc-0 bocNPC dmrnCF')]//small[contains(@class,'CommunitySection__Text-sc-1cvskyc-3 gmplQK')]")
    except NoSuchElementException:
        pass

    if communityPost is not None:
        post = communityPost.text
        return post

    else:
        return None


def getPrices(driver):
    '''
    Returns the price information of a class: 
    original price, discounts, installment period, final price
    '''

    element = None

    try:
        element = driver.find_element_by_xpath(
            "//div[contains(@class,'DiscountAndInstallmentInfoModal__HelpIconWrapper-sc-14kllou-0 uehYl')]")
        driver.execute_script("arguments[0].click();", element)
    except NoSuchElementException:
        pass

    time.sleep(2)

    if not element:
        return None, None, None, None, None, None, None

    prices = driver.find_elements_by_xpath(
        "//dd[contains(@class,'PriceDescriptionList__DescriptionText-sc-1k21asc-3 jJijyx')]")

    try:
        originalPrice = prices[0].text
    except IndexError:
        originalPrice = None

    try:
        discountAmount = prices[1].text
    except IndexError:
        discountAmount = None

    try:
        couponDiscount = prices[2].text
    except IndexError:
        couponDiscount = None

    try:
        finalPrice = prices[3].text
    except IndexError:
        finalPrice = None

    # sc-dQppl fNfNrx PriceInfoTable__TermText-sc-1asmm9b-3 cVjuSB
    installment = driver.find_elements_by_xpath(
        "//div[contains(@class, 'sc-dQppl iYUinv PriceInfoTable__TermText-sc-1asmm9b-3 cVjuSB')]")
    installment = extractText(installment)

    discount_pct = driver.find_elements_by_xpath(
        "//div[contains(@class,'sc-dQppl lnHFZc PriceInfoTable__DiscountText-sc-1asmm9b-4 omEfB')]")
    discount_pct = extractText(discount_pct)

    monthly = driver.find_elements_by_xpath(
        "//h4[contains(@class,'sc-dQppl hGEcmg PriceInfoTable__PriceText-sc-1asmm9b-6 kIAPtb')]")
    monthly = extractText(monthly)

    return originalPrice, discountAmount, couponDiscount, installment, discount_pct, finalPrice, monthly


def getFeedbackNum(driver):
    '''
    Returns the number of feedbacks of a class
    '''

    try:
        feedbackNum = driver.find_elements_by_xpath(
            "//button[contains(@class,'sc-jSgupP ckDfJz sc-bqyKva dBtbez LiveFeedbackSectionViewController__LiveFeedbackMoreButton-sc-1ahetk9-9 bYqCJB')]/a[contains(@class,'LinkComponent__StyledLink-gmbdn6-1 hYxdXM sc-dlfnbm sc-gKsewC bcaJjD BzhTL')]/span[contains(@class,'sc-eCssSg hmocIu')]")
    except NoSuchElementException:
        pass

    if not feedbackNum:
        return None

    else:
        numFeedback = extractText(feedbackNum)

        return numFeedback


def getStartDate(driver):
    '''
    Extracts and returns the start date of class
    '''

    startDate = None

    try:
        startDate = driver.find_elements_by_xpath(
            "//dd[contains(@class,'KlassSummarySection__DefinitionDescription-lcwqnj-4 jeiEOD')]")
    except NoSuchElementException:
        pass

    if not startDate:
        return None

    else:
        return startDate[1].text


def getSubject(driver):
    '''
    Extracts and returns the subject of the class
    '''

    try:
        subject = driver.find_elements_by_xpath(
            "//span[contains(@class,'ChargeSectionTitle__HightLight-sc-1s0lydo-0 dJoEdj')]")
    except NoSuchElementException:
        pass

    if not subject:
        return None

    else:
        return subject[1].text


def getTitle(driver):
    '''
    Extracts and returns the title of the class
    '''
    title = None

    try:
        title = driver.find_elements_by_xpath(
            "//h2[contains(@class,'sc-dQppl jhzFzM ProductHeader__Title-sc-4rgr4k-2 jkmuZi')]")
    except NoSuchElementException:
        pass

    classTitle = extractText(title)

    # title[1].text
    return classTitle


def getClassDuration(driver):
    '''
    Extracts and returns the duration of the class.
    '''

    duration = None

    try:
        duration = driver.find_elements_by_xpath(
            "//div[contains(@class, 'sc-dQppl gVinuv ContentSectionCard__Title-oy7lxg-3 brYcfa')]")
    except NoSuchElementException:
        pass

    if not duration:
        return None

    return duration[0].text


def getCoupon(driver):
    '''
    Extracts and returns the coupon info
    '''
    coupon = None

    try:
        coupon = driver.find_elements_by_xpath(
            "//div[contains(@class,'sc-dQppl gECXWx ProductCoverBadgefragment__Text-sc-11lvxb8-2 HWgNP')]")
    except NoSuchElementException:
        pass

    if not coupon:
        return None

    else:
        return coupon[0].text


def getClassInfo(driver, category, classURL):
    '''
    Constructs and returns pandas DataFrame containing class information.
    '''

    referenceDate = datetime.today().strftime('%Y-%m-%d')
    className = getTitle(driver)
    topic = getSubject(driver)
    level = getClassLevel(driver)
    duration = getClassDuration(driver)
    chapters, lessons = getChapterLessons(driver)
    startDate = getStartDate(driver)
    subtitles = hasSubtitles(driver)
    creatorName = getCreator(driver)
    creatorSocialMedia = getCreatorSocialMediaLinks(driver)
    reviewNum, satisfaction = getReviewsSatisfaction(driver)
    communityPosts = getCommunityPosts(driver)
    likes = getLikes(driver)
    feedbackPct, feedbackTime = getFeedbackStats(driver)
    feedbackNum = getFeedbackNum(driver)
    coupon = getCoupon(driver)
    originalPrice, discountAmount, couponDiscount, installment, discountPct, finalPrice, monthly = getPrices(
        driver)

    classInfo = pd.DataFrame({'className': [className], 'category': [category], 'topic': [topic], 'level': [level], 'duration': [duration],
                             'chapters': [chapters], 'lessons': [lessons], 'startDate': [startDate], 'subtitles': [subtitles], 'creatorName': [creatorName],
                              'creatorSocialMedia': [creatorSocialMedia], 'reviewNum': [reviewNum], 'satisfaction': [satisfaction],
                              'communityPosts': [communityPosts], 'likes': [likes], 'feedbackPct': [feedbackPct], 'feedbackTime': [feedbackTime],
                              'feedbackNum': [feedbackNum], 'originalPrice': [originalPrice], 'discountAmount': [discountAmount], 'couponDiscount': [couponDiscount],
                              'finalPrice': [finalPrice], 'installmentPeriod': [installment], 'discountPct': [discountPct],
                              'monthlyPayment': [monthly], 'coupon': [coupon], 'referenceDate': [referenceDate], 'classURL': [classURL]})

    return classInfo


def scrapePage(driver, classLink, category):
    '''
    Returns pandas dataframe of information of a class.
    '''

    classInfo = pd.DataFrame(columns=['className', 'category', 'topic', 'level', 'duration',
                             'chapters', 'lessons', 'startDate', 'subtitles', 'creatorName', 'creatorSocialMedia',
                                      'reviewNum', 'satisfaction', 'communityPosts', 'likes',
                                      'feedbackPct', 'feedbackTime', 'feedbackNum',
                                      'originalPrice', 'discountAmount', 'couponDiscount', 'finalPrice', 'installmentPeriod',
                                      'discountPct', 'monthlyPayment', 'coupon', 'referenceDate', 'classURL'])

    return classInfo


def getClassLinks(driver):
    '''
    Returns the list of class links
    '''
    classAddress = driver.find_elements_by_xpath(
        "//a[contains(@class, 'ProductCardfragment__HoverStyledLink-sc-1cja13i-0 gfCFNQ')]")

    addressList = []

    for element in classAddress:
        classlink = element.get_attribute('href')

        # adding classes that already started
        if 'products' in classlink:
            addressList.append(classlink)

    numClasses = len(classAddress)

    return addressList, numClasses


def scrapeClassLinks(driver, mainURL):
    '''
    Returns the links of classes in specified category
    '''

    pageNum = 1

    allClasses = []

    # scroll first page
    SeleniumOperation.scrape(driver, mainURL)

    # get class links from first page
    addressList, numClasses = getClassLinks(driver)
    allClasses += addressList

    print(f"Retreived links from page: {pageNum}")

    buttons = driver.find_elements_by_xpath(
        "//button[@class='sc-hKgILt eFYPau sc-crrsfI MdKCt sc-dtwoBo inCwUZ']")

    numButtons = len(buttons)

    if numButtons == 0:
        return allClasses

    else:
        driver.execute_script("arguments[0].click();", buttons[0])

    while True:

        SeleniumOperation.scroll(driver, 8)

        addressList, numClasses = getClassLinks(driver)
        allClasses += addressList

        buttons = driver.find_elements_by_xpath(
            "//button[@class='sc-hKgILt eFYPau sc-crrsfI MdKCt sc-dtwoBo inCwUZ']")
        numButtons = len(buttons)

        pageNum = pageNum + 1
        print(f"Retreived links from page: {pageNum}")

        if numClasses < 30:
            print("Reached last page")
            break
        if numClasses == 30 and numButtons == 1:
            print("Reached last page")
            break

        driver.execute_script("arguments[0].click();", buttons[1])

    return allClasses


def scrapeAllPages(driver, mainURL, category, directoryPath):
    '''
    Scrapes and exports all classes in a category as csv files.
    '''

    classDf = pd.DataFrame(columns=['className', 'category', 'topic', 'level', 'duration',
                                    'chapters', 'lessons', 'startDate', 'subtitles', 'creatorName', 'creatorSocialMedia',
                                    'reviewNum', 'satisfaction', 'communityPosts', 'likes',
                                    'feedbackPct', 'feedbackTime', 'feedbackNum',
                                    'originalPrice', 'discountAmount', 'couponDiscount', 'finalPrice', 'installmentPeriod',
                                    'discountPct', 'monthlyPayment', 'coupon', 'referenceDate', 'classURL'])

    allClassLinks = scrapeClassLinks(driver, mainURL)

    numClasses = len(allClassLinks)

    print(f"total number of classes: {numClasses}")
    tracker = 0

    for classLink in allClassLinks:
        SeleniumOperation.scrape(driver, classLink)
        classInfo = getClassInfo(driver, category, classLink)
        classDf = classDf.append(classInfo)
        tracker = tracker + 1
        print(f"completed: {tracker}")

    classDf.to_csv(f"{directoryPath}/{category}.csv")
