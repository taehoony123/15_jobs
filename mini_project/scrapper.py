import requests
from bs4 import BeautifulSoup

def search_ai_news(keyword, pages):
    jobs = []
    for i in range(pages):
        # AI Times는 페이지당 20~30개씩 넘어가는 구조 확인 필요
        url = f"https://www.aitimes.kr/news/articleList.html?view_type=sm&page={i+1}&sc_word={keyword}&sc_order_by=C"
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find_all("div", class_="item")

        for li in lis: 
            try:
                # 안전하게 추출하기 위해 find 사용
                title_tag = li.find("a", class_="auto-valign")
                title = title_tag.text.strip() if title_tag else "제목 없음"
                
                job_data = {"title": title}
                jobs.append(job_data)
            except Exception as e:
                print(f"에러 발생: {e}")
    return jobs    

def search_naver(keyword, pages):
    jobs = []
    for i in range(pages):
        # 네이버 채용 검색은 start 파라미터가 1, 11, 21 순으로 나가는 경우가 많음
        start = i * 10 + 1
        url = f"https://search.naver.com/search.naver?display=10&start={start}&query={keyword}+채용"

        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
        }
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 네이버 검색 결과 영역 선택자 (실제 네이버 HTML 구조에 따라 수정 필요)
        lis = soup.select(".sds-comps-vertical-layout.sds-comps-full-layout.lmGnb8UjvgrZYI6Dm6J9") 

        for li in lis:
            sources = soup.select(".sds-comps-profile-info-title")
            print(sources)
            titles = soup.select(".fender-ui_228e3bd1.wutHBmrX5l7e8fdP5Jzu")
            print(titles)
            details = soup.select(".sds-comps-text-ellipsis-3")
            print(details)
            dates = soup.select(".sds-comps-text-weight-sm")
            print(dates)
            links = soup.select_one('a.fender-ui_228e3bd1.wutHBmrX5l7e8fdP5Jzu')
            print(links)
            job_data = {
                "sources": sources,
                "titles": titles,
                "details": details,
                "dates": dates,
                "link": links
                
            }
            jobs.append(job_data)
    return jobs