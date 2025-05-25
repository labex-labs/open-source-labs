# 전처리 단계와 분류기를 포함한 간단한 파이프라인 구축

이 단계에서는 전처리 단계와 분류기를 포함한 간단한 파이프라인을 구축하고 시각적 표현을 보여줍니다.

먼저 필요한 모듈을 가져옵니다.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn import set_config
```

다음으로 파이프라인의 단계를 정의합니다.

```python
steps = [
    ("preprocessing", StandardScaler()),
    ("classifier", LogisticRegression()),
]
```

그런 다음 파이프라인을 생성합니다.

```python
pipe = Pipeline(steps)
```

마지막으로 파이프라인의 시각적 표현을 보여줍니다.

```python
set_config(display="diagram")
pipe
```
