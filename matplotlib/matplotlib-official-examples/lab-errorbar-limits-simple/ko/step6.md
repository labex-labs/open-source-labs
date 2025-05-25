# 상한 및 하한의 부분 집합을 갖는 오차 막대 플롯 생성

이 단계에서는 상한 및 하한의 부분 집합을 갖는 오차 막대 플롯을 생성합니다.

```python
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits, label='subsets of uplims and lolims')
```
