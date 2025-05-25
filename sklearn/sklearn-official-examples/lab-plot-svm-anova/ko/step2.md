# 파이프라인 생성

다음으로, 특징 선택 변환기, 스케일러 및 SVM 인스턴스로 구성된 파이프라인을 만듭니다. 이를 결합하여 완전한 추정기를 얻습니다.

```python
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

clf = Pipeline(
    [
        ("anova", SelectPercentile(f_classif)),
        ("scaler", StandardScaler()),
        ("svc", SVC(gamma="auto")),
    ]
)
```
