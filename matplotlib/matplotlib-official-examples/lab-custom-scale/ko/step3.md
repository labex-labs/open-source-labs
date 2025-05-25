# MercatorLatitudeTransform 클래스 구현

`MercatorLatitudeScale` 클래스 내에서 데이터를 실제로 변환할 `MercatorLatitudeTransform` 클래스를 정의합니다. 이 클래스는 `mtransforms.Transform`을 상속받습니다.

```python
    class MercatorLatitudeTransform(mtransforms.Transform):
        # 정의해야 하는 두 개의 값 멤버가 있습니다.
        # ``input_dims`` 및 ``output_dims`` 는 변환에 대한 입력
        # 차원 수와 출력 차원 수를 지정합니다.
        # 이는 변환 프레임워크에서 일부
        # 오류 검사를 수행하고 호환되지 않는 변환이
        # 함께 연결되는 것을 방지하는 데 사용됩니다. 스케일에 대한 변환을 정의할 때,
        # 이는 정의상 분리 가능하며 차원이 하나만 있으므로,
        # 이러한 멤버는 항상 1 로 설정해야 합니다.
        input_dims = output_dims = 1

        def __init__(self, thresh):
            mtransforms.Transform.__init__(self)
            self.thresh = thresh

        def transform_non_affine(self, a):
            """
            이 변환은 numpy 배열을 가져와 변환된 복사본을 반환합니다.
            Mercator 스케일의 범위는 사용자가 지정한 임계값으로 제한되므로,
            입력 배열은 유효한 값만 포함하도록 마스킹되어야 합니다. Matplotlib 는 마스킹된 배열을 처리하고
            범위를 벗어난 데이터를 플롯에서 제거합니다. 그러나,
            반환된 배열은 입력 배열과 동일한 모양을 *가져야* 합니다.
            이러한 값은 다른 차원의 값과 동기화된 상태로 유지되어야 하기 때문입니다.
            """
            masked = ma.masked_where((a < -self.thresh) | (a > self.thresh), a)
            if masked.mask.any():
                return ma.log(np.abs(ma.tan(masked) + 1 / ma.cos(masked)))
            else:
                return np.log(np.abs(np.tan(a) + 1 / np.cos(a)))

        def inverted(self):
            """
            Matplotlib 가 이 변환에 대한 역변환을 얻는 방법을 알 수 있도록
            이 메서드를 재정의합니다.
            """
            return MercatorLatitudeScale.InvertedMercatorLatitudeTransform(
                self.thresh)
```
