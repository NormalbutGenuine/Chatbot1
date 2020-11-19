from chatbot.utils.Preprocess import Preprocess
from chatbot.models.intent.IntentModel import IntentModel

p = Preprocess(word2index_dic='C:/Users/obybk/OneDrive/바탕 화면/인공지능/deepChat/chatbot/train_tools/dict/chatbot_dict.bin',
userdic='C:/Users/obybk/OneDrive/바탕 화면/인공지능/deepChat/Tokenizing/user_dic.txt')
intent = IntentModel(model_name = 'C:/Users/obybk/OneDrive/바탕 화면/인공지능/deepChat/intent_model.h5', proprocess=p)
query = "오늘 탕수육 주문 가능한가요?"
predict = intent.predict_class(query)
predict_label = intent.labels[predict]
print(query)
print("의도 예측 클래스: ", predict)
print("의도 예측 레이블: ", predict_label)