# from selenium import webdriver 
# from selenium.webdriver.common.by import By
# import time
# import json
# from bs4 import BeautifulSoup
# import pandas as pd 

# keyword = input("enter ob keyword")

# driver = webdriver.Chrome()
# driver.get(f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={keyword}")
# time.sleep(6)

# soup = BeautifulSoup(driver.page_source , "html.parser")
# driver.quit()

# # EXTRACT JOB INFO 

# jobs= []

# for job in soup.find_all("li" , class_="clearfix job-bx wht-shd-bx") :
#     title = job.header.h2.a.text.strip()
#     company = job.find("h3" , class_="joblist-comp-name").text.strip()
#     # location = job.find("ul" , class_ = "top-jd-dti").li.text.strip() 
#     loc_tags = job.find("ul" , class_ = "top-jd-dti")
#     location = loc_tags.li.text.strip if loc_tags else "not mentioned"
    

#     jobs.append({"job title" : title , "comapany" : company , "location" : location})

# # pd.DataFrame(jobs).to_csv("job Scraper/jobs.csv" , index = False)
# with open("Job Scraper/jobs.json", "w", encoding="utf-8") as f:
#     json.dump(jobs, f, indent=4, ensure_ascii=False)
# print(f"Saved {len(jobs)} jobs to jobs.csv")