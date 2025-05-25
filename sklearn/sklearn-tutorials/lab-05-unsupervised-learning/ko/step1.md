# K-평균을 이용한 군집화

탐색할 첫 번째 기법은 K-평균 알고리즘을 이용한 군집화입니다. K-평균은 관측치를 잘 분리된 그룹 (클러스터) 으로 나누는 것을 목표로 하는 인기 있는 군집화 알고리즘입니다. K-평균을 이용한 군집화를 보여주기 위해 아이리스 데이터셋을 예시로 사용해 보겠습니다.

```python
from sklearn import cluster, datasets

# 아이리스 데이터셋 로드
X_iris, y_iris = datasets.load_iris(return_X_y=True)

# K-평균 군집화 수행
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris)

# 클러스터 레이블 출력
print(k_means.labels_)
```
