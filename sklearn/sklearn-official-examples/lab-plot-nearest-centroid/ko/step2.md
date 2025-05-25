# 데이터 로드

다음으로, Scikit-learn 에서 아이리스 (iris) 데이터셋을 로드하고 시각화를 위해 처음 두 개의 특징만 선택합니다.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target
```
