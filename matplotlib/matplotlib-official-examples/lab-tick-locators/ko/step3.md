# Null Locator 정의

Null locator 는 축에 눈금을 표시하지 않는 locator 입니다. `ticker.NullLocator()`를 사용하여 null locator 를 정의할 수 있습니다.

```python
setup(axs[0], title="NullLocator()")
axs[0].xaxis.set_major_locator(ticker.NullLocator())
axs[0].xaxis.set_minor_locator(ticker.NullLocator())
```
