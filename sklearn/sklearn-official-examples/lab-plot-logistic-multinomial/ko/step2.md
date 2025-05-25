# 데이터셋 생성

scikit-learn 의 `make_blobs` 함수를 사용하여 3 개의 클래스로 구성된 데이터셋을 생성합니다. 샘플 수는 1000 개이며, 클러스터 중심은 `[-5, 0]`, `[0, 1.5]`, `[5, -1]`로 설정합니다. 그런 다음 변환 행렬을 사용하여 데이터셋을 변환하여 분류하기 더 어렵게 만듭니다.

```python
centers = [[-5, 0], [0, 1.5], [5, -1]]
X, y = make_blobs(n_samples=1000, centers=centers, random_state=40)
transformation = [[0.4, 0.2], [-0.4, 1.2]]
X = np.dot(X, transformation)
```
