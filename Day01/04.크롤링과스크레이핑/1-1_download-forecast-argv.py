#!/usr/bin/env python3
# 라이브러리를 읽어 들입니다. --- (※1)
import sys
import urllib.request as req
import urllib.parse as parse
# 명령줄 매개변수 추출 --- (※2)
# *1 : 명령줄 매개변수를 조정한다. 매개변수는 sys.argv에 리스트 형태로 들어옴. 
# sys.argv[0] : 스크립트 파일의 이름, sys.argv[1] 이상부터 : 명령줄의 매개변수
if len(sys.argv) <= 1:
    print("USAGE: download-forecast-argv <Region Number>")
    sys.exit()
regionNumber = sys.argv[1]
# 매개변수를 URL 인코딩합니다. --- (※3)
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': regionNumber
}
params = parse.urlencode(values)
url = API + "?" + params
print("url=", url)
# 다운로드합니다. --- (※3)
data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)

# 실행할 때 1-1_download-forecast-argv.py 108(명령줄에 파라미터를 붙여준다)
