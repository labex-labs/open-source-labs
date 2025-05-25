# 플롯 생성

이제 `tricontourf()` 함수를 사용하여 플롯을 생성하고 뷰 각도 (view angle) 를 사용자 정의합니다.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontourf(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)

plt.show()
```
