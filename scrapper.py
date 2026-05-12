import requests
from bs4 import BeautifulSoup

def search_incruit(keyword,pages):

    #1. 페이지 번호를 0, 30, 60, 90, 120으로 변경하여 5페이지까지 크롤링
    for i in range(pages):
        jobs = []
        page = i * 30
        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}"

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find_all("li", class_="c_col")

        #2. 각 페이지에서 회사명, 공고명, 지역, 경력, 공고 링크를 추출하여 jobs 리스트에 저장
        for li in lis:
            company = li.find("a", class_="cpname").text.strip()
            print(company)

            title = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text.strip()
            print(title)

            location = li.find("div", class_="cell_mid").find("div", class_="cl_md").find_all("span")[0].text.strip()
            print(location)

            career = li.find("div", class_="cell_mid").find("div", class_="cl_md").find_all("span")[1].text.strip()
            print(career)

            link = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").get("href")
            print(link)

            job_data = {
                "company": company,
                "title": title,
                "location": location,
                "career": career,
                "link": link
            }
            jobs.append(job_data)

        return jobs
    
def search_saramin(keyword,pages):

    #1. 페이지 번호를 0, 30, 60, 90, 120으로 변경하여 5페이지까지 크롤링
    for i in range(pages):
        jobs = []
        page = i * 30
        url = f"https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=recently&searchword={keyword}&recruitPage={i+1}&recruitSort=relation&recruitPageCount=40&inner_com_type=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&show_applied=&quick_apply=&except_read=&ai_head_hunting="
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find_all("li", class_="c_col")

        #2. 각 페이지에서 회사명, 공고명, 지역, 경력, 공고 링크를 추출하여 jobs 리스트에 저장
        for li in lis:
            company = li.find("a", class_="cpname").text.strip()
            print(company)

            title = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text.strip()
            print(title)

            location = li.find("div", class_="cell_mid").find("div", class_="cl_md").find_all("span")[0].text.strip()
            print(location)

            career = li.find("div", class_="cell_mid").find("div", class_="cl_md").find_all("span")[1].text.strip()
            print(career)

            link = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").get("href")
            print(link)

            job_data = {
                "company": company,
                "title": title,
                "location": location,
                "career": career,
                "link": link
            }
            jobs.append(job_data)

        return jobs



keyword = "파이썬"
url = f"https://www.jobkorea.co.kr/Search/?stext={keyword}&tabType=recruit"
response = requests.get(url)
#print(response.status_code)를 실행했을 때 출력되는 200은 클라이언트의 HTTP 요청이 서버에서 성공적으로 처리되었음(OK)을 의미
#print(response.status_code) 
