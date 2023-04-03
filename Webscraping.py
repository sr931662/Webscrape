import time
from random import random
from bs4 import BeautifulSoup
import json
import pandas as pd
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
from time import sleep
from selenium import webdriver
from pprint import pprint
import datetime
import pandas as pd
from bs4 import BeautifulSoup
opts = Options()

url = input("Please enter url here!!")
city = input("Enter the region : ")
tag = input("Enter the tags : ")
type = input("Enter type of scrape (profile or post) : ")

# city = "india"
# tag = "ias"
# type = "post"

driver = webdriver.Chrome(options=opts,
                          executable_path='chromedriver')


# function to ensure all key data fields have a value.
def validate_field(field):
    # if field is present pass if field:
    if field:
        pass
    else:
        field = 'No results'
    return field

#
# # driver.get method() will navigate to a page givem by the URL address
# driver.get('https://www.linkedin.com')
# driver.implicitly_wait(0.5)
#
#
# # locate email from by_client_name:
# uname = driver.find_element(By.ID, 'session_key')
#
# # send_keys() to stimulte keystrokes
# uname.send_keys('sr931662@gmail.com')
#
# # sleep for 0.5 seconds
# sleep(0.5)
#
# # locate password form by_class_name
# pswd = driver.find_element(By.ID, 'session_password')
#
# # send_keys() to stimulate keystrokes
# pswd.send_keys('R$931662ingh')
# sleep(0.5)
#
# # locate submit button by_xpath
# sign_in_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
#
# # .click() to mimic button click
# sign_in_button.click()
# sleep(0.5)


cookies = {
    'ASP.NET_SessionId': 'wsft2szyvu42cuaf5ijzser0',
    '_accessToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1bmlxdWVfbmFtZSI6IjQyMTkyNzcwMiIsIlVUWSI6IlMiLCJyb2xlIjpbIjUiLCIxMDEiXSwiU0lEIjoiMjIiLCJUSUQiOiI0MjE5Mjc3MDIiLCJJQUwiOiJGYWxzZSIsIkFJRCI6IjAiLCJPSUQiOiIwIiwiRUFVIjoiZmFsc2UiLCJpc3MiOiJodHRwczovL2F1dGguZ3VydS5jb20vIiwiYXVkIjoiaHR0cHM6Ly93d3cuZ3VydS5jb20vYXBpIiwiZXhwIjoxOTk1OTQ0OTc0LCJuYmYiOjE2ODAzMjU3NzR9.iuOJW1n-F4jQGDq9dW9NPyxay1AO8HEYAe4oHwFg8uM',
    '_refreshToken': '',
    '_clientID': '421927702',
    'visid_incap_1227176': '6Nt9c4GOSmWFtpNbBfgy3Iy8J2QAAAAAQUIPAAAAAABhu2+iSZqV/j2rER4vQLio',
    'nlbi_1227176': '/S/LVSmO2yhxQvPYmoY5nwAAAABMLlxiy+nf21lL9YVklC1X',
    'incap_ses_740_1227176': 'VZnkD1kAEy0qwNuhXANFCo28J2QAAAAA8tshD+9WMCIyI3N8BfmFuQ==',
    '_gcl_au': '1.1.814784073.1680325771',
    '_gid': 'GA1.2.1945662982.1680325772',
    'g_state': '{"i_p":1680333378145,"i_l":1}',
    '_ga_6DQ0MCG0VT': 'GS1.1.1680325772.1.1.1680326182.60.0.0',
    '_ga': 'GA1.2.2094301905.1680325772',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Apr+01+2023+10%3A46%3A23+GMT%2B0530+(India+Standard+Time)&version=6.33.0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.guru.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0',
    'AWSALB': 'S2GZZEL8ijnrZlfN+iFwulwxnp26h2p0QCJBObnUcoVkJUC2cqzjt5URhGP1oMWWEDhpmzEceaDKdTfoUOo3DZ3k3eSJmdOGtv89BmE4EOCdRGeRbDV/aAUfqSTz',
    'AWSALBCORS': 'S2GZZEL8ijnrZlfN+iFwulwxnp26h2p0QCJBObnUcoVkJUC2cqzjt5URhGP1oMWWEDhpmzEceaDKdTfoUOo3DZ3k3eSJmdOGtv89BmE4EOCdRGeRbDV/aAUfqSTz',
}

headers = {
    'authority': 'www.guru.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'ASP.NET_SessionId=wsft2szyvu42cuaf5ijzser0; _accessToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1bmlxdWVfbmFtZSI6IjQyMTkyNzcwMiIsIlVUWSI6IlMiLCJyb2xlIjpbIjUiLCIxMDEiXSwiU0lEIjoiMjIiLCJUSUQiOiI0MjE5Mjc3MDIiLCJJQUwiOiJGYWxzZSIsIkFJRCI6IjAiLCJPSUQiOiIwIiwiRUFVIjoiZmFsc2UiLCJpc3MiOiJodHRwczovL2F1dGguZ3VydS5jb20vIiwiYXVkIjoiaHR0cHM6Ly93d3cuZ3VydS5jb20vYXBpIiwiZXhwIjoxOTk1OTQ0OTc0LCJuYmYiOjE2ODAzMjU3NzR9.iuOJW1n-F4jQGDq9dW9NPyxay1AO8HEYAe4oHwFg8uM; _refreshToken=; _clientID=421927702; visid_incap_1227176=6Nt9c4GOSmWFtpNbBfgy3Iy8J2QAAAAAQUIPAAAAAABhu2+iSZqV/j2rER4vQLio; nlbi_1227176=/S/LVSmO2yhxQvPYmoY5nwAAAABMLlxiy+nf21lL9YVklC1X; incap_ses_740_1227176=VZnkD1kAEy0qwNuhXANFCo28J2QAAAAA8tshD+9WMCIyI3N8BfmFuQ==; _gcl_au=1.1.814784073.1680325771; _gid=GA1.2.1945662982.1680325772; g_state={"i_p":1680333378145,"i_l":1}; _ga_6DQ0MCG0VT=GS1.1.1680325772.1.1.1680326182.60.0.0; _ga=GA1.2.2094301905.1680325772; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Apr+01+2023+10%3A46%3A23+GMT%2B0530+(India+Standard+Time)&version=6.33.0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.guru.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0; AWSALB=S2GZZEL8ijnrZlfN+iFwulwxnp26h2p0QCJBObnUcoVkJUC2cqzjt5URhGP1oMWWEDhpmzEceaDKdTfoUOo3DZ3k3eSJmdOGtv89BmE4EOCdRGeRbDV/aAUfqSTz; AWSALBCORS=S2GZZEL8ijnrZlfN+iFwulwxnp26h2p0QCJBObnUcoVkJUC2cqzjt5URhGP1oMWWEDhpmzEceaDKdTfoUOo3DZ3k3eSJmdOGtv89BmE4EOCdRGeRbDV/aAUfqSTz',
    'referer': 'https://www.guru.com/',
    'sec-ch-ua': '"Not=A?Brand";v="8", "Chromium";v="110", "Opera GX";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0 (Edition std-1)',
}

# response = requests.get(url, headers=headers)
response = requests.get(url, cookies=cookies, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

Jobdata = []
Postdata = []
lnks = []
if type == "profile":
    for x in range(0, 20, 10):
        driver.get(
            f'https://www.google.com/search?q=site:linkedin.com/in/+AND+%22{tag}%22+AND+%22{city}%22')
        # sleep(3)
        linkedin_url = [my_elem.get_attribute("href") for my_elem in WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='yuRUbf']/a[@href]")))]
        lnks.append(linkedin_url)

elif type == "post":
    for x in range(0, 20, 10):
        driver.get(
            f'https://www.google.com/search?q=site:linkedin.com/posts/+AND+%22{tag}%22+AND+%22{city}%22')
        # sleep(3)
        linkedin_url = [my_elem.get_attribute("href") for my_elem in WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='yuRUbf']/a[@href]")))]
        lnks.append(linkedin_url)

else:
    print('Type error:: Type either profile or post!!!')

if type == "profile":
    for x in lnks:
        for i in x:
            # get the profile URL
            driver.get(i)
            time.sleep(15)
            # assigning the source code from the web page to variable sel
            sel = Selector(text=driver.page_source)

            # xpath to extract the text from the class containing the name
            name = sel.xpath(
                '//*[starts-with(@class, "text-heading-xlarge inline t-24 v-align-middle break-words")]/text()').extract_first()

            # if name exists
            if name:
                # .strip() will remove the new line /n and white spaces
                name = name.strip()

            # xpath to extract the text from the class containing the job title
            job_title = sel.xpath('//*[starts-with(@class, "text-body-medium break-words")]/text()').extract_first()
            if job_title:
                job_title = job_title.strip()

            try:
                # xpath to extract the text from the class containing the college
                company = driver.find_element(By.XPATH, '//ul[@class="pv-text-details__right-panel"]').text

            except:
                company = 'None'

            if company:
                company = company.strip()

            # xpath to extract the text from the class containing the location.
            location = sel.xpath('//*[starts-with(@class, "text-body-small inline t-black--light break-words")]/text()').extract_first()

            if location:
                location = location.strip()



            # validating if the fields exist as the profile
            name = validate_field(name)
            job_title = validate_field(job_title)
            company = validate_field(company)
            # college = validate_field(college)
            location = validate_field(location)
            linkedin_url = validate_field(linkedin_url)

            # printing the output.
            print('\n')
            print(f'Name : {name}')
            print(f'Job Title : {job_title}')
            print(f'Company : {company}')
            print(f'Location : {location}')
            print(f'URL : {linkedin_url}')
            print('\n')

            data = {
                'Name': name,
                'Job Title': job_title,
                'Company': company,
                'Location': location,
                'URL': linkedin_url
            }
            Jobdata.append(data)
            with open("profile_json.json", "w") as pf:
                json.dump(data, pf)
            print("Profile json developed!...")

if type == "post":
    for x in lnks:
        for i in x:
            # get the profile URL
            driver.get(i)
            # time.sleep(15)
            # assigning the source code from the web page to variable sel
            sel = Selector(text=driver.page_source)

            # xpath to extract the text from the class containing the name
            name = sel.xpath(
                '//*[starts-with(@class, "text-sm link-styled no-underline leading-open")]/text()').extract_first()

            # if name exists
            if name:
                # .strip() will remove the new line /n and white spaces
                name = name.strip()

            # xpath to extract the text from the class containing the job title
            job_descr = sel.xpath('//*[starts-with(@class, "!text-xs text-color-text-low-emphasis leading-[1.33333] '
                                  'm-0 truncate")]/text()').extract_first()

            # if jobdescription exists
            if job_descr:
                # .strip() will remove the new line /n and white spaces
                job_descr = job_descr.strip()

            # xpath for content
            content = sel.xpath('//*[starts-with(@class, "attributed-text-segment-list__content text-color-text '
                                '!text-sm whitespace-pre-wrap break-words")]/text()').extract_first()

            # if content exists
            if content:
                # .strip() will remove the new line /n and white spaces
                content = content.strip()

            # xpath for likes.
            likes = sel.xpath('//*[starts-with(@class, "font-normal ml-0.5")]/text()').extract_first()

            # if likes exists
            if likes:
                # .strip() will remove the new line /n and white spaces
                likes = likes.strip()

            # xpath for comments.
            comments = sel.xpath('//*[starts-with(@data-test-id, "social-actions__comments")]/text()').extract_first()

            # if comments exists
            if comments:
                # .strip() will remove the new line /n and white spaces
                comments = comments.strip()

            # xpath for uptime.
            uptime = sel.xpath('//*[starts-with(@class, "flex-none")]/text()').extract_first()

            # if upload time exists
            if uptime:
                # .strip() will remove the new line /n and white spaces
                uptime = uptime.strip()

            # validating if the fields exist as the profile
            name = validate_field(name)
            job_descr = validate_field(job_descr)
            content = validate_field(content)
            likes = validate_field(likes)
            comments = validate_field(comments)
            uptime = validate_field(uptime)

            # printing the output.
            print('\n')
            print(f'Name : {name}')
            print(f'Job Title : {job_descr}')
            print(f'content : {content}')
            print(f'likes : {likes}')
            print(f'comments : {comments}')
            print(f'upload time : {uptime}')
            print('\n')


            post_data = {
                'Name': name,
                'Job Description': job_descr,
                'Content': content,
                'Likes': likes,
                'Comments': comments,
                'Upload Time': uptime
            }

            Jobdata.append(post_data)
            with open("post_json.json", "w") as pt:
                json.dump(post_data, pt)
            print("Post json developed!...")
            print()

profile = pd.DataFrame(Jobdata)
profile.to_excel('Profile_jobdata_linkedin.xlsx')
# post = pd.DataFrame(Postdata)
# post.to_excel('Post_data_linkedin.xlsx')

# terminates the application
driver.quit()

# print data
print(Jobdata)


