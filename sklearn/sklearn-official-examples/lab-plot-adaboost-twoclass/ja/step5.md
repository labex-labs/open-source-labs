# 2 クラスの決定スコアを描画する

このステップでは、2 クラスの決定スコアを描画します。AdaBoost 分類器の`decision_function`メソッドを使って、データセットの各サンプルに対する決定スコアを取得します。そして、各クラスの決定スコアのヒストグラムを描画します。

```python
# 2 クラスの決定スコアを描画する
twoclass_output = bdt.decision_function(X)
plot_range = (twoclass_output.min(), twoclass_output.max())
plt.subplot(122)
for i, n, c in zip(range(2), class_names, plot_colors):
    plt.hist(
        twoclass_output[y == i],
        bins=10,
        range=plot_range,
        facecolor=c,
        label="Class %s" % n,
        alpha=0.5,
        edgecolor="k",
    )
x1, x2, y1, y2 = plt.axis()
plt.axis((x1, x2, y1, y2 * 1.2))
plt.legend(loc="upper right")
plt.ylabel("サンプル数")
plt.xlabel("スコア")
plt.title("決定スコア")

plt.tight_layout()
plt.subplots_adjust(wspace=0.35)
plt.show()
```
