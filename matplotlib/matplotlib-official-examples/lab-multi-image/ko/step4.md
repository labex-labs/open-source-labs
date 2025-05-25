# 이미지 업데이트

마지막으로, 다른 이미지의 norm 변경에 응답하도록 이미지를 업데이트합니다. 이를 통해 한 이미지의 colormap 및 색상 척도를 변경하고 다른 모든 이미지가 그에 따라 업데이트되도록 할 수 있습니다.

```python
def update(changed_image):
    for im in images:
        if (changed_image.get_cmap() != im.get_cmap()
                or changed_image.get_clim() != im.get_clim()):
            im.set_cmap(changed_image.get_cmap())
            im.set_clim(changed_image.get_clim())

for im in images:
    im.callbacks.connect('changed', update)
```
