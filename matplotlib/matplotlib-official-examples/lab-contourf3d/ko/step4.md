# 등고선 플롯 생성

이제 `contourf()` 메서드를 사용하여 등고선 플롯을 생성합니다. 이 메서드는 채워진 등고선을 생성합니다. `cmap` 매개변수를 `cm.coolwarm`으로 설정하여 cool-warm 컬러 맵을 사용합니다.

```python
ax.contourf(X, Y, Z, cmap=cm.coolwarm)
```
