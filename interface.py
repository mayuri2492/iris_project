from flask import Flask,jsonify,request,render_template
import config
from utilities import MedicalInsurance


app = Flask(__name__)

@app.route("/")
def app_home():
    return "Welcome to api home"


@app.route("/predict_charges",methods = ["POST","GET"])
def get_insurance_charges():

    if request.method=="POST":
        data = request.form
        age = eval(data["age"])
        sex = data["sex"]
        bmi = eval(data["bmi"])
        children =eval(data["children"])
        smoker = data["smoker"]
        region = data["region"]     

        med_insurance =MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges = med_insurance.get_predicted_charges()

        return jsonify({"Result ": f"Medical Insurance charges {charges}"})

if __name__=="__main__":
    app.run(debug =True,port = config.PORT_NUMBER,host=config.HOST)
