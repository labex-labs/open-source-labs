# データの生成

次に、2つのコンポーネントを持つガウス混合データセットを生成します。(20, 20)を中心としたシフトされたガウスデータセットと、ゼロ中心の伸ばされたガウスデータセットを作成します。その後、2つのデータセットを連結して最終的な学習セットにします。

```python
n_samples = 300

# 乱数のシードを設定
np.random.seed(0)

# (20, 20)を中心とした球状のデータを生成
shifted_gaussian = np.random.randn(n_samples, 2) + np.array([20, 20])

# ゼロ中心の伸ばされたガウスデータを生成
C = np.array([[0.0, -0.7], [3.5, 0.7]])
stretched_gaussian = np.dot(np.random.randn(n_samples, 2), C)

# 2つのデータセットを連結して最終的な学習セットにする
X_train = np.vstack([shifted_gaussian, stretched_gaussian])
```
