# 비밀 키 구성

프로덕션 환경에서는 비밀 키를 임의의 값으로 변경해야 합니다. 임의의 비밀 키를 생성하려면 다음 명령을 실행하십시오:

```bash
# 임의의 비밀 키 생성
python -c 'import secrets; print(secrets.token_hex())'
```

instance 폴더에 `config.py` 파일을 생성하고 `SECRET_KEY`를 생성된 값으로 설정합니다.

```python
# .venv/var/flaskr-instance/config.py

SECRET_KEY = 'your_generated_secret_key'
```
