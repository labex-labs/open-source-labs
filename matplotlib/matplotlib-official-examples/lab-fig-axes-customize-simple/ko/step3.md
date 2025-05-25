# Figure 에 축 추가

`fig.add_axes()` 메서드를 사용하여 figure 에 축을 추가합니다. 또한 `rect.set_facecolor()` 메서드를 사용하여 축의 배경색을 설정합니다.

```python
ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')
```
