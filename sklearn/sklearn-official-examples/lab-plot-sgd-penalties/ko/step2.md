# 데이터 생성

패널티를 적용하기 위한 샘플 데이터를 생성합니다. 이 예제에서는 각각 100 개의 샘플을 가진 두 개의 클래스 데이터를 생성합니다.

```python
np.random.seed(42)

# 두 개의 클래스 데이터 생성
X = np.random.randn(200, 2)
y = np.repeat([1, -1], 100)
```
