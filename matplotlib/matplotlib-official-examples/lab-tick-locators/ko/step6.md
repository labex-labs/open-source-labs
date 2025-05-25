# Linear Locator 정의

Linear locator 는 선형 척도에서 정기적인 간격으로 눈금을 배치하는 locator 입니다. `ticker.LinearLocator()`를 사용하여 linear locator 를 정의할 수 있습니다.

```python
setup(axs[3], title="LinearLocator(numticks=3)")
axs[3].xaxis.set_major_locator(ticker.LinearLocator(3))
axs[3].xaxis.set_minor_locator(ticker.LinearLocator(31))
```
