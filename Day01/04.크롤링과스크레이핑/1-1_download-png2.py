'''
파일에 직접 저장하는 urlrerieve() 함수와 달리 urlopen() 함수는 읽어들인 데이터를 임의의
변수에 저장하여 처리할 수 있다. 파싱이 필요한 경우 urlopen()을 사용
'''

import urllib.request 
# URL과 저장 경로 지정하기
url = "http://uta.pw/shodou/img/28/214.png"
savename = "./img/test2.png"
# 다운로드 --- (※1)
mem = urllib.request.urlopen(url).read()
# 파일로 저장하기 --- (※2)
# with를 쓰면 close 안해도 된다.
with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다...!")