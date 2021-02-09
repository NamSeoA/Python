from flask import Flask

# 웹서버 생성 
app = Flask(__name__) # main
print(__name__)

# url mapping 
@app.route('/') # 사용자 url / 요청이 오면 아래 함수가 실행되어 응답한다.
def index():
    return 'Hello~ Python'

@app.route('/hello')
def hello():
    return '<h>/hello 요청의 응답입니다.</h>'


if __name__ == '__main__':
    app.run(debug=True, port=8000)