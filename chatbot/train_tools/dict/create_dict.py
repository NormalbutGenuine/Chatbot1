from chatbot.utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing
import pickle

def read_corpus_data(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]

    return data

corpus_data = read_corpus_data('C:\\Users\\obybk\\OneDrive\\바탕 화면\\인공지능\\deepChat\\chatbot\\train_tools\\dict\\corpus.txt')
p=Preprocess()
dict=[]
for c in corpus_data:
    pos = p.pos(c[1])
    for k in pos:
        dict.append(k[0])

tokenizer = preprocessing.text.Tokenizer(oov_token='OOV')
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index

f=open("chatbot_dict.bin", "wb")
try:
    pickle.dump(word_index, f)
    print("성공")
except Exception as e:
    print(e)

finally:
    f.close()

# python -m chatbot.train_tools.dict.create_dict.py