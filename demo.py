from flask import Flask,render_template, request
import pandas as pd
import numpy as np
app = Flask(__name__)

@app.route("/")
def index():
	age = {"Sam": 20, "Ken": 30, "Grace": 23, "Peter": 29}
	return render_template("index.html", ages=age)

@app.route('/data_analysis')
def data_analysis():
	x = pd.DataFrame(np.random.randn(5, 6), columns=list('ABCDEF'))
	return render_template("data_analysis.html",  data=x.to_html())

@app.route('/data_frame_analysis')
def data_frame_analysis():
	data = [['Peter',22,3.2,63.2],['John',21,4.6,67.8],['Steve',25,5.2,81.9],['Jane',20,4.4,73.2],['Paige',27,4.1,70.5]]
	df=pd.DataFrame(data,columns=['Name','Age','Height','Weight'])
	desc=df.describe(include='all')
	return render_template("data_frame_analysis.html",  data_frame=df.to_html(), stat=desc.to_html())

@app.route('/external_data_frame_analysis')
def external_data_frame_analysis():
	df = pd.read_csv("train.csv")
	return render_template("external_data_frame_analysis.html",  data=df.head(5).to_html())

if __name__ == "__main__":
    app.run()