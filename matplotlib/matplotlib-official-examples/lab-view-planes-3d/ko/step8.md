# 각 기본 3D 뷰 평면에 대한 눈금 레이블 및 축 레이블 사용자 정의

불필요한 레이블을 제거하기 위해 각 기본 3D 뷰 평면에 대한 눈금 레이블 및 축 레이블을 사용자 정의합니다.

```python
for plane in ('XY', '-XY'):
    axd[plane].set_zticklabels([])
    axd[plane].set_zlabel('')
for plane in ('XZ', '-XZ'):
    axd[plane].set_yticklabels([])
    axd[plane].set_ylabel('')
for plane in ('YZ', '-YZ'):
    axd[plane].set_xticklabels([])
    axd[plane].set_xlabel('')
```
