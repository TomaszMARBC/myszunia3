from flask import Flask, render_template, redirect, url_for, send_from_directory
#from flask import Bootstrap5


app = Flask(__name__)
# app.config["SECRET_KEY"] = "Super_secret_key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/download')
def download():
    return send_from_directory('static', 'files/test.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
