# 랜덤 데이터 생성

`numpy.random.randn`을 사용하여 랜덤 데이터를 생성합니다. 각 12250 개의 포인트를 가진 4 개의 데이터 세트를 생성합니다.

```python
np.random.seed(19680801)
stack_data = np.random.randn(4, 12250)
```
