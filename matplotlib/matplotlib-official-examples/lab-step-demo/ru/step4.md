# Построение графика с использованием `.plot()`

Мы можем добиться того же поведения, что и у `.step()`, используя параметр `drawstyle` функции `.plot()`. Мы создадим три графика, используя разные значения для `drawstyle`.

```python
plt.plot(x, y + 2, drawstyle='steps', label='steps (=steps-pre)')
plt.plot(x, y + 1, drawstyle='steps-mid', label='steps-mid')
plt.plot(x, y, drawstyle='steps-post', label='steps-post')
plt.legend()
plt.show()
```

Вышеприведенный код создаст график с тремя кусочно-константными кривыми, каждая с разным значением для `drawstyle`.
