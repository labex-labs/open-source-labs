# 分類器を定義する

このデータセットに対して、さまざまな分類器を定義します。

```python
C = 10
kernel = 1.0 * RBF([1.0, 1.0])  # GPC 用
# さまざまな分類器を作成します。
classifiers = {
    "L1 ロジスティック回帰": LogisticRegression(
        C=C, penalty="l1", solver="saga", multi_class="multinomial", max_iter=10000
    ),
    "L2 ロジスティック回帰（多項式）": LogisticRegression(
        C=C, penalty="l2", solver="saga", multi_class="multinomial", max_iter=10000
    ),
    "L2 ロジスティック回帰（One-Vs-Rest）": LogisticRegression(
        C=C, penalty="l2", solver="saga", multi_class="ovr", max_iter=10000
    ),
    "線形 SVC": SVC(kernel="linear", C=C, probability=True, random_state=0),
    "GPC": GaussianProcessClassifier(kernel),
}
```
