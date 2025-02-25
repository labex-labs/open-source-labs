# Определение LinearLocator

LinearLocator - это делитель, который размещает деления с равномерным интервалом на линейной шкале. Мы можем определить LinearLocator с использованием `ticker.LinearLocator()`.

```python
setup(axs[3], title="LinearLocator(numticks=3)")
axs[3].xaxis.set_major_locator(ticker.LinearLocator(3))
axs[3].xaxis.set_minor_locator(ticker.LinearLocator(31))
```
