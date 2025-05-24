# 프로덕션 서버로 애플리케이션 실행

프로덕션 환경에서는 내장 개발 서버 대신 WSGI 서버를 사용해야 합니다. 여기서는 Waitress 를 WSGI 서버로 사용합니다.

먼저, Waitress 를 설치합니다:

```bash
# Waitress 설치
pip install waitress
```

이제 Waitress 에게 애플리케이션을 제공하도록 지시합니다:

```bash
# Waitress 로 애플리케이션 실행
waitress-serve --call 'flaskr:create_app'
```
