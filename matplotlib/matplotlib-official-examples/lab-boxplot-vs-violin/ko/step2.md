# 데이터 생성

numpy 를 사용하여 몇 가지 무작위 테스트 데이터를 생성합니다.

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]
```
