# モデルの訓練

次に、訓練データに対して回帰モデルを訓練します。この例では、Ridge 回帰モデルを使用します。

```python
from sklearn.linear_model import Ridge

# Train the Ridge regression model
model = Ridge(alpha=1e-2).fit(X_train, y_train)
```
