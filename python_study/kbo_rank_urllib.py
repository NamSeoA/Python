import urllib.request as req 
import re  # 정규식 이용 
import ssl

# URL
url = 'https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo'

context = ssl._create_unverified_context() 
html = req.urlopen(url, context=context)

# url 접속 
# html = req.urlopen(url)
# 응답 결과를 문자열로 변경
html_code = str(html.read().decode('utf-8'))

tag_list = re.findall(r'(<span id=\"team_)(.+)(<\/span>)', html_code)

for index, tag in enumerate(tag_list, start=1):
    #print(tag)
    print(index,'위', tag[1].split('>')[1])

