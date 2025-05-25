# 가중 샘플을 사용한 그램 행렬 미리 계산

`precompute` 옵션과 함께 샘플 가중치를 사용하여 탄성 네트워크를 맞추려면 먼저 그램 행렬을 계산하기 전에 설계 행렬을 중심에 맞추고 정규화된 가중치로 조정해야 합니다. 각 특징 열의 가중 평균을 각 행에서 빼서 설계 행렬을 중심에 맞춥니다. 그런 다음, 해당 정규화된 가중치의 제곱근으로 각 행을 곱하여 중심에 맞춘 설계 행렬을 조정합니다. 마지막으로, 조정된 설계 행렬의 전치 행렬과의 내적을 취하여 그램 행렬을 계산합니다.

```python
X_offset = np.average(X, axis=0, weights=normalized_weights)
X_centered = X - np.average(X, axis=0, weights=normalized_weights)
X_scaled = X_centered * np.sqrt(normalized_weights)[:, np.newaxis]
gram = np.dot(X_scaled.T, X_scaled)
```
