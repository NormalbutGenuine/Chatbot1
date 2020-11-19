from chatbot.utils.Preprocess import Preprocess
from chatbot.models.ner.NerModel import NerModel

p = Preprocess(word2index_dic='C:/Users/obybk/OneDrive/바탕 화면/인공지능/deepChat/chatbot/train_tools/dict/chatbot_dict.bin',
 userdic='C:/Users/obybk/OneDrive/바탕 화면/인공지능/deepChat/Tokenizing/user_dic.txt')

ner = NerModel(model_name = 'C:/Users/obybk/OneDrive/바탕 화면/인공지능/deepChat/ner_model.h5', proprocess=p)
query = "오늘 오전 13시 2분에 탕수육 주문하고 싶어요"
predicts = ner.predict(query)
print(predicts)