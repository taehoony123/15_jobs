from flask import Flask, render_template, request
# search_naver 함수를 get_naver_jobs라는 별명으로 가져옵니다.
from scrapper import search_ai_news, search_naver as get_naver_jobs

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    # keyword가 없을 경우를 대비한 예외 처리
    if not keyword:
        return "키워드를 입력해주세요."
    jobs = search_ai_news(keyword, 1)
    return render_template("search.html", jobs=enumerate(jobs), keyword=keyword)

@app.route("/search_naver")
def search_naver():
    keyword = request.args.get("keyword")
    if not keyword:
        return "키워드를 입력해주세요."
    
    # 별명(get_naver_jobs)을 사용하여 호출함으로써 TypeError 해결!
    jobs = get_naver_jobs(keyword, 1)
    return render_template("search.html", jobs=enumerate(jobs), keyword=keyword)

if __name__ == "__main__":
    app.run(debug=True)