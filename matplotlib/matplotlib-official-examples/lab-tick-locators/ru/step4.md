# Определение MultipleLocator

MultipleLocator - это делитель, который размещает деления с равномерным интервалом. Мы можем определить MultipleLocator с использованием `ticker.MultipleLocator()`.

```python
setup(axs[1], title="MultipleLocator(0.5, offset=0.2)")
axs[1].xaxis.set_major_locator(ticker.MultipleLocator(0.5, offset=0.2))
axs[1].xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
```
