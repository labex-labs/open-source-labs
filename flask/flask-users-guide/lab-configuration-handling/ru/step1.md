# Создайте приложение Flask

Сначала создадим базовое приложение Flask. Создайте файл с именем `app.py` и добавьте следующий код:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'
```

Для запуска приложения выполните следующую команду в терминале:

```shell
python app.py
```

Откройте веб-браузер и перейдите по адресу `http://localhost:5000`, чтобы увидеть сообщение "Hello, Flask!".
