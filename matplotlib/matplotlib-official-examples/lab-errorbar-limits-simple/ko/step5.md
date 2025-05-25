# 상한 및 하한을 모두 갖는 오차 막대 플롯 생성

이 단계에서는 상한 및 하한을 모두 갖는 오차 막대 플롯을 생성합니다.

```python
plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True, label='uplims=True, lolims=True')
```
