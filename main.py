# # https://replit.com/

# import requests

# indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

# print(indeed_result.text)



# import requests
# from bs4 import BeautifulSoup


# indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

# indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

# pagination = indeed_soup.find("div", {"class":"pagination"})

# pages = pagination.find_all('a')
# spans = []
# for page in pages:
#   spans.append(page.find("span"))
# print(spans[0:-1])


import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})


# for page in pages:
#   print(page.find("span"))

links = pagination.find_all('a')
pages = []
for link in links[:-1]:
    # pages.append(link.find("span").string)
    pages.append(int(link.string))
# print(pages[-1])

max_page = pages[-1]



  