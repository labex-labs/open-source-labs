# 3Dプロットを作成する

手順4で定義したレイアウトに基づいて3Dプロットを作成するために、`subplot_mosaic`を使用します。

```python
fig, axd = plt.subplot_mosaic(layout, subplot_kw={'projection': '3d'},
                              figsize=(12, 8.5))
```
