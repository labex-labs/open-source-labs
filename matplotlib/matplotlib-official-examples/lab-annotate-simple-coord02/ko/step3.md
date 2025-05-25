# 화살표 주석 추가

화살표는 플롯에서 특정 특징이나 추세를 지적하는 데 사용할 수 있습니다. 이 단계에서는 최대값을 가리키는 화살표를 플롯에 추가합니다.

```python
# Find the maximum value
y = [0, 1, 4, 9, 16]
max_index = y.index(max(y))
xmax = max_index
ymax = y[max_index]

# Add arrow annotation
ax.annotate('Maximum Value', xy=(xmax, ymax), xytext=(xmax, ymax + 5),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```
