# 비동기 뷰 정의

Flask 에서는 `async def` 구문을 사용하여 뷰를 비동기 함수로 정의할 수 있습니다. 이렇게 하면 뷰 함수 내에서 `await`를 사용하여 비동기 작업을 수행할 수 있습니다.

```python
@app.route("/get-data")
async def get_data():
    data = await async_db_query(...)
    return jsonify(data)
```

이 코드를 실행하려면 Python 파일 (예: `app.py`) 에 저장하고 Flask 개발 서버를 사용하여 파일을 실행하십시오.

```bash
flask run
```
