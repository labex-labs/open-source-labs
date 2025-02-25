# Подготовить данные

В этом шаге готовятся данные для диаграммы. Мы создадим список имен людей, их производительности и коэффициента ошибки.

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
```
