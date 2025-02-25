# scipy の疎行列との相互作用

最後に、scipy の疎行列から疎な値を持つ DataFrame を作成したり、その逆を行ったりすることができます。

```python
# 必要なライブラリをインポート
from scipy.sparse import csr_matrix

# scipy を使って疎行列を作成
arr = np.random.random(size=(1000, 5))
arr[arr <.9] = 0
sp_arr = csr_matrix(arr)

# 疎行列から DataFrame を作成
sdf = pd.DataFrame.sparse.from_spmatrix(sp_arr)

# DataFrame を表示
print(sdf.head())
print(sdf.dtypes)

# 再び疎行列に変換
print(sdf.sparse.to_coo())
```
