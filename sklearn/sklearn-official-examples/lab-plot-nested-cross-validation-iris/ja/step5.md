# ネスト交差検証（Nested Cross-Validation）

ネスト交差検証を使用して、モデルとそのハイパーパラメータの汎化誤差を推定します。内側のループでは、各訓練セットに対してグリッドサーチを行い、最適なハイパーパラメータを見つけます。外側のループでは、テストセット上でモデルの性能を評価します。

```python
from sklearn.model_selection import KFold, cross_val_score

# Number of random trials
NUM_TRIALS = 30

# Arrays to store scores
non_nested_scores = np.zeros(NUM_TRIALS)
nested_scores = np.zeros(NUM_TRIALS)

# Loop for each trial
for i in range(NUM_TRIALS):
    # Choose cross-validation techniques for the inner and outer loops,
    # independently of the dataset.
    inner_cv = KFold(n_splits=4, shuffle=True, random_state=i)
    outer_cv = KFold(n_splits=4, shuffle=True, random_state=i)

    # Nested CV with parameter optimization
    clf = GridSearchCV(estimator=svm, param_grid=p_grid, cv=inner_cv)
    nested_score = cross_val_score(clf, X=X_iris, y=y_iris, cv=outer_cv)
    nested_scores[i] = nested_score.mean()

score_difference = non_nested_score - nested_scores.mean()
```
