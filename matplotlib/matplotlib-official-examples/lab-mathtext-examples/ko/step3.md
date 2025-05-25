# 그림 및 축 생성

이 단계에서는 수학 표현식 예제를 위한 그림과 축을 생성합니다.

```python
# Creating figure and axis.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0.01, 0.01, 0.98, 0.90],
                  facecolor="white", frameon=True)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_title("Matplotlib's math rendering engine",
             color=mpl_grey_rgb, fontsize=14, weight='bold')
ax.set_xticks([])
ax.set_yticks([])
```
