# Создание графиков

Теперь мы создадим три подграфика с использованием функции `plt.subplots`. Два графика будут созданы в одной фигуре, а третий график будет создан в отдельной фигуре.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(t, s1)
ax2.plot(t, s2)
fig, ax3 = plt.subplots()
ax3.plot(t, s3)
```
