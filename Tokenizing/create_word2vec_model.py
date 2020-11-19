from gensim.models import Word2Vec
from konlpy.tag import Komoran
import time

def read_review_data(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    return data

start = time.time()
print('1) 말뭉치 데이터 읽기 시작')
review_data = read_review_data('C:/Users/obybk/OneDrive/바탕 화면/인공지능/deepChat/Tokenizing/ratings.txt')
print(len(review_data))
print('1) 말뭉치 데이터 읽기 완료: ', time.time()-start)
print('2) 형태소에서 명사만 추출 시작')
komoran = Komoran()
docs = [komoran.nouns(sentence[1]) for sentence in review_data]
print('2) 형태소에서 명사만 추출 완료: ', time.time() - start)

#word2Vec 모델 학습
print('3) 모델학습 시작')
model = Word2Vec(sentences = docs, size=200, window = 4, hs = 1, min_count = 2, sg=1)
print('3) Word2Vec 모델 학습 완료: ', time.time() - start)

# 모델 저장
print('4) 학습된 모델 저장 시작')
model.save('nvmc.model')
print('4) 학습된 모델 저장 완료: ', time.time()-start)

# 학습된 말뭉치 수, 코퍼스 내 전체 단어 수
print("corpus_count : ", model.corpus_count)
print("corpus_total_words : ", model.corpus_total_words)