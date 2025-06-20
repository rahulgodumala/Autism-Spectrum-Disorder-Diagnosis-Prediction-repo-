from flask import Flask, render_template, url_for, request, redirect, flash
from tensorflow.keras.models import load_model
import numpy as np
import webbrowser
import warnings
import pickle
warnings.filterwarnings("ignore")


# from flask import Flask, render_template, request
import pickle
# import numpy as np
# import webbrowser


model = pickle.load(open('RandomForest.pkl', 'rb'))
model2 = pickle.load(open('svm.pkl', 'rb'))

app = Flask(__name__)
app.secret_key = '12344321'  # Needed for flashing messages

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password!', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')





@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        A1 = int(request.form['dls'])
        A2 = int(request.form['dms'])
        A3 = int(request.form['dcols'])
        A4 = int(request.form['hiib'])
        A5 = int(request.form['esd'])
        A6 = int(request.form['ueash'])
        A7 = int(request.form['gi'])
        A8 = int(request.form['umer'])
        A9 = int(request.form['asew'])
        A10 = int(request.form['mfte'])

        data = np.array([[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10]])
        my_prediction = model.predict(data)
        print(my_prediction)

        return render_template('result.html', prediction=my_prediction)
        
@app.route('/charts')
def charts():
    return render_template('charts.html')


if __name__ == '__main__':
    app.run(port='5000',debug=True)