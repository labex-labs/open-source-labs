# 분류기를 정의합니다.

ROC 및 DET 곡선을 사용하여 임계값에 따른 두 개의 서로 다른 분류기의 통계적 성능을 비교할 것입니다. scikit-learn 의 `make_pipeline` 함수를 사용하여 `StandardScaler`를 사용하여 데이터를 스케일링하고 `LinearSVC` 분류기를 학습하는 파이프라인을 생성합니다. 또한 scikit-learn 의 `RandomForestClassifier` 클래스를 사용하여 최대 깊이 5, 추정자 10 개, 최대 1 개의 특징을 가진 랜덤 포레스트 분류기를 학습합니다.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

classifiers = {
    "Linear SVM": make_pipeline(StandardScaler(), LinearSVC(C=0.025, dual="auto")),
    "Random Forest": RandomForestClassifier(
        max_depth=5, n_estimators=10, max_features=1
    ),
}
```
