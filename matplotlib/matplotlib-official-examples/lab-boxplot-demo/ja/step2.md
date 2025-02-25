# データを生成する

次に、ボックスプロットで使用するサンプルデータを生成します。このチュートリアルでは、次のデータを使用します。

```python
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
```
