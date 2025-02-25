# Настройка подписей осей

Для настройки подписей осей мы можем использовать функции `set_xlabel` и `set_ylabel`. Мы также можем добавлять переводы строки с использованием символа "\n".

```python
ax0.set_xlabel('this is a xlabel\n(with newlines!)')
ax0.set_ylabel('this is vertical\ntest', multialignment='center')
```
