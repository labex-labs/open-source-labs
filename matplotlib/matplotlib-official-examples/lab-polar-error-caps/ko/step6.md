# 겹치는 세타 오차 막대 생성

이 단계에서는 출력 플롯의 가독성을 어떻게 감소시킬 수 있는지 보여주기 위해 겹치는 세타 오차 막대를 생성합니다.

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=5.25, yerr=0.1, capsize=7, fmt="o", c="darkred")
ax.set_title("Overlapping Theta Error Bars")
plt.show()
```
