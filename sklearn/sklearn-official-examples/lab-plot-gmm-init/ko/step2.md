# 초기 평균을 구하는 함수 정의

다음으로, 샘플 데이터, 초기화 방법 및 난수 상태를 입력으로 받아 초기화 평균을 반환하는 `get_initial_means` 함수를 정의합니다.

```python
def get_initial_means(X, init_params, r):
    # max_iter=0 으로 GaussianMixture 를 실행하여 초기화 평균을 출력
    gmm = GaussianMixture(
        n_components=4, init_params=init_params, tol=1e-9, max_iter=0, random_state=r
    ).fit(X)
    return gmm.means_
```
