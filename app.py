from flask import Flask,request,render_template,jsonify,url_for
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

model = pickle.load(open('ML_Project_LogisticRegression_Diabetes_prediction\model\model.pkl','rb'))
scaler = pickle.load(open('ML_Project_LogisticRegression_Diabetes_prediction\model\scaler.pkl','rb'))


@app.route('/')
def home_page():
    return render_template("ML_Project_LogisticRegression_Diabetes_prediction\templates\index.html")


if __name__ == "__main__":

    app.run(debug = True)
