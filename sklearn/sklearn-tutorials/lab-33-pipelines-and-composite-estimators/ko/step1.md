# 파이프라인 - 추정기 연결

scikit-learn 의 `Pipeline` 클래스는 여러 추정기를 하나로 연결하는 데 사용됩니다. 이를 통해 데이터에 대해 한 번에 `fit` 및 `predict`를 호출하여 추정기의 전체 시퀀스를 맞출 수 있습니다. 또한 공동 매개변수 선택을 가능하게 하고 교차 검증에서 데이터 누출을 방지하는 데 도움이 됩니다.

파이프라인을 생성하려면 각 단계를 식별하는 문자열 `key`와 추정기 객체인 `value`의 쌍 목록을 제공해야 합니다. 아래는 PCA 변환기와 SVM 분류기를 사용하여 파이프라인을 만드는 예입니다.

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
pipe = Pipeline(estimators)
```

인덱싱 또는 이름으로 파이프라인의 단계에 접근할 수 있습니다.

```python
pipe.steps[0]  # 인덱스로 접근
pipe[0]  # 위와 동일
pipe['reduce_dim']  # 이름으로 접근
```

또한 `make_pipeline` 함수를 사용하여 파이프라인을 생성하는 간단한 방법으로 사용할 수 있습니다.

```python
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import Binarizer

make_pipeline(Binarizer(), MultinomialNB())
```
