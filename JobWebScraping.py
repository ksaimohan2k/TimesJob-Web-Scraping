from bs4 import BeautifulSoup
import requests
import time

unfamiliar_skill = input("Enter your Unfamiliar Skills >  ")
print("Filtering Out ......")


def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
                             '=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all("li", class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', 'sim-posted').span.text
        if "few" in published_date:
            company = job.find("h3", class_='joblist-comp-name').text.replace(" ", '')
            skills = job.find('span', 'srp-skills').text.replace(" ", "")
            job_link = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts{index}.txt', 'w') as f:
                    f.write(f"Company Name    : {company.strip()}")
                    f.write(f"Skills Required : {skills.strip()}")
                    f.write(f"Job Link: {job_link.strip()}", )


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"waiting {time_wait} seconds......")
        time.sleep(time_wait * 60)
