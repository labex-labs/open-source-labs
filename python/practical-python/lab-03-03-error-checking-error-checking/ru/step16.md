# Упражнение 3.10: Отключение сообщений об ошибках

Измените функцию `parse_csv()` так, чтобы сообщения об ошибках при разборе могли быть отключены, если пользователь явно этого желает. Например:

```python
>>> portfolio = parse_csv('missing.csv', types=[str,int,float], silence_errors=True)
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}]
>>>
```

Обработка ошибок - одна из самых сложных вещей в большинстве программ. Как правило, вы не должны тихо игнорировать ошибки. Вместо этого лучше сообщать о проблемах и давать пользователю возможность отключить сообщение об ошибке, если он этого хочет.
