# 서버에 애플리케이션 설치

휠 파일을 서버로 복사합니다. 복사한 후, 새로운 Python 가상 환경을 설정하고 pip 를 사용하여 휠 파일을 설치합니다:

```bash
# 휠 파일 설치
pip install flaskr-1.0.0-py3-none-any.whl
```

이것은 새로운 환경이므로, 데이터베이스를 다시 초기화해야 합니다:

```bash
# 데이터베이스 초기화
flask --app flaskr init-db
```
