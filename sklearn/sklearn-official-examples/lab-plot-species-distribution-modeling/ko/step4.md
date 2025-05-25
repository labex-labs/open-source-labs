# 특정 종 번들 생성

이 단계에서는 특정 생물체에 대한 정보를 담은 번들 (bunch) 을 생성합니다. `create_species_bunch` 함수를 만들어 종 이름, 학습 데이터, 테스트 데이터, 범위 데이터, x 축 그리드, y 축 그리드를 입력으로 받아 번들 객체를 반환합니다.

```python
def create_species_bunch(species_name, train, test, coverages, xgrid, ygrid):
    """특정 생물체에 대한 정보를 담은 번들 생성

    test/train 레코드 배열을 사용하여 지정된 종 이름에 대한 데이터를 추출합니다.
    """
    bunch = Bunch(name=" ".join(species_name.split("_")[:2]))
    species_name = species_name.encode("ascii")
    points = dict(test=test, train=train)

    for label, pts in points.items():
        # 원하는 종과 관련된 점 선택
        pts = pts[pts["species"] == species_name]
        bunch["pts_%s" % label] = pts

        # 각 학습 및 테스트 점에 대한 범위 값 결정
        ix = np.searchsorted(xgrid, pts["dd long"])
        iy = np.searchsorted(ygrid, pts["dd lat"])
        bunch["cov_%s" % label] = coverages[:, -iy, ix].T

    return bunch

# 종 번들 생성
BV_bunch = create_species_bunch(
    "bradypus_variegatus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
MM_bunch = create_species_bunch(
    "microryzomys_minutus_0", data.train, data.test, data.coverages, xgrid, ygrid
)
```
