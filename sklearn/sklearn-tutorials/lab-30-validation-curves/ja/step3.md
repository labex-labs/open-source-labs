# 検証曲線を描画する

次に、`validation_curve`関数を使って検証曲線を描画しましょう。`Ridge`推定器を使用し、`alpha`ハイパーパラメータを値の範囲で変化させます。

```python
param_range = np.logspace(-7, 3, 3)
train_scores, valid_scores = validation_curve(
    Ridge(), X, y, param_name="alpha", param_range=param_range, cv=5)
```
