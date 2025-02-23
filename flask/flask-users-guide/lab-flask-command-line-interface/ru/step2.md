# Создание приложения Flask

Создайте новый файл Python с именем `app.py` и добавьте следующий код, чтобы создать базовое приложение Flask:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

Сохраните файл и выполните его с помощью следующей команды в терминале:

```
python app.py
```
