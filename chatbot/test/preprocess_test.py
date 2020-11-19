from chatbot.utils.Preprocess import Preprocess

sent = "내일 오전 10시에 탕수육 주문하고 싶어"

# 전처리 객체생성
p = Preprocess(userdic='C:/Users/obybk/OneDrive/바탕 화면/인공지능/deepChat/Tokenizing/user_dic.txt')

# 형태소 분석 실행
pos = p.pos(sent)

# 품사 태그와 같이 키워드 출력
ret = p.get_keywords(pos, without_tag=False)
print(ret)

ret = p.get_keywords(pos, without_tag=True)
print(ret)