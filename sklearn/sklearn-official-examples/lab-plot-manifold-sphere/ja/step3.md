# 局所的線形埋め込みによるマニホールド学習を実行する

次に、局所的線形埋め込み（Locally Linear Embedding：LLE）によるマニホールド学習を実行します。LLE は、少数のサンプルで複雑なマニホールドを展開できる強力な手法です。LLE の 4 つのバリエーションを使用し、それらの結果を比較します。

```python
methods = ["standard", "ltsa", "hessian", "modified"]
labels = ["LLE", "LTSA", "Hessian LLE", "Modified LLE"]

for i, method in enumerate(methods):
    t0 = time()
    trans_data = (
        manifold.LocallyLinearEmbedding(
            n_neighbors=n_neighbors, n_components=2, method=method
        )
     .fit_transform(sphere_data)
     .T
    )
    t1 = time()
    print("%s: %.2g sec" % (methods[i], t1 - t0))

    ax = fig.add_subplot(252 + i)
    plt.scatter(trans_data[0], trans_data[1], c=colors, cmap=plt.cm.rainbow)
    plt.title("%s (%.2g sec)" % (labels[i], t1 - t0))
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.yaxis.set_major_formatter(NullFormatter())
    plt.axis("tight")
```
