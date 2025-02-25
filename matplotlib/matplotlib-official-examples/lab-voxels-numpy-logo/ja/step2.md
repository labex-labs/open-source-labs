# 拡大関数の定義

次に、NumPyのロゴのボクセル画像を拡大するために使用される`explode`と呼ばれる関数を定義します。この関数は、NumPy配列を入力として受け取り、入力配列の2倍のサイズの新しいNumPy配列を返します。

```python
def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e
```
