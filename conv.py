import requests
import json
def find_rate(ff):
	response=requests.get("https://api.exchangeratesapi.io/latest")
	data =response.json()
	list_conv=[]
	dict_conv={}
	for dt in data["rates"]:
		list_conv.append(dt)

	for key,val in data["rates"].items():
		dict_conv[key]=val
	return(dict_conv[ff]*3232.87)


print(find_rate("INR"))