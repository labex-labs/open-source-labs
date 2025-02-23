# Настройка секретного ключа

В рабочей среде вы должны изменить секретный ключ на случайное значение. Чтобы сгенерировать случайный секретный ключ, выполните следующую команду:

```bash
# Сгенерировать случайный секретный ключ
python -c 'import secrets; print(secrets.token_hex())'
```

Создайте файл `config.py` в папке экземпляра и задайте `SECRET_KEY` значением, полученным выше.

```python
#.venv/var/flaskr-instance/config.py

SECRET_KEY = 'your_generated_secret_key'
```
