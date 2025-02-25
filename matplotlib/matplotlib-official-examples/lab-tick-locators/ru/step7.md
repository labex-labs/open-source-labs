# Определение IndexLocator

IndexLocator - это делитель, который размещает деления с равномерным интервалом на шкале индекса. Мы можем определить IndexLocator с использованием `ticker.IndexLocator()`.

```python
setup(axs[4], title="IndexLocator(base=0.5, offset=0.25)")
axs[4].plot([0]*5, color='white')
axs[4].xaxis.set_major_locator(ticker.IndexLocator(base=0.5, offset=0.25))
```
