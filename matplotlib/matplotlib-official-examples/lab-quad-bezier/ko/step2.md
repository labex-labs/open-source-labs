# 경로 생성

다음으로, 베지어 곡선 (Bezier Curve) 에 대한 `Path` 객체를 생성합니다. `Path` 객체는 정점 (vertices) 목록과 정점 사이의 경로 유형을 지정하는 코드를 입력으로 받습니다. 이 경우, 시작점으로 이동하기 위해 `MOVETO` 코드를 사용하고, 제어점 (control points) 과 종료점을 지정하기 위해 두 개의 `CURVE3` 코드를 사용하며, 마지막으로 경로를 닫기 위해 `CLOSEPOLY` 코드를 사용합니다.

```python
Path = mpath.Path

bezier_path = Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                   [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY])
```
