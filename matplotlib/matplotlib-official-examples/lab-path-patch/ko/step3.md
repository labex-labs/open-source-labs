# PathPatch 객체 생성

이 단계에서는 이전 단계에서 생성한 path 객체를 사용하여 `PathPatch` 객체를 생성합니다. 이 객체는 경로로 둘러싸인 영역을 채우는 데 사용됩니다. 패치의 색상과 투명도도 설정할 수 있습니다.

```python
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
```
