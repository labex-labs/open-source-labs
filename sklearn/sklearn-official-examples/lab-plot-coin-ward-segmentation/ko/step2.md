# 데이터 구조 정의

이미지의 픽셀은 인접 픽셀들과 연결되어 있습니다. 이미지에 대한 계층적 군집화를 수행하기 위해서는 데이터의 구조를 정의해야 합니다. scikit-learn 의 `grid_to_graph` 함수를 사용하여 데이터 구조를 정의하는 연결성 행렬을 생성할 수 있습니다.

```python
from sklearn.feature_extraction.image import grid_to_graph

connectivity = grid_to_graph(*rescaled_coins.shape)
```
