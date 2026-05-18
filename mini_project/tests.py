import requests
from bs4 import BeautifulSoup


url = "https://search.naver.com/search.naver?nso=&page=3&query=손흥민&sm=tab_pge&ssc=tab.ur.all&start=16"
print(url)
#{'User-Agent': 'python-requests/2.33.1', 'Accept-Encoding': 'gzip, deflate, zstd', 'Accept': '*/*', 'Connection': 'keep-alive'}
#User-Agent 헤더 지정
headers= {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers) # GET방식으로 네이버 URL에 요청
html = req.text #HTML 내용을 텍스트로 가져옴
# print(html) # 네이버 HTML 내용을 텍스트로 확인
# print(req.request.headers)
soup = BeautifulSoup(html,"html.parser")




# #class 앞에서 '.' , id 앞은 '#'
# titles = soup.select(".fender-ui_228e3bd1.wutHBmrX5l7e8fdP5Jzu")

# for title in titles:
#     print(title.text)
#     print()

# details = soup.select(".sds-comps-text-ellipsis-3")
# for detail in details:
#     print(detail.text)
#     print()

dates = soup.select(".sds-comps-text-weight-sm")
for date in dates:
    # '네이버뉴스'라는 글자가 포함된 링크는 건너뛰고 '시간'만 출력
    if "전" in date.get_text():
        print(date.text)
        print()



# sources = soup.select(".sds-comps-profile-info-title")

# for source in sources:
#     print(source.text)
# print()


# links = soup.select_one('a.fender-ui_228e3bd1.wutHBmrX5l7e8fdP5Jzu')
# for link in links:
#     print(links.get('href')) 
# print()


import requests
from bs4 import BeautifulSoup

def search_ai_news(keyword, pages):
    jobs = []
    #1. 페이지 번호를 0, 30, 60, 90, 120으로 변경하여 5페이지까지 크롤링
    for i in range(pages):
        
        page = i * 30
        url = f"https://www.aitimes.kr/news/articleList.html?view_type=sm&page={1}&sc_word={keyword}&sc_order_by=C"


        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(url,headers=header)
        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find_all("div", class_="item")

        #2. 각 페이지에서 회사명, 공고명, 지역, 경력, 공고 링크를 추출하여 jobs 리스트에 저장
        for li in lis: 
            title = li.find("a", class_="auto-valign").find("span")[1].text.strip()
            print(title)

            job_data = {
                "title": title
            }
            jobs.append(job_data)

    return jobs    

def search_naver(keyword,pages):
    jobs = []
    #1. 페이지 번호를 0, 30, 60, 90, 120으로 변경하여 5페이지까지 크롤링
    for i in range(pages):
        
        page = i + 1
        url = f"https://search.naver.com/search.naver?nso=&page={page}&query={keyword}&sm=tab_pge&ssc=tab.ur.all&start=16"

        headers= {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
        }
        response = requests.get(url,header=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find_all("div", class_="item_recruit")

        #2. 각 페이지에서 회사명, 공고명, 지역, 경력, 공고 링크를 추출하여 jobs 리스트에 저장
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

