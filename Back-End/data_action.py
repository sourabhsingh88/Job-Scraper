# from selenium import webdriver 
# from selenium.webdriver.common.by import By
# import time
# import json
# from bs4 import BeautifulSoup
# import pandas as pd 
# from fastapi import APIRouter , Query

# router =  APIRouter(prefix="/jobs" , tags= ["|| JOBS ||"])

# # keyword = input("enter ob keyword")

# @router.get("")
# def scrapjobs(keyword: str = Query(..., description="Job keyword to search") ) : 
#     driver = webdriver.Chrome()
#     driver.get(f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={keyword}")
#     time.sleep(6)

#     soup = BeautifulSoup(driver.page_source , "html.parser")
#     driver.quit()

#     # EXTRACT JOB INFO 

#     jobs= []

#     for job in soup.find_all("li" , class_="clearfix job-bx wht-shd-bx") :
#         title = job.header.h2.a.text.strip()
#         company = job.find("h3" , class_="joblist-comp-name").text.strip()
#         # location = job.find("ul" , class_ = "top-jd-dti").li.text.strip() 
#         loc_tags = job.find("ul" , class_ = "top-jd-dti")
#         location = loc_tags.li.text.strip() if loc_tags else "not mentioned"  
#         jobs.append({"job_title" : title , "company" : company , "location" : location})

#     # pd.DataFrame(jobs).to_csv("job Scraper/jobs.csv" , index = False)
#     return jobs 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fastapi import APIRouter, Query
from bs4 import BeautifulSoup

router = APIRouter(prefix="/jobs", tags=["|| JOBS ||"])

@router.get("")
def scrapjobs(
    url: str = Query(..., description="Base URL with placeholders"),
    keyword: str = Query(..., description="Job keyword to search"),
    page: int = Query(1, description="Page number (1, 2, 3...)")
):
    """
    Example URL:
    https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={keyword}&sequence={page}
    
    Use {keyword} and {page} placeholders in the URL.
    """
    
    # Replace placeholders dynamically
    final_url = url.replace("{keyword}", keyword).replace("{page}", str(page))

    # Selenium options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    driver.get(final_url)

    # Wait until job cards load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "job-bx"))
    )

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    jobs = []
    for job in soup.find_all("li", class_="clearfix job-bx wht-shd-bx"):
        title = job.header.h2.a.text.strip() if job.header and job.header.h2 else "Not mentioned"
        company = job.find("h3", class_="joblist-comp-name").text.strip() if job.find("h3", class_="joblist-comp-name") else "Not mentioned"
        loc_tags = job.find("ul", class_="top-jd-dti")
        location = loc_tags.li.text.strip() if loc_tags and loc_tags.li else "Not mentioned"

        jobs.append({
            "job_title": title,
            "company": company,
            "location": location
        })

    return {
        "url_used": final_url,
        "keyword": keyword,
        "page": page,
        "total_results": len(jobs),
        "results": jobs
    }