# 샘플 데이터 생성

다음으로, 작업할 샘플 데이터를 생성합니다. `sklearn.datasets` 모듈의 `make_blobs` 함수를 사용하여 클러스터가 있는 합성 데이터 세트를 생성합니다.

```python
# 샘플 데이터 생성
X, y = make_blobs(n_samples=100, centers=4, random_state=0, cluster_std=1.0)
```
