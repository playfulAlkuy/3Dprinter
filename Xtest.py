import requests
import json

url="http://127.0.0.1:5000/api/printer/printhead"

headers={
    
    "Connection":"keep-alive",
    "Content-Type":"application/json; charset=UTF-8",
    "Cookie":"remember_token_P5000=json|e6ed795237fcf29421c1deb1a2b649c77cda553566a06a8a6115ad1ca48a249a67814dbdc61597165fe46f5dcf2fc781a8880fd89adb05407ddfda4976534ca6; session_P5000=.eJxNjktuwzAMBe-idVGIpCRS3jn9XMOQTApxETiFZS-CondvimyynfcGmB83tc362Q37dtiLmxZ1g6MqefZNCHwzTJRIWGuusyHDDJxAotYAjKESssyE0VgxUkwBRb2UQqK1Um6-MLNhaCUzKGkSSE1qDU0De_SxAlvmlJKiWS4yN3H3kKPb9qj56tf1Tha1dV_222s59vO0377NDetxuTwtz_d_v1vvy3V98Dc4vQP6E0PEIDGJMNGHJ_gMNI5hdL9_BPhOfQ.YUGpZA.YdHVkjoaYGSN1B3LZmgZzlwxbUw",
    "User-Agent":"Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"

}

datz={
    "absolute": 'false',
    "command": 'jog',
    "z": 10
}

dath={
    "axes":'z',
    "command": 'home'
}


resp=requests.post(url,data=json.dumps(dath),headers=headers)
print(resp.text)