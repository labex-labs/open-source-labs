# 큰 반경 오차 막대 생성

이 단계에서는 데이터의 원치 않는 스케일로 이어져 표시 범위를 줄이는 방법을 보여주기 위해 큰 반경 오차 막대를 생성합니다.

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=0.25, yerr=10.1, capsize=7, fmt="o", c="orangered")
ax.set_title("Large Radius Error Bars")
plt.show()
```
