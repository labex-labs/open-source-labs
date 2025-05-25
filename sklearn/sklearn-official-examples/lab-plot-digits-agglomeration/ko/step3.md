# 연결 행렬 정의

이 단계에서는 scikit-learn 의 `grid_to_graph` 함수를 사용하여 연결 행렬을 정의합니다. 이 함수는 이미지의 픽셀 그리드를 기반으로 연결 그래프를 생성합니다.

```python
connectivity = grid_to_graph(*images[0].shape)
```
