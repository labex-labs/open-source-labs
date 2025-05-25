# 샘플 데이터 세트 생성

numpy 라이브러리를 사용하여 샘플 데이터 세트를 생성합니다. 서로 다른 표준 편차를 가진 6 개의 데이터 세트를 생성합니다.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# fake data
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]
```
