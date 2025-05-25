# 이미지를 그래프로 변환

`sklearn.feature_extraction.image`의 `img_to_graph`를 사용하여 이미지를 그래프로 변환합니다. 에지의 기울기 값도 계산됩니다.

```python
from sklearn.feature_extraction import image

graph = image.img_to_graph(img, mask=mask)
```
