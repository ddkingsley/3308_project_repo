import json 
import urllib.request

url = '	https://api.adviceslip.com/advice'

def getAdvice():
    response = urllib.request.urlopen(url)
    output = json.load(response) 
    return (output['slip']['advice'])


