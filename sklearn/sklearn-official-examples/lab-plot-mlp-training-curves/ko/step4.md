# 작은 데이터셋 로드 또는 생성

이제 이 예제에서 사용할 작은 데이터셋을 로드하거나 생성해야 합니다. 아이리스 데이터셋, 숫자 데이터셋, make_circles 및 make_moons 함수를 사용하여 생성된 두 개의 데이터셋을 사용할 것입니다.

```python
iris = datasets.load_iris()
X_digits, y_digits = datasets.load_digits(return_X_y=True)
data_sets = [
    (iris.data, iris.target),
    (X_digits, y_digits),
    datasets.make_circles(noise=0.2, factor=0.5, random_state=1),
    datasets.make_moons(noise=0.3, random_state=0),
]
```
