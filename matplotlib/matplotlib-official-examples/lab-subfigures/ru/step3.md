# Построение графиков на субрисунках

Для построения графиков на субрисунках необходимо создать для каждого субрисунка подграфик с использованием `subfig.subplots()`. Затем можно использовать любую функцию построения графиков в Matplotlib для создания графиков.

```python
ax1 = subfigs[0].subplots()
ax1.plot(np.arange(10), np.random.randn(10))

ax2 = subfigs[1].subplots()
ax2.plot(np.arange(10), np.random.randn(10))
```

Это создаст два субрисунка, каждый с графиком случайных данных.
