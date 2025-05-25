# 상한만 있는 오차 막대 플롯 생성

이 단계에서는 상한만 있는 오차 막대 플롯을 생성합니다.

```python
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
```
