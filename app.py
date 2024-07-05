from flask import Flask, render_template, request, url_for
import json
import pyautogui as py

app = Flask(__name__)

data = None

with open('savedApplications.json', 'r') as jsonData:
    data = json.loads(jsonData.read())



# https://codepen.io/Ma5a/pen/MWBGbOb
# https://codepen.io/LukyVj/pen/YzOXepM


def readData():
    with open('savedApplications.json', 'r') as jsonData:
        data = json.loads(jsonData.read())
        return data
    
def saveData(inputData):
    with open('savedApplications.json', 'w+') as jsonData:
        json.dump(inputData, jsonData)

@app.route("/redirect/")
def redirect():
    return render_template('index.html', name=readData()["remaining"]["companyData"])

@app.route("/", methods=["POST", "GET"])
def hello():
    if request.method == "POST":
        functionName = request.form.get("functionName")
        print(functionName)
        if functionName.endswith('tick'):
             for sampleData in data['remaining']['companyData']:
                if sampleData['jobID'] + "tick" == functionName:
                    index = data['remaining']['companyData'].index(sampleData)
                    sampleData['filled'] = "Yes"
                    data["completed"]["companyData"].append(sampleData)
                    data['remaining']['companyData'].pop(index)
                    saveData(data)
                    print(len(data))
                    py.press('f5')      
        if functionName.endswith('delete'):
             print("DELETE")
             for sampleData in data['remaining']['companyData']:
                if sampleData['jobID'] + "delete" == functionName:
                    index = data['remaining']['companyData'].index(sampleData)
                    print(index)
                    data['remaining']['companyData'].pop(index)
                    saveData(data)
                    print(len(data))
                    py.press('f5')           
        else:
            for sampleData in data['remaining']['companyData']:
                if sampleData['jobID'] == functionName:
                    # index = data['remaining']['companyData'].index(sampleData)
                    # sampleData['filled'] = "Yes"
                    # data["completed"]["companyData"].append(sampleData)
                    # data['remaining']['companyData'].pop(index)
                    # saveData(data)
                    print(len(data))
                    # py.press('f5')
    return render_template('index.html', remaining=readData()["remaining"]["companyData"], completed=readData()["completed"]["companyData"])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
    pass