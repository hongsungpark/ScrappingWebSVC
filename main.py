from flask import Flask

app = Flask("ScrappingWebSVC")

@app.route("/")
def home():
  return "Hello! Welcome to mi casa!"

@app.route("/contact")
def potato():
  return "Contact me!"

app.run(host="0.0.0.0")