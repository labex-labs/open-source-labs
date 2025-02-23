# Создание приложения Flask

Создайте новый файл с именем `app.py` и импортируйте необходимые модули:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

В этом коде мы создаем новое приложение Flask и определяем маршрут для корневого URL-адреса ("/"). Когда пользователь посещает корневой URL-адрес, функция `index()` будет вызвана и она будет отображать шаблон `index.html`.
