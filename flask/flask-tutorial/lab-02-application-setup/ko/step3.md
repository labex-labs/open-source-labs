# 애플리케이션 구성

동일한 `__init__.py` 파일에 애플리케이션에 필요한 구성 세부 정보를 추가합니다. 여기에는 비밀 키 설정과 데이터베이스 파일 위치 지정이 포함됩니다.

```python
# flaskr/__init__.py

# More code above...

if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# a simple page that says hello
@app.route('/')
def hello():
    return 'Hello, World!'
```
