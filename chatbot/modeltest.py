from models.intent.IntentModel import IntentModel
from utils.Preprocess import Preprocess

p=Preprocess(word2index_dic='train_tools/dict/chatbot_dict.bin',
 userdic='../Tokenizing/user_dic.txt')
intent = IntentModel(model_name='models/intent/intent_model.h5', proprocess=p)
query = "안녕하세요."
intent_predict = intent.predict_class(query)
print(intent_predict)