# データの生成

次に、ステムプロットで使用するデータを生成する必要があります。Numpy ライブラリを使用して 2 つの配列を作成します。

```python
x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))
```
