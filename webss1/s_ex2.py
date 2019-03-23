from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    Users = {
        "huyanh":{
        "name": "Nguyen Huy Anh",
		"age" : 21},
        "duc":{
        "name":"Pham Minh Duc",
        "age": 21}
    }
    if username in Users:
        username = Users[username]
        return render_template("s_ex2.html",username=username)
    else:
        return "User not found"
if __name__ == '__main__':
    app.run(debug=True)
 