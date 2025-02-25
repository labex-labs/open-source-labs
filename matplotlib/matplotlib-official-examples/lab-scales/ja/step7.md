# メルカトル変換スケールのプロットを作成する

特典として、メルカトル変換関数を使用してプロットも作成します。これはMatplotlibの組み込み関数ではないのですが、独自の順方向および逆関数を定義してメルカトル変換スケールのプロットを作成することができます。この例では、メルカトル変換用の`forward()`関数と`inverse()`関数を定義します。また、プロットにタイトルとグリッドを追加します。

```python
# Function Mercator transform
def forward(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.log(np.abs(np.tan(a) + 1.0 / np.cos(a))))

def inverse(a):
    a = np.deg2rad(a)
    return np.rad2deg(np.arctan(np.sinh(a)))

t = np.arange(0, 170.0, 0.1)
s = t / 2.

plt.plot(t, s, '-', lw=2)
plt.yscale('function', functions=(forward, inverse))
plt.title('Mercator Transform Scale')
plt.grid(True)
plt.xlim([0, 180])
```
