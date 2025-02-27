# 分類精度をプロットする

主成分の数ごとの分類精度をプロットします。

```python
best_clfs.plot(
    x=components_col, y="mean_test_score", yerr="std_test_score", legend=False, ax=ax1
)
ax1.set_ylabel("分類精度 (検証)")
ax1.set_xlabel("主成分数")

plt.xlim(-1, 70)

plt.tight_layout()
plt.show()
```
