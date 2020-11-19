from flask import Flask, request
app = Flask(__name__)

# 카카오톡 텍스트형 응답
@app.route('/api/sayHello', methods=['POST'])
def sayHello():
    body = request.get_json() # 봇 시스템 요청
    print(body) # skillpayload 출력 - 사용자의 텍스트

    responseBody={
        "version": "2.0",
        "template":{
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕 hello I'm Ryan"
                    }
                }
            ]
        }
    }
    return responseBody

# 카카오톡 이미지형 응답
@app.route('/api/showHello', methods=['POST'])
def showHello():
    body = request.get_json() # 봇 시스템 요청 body(SkillPayload)
    print(body) # SkillPayload

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage":{
                        "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
                        "altText": "hello I'm Ryan ㅎㅎㅎ"
                    }
                }
            ]
        }
    }
    return responseBody

if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=5000)
    