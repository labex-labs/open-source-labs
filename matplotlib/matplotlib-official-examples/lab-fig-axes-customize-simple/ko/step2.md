# Figure 생성 및 배경 설정

`plt.figure()` 메서드를 사용하여 `matplotlib.figure.Figure` 인스턴스를 생성하는 figure 를 생성합니다. `rect.set_facecolor()` 메서드를 사용하여 figure 의 배경색을 설정합니다.

```python
fig = plt.figure()
rect = fig.patch  # a rectangle instance
rect.set_facecolor('lightgoldenrodyellow')
```
