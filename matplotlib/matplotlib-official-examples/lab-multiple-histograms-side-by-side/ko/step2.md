# 예제 데이터 세트 생성

다음으로, 히스토그램에 사용할 예제 데이터 세트를 생성합니다. 각각 387 개의 데이터 포인트를 가진 세 개의 데이터 세트를 생성합니다.

```python
np.random.seed(19680801)
number_of_data_points = 387
labels = ["A", "B", "C"]
data_sets = [np.random.normal(0, 1, number_of_data_points),
             np.random.normal(6, 1, number_of_data_points),
             np.random.normal(-3, 1, number_of_data_points)]
```
