# Сохранение графика

После того, как мы создали график, мы можем сохранить его в файл.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.savefig('my_plot.png')
```

Здесь мы используем функцию `savefig` для сохранения нашего графика в файл с именем `my_plot.png`.
