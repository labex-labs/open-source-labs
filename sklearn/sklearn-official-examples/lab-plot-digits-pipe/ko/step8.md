# 분류 정확도 플롯

각 구성 요소 수에 대한 분류 정확도를 플롯합니다.

```python
best_clfs.plot(
    x=components_col, y="mean_test_score", yerr="std_test_score", legend=False, ax=ax1
)
ax1.set_ylabel("분류 정확도 (검증)")
ax1.set_xlabel("n_components")

plt.xlim(-1, 70)

plt.tight_layout()
plt.show()
```
