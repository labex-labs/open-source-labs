# 그리드 생성

이제 배치 객체로부터 지도 그리드를 생성할 것입니다. `construct_grids` 함수를 사용하여 이 작업을 수행할 것입니다.

```python
def construct_grids(batch):
    """배치 객체로부터 지도 그리드를 생성합니다.

    매개변수
    ----------
    batch : 배치 객체
        :func:`fetch_species_distributions` 함수에서 반환된 객체

    반환값
    -------
    (xgrid, ygrid) : 1 차원 배열
        batch.coverages 의 값에 해당하는 그리드
    """
    # 모서리 셀의 x,y 좌표
    xmin = batch.x_left_lower_corner + batch.grid_size
    xmax = xmin + (batch.Nx * batch.grid_size)
    ymin = batch.y_left_lower_corner + batch.grid_size
    ymax = ymin + (batch.Ny * batch.grid_size)

    # 그리드 셀의 x 좌표
    xgrid = np.arange(xmin, xmax, batch.grid_size)
    # 그리드 셀의 y 좌표
    ygrid = np.arange(ymin, ymax, batch.grid_size)

    return (xgrid, ygrid)

# 함수를 호출하고 결과를 xgrid 와 ygrid 에 저장
xgrid, ygrid = construct_grids(data)
```
