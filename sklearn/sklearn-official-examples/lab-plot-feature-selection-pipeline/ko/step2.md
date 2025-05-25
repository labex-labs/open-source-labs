# 파이프라인 구축

이제 특징 선택 및 SVM 분류로 구성된 파이프라인을 구축합니다. Scikit-learn 의 `SelectKBest` 함수를 특징 선택에 사용하고, Scikit-learn 의 `LinearSVC` 함수를 SVM 분류에 사용합니다. `SelectKBest` 함수는 각 특징과 대상 변수 간의 ANOVA F-값을 계산하는 `f_classif` 방법을 기반으로 가장 정보가 풍부한 `k`개의 특징을 선택합니다. 이 예제에서는 `k=3`으로 설정합니다.

```python
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

anova_filter = SelectKBest(f_classif, k=3)
clf = LinearSVC(dual="auto")
anova_svm = make_pipeline(anova_filter, clf)
```
