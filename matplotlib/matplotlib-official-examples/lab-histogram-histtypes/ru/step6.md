# Создаем гистограмму с пользовательскими ширинами корзин

Мы можем создать гистограмму с пользовательскими и неравными ширинами корзин, предоставив список границ корзин. В этом примере мы создадим гистограмму с неравномерно расположенными корзинами.

```python
bins = [100, 150, 180, 195, 205, 220, 250, 300]
plt.hist(x, bins=bins, density=True, histtype='bar', rwidth=0.8)
plt.show()
```
