# MercatorLatitudeScale 클래스 정의

다음으로, 사용자 정의 스케일을 구현할 `MercatorLatitudeScale` 클래스를 정의합니다. 이 클래스는 `mscale.ScaleBase`를 상속받습니다.

```python
class MercatorLatitudeScale(mscale.ScaleBase):
    """
    Mercator 투영법에서 위도를 스케일링하는 데 사용되는 시스템을 사용하여 -pi/2에서 pi/2 (-90 도에서 90 도) 범위의 데이터를 스케일링합니다.

    스케일 함수:
      ln(tan(y) + sec(y))

    역 스케일 함수:
      atan(sinh(y))

    Mercator 스케일은 +/- 90 도에서 무한대로 향하는 경향이 있으므로,
    아무것도 플로팅되지 않는 사용자 정의 임계값이 있습니다. 이는 기본적으로 +/- 85 도입니다.

    __ https://en.wikipedia.org/wiki/Mercator_projection
    """
```
