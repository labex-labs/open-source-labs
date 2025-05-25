# Path 데이터 정의

이 단계에서 Path 데이터를 정의합니다. Path 데이터는 경로의 정점 (vertices) 과 코드 (codes) 를 지정하는 튜플 시퀀스입니다. `mpath.Path` 클래스를 사용하여 이 데이터로부터 Path 객체를 생성합니다.

```python
Path = mpath.Path
path_data = [
    (Path.MOVETO, (1.58, -2.57)),
    (Path.CURVE4, (0.35, -1.1)),
    (Path.CURVE4, (-1.75, 2.0)),
    (Path.CURVE4, (0.375, 2.0)),
    (Path.LINETO, (0.85, 1.15)),
    (Path.CURVE4, (2.2, 3.2)),
    (Path.CURVE4, (3, 0.05)),
    (Path.CURVE4, (2.0, -0.5)),
    (Path.CLOSEPOLY, (1.58, -2.57)),
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
```
