# 結果をプロットする

元のアヤメデータセットとランダマイズされたデータの両方について、順列スコア（空分布）のヒストグラムをプロットします。また、赤色の線を使って、元のデータで分類器が得たスコアを示します。各グラフには p 値が表示されます。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# 元のデータ
ax.hist(perm_scores_iris, bins=20, density=True)
ax.axvline(score_iris, ls="--", color="r")
score_label = f"Score on original\ndata: {score_iris:.2f}\n(p-value: {pvalue_iris:.3f})"
ax.text(0.7, 10, score_label, fontsize=12)
ax.set_xlabel("Accuracy score")
_ = ax.set_ylabel("Probability density")

plt.show()

fig, ax = plt.subplots()

# ランダムデータ
ax.hist(perm_scores_rand, bins=20, density=True)
ax.set_xlim(0.13)
ax.axvline(score_rand, ls="--", color="r")
score_label = f"Score on original\ndata: {score_rand:.2f}\n(p-value: {pvalue_rand:.3f})"
ax.text(0.14, 7.5, score_label, fontsize=12)
ax.set_xlabel("Accuracy score")
ax.set_ylabel("Probability density")

plt.show()
```
