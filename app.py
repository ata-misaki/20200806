# Flaskからインポートしてflaskを使えるようにする
from flask import Flask, render_template
import sqlite3

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

@app.route("/anime")
def anime():
    return render_template("anime.html") 



@app.route("/weather")
def weather():
    py_weather = "晴れ"
    return render_template("weather.html" , name = py_weather)
    
@app.route("/dbtest")
def dbtest():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    # 課題１ SQL文を書いてスタッフ1名の情報を取得
    c.execute("SELECT id,name,age,adress FROM staff WHERE id = 1" )

    staff_info = c.fetchone()
    c.close()
    print(staff_info[0])



    #課題２ 新たなHTMLを作成し、１で取得したスタッフの情報をそれぞれ表示する

    # return render_template("index.html" ,id = staff_info[0] ,name = staff_info[1] ,age = staff_info[2] , adress = staff_info[3])
    return render_template("index.html" ,list = staff_info)

if __name__ == "__main__":
    app.run(debug = True)








if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します
    app.run(debug=True)