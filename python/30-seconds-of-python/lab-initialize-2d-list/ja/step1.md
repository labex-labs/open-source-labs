# 2次元リストを初期化する

幅と高さ、および値が与えられた2次元リストを初期化する関数`initialize_2d_list(w, h, val=None)`を作成します。この関数は、幅`w`、高さ`h`の`h`行からなるリストを返し、各行は長さ`w`のリストで、`val`で初期化されます。`val`が指定されない場合、既定値は`None`でなければなりません。

```python
def initialize_2d_list(w, h, val = None):
  return [[val for x in range(w)] for y in range(h)]
```

```python
initialize_2d_list(2, 2, 0) # [[0, 0], [0, 0]]
```
