# データを作成する

ここでは、外れ値（outlier）を含むランダムなデータを作成します。`numpy.random.rand` を使用して 30 個のランダムな数値を生成し、その後データに 2 つの外れ値を追加します。

```python
np.random.seed(19680801)

pts = np.random.rand(30)*.2
# Now let's make two outlier points which are far away from everything.
pts[[3, 14]] +=.8
```
