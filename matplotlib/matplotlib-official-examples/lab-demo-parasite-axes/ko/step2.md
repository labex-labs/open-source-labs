# Figure 생성 및 호스트 축 추가

`plt.figure()` 메서드를 사용하여 figure 를 생성하고, `fig.add_axes()` 메서드를 사용하여 호스트 축 (host axes) 을 추가합니다. 호스트 축은 기생 축 (parasite axes) 과 x 축 스케일을 공유합니다.

```python
fig = plt.figure()
host = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
```
