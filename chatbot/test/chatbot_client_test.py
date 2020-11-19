import socket
import json


host = "127.0.0.1"  # host
port = 5050  # port 


while True:
    print("질문 : ")
    query = input()  # 질문 입력
    if(query == "exit"):
        exit(0)
    print("-" * 40)

    # 챗봇 엔진 서버 연결
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # 챗봇 엔진 질의 요청
    json_data = {
        'Query': query,
        'BotType': "MyService"
    }
    message = json.dumps(json_data)
    mySocket.send(message)
    # 챗봇 엔진 답변 출력
    data = mySocket.recv(2048)
    ret_data = json.loads(data)
    print("답변 : ")
    print(ret_data['Answer'])
    print(ret_data)
    print(type(ret_data))
    print("\n")

# 챗봇 엔진 서버 연결 소켓 닫기
mySocket.close()
