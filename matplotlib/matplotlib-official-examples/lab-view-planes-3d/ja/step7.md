# 各一次3Dビュープレーンにラベルを付ける

手順2で定義した`annotate_axes`関数を使用して、各一次3Dビュープレーンにそれぞれの角度を付けてラベルを付けます。

```python
for plane, angles in views:
    label = f'{plane}\n{angles}'
    annotate_axes(axd[plane], label, fontsize=14)
```
