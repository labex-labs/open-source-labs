# 등고선 프로파일 투영

이제 등고선 프로파일을 그래프의 벽에 투영합니다. 이는 `contourf` 메서드를 사용하여 수행됩니다. `zdir` 매개변수를 'z', 'x', 'y'로 설정하여 등고선 프로파일을 각각 z, x, y 벽에 투영합니다. 또한 적절한 축 제한에 맞게 `offset` 매개변수를 설정합니다.

```python
ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
