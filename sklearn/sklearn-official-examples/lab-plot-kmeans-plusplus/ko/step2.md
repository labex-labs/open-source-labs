# K-Means++ 에서 시드 계산

scikit-learn 라이브러리의 `kmeans_plusplus` 함수를 사용하여 K-Means++ 에서 시드를 계산합니다. 이 함수는 k-means 클러스터링에 사용되는 초기 클러스터 중심을 반환합니다. K-Means++ 를 사용하여 4 개의 클러스터를 계산합니다.

```python
# K-Means++ 에서 시드 계산
centers_init, indices = kmeans_plusplus(X, n_clusters=4, random_state=0)
```
