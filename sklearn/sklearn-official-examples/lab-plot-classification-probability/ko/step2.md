# 데이터셋 로드

다음으로, Scikit-learn 에서 아이리스 (iris) 데이터셋을 로드합니다.

```python
iris = datasets.load_iris()
X = iris.data[:, 0:2]  # 시각화를 위해 처음 두 개의 특징만 사용
y = iris.target
n_features = X.shape[1]
```
