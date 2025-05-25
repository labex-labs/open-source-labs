# 풍부한 HTML 표현

추정기를 표시하는 두 번째 방법은 풍부한 HTML 표현입니다. 노트북에서 추정기와 파이프라인은 풍부한 HTML 표현을 사용합니다. 이는 파이프라인 및 기타 복합 추정기의 구조를 요약하는 데 특히 유용하며, 세부 정보를 제공하기 위한 상호 작용 기능을 갖추고 있습니다.

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression

# 숫자형 및 범주형 데이터에 대한 파이프라인 생성
num_proc = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
cat_proc = make_pipeline(
    SimpleImputer(strategy="constant", fill_value="missing"),
    OneHotEncoder(handle_unknown="ignore"),
)

# 특정 열에 숫자형 및 범주형 파이프라인을 적용하는 전처리기 생성
preprocessor = make_column_transformer(
    (num_proc, ("feat1", "feat3")), (cat_proc, ("feat0", "feat2"))
)

# 전처리기와 로지스틱 회귀를 적용하는 파이프라인 생성
clf = make_pipeline(preprocessor, LogisticRegression())

# 파이프라인 표시
clf
```
