# Auto Locator 정의

Auto locator 는 자동으로 정기적인 간격으로 눈금을 배치하는 locator 입니다. `ticker.AutoLocator()`를 사용하여 auto locator 를 정의할 수 있습니다.

```python
setup(axs[5], title="AutoLocator()")
axs[5].xaxis.set_major_locator(ticker.AutoLocator())
axs[5].xaxis.set_minor_locator(ticker.AutoMinorLocator())
```
