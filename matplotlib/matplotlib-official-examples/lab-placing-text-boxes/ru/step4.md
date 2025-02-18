# Создание текста для текстового поля

Мы создадим строку, содержащую среднее значение (mean), медиану (median) и стандартное отклонение (standard deviation) наших данных.

```python
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu, ),
    r'$\mathrm{median}=%.2f$' % (median, ),
    r'$\sigma=%.2f$' % (sigma, )))
```
