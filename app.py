from flask import Flask, render_template, request , send_file
from scrapper import search_incruit
from scrapper import search_saramin
from file import save_to_csv


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")
   

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    jobs =search_incruit(keyword, 1)
    return render_template("search.html", jobs = enumerate(jobs) , keyword = keyword)

@app.route("/search_saramin")
def search_saramins():
    keyword = request.args.get("keyword")
    jobs =search_saramin(keyword, 1)
    return render_template("search.html", jobs = enumerate(jobs) , keyword = keyword)

@app.route("/file")
def file():
    keyword = request.args.get("keyword")
    jobs =search_incruit(keyword, 1)
    save_to_csv(jobs)
    return send_file("download.csv", as_attachment=True)

@app.route("/map")
def map():
    kakao_map_key = '8a3505b5c4d91ef386726ab00cbaf9cb'
    return render_template('map.html', kakao_map_key=kakao_map_key)

if __name__ == "__main__":
    app.run(debug=True)