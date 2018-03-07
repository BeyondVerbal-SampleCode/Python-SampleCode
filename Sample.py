import requests 
requests.packages.urllib3.disable_warnings()

def getAnalysis(API_Key,WavPath):
    res = requests.post("https://token.beyondverbal.com/token",data={"grant_type":"client_credentials","apiKey":API_Key})
    token = res.json()['access_token']
    headers={"Authorization":"Bearer "+token}
    #Please change the URL to the desired API version
    # https://apiv3.beyondverbal.com/v3/recording/start
    # https://apiv4.beyondverbal.com/v4/recording/start
    # https://apiv5.beyondverbal.com/v5/recording/start
    pp = requests.post("https://apiv5.beyondverbal.com/v5/recording/start",json={"dataFormat": { "type":"WAV" }},verify=False,headers=headers)
    if pp.status_code != 200:
        print(pp.status_code, pp.content)
        return
    recordingId = pp.json()['recordingId']
    with open(WavPath,'rb') as wavdata:
        r = requests.post("https://apiv5.beyondverbal.com/v5/recording/"+recordingId,data=wavdata, verify=False, headers=headers)
        return r.json()


json = getAnalysis("API_KEY","PathTOWav.wav")
print(json)
