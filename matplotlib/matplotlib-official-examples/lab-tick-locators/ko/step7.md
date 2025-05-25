# Index Locator 정의

Index locator 는 인덱스 척도에서 정기적인 간격으로 눈금을 배치하는 locator 입니다. `ticker.IndexLocator()`를 사용하여 index locator 를 정의할 수 있습니다.

```python
setup(axs[4], title="IndexLocator(base=0.5, offset=0.25)")
axs[4].plot([0]*5, color='white')
axs[4].xaxis.set_major_locator(ticker.IndexLocator(base=0.5, offset=0.25))
```
