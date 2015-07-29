from rgb_cie import Converter
from PIL import ImageGrab
import json
import httplib2
import time

setting_device = 'newdeveloper'
setting_light = '6'
setting_bridge = '192.168.1.223'


def mainLoop():
    setup()
    
    while True:
        start()
        
def setup():
    path = 'lights/' + setting_light + '/state'
    #turn light on first and set saturation to max
    parameters = '{"on": true, "sat": 254}'
    result = json_request('PUT', path, parameters)    

def start():
    x, y = getPixels()
    changeLight(x,y)
    time.sleep(.2)
    
    
    
def json_request(method, path=None, body=None):
    final_path = 'http://' + setting_bridge + '/api/' + setting_device + '/' + path
    connection = httplib2.Http()
    response, content = connection.request(
        uri=final_path,
        method=method,
        headers={'Content-Type': 'application/json; charset=UTF-8'},
        body=body,
    )
    
    #determine success
    result = json.loads(content.decode())
    return result

def changeLight(x, y):
    x = round(x, 4)
    y = round(y, 4)
    put_path = 'lights/' + setting_light + '/state'
    parameters = '{}{},{}{}'.format('{"xy": [', x,y, '], "sat":254}')
    result = json_request('PUT', put_path, parameters)

def getPixels():
        #grab screenshot and get the size
        image = ImageGrab.grab()
        im = image.load()
        maxX, maxY = image.size
        step = 100
        #loop through pixels for rgb data
        data = []
        for y in range(0, maxY, step):
            for x in range(0, maxX, step):
                pixel = im[x,y]
                data.append(pixel)
                
        #loop and check for white/black to exclude from averaging
        r = 0
        g = 0
        b = 0
        threshMin = 60
        threshMax = 200
        counter = 0
        for z in range(len(data)):
            rP, gP, bP = data[z]
            if rP > threshMax and gP > threshMax and bP > threshMax or rP < threshMin and gP < threshMin and bP < threshMin:
                pass
            else:
                r+= rP
                g+= gP
                b+= bP
                counter+= 1
        if counter > 0:        
            rAvg = r/counter
            gAvg = g/counter
            bAvg = b/counter
            
            converter = Converter()
            hueColor = converter.rgbToCIE1931(rAvg, gAvg, bAvg)
            return hueColor
        else:
            print('problem')
            return (0,0)
            
mainLoop() 
