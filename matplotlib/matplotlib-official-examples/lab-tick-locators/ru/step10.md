# Определение LogLocator

LogLocator - это делитель, который размещает деления с равномерным интервалом на логарифмической шкале. Мы можем определить LogLocator с использованием `ticker.LogLocator()`.

```python
setup(axs[7], title="LogLocator(base=10, numticks=15)")
axs[7].set_xlim(10**3, 10**10)
axs[7].set_xscale('log')
axs[7].xaxis.set_major_locator(ticker.LogLocator(base=10, numticks=15))
```
