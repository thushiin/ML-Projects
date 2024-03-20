from flask import Flask, render_template,request
import pickle
model=open(r'/Users/thushinbhanu/Desktop/heartml/heart.pkl','rb')
mfile=pickle.load(model)

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('heart.html')

@app.route('/predict', methods=['post'])
def pred():
    if request.method=='POST':
        age=int(request.form['age'])
        sex=int(request.form['sex'])
        chestpain=int(request.form['chestpain'])
        rbp=int(request.form['rbp'])
        chol=int(request.form['chol'])
        ecg=int(request.form['ecg'])
        hr=int(request.form['hr'])
        oldp=float(request.form['oldp'])
        stslope=int(request.form['stslope'])
        prediction=mfile.predict([[age,sex,chestpain,rbp,chol,ecg,hr,oldp,stslope]])
        print(prediction)
        if prediction==0:
            res='YOU ARE HEALTHY'
        else:
            res='Some issues detetcted, please consult'
        return render_template('heart.html',output=res)
    
    
    


if __name__=='__main__':
    app.run(debug=True,port=5001)