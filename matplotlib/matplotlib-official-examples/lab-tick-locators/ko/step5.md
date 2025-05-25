# Fixed Locator 정의

Fixed locator 는 고정된 위치에 눈금을 배치하는 locator 입니다. `ticker.FixedLocator()`를 사용하여 fixed locator 를 정의할 수 있습니다.

```python
setup(axs[2], title="FixedLocator([0, 1, 5])")
axs[2].xaxis.set_major_locator(ticker.FixedLocator([0, 1, 5]))
axs[2].xaxis.set_minor_locator(ticker.FixedLocator(np.linspace(0.2, 0.8, 4)))
```
