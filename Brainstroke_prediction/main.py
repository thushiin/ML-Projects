from flask import Flask,render_template,request
import pickle
model=open('brainstroke.pkl','rb')
mfile=pickle.load(model)


app=Flask(__name__)
@app.route('/')
def home():
       return render_template('index.html')
   
@app.route('/home')
def home1():
       return render_template('index.html')

@app.route('/about')
def about():
       return render_template('about.html')
   
@app.route('/service')
def service():
       return render_template('service.html')
   
@app.route('/team')
def team():
       return render_template('team.html')

@app.route('/contact')
def contact():
       return render_template('contact.html')
   
@app.route('/test')
def test():
       return render_template('testimonial.html')
   
@app.route('/appoin')
def appoin():
       return render_template('appointment.html')
   
@app.route('/brain')
def brain():
       return render_template('brainstrokeprediction.html')


@app.route('/predict',methods=['POST'])
def pred():
    if request.method=='POST':
        gender=request.form['gender']
        age=request.form['age']
        hypertension=request.form['hypertension']
        heartdisease=request.form['heartdisease']
        worktype=request.form['worktype']
        residencetype=request.form['residencetype']
        avg_glucose_level=float(request.form['avg_glucose_level'])
        bmi=float(request.form['bmi'])
        smoke=request.form['smoke']
        prediction=mfile.predict([[gender,age,hypertension,heartdisease,worktype,residencetype,avg_glucose_level,bmi,smoke]])
        if prediction==0:
            res='YOU ARE HEALTHY'
        else:
            res='Some issues detetcted, please consult'
        return render_template('brainstrokeprediction.html',output=res)
    
if __name__=='__main__':
    app.run(debug=True,port=5002)