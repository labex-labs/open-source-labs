# Python 에서 개발 서버 실행

Flask CLI 명령을 사용하는 것 외에도 Python 코드에서 개발 서버를 시작할 수도 있습니다. `app.py` 파일의 끝에 다음 코드를 추가합니다.

```python
if __name__ == "__main__":
    app.run(debug=True)
```

이제 Python 으로 `app.py` 파일을 실행하여 개발 서버를 실행할 수 있습니다.

```bash
python app.py
```

이렇게 하면 개발 서버가 시작되고 이전과 동일한 방식으로 Flask 애플리케이션에 액세스할 수 있습니다.
