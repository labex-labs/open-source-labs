# OpenML 데이터 로드

먼저, scikit-learn 의 datasets 모듈에서 `fetch_openml` 함수를 사용하여 와인 리뷰 데이터셋을 로드합니다. 데이터에서 숫자형 및 범주형 특징의 일부만 사용할 것입니다. 다음과 같은 숫자형 및 범주형 특징의 하위 집합을 사용합니다: `numerical_features = ["price"]` 및 `categorical_features = ["country", "province", "region_1", "region_2", "variety", "winery"]`.
