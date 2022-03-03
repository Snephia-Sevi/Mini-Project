
from flask import Flask , render_template,request
import numpy as np
import pickle 


filename = 'rfr.pkl'
regressor = pickle.load(open(filename, 'rb'))




app = Flask(__name__)






@app.route("/")
def home():
	return render_template('test.html')



@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    if request.method=='POST':
        
        data1 = float(request.form['pm2_5'])
        data2 = float(request.form['pm10'])
        data3 = float(request.form['no'])
        data4 = float(request.form['no2'])
        data5 = float(request.form['nox'])
        data6 = float(request.form['nh3'])
        data7 = float(request.form['co'])
        data8 = float(request.form['so2'])
        data9 = float(request.form['o3'])
        data10 = float(request.form['benzene'])
        data11 = float(request.form['toluene'])
        data12 = float(request.form['xylene'])

    if(data1==0 and data2==0 and data3==0 and data4==0 and data5==0 and data6==0 and data7==0 and data8==0
       and data9==0 and data10==0 and data11==0 and data12 == 0):
            
        nodata= "Enter Real Values!!!!"
        return render_template("result.html",prediction_result=nodata)
    else:        

        temp_array = temp_array + [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12]
        


        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data)[0])
        if(my_prediction > 0 and my_prediction < 51):
            str = "Air quality is Good"
        elif(my_prediction > 50 and my_prediction < 101):
            str= "Air quality is Satisfactory"
        elif(my_prediction > 100 and my_prediction < 201):
            str= "Air quality is Moderate"
        elif(my_prediction > 200 and my_prediction < 301):
            str= "Air quality is Poor"
        elif(my_prediction > 300 and my_prediction < 401):
            str= "Air quality is Very Poor"
        elif(my_prediction > 400 and my_prediction < 501):
            str= "Air quality is Severe"
        else:
            str= "Not valid AQI"


        
        
    return render_template("result.html",prediction_result=my_prediction , string = str)

if __name__== "__main__":
    app.run(debug=True)