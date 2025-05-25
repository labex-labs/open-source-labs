# 기본 범주형 특징 지원

이 섹션에서는 `HistGradientBoostingRegressor`에서 기본 범주형 특징 지원을 사용하는 파이프라인을 구축하고 평가합니다. `HistGradientBoostingRegressor`는 최대 255 개의 고유 범주만 지원합니다. 범주형 특징을 저카디널리티 (low cardinality) 특징과 고카디널리티 (high cardinality) 특징으로 그룹화합니다. 고카디널리티 특징은 대상 인코딩 (target encoding) 을 사용하고, 저카디널리티 특징은 그래디언트 부스팅에서 기본 범주형 특징을 사용합니다.
