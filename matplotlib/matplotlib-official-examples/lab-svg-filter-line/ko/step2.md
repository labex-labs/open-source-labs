# Figure 및 Axes 생성

`plt.figure()`를 사용하여 figure 객체를 생성하고, `fig1.add_axes()`를 사용하여 axes 객체를 추가합니다. 또한 `[0.1, 0.1, 0.8, 0.8]`을 사용하여 axes 의 크기와 위치를 설정합니다.

```python
fig1 = plt.figure()
ax = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
```
