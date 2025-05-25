# Log Locator 정의

Log locator 는 로그 스케일에서 정기적인 간격으로 눈금을 배치하는 locator 입니다. `ticker.LogLocator()`를 사용하여 log locator 를 정의할 수 있습니다.

```python
setup(axs[7], title="LogLocator(base=10, numticks=15)")
axs[7].set_xlim(10**3, 10**10)
axs[7].set_xscale('log')
axs[7].xaxis.set_major_locator(ticker.LogLocator(base=10, numticks=15))
```
