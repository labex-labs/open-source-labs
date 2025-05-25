# 양쪽 한계 (기본값) 를 가진 오차 막대 플롯 생성

이 단계에서는 기본 동작인 상한 및 하한을 모두 갖는 오차 막대 플롯을 생성합니다.

```python
plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
```
