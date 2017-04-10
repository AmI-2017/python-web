from flask import Flask, url_for, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "MUVETSOssIHYJGeeNM3"


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/secret.html', methods=['POST'])
def hello():
    username = request.form['username']
    value = len(username)

    session['username'] = username
    session['value'] = value

    if value==0:
        return render_template("error.html")
    else:
        return render_template("secret.html",
                           username=username, secret_value=value)


@app.route("/secret_data.html")
def data():
    secretdata = [ 1, 1, 2, 3, 5, 8, 13, 21 ] # FAKE DATA -- should be user dependent
    return render_template("data.html", username=session['username'], secretdata=secretdata)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
