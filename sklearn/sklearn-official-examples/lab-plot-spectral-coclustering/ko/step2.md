# 데이터셋 생성

`make_biclusters` 함수를 사용하여 크기가 (300, 300) 이고 5 개의 이분 클러스터와 잡음이 5 인 데이터셋을 생성합니다.

```python
data, rows, columns = make_biclusters(shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=0)
```
