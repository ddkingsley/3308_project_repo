import json 
import urllib.request

#api url
url = '	https://api.adviceslip.com/advice'

#simple function to call advice slip-api, returns random advice
def getAdvice():
    response = urllib.request.urlopen(url)
    output = json.load(response) 
    return (output['slip']['advice'])


