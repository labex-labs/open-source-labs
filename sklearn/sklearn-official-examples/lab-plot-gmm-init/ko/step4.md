# 결과 해석

플롯에서 볼 수 있듯이 `k-means++`는 초기화 시간이 짧고 GaussianMixture 가 수렴하는 반복 횟수가 적은 좋은 성능을 보여줍니다. `random_from_data` 또는 `random`으로 초기화할 경우 모델이 수렴하는 데 더 많은 반복이 필요합니다. 세 가지 대안 방법 모두 `kmeans`에 비해 초기화 시간이 더 짧습니다.
