# 重み付きデータセットを作成する

numpy ライブラリを使って重み付きデータセットを作成します。ランダムな値を持つ 20 個の点を生成し、最後の 10 個のサンプルにより大きな重みを割り当てます。

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
sample_weight = 100 * np.abs(np.random.randn(20))
sample_weight[:10] *= 10
```
