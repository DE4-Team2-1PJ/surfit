from bs4 import BeautifulSoup
from selenium import webdriver
import time

jobs = []
# URL에 따른 카테고리 이름
category_to_name = {
    "develop/data": "데이터 엔지니어",
    "develop/data-science": "데이터 사이언티스트",
    "develop/bigdata-ai-ml": "머신러닝 엔지니어",
    "planning/biz-analyst": "비즈니스 분석가"
}
cat_key = category_to_name.keys()
driver = webdriver.Chrome(executable_path=r"C:\Users\User\Desktop\chromedriver-win64\chromedriver.exe")

for cat in cat_key:
    base_url = f"https://jobs.surfit.io/{cat}" 

    driver.get(base_url)
    time.sleep(1)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 스크롤하는 동작이 없으면 공고가 로드되지 않음
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    job_titles = soup.find_all('span', class_="post-title")
    #print(job_titles)
    for job in job_titles:
        job_info = {'title': job.get_text().strip()} # 공고 제목
        job_url = job.find_parent('a')['href']
        
        driver.get(job_url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # 공고제목 - title, 회사이름 - company_name, 공고주소 - detail_url, 이미지주소 - img_link, 
        # 등록일 - pub_date, 마감일 - end_date, 카테고리 - category_name, 기술스택 - stack
        # 지역 - region, 신입/경력 - career
        job_info['company_name'] = soup.select_one('#app > div.jobs > div > div > div > div > div.iTVFTT > div.zpulQ > div > div > span').get_text().strip()
        job_info['detail_url'] = job_url
        job_info['end_date'] = soup.select_one("#app > div.jobs > div > div > div > div > div.content-area.isNepE > div > div > ul > li:nth-child(3) > span.value").get_text().strip()
        job_info['platform_name'] = "Surfit"
        job_info['category_name'] = category_to_name[cat]
        
        stacks = soup.select_one("#app > div.jobs > div > div > div > div > div.content-area.isNepE > div > div > div.job-post-info > div:nth-child(2) > ul")
        if not stacks:
            job_info['stack'] = None
        else:
            stacks = stacks.find_all('li')
            job_info['stack'] = [stack.get_text().strip() for stack in stacks]
            
        region = soup.find("span", class_="location-text").get_text().strip()
        job_info['region'] = " ".join(region.split()[:2])  # 주소 텍스트에서 서울특별시 **구, 경기도 **시 까지만 저장
        job_info['career'] = soup.select_one("#app > div.jobs > div > div > div > div > div.content-area.isNepE > div > div > ul > li:nth-child(1) > span.value").get_text().strip()
        jobs.append(job_info)

driver.quit()

for job in jobs: # 결과 출력
    print(job)

