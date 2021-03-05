from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("ScrappingWebSVC")

#@는 데코레이터. 바로 아래에 있는 '함수'를 실행하게 함
@app.route("/")
def home():
  return render_template("potato.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    jobs = get_jobs(word)
  else:
    return redirect("/")
  return render_template("report.html", searchingBy=word)  


app.run(host="0.0.0.0")
