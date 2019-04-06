from flask import *
from databike import all_bike
from bson.objectid import ObjectId
app = Flask(__name__)
@app.route('/new_bike',methods=["GET","POST"])
def update():
  if request.method =='GET':
    return render_template('bikeapp.html')
  elif request.method == 'POST':
    form = request.form
    bike_model=(form["input_Model"])
    bike_dailyfee=(form["input_Daily_Fee"])
    bike_image=(form["input_Image"])
    bike_year=(form["input_Year"])
    
    new_bike={
      
        "Model":bike_model,
        "Daily_Fee":bike_dailyfee,
        "Image":bike_image,
        "Year":bike_year,
        
      
    }
    all_bike.insert_one(new_bike)
    print(new_bike)

    return redirect('/new_bike')
if __name__ == '__main__':
  app.run(debug=True)