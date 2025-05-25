# 인접 행렬 계산

인접 그래프를 scipy 희소 행렬로 추출합니다. 먼저 리디렉션을 해결합니다. X(scipy 희소 인접 행렬), 문서 이름에서 문서 이름으로의 파이썬 딕셔너리인 리디렉션, 그리고 문서 이름에서 파이썬 정수 (문서 인덱스) 로의 파이썬 딕셔너리인 index_map 을 반환합니다.

```python
import numpy as np
from scipy import sparse


def get_adjacency_matrix(redirects_filename, page_links_filename, limit=None):
    """인접 그래프를 scipy 희소 행렬로 추출합니다."""
    index_map = dict()
    links = list()
    for l, line in enumerate(BZ2File(page_links_filename)):
        split = line.split()
        if len(split) != 4:
            print("잘못된 형식의 줄 무시: " + line)
            continue
        i = index(redirects, index_map, short_name(split[0]))
        j = index(redirects, index_map, short_name(split[2]))
        links.append((i, j))
        if l % 1000000 == 0:
            print("[%s] 줄: %08d" % (datetime.now().isoformat(), l))

        if limit is not None and l >= limit - 1:
            break

    print("인접 행렬 계산")
    X = sparse.lil_matrix((len(index_map), len(index_map)), dtype=np.float32)
    for i, j in links:
        X[i, j] = 1.0
    del links
    print("CSR 표현으로 변환")
    X = X.tocsr()
    print("CSR 변환 완료")
    return X, redirects, index_map


# RAM 에서 작업할 수 있도록 5 백만 개의 링크 이후에 중지
X, redirects, index_map = get_adjacency_matrix(
    redirects_filename, page_links_filename, limit=5000000
)
names = {i: name for name, i in index_map.items()}
```
