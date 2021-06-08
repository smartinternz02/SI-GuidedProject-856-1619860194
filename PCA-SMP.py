import requests
import json 


API_KEY = "RvLBg8GMl8gitnEGyrAFc3kVTLr6ap-b1X-7WEMX42Dg"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


payload_scoring ={"input_data":[{"field":[["Global_reactive_power","Global_intensity","Sub_metering_1","Sub_metering_2","Sub_metering_3"]],
                   "values": [[0.418,18.4,0.0,1.0,17.0]]    }]}
response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/929df1a6-62a6-4469-82e8-979005ca4cb7/predictions?version=2021-06-02', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})


predictions= response_scoring.json()
pred= predictions["predictions"][0]['values'][0][0]
print("The Global Active Power is " + str(pred))