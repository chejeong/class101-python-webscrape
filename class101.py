import SeleniumOperation


url = "https://class101.net/search?category=604f1c9756c3676f1ed00304&sort=likedOrder"

driver = SeleniumOperation.getHeadlessDriver()

SeleniumOperation.scrape(url, driver)

priceResults = driver.find_elements_by_xpath(
    "//strong[contains(@class,'SellingPrice-yffb6l-0 cUbeAw')]")

# for price in priceResults:
#     print(price)

# print(len(priceResults))


# clicking on individual class
classAddress = driver.find_elements_by_xpath(
    "//a[contains(@class, 'ProductCardfragment__HoverStyledLink-sc-1cja13i-0 gfCFNQ')]")

addressList = []

for element in classAddress:
    addressList.append(element.get_attribute('href'))

print(addressList)
print(len(addressList))


driver.get(addressList[0])

reviews = driver.find_element_by_xpath(
    "//dd[contains(@class, 'PostReviewSectionViewController__PostReviewInfoDescription-sc-1khhvgt-5 lhQFbC')]").text


print(reviews)
