#f1482071c1585824e5dad9813475caff
 
#https://api.openweathermap.org/data/2.5/weather
 
from flask import Flask,render_template,request
import requests
app =Flask(__name__)
#this will rander data from index.html
@app.route('/') 
def homepage():
    return render_template('index.html')

@app.route('/weatherapp',methods=['POST','get'])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param={
        'q':request.form.get("city"),
        'appid':request.form.get('appid'),
        'unit':request.form.get("units")
    }
    responce=requests.get(url,params=param)
    data=responce.json()
  
    return f"Data{data} cordinate {data.get('coord')}"
    



if __name__=='__main__':
    app.run(host='0.0.0.0')