from flask import Flask, render_template, request, make_response
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    weather_info = "Danes je zelo lep dan"
    current_time = datetime.datetime.now()
    time = current_time.strftime('%H:%M:%S')
    return render_template("index.html", weather_info=weather_info, time=time)

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        name = request.cookies.get("name")
        return render_template("about.html", name=name)
    elif request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        print(name)
        print(email)
        print(message)

        response = make_response(render_template("success.html"))
        response.set_cookie("name", name)
        return response


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
