# Figure 및 Axes 생성

`subplots()` 함수를 사용하여 figure 와 axes 객체를 생성합니다. 또한 `patches.Circle()` 함수를 사용하여 axes 객체에 노란색 원 패치를 추가합니다.

```python
fig, ax = plt.subplots()
circ = patches.Circle((0.5, 0.5), 0.25, alpha=0.8, fc='yellow')
ax.add_patch(circ)
```
