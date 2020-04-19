import os
import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter

print('cwd: '+ os.getcwd())
#exit()

# utf-16 인코딩으로 파일을 열고 글자를 출력하기 --- (※1)
fp =  codecs.open("./file/BEXX0003.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("body > text")
text = body.getText()

# 텍스트를 한 줄씩 처리하기 --- (※2)
twitter = Twitter()
word_dic = {}
lines = text.split("\n")
for line in lines:
    malist = twitter.pos(line)
    # print(mallist)
    '''
    [('"', 'Punctuation'), ('일이', 'Modifier'), ('재미있게', 'Adjective'), ('되어', 'Verb'), ('갈', 'Verb'), ('게다', 'Noun'), ('.', 'Punctuation'), ('이런', 'Adjective'), ('일도', 'Noun'), ('어짜믄', 'Noun'), 
    ('좋은', 'Adjective'), ('징조', 'Noun'), ('가', 'Josa'), ('아닌가', 'Adjective'), ('모르겠네', 'Verb'), ('."', 'Punctuation'), ('결심', 'Noun'), ('을', 'Josa'), ('굳게', 'Adjective'), ('하는지', 'Verb'), (' 
    평산', 'Noun'), ('의', 'Josa'), ('얼굴', 'Noun'), ('이', 'Josa'), ('쌍글', 'Adverb'), ('해졌다', 'Verb'), ('.', 'Punctuation')]
    '''
    for word in malist:
        if word[1] == "Noun": #  명사 확인하기 --- (※3)
            if not (word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1 # 카운트하기
            
# 많이 사용된 명사 출력하기 --- (※4)
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True) # 내림차순 정렬
for word, count in keys[:50]: # 50개만 추출
    print("{0}({1}) ".format(word, count), end="")
print()