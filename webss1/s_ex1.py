from flask import Flask,render_template
app = Flask(__name__)


@app.route('/bmi/<int:a>/<int:b>')
def BMI(b,a):
    doi=b/100
    BMI = a/doi**2
    if BMI<16:
        notify = "Ban suy dinh duong cmnr" 
    elif 16<BMI<18.5:
        notify = " Ban hoi gay nha :>"
    elif 18.5<BMI<25:
        notify = "Ban rat rat binh thuong"
    elif 25<BMI<30:
        notify = "Ban hoi phung phinh"
    else :
        notify = "Ban beo vailin"
    return render_template("s_ex1.html",
                            notify=notify,
                            BMI=BMI)
if __name__ == '__main__':
  app.run(debug=True)
 