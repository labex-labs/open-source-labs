# カスタムスケールのプロットを作成する

調べる最後のスケール変換のタイプはカスタムです。これにより、スケール変換用の独自の順方向および逆関数を定義できます。この例では、データの平方根を取得するカスタム関数を定義します。カスタムスケールのプロットを作成するには、`set_yscale()` メソッドを使用して文字列 `'function'` を渡します。また、`forward()` 関数と `inverse()` 関数を定義し、それらを `functions` パラメータの引数として渡します。また、プロットにタイトルとグリッドを追加します。

```python
# Function x**(1/2)
def forward(x):
    return x**(1/2)

def inverse(x):
    return x**2

plt.plot(x, y)
plt.yscale('function', functions=(forward, inverse))
plt.title('Custom Scale')
plt.grid(True)
```
