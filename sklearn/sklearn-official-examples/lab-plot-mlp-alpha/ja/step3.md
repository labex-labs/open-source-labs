# 分類器の作成

alpha の各値に対して MLP 分類器を作成します。データを標準化するための StandardScaler と、異なる alpha 値の MLPClassifier を含むパイプラインを作成します。ソルバーを'lbfgs'に設定します。これは準ニュートン法のファミリーに属する最適化手法です。オーバーフィットを防ぐために max_iter を 2000 に設定し、early_stopping を True に設定します。2 つの隠れ層を持ち、各層に 10 個のニューロンを使用します。

```python
classifiers = []
names = []
for alpha in alphas:
    classifiers.append(
        make_pipeline(
            StandardScaler(),
            MLPClassifier(
                solver="lbfgs",
                alpha=alpha,
                random_state=1,
                max_iter=2000,
                early_stopping=True,
                hidden_layer_sizes=[10, 10],
            ),
        )
    )
    names.append(f"alpha {alpha:.2f}")
```
