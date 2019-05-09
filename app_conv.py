from flask import Flask,render_template,redirect,url_for,request
import requests
import json

app=Flask(__name__,template_folder='template')

@app.route("/")
def home():
	return(render_template("home.html"))

@app.route("/form",methods=["POST","GET"])
def form():
	return(render_template("form.html"))

@app.route("/about",methods=["POST","GET"])
def about():
	return(render_template("about.html"))

#@app.route("/success")
#def success(data):
#	return(render_template("success.html",data=data))

def find_rate(conv,price):
	response=requests.get("https://api.exchangeratesapi.io/latest")
	data =response.json()
	list_conv=[]
	dict_conv={}
	for dt in data["rates"]:
		list_conv.append(dt)

	for key,val in data["rates"].items():
		dict_conv[key]=val
	finalamt=dict_conv[conv]*price
	return(finalamt)
		
@app.route("/conversion",methods=["GET","POST"])
def weather():
	if(request.method=="POST"):
		rate= request.form["rate"]
		price= request.form["price"]
		rate= str(rate)
		price= float(price)
		amount= find_rate(rate,price)
	return render_template("success.html",rate=rate,price=price,amount=amount)


if __name__=="__main__":
	app.run(debug=True)

"""app1=wea(str(city))
		data = app1.find_data()
	return render_template("success.html",data=data)"""
