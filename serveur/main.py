import json
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/temperature')
def temperature():
    with open('data.json') as json_data:
        data_dict = json.load(json_data)
        data_str = json.dumps(data_dict)
    return data_str
    

if __name__ == '__main__':
  app.run(debug=True)