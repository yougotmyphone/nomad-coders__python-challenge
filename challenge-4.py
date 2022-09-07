from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        results = []
        soup = BeautifulSoup(request.text, "html.parser")
        # write your ✨magical✨ code here
        term = "python"
        pages = soup.find_all('tr')
        for page in pages:
            company_and_positions = page.find_all(
                'td', class_="company_and_position")
            for company_and_position in company_and_positions:

                companys = company_and_position.find_all('h3')
                for company in companys:
                    company = company.string
                    company = company.replace("\n", "")
                  
                jobs = company_and_position.find_all('h2')
                for job in jobs:
                    job = job.string
                    job = job.replace("\n", "")
                  
                anchors = company_and_position.find_all('a')
                for anchor in anchors:
                    link = anchor['href']
                    if not link.startswith("https://"):
                        link = f"https://{link}"
                job_data = {'company': company, 'job': job, 'link': link}
                results.append(job_data)
              
        results.pop(0)
        for result in results:
            print(result)
    else:
        print("Can't get jobs.")


extract_jobs("rust")