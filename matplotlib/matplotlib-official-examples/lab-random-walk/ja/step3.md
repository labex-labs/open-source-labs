# 更新関数を定義する

アニメーションの各フレームに対してプロットを更新する関数を定義します。この関数は 3 つの入力を受け取ります。`num`は現在のフレーム番号、`walks`はすべてのランダムウォークのリスト、`lines`はプロット内のすべての線のリストです。各線とウォークに対して、現在のフレーム番号までの線の x、y、z 座標のデータを更新します。x-y 座標と z 座標をそれぞれ更新するために`line.set_data()`と`line.set_3d_properties()`を使用します。

```python
def update_lines(num, walks, lines):
    for line, walk in zip(lines, walks):
        # NOTE: there is no.set_data() for 3 dim data...
        line.set_data(walk[:num, :2].T)
        line.set_3d_properties(walk[:num, 2])
    return lines
```
