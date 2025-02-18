# Erstellen eines PathClippedImagePatch

Erstellen Sie ein `PathClippedImagePatch`-Objekt, um ein Bild eines Textpfads zu zeichnen. Verwenden Sie den folgenden Code, um ein `PathClippedImagePatch`-Objekt zu erstellen:

```python
class PathClippedImagePatch(PathPatch):
    def __init__(self, path, bbox_image, **kwargs):
        super().__init__(path, **kwargs)
        self.bbox_image = BboxImage(
            self.get_window_extent, norm=None, origin=None)
        self.bbox_image.set_data(bbox_image)

    def set_facecolor(self, color):
        super().set_facecolor("none")

    def draw(self, renderer=None):
        self.bbox_image.set_clip_path(self._path, self.get_transform())
        self.bbox_image.draw(renderer)
        super().draw(renderer)
```
