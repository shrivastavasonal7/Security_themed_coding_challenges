import requests
from bs4 import BeautifulSoup

URL = "https://pythonjobs.github.io/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="container")

# print(results.prettify())

'''
python_jobs = results.find_all(
    "h1", string=lambda text: "python" in text.lower()
)
'''
job_elements = results.find_all("div", class_="job")

for job_element in job_elements:
    title_element = job_element.find("h1")
    location_element = (job_element.find("span"))
    company_name = position_type = job_element.find_all("span")[3]
    position_type = job_element.find_all("span")[2]
    print(title_element.text.strip())
    print(location_element.text.strip())
    print(f"Company Name: {company_name.text.strip()}")
    print(f"Position Type: {position_type.text.strip()}")

    link_url = job_element.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")

    print()