# Регистрация команд в приложении Flask

Чтобы ваши собственные команды были доступны через CLI Flask, вам нужно зарегистрировать их в вашем приложении Flask. Откройте файл `app.py` и измените его следующим образом:

```python
from flask import Flask
from commands import greet

app = Flask(__name__)
app.cli.add_command(greet)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

Сохраните файл и перезапустите сервер разработки Flask с помощью команды `flask run`. Теперь вы можете выполнить свою собственную команду `greet` из командной строки:

```
flask greet John
```

В терминале должно появиться сообщение "Hello, John!".
