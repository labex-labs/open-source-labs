# 맵 그리드 생성

이 단계에서는 데이터 객체로부터 맵 그리드를 생성합니다. `construct_grids`라는 함수를 만들어 데이터 객체를 입력으로 받아 xgrid 와 ygrid 를 반환합니다.

```python
def construct_grids(batch):
    """배치 객체로부터 맵 그리드를 생성합니다.

    매개변수
    ----------
    batch : 배치 객체
        fetch_species_distributions 함수의 반환 값

    반환값
    -------
    (xgrid, ygrid) : 1 차원 배열
        batch.coverages 의 값에 해당하는 그리드
    """
    # 모서리 셀의 x, y 좌표
    xmin = batch.x_left_lower_corner + batch.grid_size
    xmax = xmin + (batch.Nx * batch.grid_size)
    ymin = batch.y_left_lower_corner + batch.grid_size
    ymax = ymin + (batch.Ny * batch.grid_size)

    # 그리드 셀의 x 좌표
    xgrid = np.arange(xmin, xmax, batch.grid_size)
    # 그리드 셀의 y 좌표
    ygrid = np.arange(ymin, ymax, batch.grid_size)

    return (xgrid, ygrid)

# 맵 그리드 생성
xgrid, ygrid = construct_grids(data)
```
