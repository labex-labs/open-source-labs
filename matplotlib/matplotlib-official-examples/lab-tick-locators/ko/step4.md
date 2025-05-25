# Multiple Locator 정의

Multiple locator 는 정기적인 간격으로 눈금을 배치하는 locator 입니다. `ticker.MultipleLocator()`를 사용하여 multiple locator 를 정의할 수 있습니다.

```python
setup(axs[1], title="MultipleLocator(0.5, offset=0.2)")
axs[1].xaxis.set_major_locator(ticker.MultipleLocator(0.5, offset=0.2))
axs[1].xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
```
