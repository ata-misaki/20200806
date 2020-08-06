# Flaskからインポートしてflaskを使えるようにする
from flask import Flask, render_template

# appという名前でFlaskあぷりをつくっていくよ
app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "Hello World."

@app.route("/<name>")
def greet(name):
    return name + "さん、はろー！"

@app.route("/template")
def template():
    py_name = "あたあああああ"
    return render_template("index.html", name = py_name)









if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します
    app.run(debug=True)