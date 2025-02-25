# メッシュグリッドの作成

3 番目のステップは、`linspace` を使ってメッシュグリッドを作成することです。

```python
xs = np.linspace(-1, 1, 50)
ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)
```
