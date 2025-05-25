# 분류기 및 색상 정의

이 실습에서 사용할 이상치 탐지 분류기를 정의하고 결과를 시각화하는 데 사용할 색상도 정의합니다.

```python
# 사용할 "분류기" 정의
classifiers = {
    "Empirical Covariance": EllipticEnvelope(support_fraction=1.0, contamination=0.25),
    "Robust Covariance (Minimum Covariance Determinant)": EllipticEnvelope(
        contamination=0.25
    ),
    "OCSVM": OneClassSVM(nu=0.25, gamma=0.35),
}
colors = ["m", "g", "b"]
```
