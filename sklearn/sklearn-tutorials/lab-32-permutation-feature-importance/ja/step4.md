# パーミュテーション特徴量重要度の計算

次に、scikit - learn の`permutation_importance`関数を使ってパーミュテーション特徴量重要度を計算します。この関数は、訓練済みのモデル、検証セット、および特徴量を入れ替える回数を入力として受け取ります。

```python
from sklearn.inspection import permutation_importance

# Calculate permutation feature importance
result = permutation_importance(model, X_val, y_val, n_repeats=30, random_state=0)

# Print the feature importances
for i in result.importances_mean.argsort()[::-1]:
    if result.importances_mean[i] - 2 * result.importances_std[i] > 0:
        print(f"{diabetes.feature_names[i]}: {result.importances_mean[i]:.3f} +/- {result.importances_std[i]:.3f}")
```
