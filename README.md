# class101-python-webscrape

### Brief Overview
Webscraping project to collect data from Class101, an online learning platform based in Korea: https://class101.net/ 

Blogpost of basic exploratory data analysis on number of likes of courses (written in Korean): https://chenotjay.tistory.com/3

Contained within the `Data` directory are tabular data files created from the scraped data. Detailed descriptions of the columns in each file are provided below:

**Class101DataClean.xlsx**

| ColumnName        | Description                                                                            |
|-------------------|----------------------------------------------------------------------------------------|
| ClassName         | Title of the class                                                                     |
| Category          | General category of the class (i.e. Drawing, Cooking, Sports etc.)                     |
| Topic             | Topic the class teaches                                                                |
| Level             | Level of difficulty (target audience) of the class (i.e. beginners, experts)           |
| Duration          | Duration of the class (i.e. 12 weeks, 14 weeks)                                        |
| Chapters          | Number of chapters featured in a class                                                 |
| Lessons           | Number of lessons featured in a class                                                  |
| StartDate         | Date a class starts                                                                    |
| Subtitles         | True if class offer subtitles, False if there are no subtitles                         |
| CreatorName       | Name of the class creator/instructor                                                   |
| ReviewNum         | Number of reviews class received from students                                         |
| SatisfactionPct   | Level of satisfaction by students of class in percentage                               |
| CommunityPosts    | Number of posts in class "blog"/"Q&A"                                                  |
| likes             | Number of likes a class received                                                       |
| feedbackPct       | Percentage of posts that receives feedback from instructor                             |
| feedbackTime      | Average time that takes for instructor to provide feedback to users                    |
| feedbackNum       | Number of feedbacks                                                                    |
| originalPrice     | Original price of a class                                                              |
| discountAmount    | Amount of discount price.                                                              |
| couponDiscount    | Discount amount by coupons offered by class                                            |
| finalPrice        | Final price of class after discounts                                                   |
| installmentPeriod | Period of payment installation (i.e. 5 months)                                         |
| discountPct       | Discount percentage                                                                    |
| monthlyPayment    | Payment amount per installment/month (roughly finalPrice divided by installmentPeriod) |
| coupon            | Name of coupon offered                                                                 |
| referenceDate     | The date when class information was scraped.                                           |
| classURL          | URL of class                                                                           |


**SocialMediaData.csv**

|ColumnName        |Description                           |
|------------------|--------------------------------------|
|CreatorName       |Name of creator/instructor of class   |
|CreatorSocialMedia|URL of creator's social media account |

*Each row maps a creator to one social media account. Thus, creators with multiple social media accounts appears in multiple rows*

### Requirements

Refer to the `requirements.txt` file for required packages.

This project also utilizes the `YoutubeDataAPIv3` to request creators' youtube channel data.

### Files Overview

<ul>
  <li>SeleniumOperation.py</li>
    <ul>
    <li>Contains functions that perform selenium scrolling</li>
    </ul>
  <li>Class101.py</li>
    <ul>
      <li>Includes functions using xpath operations to obtain specific data from website.</li>
      <li>Includes function that accumulates data as a pandas dataframe, which converts and exports it as csv</li>
    </ul>
  <li>main.py</li>
    <ul>
      <li>Invokes functions from `Class101.py` file to scrape data from the main page of specified category</li>
    </ul>
  <li>DataCleaning.R</li>
    <ul>
      <li>Cleans data from `main.py`</li>
        <ul>
          <li>i.e. Drop currency symbol from price string and convert to int</li>
          <li>i.e. Drop punctuation marks</li>
        </ul>
    </ul>
  <li>analysis.ipynb</li>
    <ul>
      <li>Uses pandas operations to perform exploratory data analysis and generate visualizations</li>
      <li>Includes function to extract youtube channel id from instructors' social media URL</li>
      <li>Uses `YoutubeDataAPIv3` to request channel information</li>
    </ul>
</ul>
