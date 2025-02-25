# Создать фигуру и подграфик

Далее нам нужно создать фигуру и подграфик для нашего графика. Мы будем использовать параметр `projection` метода `add_subplot`, чтобы создать полярный график.

```python
fig = plt.figure()
ax = fig.add_subplot(projection="polar", facecolor="lightgoldenrodyellow")
```
