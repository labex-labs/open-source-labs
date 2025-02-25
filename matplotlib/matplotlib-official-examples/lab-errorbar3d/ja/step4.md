# プロットに誤差棒を追加する

`Axes3D`オブジェクトの`errorbar`メソッドを使って、プロットに誤差棒を追加します。どのデータポイントが上限と下限を持つかを指定する配列に、`zuplims`と`zlolims`パラメータを設定します。誤差棒の頻度を制御するために、`errorevery`パラメータを設定します。

```python
estep = 15
i = np.arange(t.size)
zuplims = (i % estep == 0) & (i // estep % 3 == 0)
zlolims = (i % estep == 0) & (i // estep % 3 == 2)

ax.errorbar(x, y, z, 0.2, zuplims=zuplims, zlolims=zlolims, errorevery=estep)
```
