# 데이터 로드

다음으로, 머신 러닝에서 널리 사용되는 아이리스 (iris) 데이터셋을 로드할 것입니다. 이 데이터셋은 서로 다른 종류의 아이리스 꽃의 특징에 대한 정보를 포함하고 있습니다. 이 데이터셋을 사용하여 K-Means 군집화 알고리즘을 보여줄 것입니다.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```
