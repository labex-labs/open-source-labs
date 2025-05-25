# numpy 배열을 Pillow 이미지로 저장

numpy 배열이 생성되었으므로, 이를 Pillow 에 전달하여 Pillow 가 지원하는 모든 형식으로 저장할 수 있습니다. 이 예제에서는 그래프를 BMP 이미지로 저장합니다.

```python
from PIL import Image

im = Image.fromarray(rgba)
im.save("test.bmp")
```
