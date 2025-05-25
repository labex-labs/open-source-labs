# 결과 시각화

이 단계에서는 릿지 회귀 경로의 결과를 시각화합니다.

```python
ax = plt.gca()

ax.plot(alphas, coefs)
ax.set_xscale("log")
ax.set_xlim(ax.get_xlim()[::-1])  # 축 반전
plt.xlabel("alpha")
plt.ylabel("가중치")
plt.title("정규화에 따른 릿지 계수")
plt.axis("tight")
plt.show()
```
