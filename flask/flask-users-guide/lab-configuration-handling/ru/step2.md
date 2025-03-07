# Основная конфигурация

Теперь добавим некоторую базовую конфигурацию в наше приложение Flask. В том же файле `app.py` добавьте следующий код:

```python
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecretkey'
```

Конфигурация `DEBUG` включает режим отладки, который предоставляет полезные сообщения об ошибках в процессе разработки. Конфигурация `SECRET_KEY` используется для безопасной подписи сессионных файлов cookie и других целей, связанных с безопасностью.

Для доступа к значениям конфигурации вы можете использовать словарь `app.config`. Например, чтобы вывести значение `SECRET_KEY`, добавьте следующий код в маршрут `hello`:

```python
@app.route('/')
def hello():
    secret_key = app.config['SECRET_KEY']
    return f'Hello, Flask! Secret Key: {secret_key}'
```

Перезапустите приложение Flask и перейдите по адресу `http://localhost:5000`, чтобы увидеть обновленное сообщение с секретным ключом.
