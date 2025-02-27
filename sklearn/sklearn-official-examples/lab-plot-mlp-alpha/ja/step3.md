# 分類器の作成

alphaの各値に対してMLP分類器を作成します。データを標準化するためのStandardScalerと、異なるalpha値のMLPClassifierを含むパイプラインを作成します。ソルバーを'lbfgs'に設定します。これは準ニュートン法のファミリーに属する最適化手法です。オーバーフィットを防ぐためにmax_iterを2000に設定し、early_stoppingをTrueに設定します。2つの隠れ層を持ち、各層に10個のニューロンを使用します。

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
