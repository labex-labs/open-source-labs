# Определение MaxNLocator

MaxNLocator - это делитель, который размещает максимальное количество делений на оси. Мы можем определить MaxNLocator с использованием `ticker.MaxNLocator()`.

```python
setup(axs[6], title="MaxNLocator(n=4)")
axs[6].xaxis.set_major_locator(ticker.MaxNLocator(4))
axs[6].xaxis.set_minor_locator(ticker.MaxNLocator(40))
```
