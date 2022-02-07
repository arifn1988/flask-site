from flask import Flask,render_template, request
import urllib
import xml.etree.ElementTree as ET
import requests
import validators

#https://www.youtube.com/watch?v=DhUpxWjOhME

app = Flask(__name__)

@app.route("/" , methods=['POST','GET'])
def hello_world():

	link = request.form.get('fname')

	if link:
		if not valid_url(link):
			return render_template('home.html',invalid_url=True,error='invalid url')
		elif not check_url(link):
			return render_template('home.html' ,invalid_url=True,error='not working link')
		else:
			news= readrss(link)
			if news:
				return render_template('home.html',news=news)
			else:
				return render_template('home.html',invalid_url=True,error='not a xml file')
	else:
		return render_template('home.html')

def valid_url(url):
	if validators.url(url):
		return True  
	else:
		return False

def check_url(url):
	try:
	 request=requests.head(url, allow_redirects=True).status_code == 200
	except:
		print('error')
		request=False

	return request

def readrss(url):
	file = urllib.request.urlopen(url).read()
	
	try:
		tree= ET.fromstring(file)[0]
	except:
		return False

	feed=[]

	for root in tree:
		newsitem={}
		for item in root:
			newsitem[item.tag]=item.text

		feed.append(newsitem)

	return feed

if __name__=='__main__':
	app.run(debug=True)