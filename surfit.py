from bs4 import BeautifulSoup
from selenium import webdriver
import time

jobs = []
base_url = "https://jobs.surfit.io/develop/data" # 데이터 엔지니어 카테고리만 수집

driver = webdriver.Chrome(executable_path=r"C:\Users\User\Desktop\chromedriver-win64\chromedriver.exe")
driver.get(base_url)
time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 스크롤하는 동작이 없으면 공고가 로드되지 않음
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

job_titles = soup.find_all('span', class_="post-title")
print(job_titles)
for job in job_titles:
    job_info = {'title': job.get_text().strip()} # 공고 제목
    job_url = job.find_parent('a')['href']
    
    driver.get(job_url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # 공고제목 - title, 회사이름 - company_name, 공고주소 - detail_url, 이미지주소 - img_link, 등록일 - pub_date, 마감일 - end_date
    job_info['company_name'] = soup.select_one('#app > div.jobs > div > div > div > div > div.iTVFTT > div.zpulQ > div > div > span').get_text().strip()
    job_info['detail_url'] = job_url
    job_info['end_date'] = soup.select_one("#app > div.jobs > div > div > div > div > div.content-area.isNepE > div > div > ul > li:nth-child(3) > span.value").get_text().strip()
    job_info['platform_name'] = "Surfit"
    jobs.append(job_info)

driver.quit()

for job in jobs: # 결과 출력
    print(job)

