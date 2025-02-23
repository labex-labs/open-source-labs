# Создать приложение на `Python` (без использования Docker)

Выполните следующую команду, чтобы создать файл с именем `app.py` с простой программой на Python. (скопируйте и вставьте весь код блока)

```bash
cd ~/project
```

```bash
echo 'from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")' > app.py
```

Это простое приложение на Python, которое использует Flask для предоставления HTTP-сервера на порту 5000 (5000 - это стандартный порт для Flask). Не беспокойтесь, если вы не слишком знакомы с Python или Flask, эти концепции могут быть применены к приложению, написанному на любом языке.

**По желанию:** Если у вас установлены Python и pip, вы можете запустить это приложение локально. Если нет, перейдите к следующему шагу.

```bash
$ python3 --version
$ pip3 --version
$ pip3 install flask

$ python3 app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Откройте приложение в новой вкладке браузера, используя `http://0.0.0.0:5000/`.

![Flask app browser output](../assets/20230829-13-51-38-psaOqQ42.png)
