# 플롯 설정

이제 시뮬레이션을 위한 플롯을 설정합니다. 진자의 최대 길이에 해당하는 x 및 y 제한이 있는 그림을 만들고, 종횡비를 동일하게 설정하고, 그리드를 추가합니다.

```python
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(-L, 1.))
ax.set_aspect('equal')
ax.grid()
```
