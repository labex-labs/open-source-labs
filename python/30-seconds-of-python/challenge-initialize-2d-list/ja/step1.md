# 2次元リストを初期化する

## 問題

幅と高さ、および値が与えられた2次元リストを初期化する関数`initialize_2d_list(w, h, val=None)`を書きます。この関数は、`h`行のリストを返す必要があり、各行は長さ`w`のリストで、`val`で初期化されています。`val`が指定されていない場合、既定値は`None`でなければなりません。

## 例

```python
initialize_2d_list(2, 2, 0) # [[0, 0], [0, 0]]
initialize_2d_list(3, 3, "x") # [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
initialize_2d_list(2, 3) # [[None, None], [None, None], [None, None]]
```
