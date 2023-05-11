from flask import Flask,render_template
flask_app=Flask(__name__)
@flask_app.route("/")
def Home():
    return render_template("Task1.html")
if __name__ =="__main__":
    flask_app.run(debug=True)