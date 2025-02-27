# OOBエラー率を視覚化する

最後に、各分類器のOOBエラー率を推定器の数の関数としてプロットします。これにより、エラー率が安定する推定器の数を特定できます。Matplotlibを使ってグラフを生成します。

```python
for label, clf_err in error_rate.items():
    xs, ys = zip(*clf_err)
    plt.plot(xs, ys, label=label)

plt.xlim(min_estimators, max_estimators)
plt.xlabel("n_estimators")
plt.ylabel("OOB error rate")
plt.legend(loc="upper right")
plt.show()
```
