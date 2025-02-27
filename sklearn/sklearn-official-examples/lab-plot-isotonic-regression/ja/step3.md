# 等張回帰と線形回帰モデルを適合させる

ここで、生成したデータに対して等張回帰と線形回帰の両方のモデルを適合させます。

```python
ir = IsotonicRegression(out_of_bounds="clip")
y_ = ir.fit_transform(x, y)

lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)  # x needs to be 2d for LinearRegression
```
