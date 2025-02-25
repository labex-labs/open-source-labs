# 行を列に分割する

`delimiter` 引数は、行をどのように列に分割するかを定義するために使用されます。デフォルトでは、`numpy.genfromtxt` は `delimiter=None` を想定しており、これは行が空白文字（タブを含む）に沿って分割されることを意味します。

```python
np.genfromtxt(StringIO(data), delimiter=",")
```
