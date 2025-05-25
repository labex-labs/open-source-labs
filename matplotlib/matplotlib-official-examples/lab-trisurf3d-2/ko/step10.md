# 표면 플롯

마지막으로, `plot_trisurf()` 함수를 사용하여 표면을 플롯합니다.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)
```
