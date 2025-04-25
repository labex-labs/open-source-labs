# 3D プロットを作成する

手順 4 で定義したレイアウトに基づいて 3D プロットを作成するために、`subplot_mosaic`を使用します。

```python
fig, axd = plt.subplot_mosaic(layout, subplot_kw={'projection': '3d'},
                              figsize=(12, 8.5))
```
