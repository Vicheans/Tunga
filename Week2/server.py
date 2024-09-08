from flask import Flask, make_response, render_template, request, url_for # type: ignore
app = Flask(__name__)



# "/" route
@app.route("/")
def hello_world():
    return render_template("index.html")


# "/about" route
@app.route("/about")
def about():
    return "About Page"


@app.route("/post/<int:post_id>")
def view_post(post_id):
    return f"Viewing Blog #{post_id}"


@app.route("/user/<string:username>")
def user_profile(username):
    url = url_for("user_profile", username="alice")
    return f"Viewing User #{username, url}"

@app.route("/user/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def user_methods(user_id):
    if request.method == "GET":
        return "MADE GET"
    elif request.method == "PUT":
        return "MADE PUT"
    elif request.method == "DELETE":
        return "MADE DELETE"
    
@app.route("/search")
def search():
    search_word = request.args.get("key", "")

@app.route("/json_data", methods=["POST"])
def json_data():
    data = request.json


@app.route("/upload_file", methods=["POST"])
def upload_file():
    if "file" in request.files:
        file = request.files["file"]


@app.route("/cookies")
def cookies():
    user_id = request.cookies.get("user_id")

@app.route("/set_cookie")
def set_cookie():
    response = "Cookie created"
    res = make_response(response)
    res.set_cookie("user_id", "123")
    res.headers["Custom-Header"] = "Custom Value"
    return res

if __name__ == "__main__":
    app.run()