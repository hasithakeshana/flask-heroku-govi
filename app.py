from flask import Flask,jsonify,request
import pickle
import pandas as pd 

app = Flask(__name__)

@app.route('/')
def main():
    return ''


@app.route('/getBeansYield', methods=['POST'])
def getBeans():
        
        # user inputs
        data = request.get_json();

        temperature = data.get('temperature', '');
        humidity = data.get('humidity', '');
        rainfall = data.get('rainfall', '');
        wind = data.get('wind', '');

        # pickle file name
        file_name = 'beans-statistical.pkl'

        # load the pickle file 
        loaded_model = pickle.load(open(file_name,'rb'));

        # forecast using the model
        out = loaded_model.predict([[temperature,humidity,rainfall,wind]]);


        print(out[0])

        # prediction = loaded_model.predict(d)
        listtype = out.tolist(); 

        # convert to jsons
        return {
        "vegetable-code" : "TY-BEANS",
        "vegetable-name" : "beans",
        "area" : "nuwaraeliya",
        "yield-output": out[0],
        "status-code": 200
        }

 

@app.route('/getCarrotYield', methods=['POST'])
def getCarrot():
        
        # user inputs
        data = request.get_json();

        temperature = data.get('temperature', '');
        humidity = data.get('humidity', '');
        rainfall = data.get('rainfall', '');
        wind = data.get('wind', '');

        # pickle file name
        file_name = 'carrot-statistical.pkl'

        # load the pickle file 
        loaded_model = pickle.load(open(file_name,'rb'));

        # forecast using the model
        out = loaded_model.predict([[temperature,humidity,rainfall,wind]]);


        print(out[0])

        # prediction = loaded_model.predict(d)
        listtype = out.tolist(); 

        # convert to jsons
        return {
        "vegetable-code" : "TY-CARROT",
        "vegetable-name" : "carrot",
        "area" : "nuwaraeliya",
        "yield-output": out[0],
        "status-code": 200
        }
       

@app.route('/getTomatoYield', methods=['POST'])
def getTomato():
        
        # user inputs
        data = request.get_json();

        temperature = data.get('temperature', '');
        humidity = data.get('humidity', '');
        rainfall = data.get('rainfall', '');
        wind = data.get('wind', '');

        # pickle file name
        file_name = 'tomato-statistical.pkl'

        # load the pickle file 
        loaded_model = pickle.load(open(file_name,'rb'));

        # forecast using the model
        out = loaded_model.predict([[temperature,humidity,rainfall,wind]]);


        print(out[0])

        # prediction = loaded_model.predict(d)
        listtype = out.tolist(); 

        # convert to jsons
        return {
        "vegetable-code" : "TY-TOMATO",
        "vegetable-name" : "tomato",
        "area" : "nuwaraeliya",
        "yield-output": out[0],
        "status-code": 200
        }


@app.route('/getCabbageYield', methods=['POST'])
def getCabbage():
        
        # user inputs
        data = request.get_json();

        temperature = data.get('temperature', '');
        humidity = data.get('humidity', '');
        rainfall = data.get('rainfall', '');
        wind = data.get('wind', '');

        # pickle file name
        file_name = 'cabbage-statistical.pkl'

        # load the pickle file 
        loaded_model = pickle.load(open(file_name,'rb'));

        # forecast using the model
        out = loaded_model.predict([[temperature,humidity,rainfall,wind]]);


        print(out[0])

        # prediction = loaded_model.predict(d)
        listtype = out.tolist(); 

        # convert to jsons
        return {
        "vegetable-code" : "TY-CABBAGE",
        "vegetable-name" : "cabbage",
        "area" : "nuwaraeliya",
        "yield-output": out[0],
        "status-code": 200
        }


@app.route('/getPotatoYield', methods=['POST'])
def getPotato():
        
        # user inputs
        data = request.get_json();

        temperature = data.get('temperature', '');
        humidity = data.get('humidity', '');
        rainfall = data.get('rainfall', '');
        wind = data.get('wind', '');

        # pickle file name
        file_name = 'potato-statistical.pkl'

        # load the pickle file 
        loaded_model = pickle.load(open(file_name,'rb'));

        # forecast using the model
        out = loaded_model.predict([[temperature,humidity,rainfall,wind]]);


        print(out[0])

        # prediction = loaded_model.predict(d)
        listtype = out.tolist(); 

        # convert to jsons
        return {
        "vegetable-code" : "TY-POTATO",
        "vegetable-name" : "potato",
        "area" : "nuwaraeliya",
        "yield-output": out[0],
        "status-code": 200
        }



@app.route('/getBeetrootYield', methods=['POST'])
def getBeetroot():
        
        # user inputs
        data = request.get_json();

        temperature = data.get('temperature', '');
        humidity = data.get('humidity', '');
        rainfall = data.get('rainfall', '');
        wind = data.get('wind', '');

        # pickle file name
        file_name = 'beetroot-statistical.pkl'

        # load the pickle file 
        loaded_model = pickle.load(open(file_name,'rb'));

        # forecast using the model
        out = loaded_model.predict([[temperature,humidity,rainfall,wind]]);


        print(out[0])

        # prediction = loaded_model.predict(d)
        listtype = out.tolist(); 

        # convert to jsons
        return {
        "vegetable-code" : "TY-BEETROOT",
        "vegetable-name" : "beetroot",
        "area" : "nuwaraeliya",
        "yield-output": out[0],
        "status-code": 200
        }



@app.route('/getGraphsBeansYield', methods=['POST'])
def getMonthly(): 

        months = [868, 902, 936, 730, 921, 650]

        # convert to jsons
        return {
        "vegetable-code" : "TY-Beans",
        "vegetable-name" : "beans",
        "area" : "nuwaraeliya",
        "yield-output": months,
        "status-code": 200
        }  

 
@app.route('/getGraphsBeetrootYield', methods=['POST'])
def getMonthlyBeetroot(): 

        months = [560, 750, 1234, 1567, 650, 1800]

        # convert to jsons
        return {
        "vegetable-code" : "TY-Beetroot",
        "vegetable-name" : "beetroot",
        "area" : "nuwaraeliya",
        "yield-output": months,
        "status-code": 200
        }             

 
@app.route('/getGraphsCabbageYield', methods=['POST'])
def getMonthlyCabbage(): 

        months = [950, 1234, 560, 450, 340, 540]

        # convert to jsons
        return {
        "vegetable-code" : "TY-Cabbage",
        "vegetable-name" : "cabbage",
        "area" : "nuwaraeliya",
        "yield-output": months,
        "status-code": 200
        } 


@app.route('/getGraphsCarrotYield', methods=['POST'])
def getMonthlyCarrot(): 

        months = [1902, 1915, 2182, 2150, 2235, 2123]

        # convert to jsons
        return {
        "vegetable-code" : "TY-Carrot",
        "vegetable-name" : "carrot",
        "area" : "nuwaraeliya",
        "yield-output": months,
        "status-code": 200
        } 




@app.route('/getGraphsPotatoYield', methods=['POST'])
def getMonthlyPotato(): 

        months = [1123, 1200, 980, 456, 678, 1245]

        # convert to jsons
        return {
        "vegetable-code" : "TY-Potato",
        "vegetable-name" : "potato",
        "area" : "nuwaraeliya",
        "yield-output": months,
        "status-code": 200
        } 


@app.route('/getGraphsTomatoYield', methods=['POST'])
def getMonthlyTomato(): 

        months = [1525, 1546, 1588, 1498, 1602, 2234]

        # convert to jsons
        return {
        "vegetable-code" : "TY-Tomato",
        "vegetable-name" : "tomato",
        "area" : "nuwaraeliya",
        "yield-output": months,
        "status-code": 200
        }                  


@app.route('/getGraphsTomatoPrice', methods=['POST'])
def getMonthlyPriceTomato(): 

        months = [155, 90, 84, 112, 134, 147]

        # convert to jsons
        return {
        "vegetable-code" : "TY-Tomato",
        "vegetable-name" : "tomato",
        "area" : "nuwaraeliya",
        "price-output": months,
        "status-code": 200
        }   



@app.route('/getGraphsBeansPrice', methods=['POST'])
def getMonthlyPricegraph(): 

        months = [220, 245, 195, 134, 120, 95]

        # convert to jsons
        return {
        "vegetable-code" : "TY-Beans",
        "vegetable-name" : "beans",
        "area" : "nuwaraeliya",
        "yield-output": months,
        "status-code": 200
        } 



@app.route('/getGraphsTomatoPrice', methods=['POST'])
def getMonthlyTomatoPrice(): 

        months = [155, 90, 84, 112, 134, 147]

        # convert to jsons
        return {
        "vegetable-code" : "TY-Tomato",
        "vegetable-name" : "tomato",
        "area" : "nuwaraeliya",
        "yield-output": months,
        "status-code": 200
        }

if __name__ == '__main__':
        app.run(debug=True)