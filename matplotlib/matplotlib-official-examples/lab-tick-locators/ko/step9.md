# MaxN Locator 정의

MaxN locator 는 축에 최대 개수의 눈금을 배치하는 locator 입니다. `ticker.MaxNLocator()`를 사용하여 MaxN locator 를 정의할 수 있습니다.

```python
setup(axs[6], title="MaxNLocator(n=4)")
axs[6].xaxis.set_major_locator(ticker.MaxNLocator(4))
axs[6].xaxis.set_minor_locator(ticker.MaxNLocator(40))
```
