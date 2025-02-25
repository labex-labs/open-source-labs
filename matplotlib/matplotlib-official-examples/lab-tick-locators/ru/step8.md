# Определение AutoLocator

AutoLocator - это делитель, который автоматически размещает деления с равномерным интервалом. Мы можем определить AutoLocator с использованием `ticker.AutoLocator()`.

```python
setup(axs[5], title="AutoLocator()")
axs[5].xaxis.set_major_locator(ticker.AutoLocator())
axs[5].xaxis.set_minor_locator(ticker.AutoMinorLocator())
```
