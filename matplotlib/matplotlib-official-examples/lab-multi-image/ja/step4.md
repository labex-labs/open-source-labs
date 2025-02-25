# 画像の更新

最後に、他の画像のノルムの変化に応答して画像を更新します。これにより、1つの画像のカラーマップと色スケールを変更したときに、他のすべての画像もそれに応じて更新されるようになります。

```python
def update(changed_image):
    for im in images:
        if (changed_image.get_cmap()!= im.get_cmap()
                or changed_image.get_clim()!= im.get_clim()):
            im.set_cmap(changed_image.get_cmap())
            im.set_clim(changed_image.get_clim())

for im in images:
    im.callbacks.connect('changed', update)
```
