# 사용자 지정 삼각 측량 플롯

`triplot` 함수를 사용하여 사용자 지정 삼각 측량 (triangulation) 을 플롯합니다.

```python
fig2, ax2 = plt.subplots()
ax2.set_aspect('equal')
ax2.triplot(x, y, triangles, 'go-', lw=1.0)
ax2.set_title('사용자 지정 삼각 측량의 Triplot')
ax2.set_xlabel('경도 (degrees)')
ax2.set_ylabel('위도 (degrees)')
```
