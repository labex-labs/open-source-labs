# Создать данные

Далее нам нужно создать некоторые данные для построения графика. В этом примере мы создадим массив значений для времени (`t`) и массив значений для напряжения (`s`).

```python
t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)
```
