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

def extractText(webElements):

    text = ""

    for element in webElements:

        text = text + element.text

    return text


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


def getFeedbackStats(driver):
    '''
    '''

    feedbacks = findFeedback(driver)

    if not feedbacks:
        return None, None

    else:
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


def getCreator(driver):
    '''
    Extracts and returns the text name of the creator/instructor
    '''

    creatorName = driver.find_element_by_xpath(
        "//div[contains(@class, 'CreatorIntroSection__Title-sc-1omckp4-0 exZRo')]//strong")

    return creatorName.text


def getCreatorSocialMediaLinks(driver):
    '''
    Given a webdriver, extracts and returns the social media links of class creator(instructor)
    '''

    socialmedia = driver.find_elements_by_xpath(
        "//div[contains(@class,'ChannelButtonGroup__Container-dcuo70-0 jKQAqu')]//a[contains(@class, 'LinkComponent__Anchor-gmbdn6-0 johiBf sc-dlfnbm sc-gKsewC bcaJjD BzhTL')]")

    sns_links = []

    # check if creator does not have social media
    if not socialmedia:
        return None

    else:
        for _ in socialmedia:
            sns_links.append(_.get_attribute('href'))

        return sns_links


def getCommunityPosts(driver):
    '''
    Extracts and returns the number of post in community 
    '''

    communityPost = driver.find_element_by_xpath(
        "//div[contains(@class,'ContentSectionStyle__SectionTitleColumn-sc-10cmaiq-0 CommunitySection__SectionWithTitleColumn-sc-1cvskyc-0 bocNPC dmrnCF')]//small[contains(@class,'CommunitySection__Text-sc-1cvskyc-3 gmplQK')]")

    if communityPost is not None:
        post = communityPost.text

        countIndex = post.index("개")
        postNum = post[:countIndex]

        return int(postNum)
    else:
        return None


def getPrices(driver):
    '''

    '''
    element = driver.find_element_by_xpath(
        "//div[contains(@class,'DiscountAndInstallmentInfoModal__HelpIconWrapper-sc-14kllou-0 uehYl')]")

    driver.execute_script("arguments[0].click();", element)

    driver.implicitly_wait(3)

    prices = driver.find_elements_by_xpath(
        "//dd[contains(@class,'PriceDescriptionList__DescriptionText-sc-1k21asc-3 jJijyx')]")

    originalPrice = prices[0].text
    discountAmount = prices[1].text

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

    return originalPrice, discountAmount, installment, discount_pct, monthly


def getFeedbackNum(driver):
    '''

    '''
    feedbackNum = driver.find_elements_by_xpath(
        "//span[contains(@class,'sc-jSgupP ckDfJz sc-bqyKva dBtbez LiveFeedbackSectionViewController__LiveFeedbackMoreButton-sc-1ahetk9-9 bYqCJB')]/a[contains(@class,'LinkComponent__StyledLink-gmbdn6-1 hYxdXM sc-dlfnbm sc-gKsewC bcaJjD BzhTL')]/span[contains(@class,'sc-eCssSg hmocIu')]")

    numFeedback = extractText(feedbackNum)

    countIndex = numFeedback.index("개")

    numFeedback = numFeedback[:countIndex]

    return int(numFeedback)


def getStartDate(driver):
    '''
    Extracts and returns the start date of class
    '''
    startDate = driver.find_elements_by_xpath(
        "//dd[contains(@class,'KlassSummarySection__DefinitionDescription-lcwqnj-4 jeiEOD')]")

    return startDate[1].text


def getSubject(driver):
    '''
    Extracts and returns the subject of the class
    '''

    subject = driver.find_elements_by_xpath(
        "//span[contains(@class,'ChargeSectionTitle__HightLight-sc-1s0lydo-0 dJoEdj')]")

    return subject[1].text


def getTitle(driver):
    '''
    Extracts and returns the title of the class
    '''

    title = driver.find_elements_by_xpath(
        "//h2[contains(@class,'sc-dQppl jhzFzM ProductHeader__Title-sc-4rgr4k-2 jkmuZi')]")

    return title[1].text


def getClassDuration(driver):
    '''
    Extracts and returns the duration of the class.
    '''
    duration = driver.find_elements_by_xpath(
        "//div[contains(@class, 'sc-dQppl gVinuv ContentSectionCard__Title-oy7lxg-3 brYcfa')]")

    return duration[0].text


def getCoupon(driver):
    '''
    Extracts and returns the coupon info
    '''

    coupon = driver.find_elements_by_xpath(
        "//div[contains(@class,'sc-dQppl gECXWx ProductCoverBadgefragment__Text-sc-11lvxb8-2 HWgNP')]")

    return coupon[0].text
