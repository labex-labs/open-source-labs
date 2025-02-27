# 分類器とパラメータの定義

このステップでは、特徴量の離散化プロセスで使用する分類器とパラメータを定義します。ロジスティック回帰、線形サポートベクターマシン（SVM）、勾配ブースティング分類器、およびラジアルベーシス関数カーネルを持つSVMを含む分類器のリストを作成します。また、GridSearchCVアルゴリズムで使用する各分類器のパラメータセットも定義します。

```python
# (推定器, パラメータグリッド) のリストで、パラメータグリッドはGridSearchCVで使用されます
# この例では、実行時間を短縮するためにパラメータ空間を狭い範囲に限定しています。
# 実際の使用例では、アルゴリズムのためのより広い探索空間を使用する必要があります。
classifiers = [
    (
        make_pipeline(StandardScaler(), LogisticRegression(random_state=0)),
        {"logisticregression__C": np.logspace(-1, 1, 3)},
    ),
    (
        make_pipeline(StandardScaler(), LinearSVC(random_state=0, dual="auto")),
        {"linearsvc__C": np.logspace(-1, 1, 3)},
    ),
    (
        make_pipeline(
            StandardScaler(),
            KBinsDiscretizer(encode="onehot"),
            LogisticRegression(random_state=0),
        ),
        {
            "kbinsdiscretizer__n_bins": np.arange(5, 8),
            "logisticregression__C": np.logspace(-1, 1, 3),
        },
    ),
    (
        make_pipeline(
            StandardScaler(),
            KBinsDiscretizer(encode="onehot"),
            LinearSVC(random_state=0, dual="auto"),
        ),
        {
            "kbinsdiscretizer__n_bins": np.arange(5, 8),
            "linearsvc__C": np.logspace(-1, 1, 3),
        },
    ),
    (
        make_pipeline(
            StandardScaler(), GradientBoostingClassifier(n_estimators=5, random_state=0)
        ),
        {"gradientboostingclassifier__learning_rate": np.logspace(-2, 0, 5)},
    ),
    (
        make_pipeline(StandardScaler(), SVC(random_state=0)),
        {"svc__C": np.logspace(-1, 1, 3)},
    ),
]

names = [get_name(e).replace("StandardScaler + ", "") for e, _ in classifiers]
```
