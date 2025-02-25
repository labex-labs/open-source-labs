# メモリ効率の確認

次に、疎データ構造を使用した場合のメモリ効率を確認します。大きな DataFrame を作成し、それを疎に変換してから、メモリ使用量を比較します。

```python
# ランダムな値を持つ大きな DataFrame を作成
df = pd.DataFrame(np.random.randn(10000, 4))

# DataFrame の大部分を NaN に設定
df.iloc[:9998] = np.nan

# DataFrame を疎に変換
sdf = df.astype(pd.SparseDtype("float", np.nan))

# 高密度と低密度の DataFrame のメモリ使用量を確認
print('dense : {:0.2f} bytes'.format(df.memory_usage().sum() / 1e3))
print('sparse: {:0.2f} bytes'.format(sdf.memory_usage().sum() / 1e3))
```
