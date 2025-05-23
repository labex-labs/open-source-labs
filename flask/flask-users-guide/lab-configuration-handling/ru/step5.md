# Папка с экземпляром

Flask предоставляет папку с экземпляром для хранения конфигурационных файлов, специфичных для определенной развертки. Это позволяет отделить конфигурации, специфичные для развертки, от остальной части кода. По умолчанию Flask использует папку с именем `instance` в том же каталоге, что и ваше приложение.

Создайте новую папку с именем `instance` в том же каталоге, что и файл `app.py`. В папке `instance` создайте файл с именем `config.cfg` и добавьте следующий код:

```
DEBUG = True
SECRET_KEY = 'instancekey'
```

В файле `app.py` добавьте следующий код перед кодом конфигурации:

```python
app.instance_path = os.path.abspath(os.path.dirname(__file__))
app.config.from_pyfile('config.cfg')
```

`instance_path` устанавливается в абсолютный путь к папке `instance`. Метод `from_pyfile` загружает конфигурацию из файла `config.cfg` в папке с экземпляром.

Перезапустите приложение Flask и перейдите по адресу `http://localhost:5000`, чтобы увидеть обновленное сообщение с значениями конфигурации экземпляра.
