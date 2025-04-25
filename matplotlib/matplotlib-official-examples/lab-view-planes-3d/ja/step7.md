# 各一次 3D ビュープレーンにラベルを付ける

手順 2 で定義した`annotate_axes`関数を使用して、各一次 3D ビュープレーンにそれぞれの角度を付けてラベルを付けます。

```python
for plane, angles in views:
    label = f'{plane}\n{angles}'
    annotate_axes(axd[plane], label, fontsize=14)
```
