from flask import Flask, render_template
app = Flask(__name__)
@app.route('/about_me')
def about_me():
   about_mes=[
       {"Name":"Huy Anh",
       "Work":"Sinh Vien",
       "Hobbies":"have sex",
       "School":"MTA",
       "My_Dog":"Duc Pham",
       }
   ]
   return render_template("btvnweb.html",
                            about_mes=about_mes)
if __name__ == '__main__':
  app.run(debug=True)