# 라이브러리 가져오기 및 데이터셋 로드

필요한 라이브러리를 가져오고 아이리스 데이터셋을 로드하는 것으로 시작하겠습니다. `sklearn.datasets` 모듈의 `load_iris` 함수를 사용하여 데이터셋을 로드합니다.

```python
from sklearn.datasets import load_iris

# 아이리스 데이터셋 로드
iris = load_iris()
X = iris.data  # 특징
y = iris.target  # 목표 변수

print("샘플 수:", X.shape[0])
print("특징 수:", X.shape[1])
print("클래스 수:", len(set(y)))
```
