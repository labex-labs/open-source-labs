# 회귀 계수 비교

이제 음수가 아닌 최소 제곱 회귀와 일반 선형 회귀 사이의 회귀 계수를 비교할 것입니다. 계수를 서로 그래프로 나타내면 높은 상관관계를 보일 것입니다. 그러나 음수가 아닌 최소 제곱 제약 조건으로 인해 일부 계수가 0 으로 축소됩니다. 이는 음수가 아닌 최소 제곱이 본질적으로 희소 결과를 생성하기 때문입니다.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(reg_ols.coef_, reg_nnls.coef_, linewidth=0, marker=".")

low_x, high_x = ax.get_xlim()
low_y, high_y = ax.get_ylim()
low = max(low_x, low_y)
high = min(high_x, high_y)
ax.plot([low, high], [low, high], ls="--", c=".3", alpha=0.5)
ax.set_xlabel("OLS 회귀 계수", fontweight="bold")
ax.set_ylabel("음수가 아닌 최소 제곱 회귀 계수", fontweight="bold")
```
