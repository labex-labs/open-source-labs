# Определение FixedLocator

FixedLocator - это делитель, который размещает деления в фиксированных позициях. Мы можем определить FixedLocator с использованием `ticker.FixedLocator()`.

```python
setup(axs[2], title="FixedLocator([0, 1, 5])")
axs[2].xaxis.set_major_locator(ticker.FixedLocator([0, 1, 5]))
axs[2].xaxis.set_minor_locator(ticker.FixedLocator(np.linspace(0.2, 0.8, 4)))
```
