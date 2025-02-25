# Построим текст

Теперь, когда мы определили текст, мы можем построить его с использованием Matplotlib. В этом шаге мы создаем фигуру и добавляем текст в нее с помощью метода `fig.text()`.

```python
fig = plt.figure(figsize=(8, len(tests) + 2))
for i, s in enumerate(tests[::-1]):
    fig.text(0, (i +.5) / len(tests), s, fontsize=32)

plt.show()
```
