from flask import Flask,request,render_template,jsonify,url_for
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

model = pickle.load(open('ML_Project_LogisticRegression_Diabetes_prediction\model\model.pkl','rb'))
scaler = pickle.load(open('ML_Project_LogisticRegression_Diabetes_prediction\model\scaler.pkl','rb'))


@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/form',methods = ['GET','POST'])
def form_page():
    if (request.method == 'POST'):
        Pregnancies = int(request.form['Pregnancies'])
        if Pregnancies == None:
            Pregnancies = 0
        Glucose = int(request.form['Glucose'])
        BloodPressure = int(request.form['BloodPressure'])
        SkinThickness = int(request.form['SkinThickness'])
        Insulin = int(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = int(request.form['Age'])

        feature_names = [[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
        scaled_data = scaler.transform(feature_names)
        result = model.predict(scaled_data)
        if result[0] == 0:
            result = "you dont have Diabetes Problem..."
        else:
            result = "you have a Diabetes Problem..."
        return render_template('form.html', result = result)
    
    else:
        return render_template('form.html')
    
    
if __name__ == "__main__":

    app.run(debug = True)
