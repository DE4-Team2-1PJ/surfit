# surfit
Surfit의 채용공고 크롤링
- 각 카테고리에 해당하는 URL에서 공고 제목 수집
    - **데이터 엔지니어, 데이터 사이언티스트, 머신러닝 엔지니어, 비즈니스 분석가** 총 4개
    - 추후 카테고리 통일해서 재분류 예정
- 공고 제목으로 링크 들어가서 회사 이름, 공고 주소, 마감일, 스택, 지역, 신입/경력 수집
    - 지역의 경우 **"100% 원격근무"**가 존재

### 크롤링 결과
{'title': 'AI Core Researcher (경력)', 'company_name': '달파(Dalpha)', 'detail_url': 'https://jobs.surfit.io/post/68705', 'end_date': '채용시까지', 'platform_name': 'Surfit', 'category_name': '데이터 엔지니어', 'stack': ['Python', 'GitHub', 'Docker', 'Linux', 'Pytorch', 'Terraform', 'AWS', 'K8S'], 'region': '서울특별시 관 악구', 'career': '3년 이상'}
{'title': 'AI Engineer & Data Scientist', 'company_name': 'Nimbyx(Evident)', 'detail_url': 'https://jobs.surfit.io/post/80897', 'end_date': '채용시까지', 'platform_name': 'Surfit', 'category_name': '데이터 엔지니어', 'stack': None, 'region': '100% 원격근무', 'career': '경력직'}
{'title': 'AI Engineer & Data Scientist', 'company_name': 'Nimbyx(Evident)', 'detail_url': 'https://jobs.surfit.io/post/80897', 'end_date': '채용시까지', 'platform_name': 'Surfit', 'category_name': '데이터 사이언티스트', 'stack': None, 'region': '100% 원격근무', 'career': '경력직'}
{'title': 'AI Core Researcher (경력)', 'company_name': '달파(Dalpha)', 'detail_url': 'https://jobs.surfit.io/post/68705', 'end_date': '채용시까지', 'platform_name': 'Surfit', 'category_name': '머신러닝 엔지니어', 'stack': ['Python', 'GitHub', 'Docker', 'Linux', 'Pytorch', 'Terraform', 'AWS', 'K8S'], 'region': '서울특별시  관악구', 'career': '3년 이상'}
{'title': 'AI Engineer & Data Scientist', 'company_name': 'Nimbyx(Evident)', 'detail_url': 'https://jobs.surfit.io/post/80897', 'end_date': '채용시까지', 'platform_name': 'Surfit', 'category_name': '머신러닝 엔지니어', 'stack': None, 'region': '100% 원격근무', 'career': '경력직'}
{'title': '의료영상 AI Engineer(Junior)', 'company_name': '웨이센', 'detail_url': 'https://jobs.surfit.io/post/111135', 'end_date': '채용시까지', 'platform_name': 'Surfit', 'category_name': '머신러닝 엔지니어', 'stack': ['C', 'Python', 'Java', 'Scipy', 'Pandas', 'NumPy', 'TensorFlow', 'Pytorch'], 'region': '서울특별시 강남구', 'career': '경력 무관'}
{'title': '의료영상 AI Engineer(Senior)', 'company_name': '웨이센', 'detail_url': 'https://jobs.surfit.io/post/111260', 'end_date': '채용시까지', 'platform_name': 'Surfit', 'category_name': '머신러닝 엔지니어', 'stack': ['Python', 'TensorFlow', 'Pytorch', 'Caffe'], 'region': '서울특별시 강남구', 'career': '5년 이상'}      
{'title': '[flex] HR Partner', 'company_name': '플렉스(flex)', 'detail_url': 'https://jobs.surfit.io/post/68205', 'end_date': '채용시까지', 'platform_name': 'Surfit', 'category_name': '비즈니스 분석가', 'stack': ['HR', 'HRM', 'HRD', 'HRIS', '인사', '인사컨설팅', 'HR 운영'], 'region': '경기도 성남시', 'career': '3년 이상'}
