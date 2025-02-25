# Определение NullLocator

NullLocator - это делитель, который не размещает ни одного деления на оси. Мы можем определить NullLocator с использованием `ticker.NullLocator()`.

```python
setup(axs[0], title="NullLocator()")
axs[0].xaxis.set_major_locator(ticker.NullLocator())
axs[0].xaxis.set_minor_locator(ticker.NullLocator())
```
