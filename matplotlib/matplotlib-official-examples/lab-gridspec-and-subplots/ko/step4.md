# 기본 Axes 제거

다음 단계에서 생성할 더 큰 axes 에 의해 덮일 기본 axes 를 제거합니다.

```python
for ax in axs[1:, -1]:
    ax.remove()
```
