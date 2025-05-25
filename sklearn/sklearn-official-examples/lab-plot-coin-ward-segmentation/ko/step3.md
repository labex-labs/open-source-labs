# 군집화 계산

데이터와 연결성 행렬이 정의되었으므로 이제 계층적 군집화를 수행할 수 있습니다. scikit-learn 의 `AgglomerativeClustering` 클래스를 사용하여 군집화를 수행할 것입니다. 이미지 내 동전 개수인 27 개의 클러스터를 설정할 것입니다. "ward" 연결 방법을 사용할 것입니다. 이 방법은 병합되는 클러스터 간 거리의 분산을 최소화합니다. 또한 2 단계에서 만든 연결성 행렬을 전달할 것입니다.

```python
from sklearn.cluster import AgglomerativeClustering
import time as time

print("구조화된 계층적 군집화 계산...")
st = time.time()
n_clusters = 27  # 영역 개수
ward = AgglomerativeClustering(
    n_clusters=n_clusters, linkage="ward", connectivity=connectivity
)
ward.fit(X)
label = np.reshape(ward.labels_, rescaled_coins.shape)
print(f"경과 시간: {time.time() - st:.3f}초")
print(f"픽셀 개수: {label.size}")
print(f"클러스터 개수: {np.unique(label).size}")
```
