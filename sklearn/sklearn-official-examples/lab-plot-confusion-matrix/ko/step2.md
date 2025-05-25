# 데이터 로드

scikit-learn 의 iris 데이터셋을 사용할 것입니다. 이 데이터셋은 150 개의 샘플로 구성되며, 각 샘플은 네 가지 특징과 대상 레이블을 포함합니다.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
```
