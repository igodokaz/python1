
import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL= f"https://www.indeed.com/jobs?q=python&start={LIMIT}&vjk=37342e86d2a94982"

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:

        pages.append(link.string)

    max_page = pages[-1]
    return max_page

# def extract_indeed_jobs(last_page):
#     jobs = []
#     # for page in range(last_page):
#         # print(f"&start={page * LIMIT}")
#     result = requests.get(f"{URL}&start={0*LIMIT}")
#     soup = BeautifulSoup(result.text, "html.parser")
#     results = soup.find_all("div",{"class":"job_seen_beacon"})
#     for result in results:
#         title = result.find("td",{"class":"resultContent"})
#         print(title.find("span").string)
#     return jobs

# def extract_indeed_jobs(last_page):
#     jobs = []
#     # for page in range(last_page):
#         # print(f"&start={page * LIMIT}")
#     result = requests.get(f"{URL}&start={0*LIMIT}")
#     soup = BeautifulSoup(result.text, "html.parser")
#     results = soup.find_all("div",{"class":"job_seen_beacon"})
#     for result in results:
#         title = result.find("div",{"class":"heading4"}).find("span").string
#         if title == "new":
#             pass
#         company = result.find("span", {"class":"companyName"}).string
#         print(title, company)
#     return jobs

def extract_job(html):
        title = html.find("div",{"class":"heading4"}).find("span").string
        if title == "new":
            pass # ?????????????
        company = html.find("span", {"class":"companyName"}).string
        location = html.find("div", {"class":"companyLocation"}).string
        return {'title':title,'company':company,'location':location}




def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    #     print(f"Scrapping page {page}")
        # print(f"&start={page * LIMIT}")
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div",{"class":"job_seen_beacon"})
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs


