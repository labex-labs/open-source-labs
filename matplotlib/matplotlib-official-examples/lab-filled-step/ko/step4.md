# 고정 빈 (bin) 을 위한 히스토그램 함수 설정

`numpy.histogram`을 사용하여 고정 빈 (bin) 을 가진 히스토그램 함수를 설정합니다. -3 에서 3 까지의 범위를 갖는 20 개의 빈 (bin) 을 생성합니다.

```python
edges = np.linspace(-3, 3, 20, endpoint=True)
hist_func = partial(np.histogram, bins=edges)
```
