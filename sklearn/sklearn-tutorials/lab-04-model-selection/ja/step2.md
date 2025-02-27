# 交差検証ジェネレータ

Scikit-learn は、一般的な交差検証戦略のための学習用/テスト用インデックスを生成するために使用できるクラスのコレクションを提供しています。これらのクラスには、入力データセットを受け取り、交差検証プロセスの各反復に対する学習用/テスト用セットのインデックスを生成する `split` メソッドがあります。

```python
from sklearn.model_selection import KFold

# KFold 交差検証を使用してデータを K 分割する
k_fold = KFold(n_splits=5)
for train_indices, test_indices in k_fold.split(X_digits):
    print(f'Train: {train_indices} | test: {test_indices}')
```

`cross_val_score` ヘルパー関数を使用すると、交差検証スコアを直接計算できます。これは、交差検証の各反復でデータを学習用とテスト用に分割し、学習用セットで推定器を学習させ、テスト用セットに基づいてスコアを計算します。

```python
from sklearn.model_selection import cross_val_score

# SVM 分類器の交差検証スコアを計算する
scores = cross_val_score(svc, X_digits, y_digits, cv=k_fold, n_jobs=-1)
print(scores)
```
