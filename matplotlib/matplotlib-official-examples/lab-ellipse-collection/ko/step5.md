# 플롯에 컬렉션 추가

`EllipseCollection`을 플롯에 추가합니다.

```python
ax.add_collection(ec)
ax.autoscale_view()
ax.set_xlabel('X')
ax.set_ylabel('y')
cbar = plt.colorbar(ec)
cbar.set_label('X+Y')
plt.show()
```
