# Создаем данные

В этом шаге мы создадим словарь `data`, содержащий значения для переменных `a`, `b`, `c` и `d`.

```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
```
