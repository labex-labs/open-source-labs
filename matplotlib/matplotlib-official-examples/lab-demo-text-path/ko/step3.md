# PathClippedImagePatch 생성

텍스트 경로의 이미지를 그리기 위해 PathClippedImagePatch 객체를 생성합니다. 다음 코드를 사용하여 PathClippedImagePatch 객체를 생성합니다.

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
